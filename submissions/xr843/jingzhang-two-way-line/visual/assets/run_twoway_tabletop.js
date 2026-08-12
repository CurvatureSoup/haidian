#!/usr/bin/env node
/**
 * 对开协议·桌面推演 / Two-Way Protocol tabletop
 *
 * 用途：让评审者可复算地检验「对开协议」是不是真的成立，而不是只读一段散文。
 *
 *   node run_twoway_tabletop.js                  # 判定并打印报告
 *   node run_twoway_tabletop.js --json           # 输出机读结果
 *   node run_twoway_tabletop.js --write-evidence # 重写 twoway-tabletop-evidence.json
 *
 * 判定两件事：
 *   1. 十二张真实班次卡是否全部满足协议六条规则（全过才算成立）；
 *   2. 六个变异用例是否**各自被对应规则拦下**（拦不下说明这道闸门是摆设）。
 *
 * 任一项不成立即以非零码退出。无外部依赖，Node 18+ 可直接运行。
 *
 * 边界：本脚本检验的是本方案自设的准入契约，不是行政审批、法律合规或政府承诺；
 * 运行图中的机构名称均为方案提出的概念性运营架构。
 */

'use strict';

const fs = require('fs');
const path = require('path');

const HERE = __dirname;
const RUNBOOK = path.join(HERE, 'twoway-runbook.json');
const EVIDENCE = path.join(HERE, 'twoway-tabletop-evidence.json');

const nonEmpty = (v) => typeof v === 'string' && v.trim().length > 0;

/** 六条规则，逐条对应 proposal.md 的原文出处。返回 null 表示通过，返回字符串表示违规原因。 */
const RULES = [
  {
    id: 'R1_THREE_ELEMENTS',
    check(r) {
      const missing = [];
      if (!nonEmpty(r.node)) missing.push('节点');
      if (!nonEmpty(r.operator)) missing.push('运营主体');
      if (!nonEmpty(r.uplink && r.uplink.takes)) missing.push('上行清单');
      if (!Array.isArray(r.uplink && r.uplink.data_classes) || r.uplink.data_classes.length === 0) missing.push('上行数据类别');
      if (!nonEmpty(r.downlink && r.downlink.returns)) missing.push('下行清单');
      return missing.length ? `三要素缺 ${missing.join('、')}，不得排图` : null;
    },
  },
  {
    id: 'R2_NO_TAKE_WITHOUT_RETURN',
    check(r) {
      const takes = nonEmpty(r.uplink && r.uplink.takes);
      if (!takes) return null; // 无上行则不受本条约束，由 R1 处理
      if (!nonEmpty(r.downlink && r.downlink.returns)) return '有上行无下行，属只取不还';
      if (!nonEmpty(r.downlink && r.downlink.public_commitment)) return '下行缺可被公众核对的承诺形式，属只取不还';
      return null;
    },
  },
  {
    id: 'R3_WHO_CAN_HALT',
    check(r) {
      if (!nonEmpty(r.review_and_exit && r.review_and_exit.mechanism)) return '未声明复核与退出机制';
      if (!nonEmpty(r.review_and_exit && r.review_and_exit.who_can_halt)) return '未声明叫停主体，「谁能叫停」无解';
      return null;
    },
  },
  {
    id: 'R4_PRIVACY_REDLINE',
    check(r) {
      const p = r.privacy || {};
      const bad = [];
      if (p.face_recognition_surveillance !== false) bad.push('人脸识别布控');
      if (p.identifiable_trajectory !== false) bad.push('可识别个体轨迹');
      return bad.length ? `触碰隐私红线：${bad.join('、')}` : null;
    },
  },
  {
    id: 'R5_NON_AI_FALLBACK',
    check(r) {
      return nonEmpty(r.non_ai_fallback) ? null : '缺非AI等价服务路径';
    },
  },
  {
    id: 'R6_TEST_NOT_APPROVED',
    check(r) {
      const isTest = typeof r.service_id === 'string' && r.service_id.startsWith('T');
      if (isTest && r.status !== 'proposed') {
        return `测试班次状态为 ${r.status}，不得表述为已批准或已排图运营`;
      }
      return null;
    },
  },
];

function judge(receipt) {
  const violations = [];
  for (const rule of RULES) {
    const why = rule.check(receipt);
    if (why) violations.push({ rule_id: rule.id, why });
  }
  return { service_id: receipt.service_id, violations, schedulable: violations.length === 0 };
}

function main() {
  const args = process.argv.slice(2);
  const asJson = args.includes('--json');
  const writeEvidence = args.includes('--write-evidence');

  const runbook = JSON.parse(fs.readFileSync(RUNBOOK, 'utf8'));

  // 1) 十二张真实班次卡：必须全部可排图
  const serviceResults = runbook.services.map(judge);
  const failedServices = serviceResults.filter((r) => !r.schedulable);

  // 2) 六个变异用例：必须各自被指定规则拦下
  const mutationResults = runbook.rejection_cases.map((c) => {
    const verdict = judge(c.receipt);
    const caughtBy = verdict.violations.map((v) => v.rule_id);
    const caughtByExpected = caughtBy.includes(c.must_violate);
    return {
      case_id: c.case_id,
      must_violate: c.must_violate,
      caught_by: caughtBy,
      caught_by_expected_rule: caughtByExpected,
      rejected: !verdict.schedulable,
      gate_is_live: caughtByExpected && !verdict.schedulable,
      why_zh: c.why_zh,
    };
  });
  const deadGates = mutationResults.filter((m) => !m.gate_is_live);

  const ok = failedServices.length === 0 && deadGates.length === 0;

  const result = {
    protocol: runbook.protocol,
    rules_source: runbook.rules_source,
    ok,
    services_total: serviceResults.length,
    services_schedulable: serviceResults.filter((r) => r.schedulable).length,
    services_failed: failedServices,
    mutation_cases_total: mutationResults.length,
    mutation_cases_caught: mutationResults.filter((m) => m.gate_is_live).length,
    mutation_results: mutationResults,
    dead_gates: deadGates.map((m) => m.case_id),
    disclaimer_zh: runbook.disclaimer_zh,
  };

  if (writeEvidence) {
    fs.writeFileSync(EVIDENCE, JSON.stringify(result, null, 2) + '\n', 'utf8');
    process.stderr.write(`evidence written: ${path.basename(EVIDENCE)}\n`);
  }

  if (asJson) {
    process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  } else {
    const line = '-'.repeat(64);
    console.log('对开协议·桌面推演 / Two-Way Protocol tabletop');
    console.log(line);
    console.log(`规则出处：${runbook.rules_source}`);
    console.log('');
    console.log(`一、十二张班次卡：${result.services_schedulable}/${result.services_total} 满足六条规则，可进入运行图`);
    for (const f of failedServices) {
      console.log(`   ✗ ${f.service_id}: ${f.violations.map((v) => `${v.rule_id} ${v.why}`).join('；')}`);
    }
    console.log('');
    console.log(`二、闸门有效性（变异用例必须被拦下）：${result.mutation_cases_caught}/${result.mutation_cases_total}`);
    for (const m of mutationResults) {
      const mark = m.gate_is_live ? '✓' : '✗';
      console.log(`   ${mark} ${m.case_id} 应违反 ${m.must_violate} → 实际被 ${m.caught_by.join(',') || '（无）'} 拦下`);
    }
    console.log(line);
    console.log(ok ? '结论：对开协议在本运行图上成立，且六道闸门均能判红。' : '结论：不成立，见上方 ✗ 项。');
    console.log(runbook.disclaimer_zh);
  }

  process.exit(ok ? 0 : 1);
}

main();
