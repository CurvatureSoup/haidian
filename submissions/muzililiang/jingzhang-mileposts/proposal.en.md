---
title: "The Jing-Zhang Mileposts: From Mile Zero to a World-Class AI Innovation Belt"
author_github: "muzililiang"
language: "en"
proposal_format_version: "2"
bilingual_contract_version: "1"
translation_of: "proposal.md"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "Taking the real mileposts of the Jing-Zhang Railway as a heritage clue, the proposal turns distance into milestones: the Beijing AI Origin Community is Mile Zero, Zhongzhiyuan is the full-stack acceleration segment, and Dazhongsi is the urban terminus. A three-layer milepost system (physical, digital, cultural) organizes space, scenarios, honor, and operations into a markable, celebratable, traceable world-class AI innovation belt."
tracks: ["jingzhang-heritage-narrative", "ai-origin-community", "enterprise-services-ecosystem"]
scenarios: ["ai-traffic-walkability", "ai-health-service-navigation", "enterprise-service-copilot", "robot-delivery-low-speed", "ai-cultural-guide"]
iteration: "v0.1"
---

# The Jing-Zhang Mileposts: From Mile Zero to a World-Class AI Innovation Belt

## Design Basis and Source List

This proposal takes the Qualification Pre-Announcement for the Centennial Jing-Zhang AI Innovation Belt International Urban Design Competition, published by the Haidian Branch of the Beijing Municipal Commission of Planning and Natural Resources, as its primary authority; the announcement establishes the three scope levels, the three key areas, the scale framework of approximately 43.6 km² / 11.4 km² and 368.4 ha, and the required urban-design depth of regulatory detailed planning and comprehensive implementation planning [source:OFFICIAL-ANNOUNCEMENT]. The agent-facing open-call taskbook adds the three positioning statements, five functions, the three-areas-two-wings structure, six agent tasks, and a unified boundary clause, which this proposal treats as the direct task source for concept, scenario, branding, and operation design [source:AGENT-TASKBOOK]. The site package (`brief/site-package/`) provides the enums, allowed design space, planning limits, schemas, and local standard references that govern every machine-readable file in this proposal [source:SITE-PACKAGE].

The public source registry is the boundary for source use: only sources marked `usable_for_formal="yes"` may support formal conclusions, while background_only and provisional_only sources may be used for background narrative, temporary generation, and design discussion only [source:SOURCE-REGISTRY]. Every spatial conclusion in this proposal relies on public sources registered in the repository or on user-provided cleared materials; no non-public planning drawings or internal control indicators are used or claimed.

Because the repository does not yet hold official precise redlines or official polygons for the three key areas, this proposal follows the rules and uses the clearly labeled `provisional_constraint` boundaries from `brief/site-package/geometry/provisional_boundaries.geojson` to produce a temporary formal package [source:BOUNDARY-SOURCE]. These boundaries serve generation, self-check, visualization, and design discussion only; they are not an official redline, approval basis, or precise-area basis. When official polygons are published, the site boundary, key areas, land use, roads, green space, public space, buildings, phasing, and all spatial metrics must be recomputed uniformly [source:KEY-AREA-SOURCE] [depth:three_level_scope_framework].

The recomputed area of the overall design scope is recorded in [data:geometry/site_boundary.geojson#SITE-001] and [metric:site_area_sqm]; the three key areas are expressed by the three KEY_AREA features PROV-KEY-001/002/003 in `key_areas.geojson`, with their count verified by [metric:key_area_count]. Complete indexes of sources, metrics, standards, design depth, and task coverage are kept in `sources.json`, `metrics.json`, `compliance_matrix.json`, `standard_matrix.json`, and `design_depth_matrix.json`; the narrative does not repeat the machine index.

![Evidence chain and submission package relationship](assets/figures/site-overview.png)

## Three-Level Scope Framework

The proposal organizes work in the three levels determined by the announcement; the levels are not a set of disconnected drawings but a cascade from industrial strategy to detailed design [depth:three_level_scope_framework].

**Coordinated research area (approx. 43.6 km²)** answers "why the AI innovation belt is here and how it compares with the world": it studies Haidian's AI industry base, three-areas-two-wings synergy, the organization of the innovation and industrial chains, and the future urban form of the AI era. Its outputs are industrial and future-city strategy, naming, and an ecosystem map, carried in the task responses of `compliance_matrix.json` and `standard_matrix.json`; no new redlines are added.

**Overall design area (approx. 11.4 km²)** answers "how renewal happens": organized around the Jing-Zhang Heritage Park spine, it coordinates land-use, building, road, green-space, public-space, and phasing layers to form a renewal framework at regulatory-plan-level urban-design depth [data:geometry/land_use.geojson#LU-001] [depth:overall_spatial_structure]. All areas and ratios in this layer are recomputable from the submitted geometry ([metric:site_area_sqm], [metric:green_ratio], [metric:building_footprint_area_sqm]); conclusions touching regulatory controls, heights, densities, or redlines are labeled as pending official conditions.

**Key detailed-design area (approx. 368.4 ha)** answers "what happens inside the three cores": the Zhongzhiyuan AI Autonomous Innovation Acceleration Area, the Beijing AI Origin Community, and the Dazhongsi AI Industry Cluster each receive a readable mini-proposal of "positioning + spatial structure + building renewal + mobility + public space + AI scenarios + implementation risk" [depth:three_key_area_detailed_design], mapped to [data:geometry/key_areas.geojson#PROV-KEY-001], [data:geometry/key_areas.geojson#PROV-KEY-002], and [data:geometry/key_areas.geojson#PROV-KEY-003].

| Level | Design question | This proposal's answer | Data anchor |
| --- | --- | --- | --- |
| Coordinated research area | How to organize the AI ecosystem and future urban form | Milepost ecosystem map: university origination—open-source collaboration—enterprise transformation—public experience—international communication | compliance_matrix.json, standard_matrix.json |
| Overall design area | How renewal is drawn | One Belt · Three Cores · Two Wings · Nine Stations structure expressed by land-use/building/road/green/phasing layers | [data:geometry/land_use.geojson#LU-001], [data:geometry/roads.geojson#ROAD-001] |
| Key areas | What happens inside the three cores | Detailed designs for Mile Zero, the full-stack acceleration segment, and the urban terminus | [data:geometry/key_areas.geojson#PROV-KEY-001] [data:geometry/key_areas.geojson#PROV-KEY-002] [data:geometry/key_areas.geojson#PROV-KEY-003] |

All three levels use provisional boundaries. The proposal, HTML, sources, assumptions, and self-check prominently disclose this limitation: boundary precision is `provisional_rough`, the list of layers and metrics to be recomputed after official polygons arrive is in `assumptions.json`, and this organizer data gap itself does not block content scoring.

![Three-level scope and spatial working framework](assets/figures/land-use-structure.png)

## Coordinated Research Area: Industry and Future City Research

### Overall concept: The Jing-Zhang Mileposts

The Jing-Zhang Railway was the first trunk railway designed and built independently by China; along every kilometer stood a milepost—measuring not only the length of the track but the first mileage of Chinese independent innovation. A century later, the AI innovation belt reinvents "distance" as "milestones": **along the Jing-Zhang Heritage Park spine, every kilometer becomes a markable, celebratable, traceable node of AI innovation** [source:AGENT-TASKBOOK] [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK].

- **Physical mileposts**: a network of public-space installations along the park spine; each mile station carries a theme (open source, ecology, scenarios, honor, testing, international) and forms a tangible scale by which the AI era measures its own progress;
- **Digital mileposts**: an open-source milestone protocol—when an open-source project, AI model, or scenario test in the belt reaches a defined node, the corresponding digital milepost "lights up," structurally isomorphic to GitHub Milestones, making contributions versionable;
- **Cultural mileposts**: the 1909 opening of the Jing-Zhang Railway, Zhongguancun's entrepreneurship, and the new AI culture are organized into a centennial timeline read through wayfinding and exhibits at the mile stations.

Each key area has an identity in the milepost system: the **Beijing AI Origin Community is Mile Zero (JZ-K0)**—all innovation starts here, and the Zero Milepost is the spiritual origin; **Zhongzhiyuan is the full-stack acceleration segment (JZ-K4/K5)**—standards, safety governance, and full-stack autonomous innovation are tested here; **Dazhongsi is the urban terminus (JZ-K6)**—AI-native new businesses and international exchange face the world here. The Zhongguancun Technology Service Wing and the Xiaoyuehe Scenario Empowerment Wing form the "two wings" that support global allocation of innovation factors and AI scenario implementation [source:OFFICIAL-ANNOUNCEMENT].

### Naming system and logo direction

- Primary name: **京张里程标**; English name: **The Jing-Zhang Mileposts** (abbr. **JZ-MP**);
- Tagline (Chinese): **从第 0 公里开始**;
- Tagline (English): **Every mile, a milestone.**
- Mileage scale system: JZ-K0 (Origin) → JZ-K1 Ecology Station → JZ-K2 Scenario Station → JZ-K3 Open-Source Station → JZ-K4 Testing Station → JZ-K5 Honor Station → JZ-K6 Terminus; the scale is a conceptual "innovation mileage" symbol, not measured kilometers;
- Logo direction: a railway milepost stone-pedestal silhouette embedding a "0.0 km" digital display and a rail/code double-line symbol, supporting both dark monument and light digital contexts; the visual system uses a three-color identity—off-white base, railway rust red (Jing-Zhang Railway), code green (AI), and stone grey (Zhongguancun). The naming, logo, and visual elements are conceptual directions; no unauthorized fonts, trademarks, or corporate identities are used [source:AGENT-TASKBOOK].

### Five functions and the three-areas-two-wings synergy loop

The proposal maps the five functions to space and mechanisms: the **full-stack autonomous innovation system** is carried by the Zhongzhiyuan full-stack acceleration mileage (standards, safety governance, model testing); the **world-class AI innovation ecosystem** is carried by the "university origination—transformation—open-source collaboration" loop of the Mile Zero Origin Community; the **AI+ scenario empowerment paradigm** is carried by the test-and-validation scenarios of the Xiaoyuehe Scenario Empowerment Wing; the **intelligent, vibrant AI city** is carried by the public scenarios of the urban AI life-experience belt; and **global discourse power in AI governance** is carried by the "Digital Milepost Protocol"—distilling open-source milestones, human review, and red-teaming into exportable governance methods [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]. The synergy loop of the three areas and two wings is: universities and research institutes (origination) → Origin Community (transformation and open source) → Zhongzhiyuan (acceleration and governance) → Dazhongsi (industry and international) → two wings (services and scenarios), flowing back to new origination needs [source:OFFICIAL-ANNOUNCEMENT].

### Global AI innovation ecosystem cases (5–8)

| # | Case | Transferable lesson | Haidian transformation mechanism (conceptual) |
| --- | --- | --- | --- |
| 1 | London King's Cross regeneration | Railway heritage district regenerated as a knowledge district; TOD plus creative industries and headquarters offices | The closest analog for the Jing-Zhang Heritage Park corridor; integrated heritage-park—innovation-district development model |
| 2 | Kendall Square, Cambridge | Near-campus innovation, biotech and AI clustering, high-density innovation exchange space | Origin Community "near-campus" spatial organization and transformation service chain |
| 3 | Stanford Research Park, Silicon Valley | Closed loop of university origination—venture capital—industrial clustering | Capital and IP service mechanisms of the Zhongguancun Technology Service Wing |
| 4 | Dream Town / Future Sci-Tech City, Hangzhou | Talent special zone, digital economy ecosystem, low-cost start space | Combined supply of talent apartments, incubators, and open scenarios |
| 5 | Jurong Innovation District (JID), Singapore | National-level testbed and government–industry–academia collaboration | Zhongzhiyuan full-stack testing ground and standards governance sandbox |
| 6 | Toronto AI cluster | Building industry and ethical governance discourse simultaneously | Governance output mechanism of the Digital Milepost Protocol |
| 7 | Helsinki open city data | Urban agents and public-data governance practice | Urban-agent governance desk and public-source review mechanism |

These cases extract mechanisms only; no unauthorized company lists, investment figures, or output values are cited. Any mechanism transformed into space, operation, or scenarios is expressed as a conceptual suggestion [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]. Industrial strategy ultimately lands on a visible, verifiable spatial structure: land-use layers express functional zoning [data:geometry/land_use.geojson#LU-001], public-space layers express the exchange network [data:geometry/public_space.geojson#PUBLIC-001], blue-green layers express the continuous green system [data:geometry/green_space.geojson#GREEN-001], and professional coordination follows [standard:MOHURD-URBAN-DESIGN-MEASURES].

## Overall Design Area: Urban Renewal and Regulatory-Plan-Level Urban Design

### Spatial structure: One Belt · Three Cores · Two Wings · Nine Stations

The overall design area takes the **Jing-Zhang Heritage Park innovation spine** as its skeleton (One Belt), connects the **three key cores** (Three Cores), links the **Zhongguancun Technology Service Wing and the Xiaoyuehe Scenario Empowerment Wing** (Two Wings), and places **nine themed mile stations** along the spine (Nine Stations, conceptual): JZ-K0 Zero Milepost (Origin Community), JZ-K1 Ecology Station (Qinghe interface), JZ-K2 Scenario Station (Xiaoyuehe), JZ-K3 Open-Source Station (Beihang/BUPT segment), JZ-K4 Testing Station (south Zhongzhiyuan), JZ-K5 Honor Station (north Zhongzhiyuan), JZ-K6 Terminus (Dazhongsi), plus two gateway nodes (North Fifth Ring gateway, Xizhimen gateway) [depth:overall_spatial_structure].

The spine is not a new redline; it translates the north-south connection and east-west stitching goals of the heritage park into a composite system of slow mobility, green space, public space, and AI scenarios: low-efficiency spaces on both sides of the park are identified as renewal objects; campuses, parks, and neighborhoods are stitched by walking and cycling; and rail stations (Wudaokou, Qinghua East Road West, Dazhongsi) become integrated interchange points of the mile stations [standard:MOHURD-CONTROL-DETAILED-PLANNING]. The overall land-use layout is in [data:geometry/land_use.geojson#LU-001] and the phasing is in [data:geometry/phasing.geojson#PHASE-001].

### Industrial goals, functional layout, and innovation indicator system

Based on Haidian's "1+X+1" industrial system and "AI+" vertical applications, the proposal sketches a functional-share concept for the three cores (conceptual): the Origin Community centers on **cultural display and transformation** (led by cultural land 0803 and educational land 0804), Zhongzhiyuan centers on **research and full-stack acceleration** (led by research land 0802), and Dazhongsi centers on **commercial services and the intelligent economy** (led by commercial land 05) [source:OFFICIAL-ANNOUNCEMENT]. The submitted geometry recomputes about 1.45 million m² of research land, 2.47 million m² of educational land, and 1.25 million m² of commercial-services land [metric:scientific_research_land_area_sqm] [metric:education_research_land_area_sqm] [metric:commercial_land_area_sqm]; these recomputed values provide order-of-magnitude anchors for design discussion. AI innovation index, talent density, and output scale have no official statistics and are recorded as pending calibration in [metric:ai_innovation_index] and [metric:talent_density]; no fabricated numbers are presented.

### Overall renewal framework

The renewal framework organizes objects into four conceptual categories—**retain, renovate, renew, reserve**: **retain** the Jing-Zhang Railway heritage, the Qinghuayuan Station site (indicative protection area in [data:geometry/constraints.geojson#CONSTR-07]) and existing university research buildings; **renovate** low-efficiency industrial spaces and aging community service facilities; **renew** industrial carriers, slow-mobility gaps, and public-space nodes; **reserve** parcels without sufficient conditions (about 195,000 m² of reserve land in [data:geometry/land_use.geojson#LU-001], pending ownership and regulatory conditions). Project functions, AI-enterprise agglomeration targets, and industrial space scale are conceptual; implementation policy and phasing are detailed in the "Renewal Projects, Implementation Policy, and Phasing" chapter [depth:retain_renovate_demolish].

### Building scale and carrying capacity

The submitted geometry contains a conceptual building footprint of about 985,000 m² [metric:building_footprint_area_sqm] and a design density of about 8.6% [metric:building_density], serving only as order-of-magnitude references for spatial organization. Regulatory indicators—floor area ratio, building height, building density, green ratio, setbacks—are labeled **pending official regulatory conditions** until the approved regulatory plan is published; they must not be disguised as approved values [standard:MOHURD-CONTROL-DETAILED-PLANNING]. Transport, rail, municipal, and supporting facility layouts are developed in the corresponding chapters [depth:traffic_rail_slow_parking] [depth:municipal_new_infrastructure].

## Detailed Design of Key Areas

All three key areas use provisional polygons; every conclusion is directional design. When official polygons are published, geometry, metrics, and drawings must be redone against the new boundaries [data:geometry/key_areas.geojson#PROV-KEY-001] [depth:three_key_area_detailed_design].

### Zhongzhiyuan AI Autonomous Innovation Acceleration Area—"full-stack acceleration segment" (JZ-K4/K5)

- **Positioning**: a garden-style full-stack autonomous innovation block; the acceleration and governance test segment of the national AI platform.
- **Spatial structure**: the Qinghe interface forms the ecological base (conceptual Qinghe Low-Carbon Innovation Corridor, [data:geometry/green_space.geojson#GREEN-001]); research land forms the industrial main body; the Fifth Ring interface transitions through protective green space; external transport optimization is proposed along the North Fifth Ring and Jingzang Expressway corridors.
- **Building renewal**: a mixed concept of R&D, laboratories, incubators, and talent apartments; existing building stock awaits official data.
- **Mobility**: the northern spine connects to the Wudaokou-direction slow network; a waterfront trail runs along the Qinghe.
- **Public space**: the full-stack testing ground (model standard evaluation, red-teaming, safety-governance sandbox display) combined with industry-display functions [source:AGENT-TASKBOOK].
- **AI scenarios**: JZ-T1 Full-Stack Testing Ground (industry test/validation), JZ-05 Qinghe Low-Carbon Innovation Corridor.
- **Implementation risk**: Qinghe blue-line, ecological, and flood-control conditions pending; platform facilities and timing are constrained by higher-level arrangements.

### Beijing AI Origin Community—"Mile Zero" (JZ-K0)

- **Positioning**: a near-campus AI innovation block; the origination and transformation point for original innovation from Tsinghua, Peking University, and the CAS—and the zero point of the whole milepost system.
- **Spatial structure**: centered on the Zero Milepost Plaza ([data:geometry/public_space.geojson#PUBLIC-SPINE-0KM]); cultural-display land organizes release events and open-source collaboration, educational-research land connects to universities, and residential and community-service land secures talent life [data:geometry/land_use.geojson#LU-001].
- **Building renewal**: a low-disturbance, organic renewal model (conceptual): ground floors for display, release, incubation, and community services; upper floors for talent apartments and small offices; heritage-sensitive design around the Qinghuayuan Station site (indicative protection area [data:geometry/constraints.geojson#CONSTR-07]).
- **Mobility**: integrated design around Wudaokou and Qinghua East Road West rail stations; slow-mobility stitching of campus—park—neighborhood [source:OFFICIAL-ANNOUNCEMENT].
- **Public space**: Zero Milepost installation, open-source showcase gallery, and contributor honor wall (conceptual).
- **AI scenarios**: JZ-0KM Zero Release Hall (industry test/validation), JZ-06 Transformation Street.
- **Implementation risk**: campus boundaries, ownership, and ground-floor program changes require multi-party coordination; low-disturbance renewal depends on property-rights coordination mechanisms.

### Dazhongsi AI Industry Cluster—"urban terminus" (JZ-K6)

- **Positioning**: an urban intelligent-economy block; the display, trade, and international-exchange interface for AI-native and AI+ new businesses such as agents, intelligent terminals, and content consumption.
- **Spatial structure**: organized around Dazhongsi Station with four-quadrant pedestrian connectivity (conceptual, [data:geometry/public_space.geojson#PUBLIC-001]); commercial-services land carries AI-native consumption [data:geometry/land_use.geojson#LU-001]; planned green space is co-used for public experience.
- **Building renewal**: upgrading the public environment around anchor enterprises and studying potential parcels (conceptual); mixed commercial services and research offices.
- **Mobility**: Dazhongsi Station integration, four-quadrant pedestrian connectivity, bicycle parking, and static-traffic organization (conceptual) [source:OFFICIAL-ANNOUNCEMENT].
- **Public space**: International Roadshow Lounge and Data-Element Reception Hall (conceptual).
- **AI scenarios**: JZ-03 International Roadshow Lounge, JZ-04 Data-Element Reception Hall.
- **Implementation risk**: station renovation and intersection engineering conditions pending; enterprise buildings and owned spaces must not be modified without authorization.

![Key areas index and design tasks](assets/figures/key-areas.png)

## AI Innovation Ecosystem, Personas, and AI+ Scenarios

### Six user personas

| Persona | Typical needs | Spatial response (conceptual) | Privacy and self-check boundary |
| --- | --- | --- | --- |
| Open-source developer | Release, collaboration, testing, community reputation, recorded contribution | Zero Release Hall in Origin Community, open-source showcase gallery, contributor milepost installation, night collaboration space | No personal behavior tracking; event data aggregated only |
| AI start-up team | Low-cost office, compute access, product testbed, policy services | Shared testing ground in Zhongzhiyuan, edge-compute stations, combined incubator and talent apartments | Compute and data services require separate authorization |
| Anchor-enterprise visitors & executives | Showcase, negotiation, international reception, recruiting | International Roadshow Lounge in Dazhongsi, station interchange, public environment around anchor enterprises | Enterprise identities and cases require cleared rights |
| University faculty & students | Transformation, cross-campus collaboration, daily mobility, academic exchange | Campus—park slow stitching, Transformation Street, AI education experience points | Campus data and research results require authorization |
| Local residents | Commute, leisure, community services, low-disturbance renewal | Heritage Park slow loop, embedded community services, graded night lighting | Resident profiles not used for commercial recommendation |
| City managers & governance bodies | AI governance, scenario oversight, open decision-making, public participation | Urban-agent governance desk, milestone-protocol review nodes | Governance data public; human review as backstop |

The six personas exceed the required five persona categories; the scenario—space—operation mapping follows in the next subsection [source:AGENT-TASKBOOK].

### Twelve AI scenario cards

All scenario cards are conceptual; those involving testing are labeled "industry test/validation." All scenarios follow data minimization, public sources, explainability, and human review [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK].

| # | Scenario card | Spatial carrier | Users | Operating data | Privacy boundary and human review | Layer/metric |
| --- | --- | --- | --- | --- | --- | --- |
| JZ-0KM | Zero Release Hall (industry test/validation) | Zero Milepost Plaza, Origin Community | Open-source developers, start-ups | Release records, open-source license labels | Public materials; human copyright review [metric:ai_testing_scenario_count] | public_space.geojson#PUBLIC-SPINE-0KM |
| JZ-T1 | Full-Stack Testing Ground (industry test/validation) | Zhongzhiyuan | Model teams, governance bodies | Standard evaluation, red-team records | Test data de-identified; results human-reviewed | land_use.geojson (0802) |
| JZ-T2 | Edge-Compute Station (industry test/validation) | Nodes across the overall area | Start-ups, residents | Aggregated energy and compute use | No personal content collection; energy data public | constraints.geojson |
| JZ-01 | Milepost Slow-Mobility Navigation | Heritage Park spine | Residents, visitors, commuters | Aggregated gap/congestion data | Low-intrusion sensing; no individual tracking [metric:ai_scenario_card_count] | roads.geojson#ROAD-001 |
| JZ-02 | Open-Source Showcase Gallery | Open-Source Station on the spine | Developers, public | Public records of projects and PR contributions | Contributor-authorized display | public_space.geojson |
| JZ-03 | International Roadshow Lounge | Dazhongsi | Enterprise visitors, international bodies | Event booking, matchmaking | Business data de-identified; enterprise cases cleared | key_areas.geojson#PROV-KEY-003 |
| JZ-04 | Data-Element Reception Hall | Dazhongsi | Data-service firms, regulators | Data-element circulation demo | Compliant, auditable, revocable authorization | land_use.geojson (05) |
| JZ-05 | Qinghe Low-Carbon Innovation Corridor | Qinghe interface, Zhongzhiyuan | Enterprises, residents | Aggregated energy, runoff, carbon | Public dashboards; ecological data human-reviewed | green_space.geojson#GREEN-001 |
| JZ-06 | Transformation Street | Origin Community | Faculty, students, start-ups | Transformation and IP services | Research authorization; de-identified service records | buildings.geojson#BLDG-001 |
| JZ-07 | AI Life Model Street | Community–commerce interface | Residents | AI+ health/education/legal/life services | Strict privacy boundary; human review and complaints channel [metric:user_persona_count] | land_use.geojson (05/0701) |
| JZ-08 | Urban-Agent Governance Desk | Public governance node | Managers, public | Public materials, scenario rehearsal, feedback | Public data; human review backstop | compliance_matrix.json |
| JZ-09 | Milepost Festival public route | Belt-wide public space | All publics | Participation, aggregated tours | Aggregated event data; cleared copyright | phasing.geojson#PHASE-001 |

JZ-0KM, JZ-T1, and JZ-T2 are the three AI industry test/validation scenarios; all twelve cards satisfy the requirement of no fewer than ten scenario cards [source:AGENT-TASKBOOK] [metric:ai_testing_scenario_count].

## Land Use, Building Scale, and Retain-Renovate-Demolish Strategy

### Land-use layout

Land-use zones follow the land codes of the Guide to Land and Sea Use Classification for Territorial-Space Surveys, Planning, and Use Control [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE]; the partition seamlessly covers the submitted boundary (symmetric difference of zero). Recomputed main land uses within the overall design area (EPSG:4548, provisional boundary): educational land about 2.468 million m² (21.6%), research land about 1.451 million m² (12.7%), residential land about 1.678 million m² (14.7%), commercial-services land about 1.254 million m² (11.0%), cultural land about 0.507 million m² (4.4%), medical land about 0.277 million m² (2.4%), road land about 0.545 million m² (4.8%), green space about 2.679 million m² (23.5%), plazas about 0.258 million m² (2.3%), and reserve land about 0.195 million m² (1.7%) [data:geometry/land_use.geojson#LU-001] [metric:land_use_area_sqm]. The shares express a "blue-green foundation, innovation-led, livable" structure supporting an integrated work—life—social—learning environment for talent.

### Building scale and retain-renovate-demolish

The conceptual building footprint is about 985,000 m² [metric:building_footprint_area_sqm], organized by building type (AI R&D, labs, incubators, mixed use, education, residential, talent apartments, community services, cultural display, etc.), see [data:geometry/buildings.geojson#BLDG-001] [depth:height_massing_character]. Retain-renovate-demolish is organized conceptually in four categories: **retain** (heritage, protected structures, existing university research buildings), **renovate** (low-efficiency industrial space, aging community services), **renew** (industrial carriers, public space), and **reserve** (parcels pending conditions). Because existing building stock, ownership, and regulatory conditions are missing, retain-renovate-demolish expresses method and a pending-calibration list, not parcel-level conclusions [depth:retain_renovate_demolish]; regulatory values—floor area ratio, height, density, green ratio—remain pending official conditions until the approved regulatory plan is published (see [metric:floor_area_ratio], [metric:building_height_m], [metric:green_ratio_official]).

## Transport, Rail, Municipal Infrastructure, and Public Services

### Transport and slow mobility

The proposal organizes "spine slow mobility + rail interchange + branch-road microcirculation" (conceptual): the heritage-park spine forms a north-south continuous pedestrian-and-cycle corridor connecting the three rail interchange points of Wudaokou, Qinghua East Road West, and Dazhongsi [data:geometry/roads.geojson#ROAD-001] [metric:road_network_length_m]; external transport optimization along the North Fifth Ring and Jingzang Expressway corridors follows the Fifth Ring integrated planning direction; overpass nodes, slow-mobility gaps, and accessibility shortfalls are listed as engineering conditions for deepening [depth:traffic_rail_slow_parking]. Bicycle parking and static traffic concentrate at station quadrants and public-space nodes.

### Rail-station integration

Wudaokou, Qinghua East Road West (Origin Community), and Dazhongsi (industry cluster) are organized as mile stations for integrated design: stations connect directly by walking networks to the Zero Milepost Plaza, showcase galleries, and roadshow lounges, encouraging function mixing around stations [source:OFFICIAL-ANNOUNCEMENT].

### Municipal infrastructure and new infrastructure

AI industrial-service facilities, innovation-platform services, and talent-life facilities are conceptually distributed by service radius (method and standard direction proposed; detailed layout pending professional deepening). New infrastructure explores an integrated model of "distributed energy + edge compute + traditional municipal facilities" (conceptual, e.g., edge-compute station prototypes); traditional utilities rely on upgrading existing systems [depth:municipal_new_infrastructure]. Utility, energy, drainage, flood-control, and fire-safety data are missing and listed as prerequisites for formal deepening.

![Mobility, blue-green, and public-space composite system](assets/figures/mobility-bluegreen.png)

## Blue-Green Network, Public Space, and Urban Character

### Blue-green network and the Jing-Zhang Heritage Park vitality belt

With the Heritage Park vitality belt as the skeleton, the proposal coordinates the Qinghe and Xiaoyuehe blue-green spaces into a north-south continuous, east-west connected pedestrian, cycle, and green-space system (conceptual) [data:geometry/green_space.geojson#GREEN-001] [depth:blue_green_public_space]. The submitted geometry contains about 2.679 million m² of green space, a green ratio of about 23.5% [metric:green_ratio]—a design recomputation supporting the "blue-green foundation" quality judgment, not an approved official green ratio. Public space (including the Dazhongsi four-quadrant plaza and spine public nodes) totals about 1.066 million m², about 9.3% [metric:public_space_ratio], supporting innovation exchange and public experience.

### AI public space and pilgrimage landmarks (no fewer than three)

Four AI pilgrimage landmarks and honor-display nodes are set along the spine (conceptual) [source:AGENT-TASKBOOK]:

1. **Zero Milepost (JZ-K0)**: the "0.0 km" installation in the Origin Community; all innovation starts here—the spiritual origin of "starting from zero" [data:geometry/public_space.geojson#PUBLIC-SPINE-0KM];
2. **Centennial Mile Wall**: a timeline installation of Jing-Zhang 1909 → Zhongguancun → AI 2026 on the spine, turning a century of independent innovation into a walkable public exhibition [data:geometry/public_space.geojson#PUBLIC-SPINE-K2];
3. **Contributor Milepost digital installation**: linked to the Digital Milepost Protocol—when an open-source project, model, or scenario test reaches a node, one notch lights up and contributor names enter the honor wall (echoing the call's "agent contribution honor wall, AI milestones" memorial system) [data:geometry/public_space.geojson#PUBLIC-SPINE-K1] [data:geometry/public_space.geojson#PUBLIC-SPINE-K4];
4. **Dazhongsi "Terminus" urban landmark**: the International Roadshow Lounge and four-quadrant plaza as a window to the world [data:geometry/public_space.geojson#PUBLIC-001].

The landmark count satisfies the requirement of no fewer than three [metric:ai_landmark_count]. All installations, logos, fonts, images, and personal/business identities require cleared rights; nothing may be over-entertained or presented as approved construction.

### Urban character

The urban tone fuses three cultural temperaments (conceptual): the **engineering rationality** of the Jing-Zhang Railway (rust red, stone, rail symbols), the **innovation sharpness** of Zhongguancun (glass curtain walls, luminous interfaces, stone grey), and the **code order** of AI culture (modular, editable, digital display). Heritage resources such as the Qinghuayuan Station site are displayed and used with low disturbance; the Qinghe and Xiaoyuehe waterfronts shape livable, workable, enjoyable interfaces; renewal-capable areas receive guiding directions for building height, intensity, character, roof form, massing, and interfaces—specific control values pending official regulatory and heritage conditions [standard:MOHURD-URBAN-DESIGN-MEASURES].

## Renewal Projects, Implementation Policy, and Phasing

### Renewal project list

| No. | Project | Type | Location | Key dependencies | Evidence |
| --- | --- | --- | --- | --- | --- |
| JZ-01 | Zero Milepost Plaza | Public space/Culture | Origin Community | Ownership, heritage, mobility connectivity review | [data:geometry/public_space.geojson#PUBLIC-SPINE-0KM] |
| JZ-02 | Centennial Mile Wall | Public space/Culture | Mid-spine | Heritage-park management, event permits | [data:geometry/public_space.geojson#PUBLIC-SPINE-K2] |
| JZ-03 | Contributor Milepost Installation | Public space/Digital facility | Open-Source Station on spine | Protocol design, copyright clearance | [data:geometry/public_space.geojson#PUBLIC-SPINE-K1] |
| JZ-04 | Full-Stack Testing Ground | Industrial service | Zhongzhiyuan | Platform resources, safety governance conditions | research land layer 0802 |
| JZ-05 | Qinghe Low-Carbon Innovation Corridor | Blue-green space | Qinghe interface, Zhongzhiyuan | River blue line, ecological and flood conditions | [data:geometry/green_space.geojson#GREEN-001] |
| JZ-06 | Transformation Street | Urban renewal/Industrial service | Origin Community | Campus boundary, ownership, ground-floor program | building-type mapping in buildings.geojson |
| JZ-07 | Dazhongsi Four-Quadrant Pedestrian Connectivity | Rail integration/Slow mobility | Dazhongsi | Station, intersection, utility lines | [data:geometry/public_space.geojson#PUBLIC-001] |
| JZ-08 | International Roadshow Lounge | Industrial service/Public space | Dazhongsi | Enterprise collaboration, event operation | PROV-KEY-003 in key_areas.geojson |
| JZ-09 | Edge-Compute Station Network | New infrastructure/Public service | Overall area | Energy, compute, security, operator | [data:geometry/constraints.geojson#CONSTR-01] |
| JZ-10 | Milepost Festival route and operation system | Operation/Brand | Belt-wide public space | Public-space permits, event safety, copyright | PHASE-001 in phasing.geojson |

All projects are conceptual; implementing bodies, funding, timing, and approval paths await professional deepening [depth:renewal_project_list].

### Implementation policy suggestions (conceptual)

Coordinated urban-renewal implementation (district-level coordination, property-rights synergy, low-disturbance renewal), industrial-space supply policy (combined incubators and talent apartments), scenario-open operation policy (booking-based testbed opening, compliant data-element circulation), public participation (open comment channels, human review), and the governance-method output of the "Digital Milepost Protocol." All policy mechanisms are directions for professional teams to deepen [source:AGENT-TASKBOOK].

### Phasing (conceptual)

Near term (2026–2028): lighting up the Zero Milepost, slow-mobility stitching in the Origin Community, spine pilot installations, the first Milepost Festival [data:geometry/phasing.geojson#PHASE-001]; mid term (2029–2031): the Zhongzhiyuan full-stack testing ground, Dazhongsi four quadrants, the Data-Element Reception Hall [data:geometry/phasing.geojson#PHASE-002]; long term (2032–2035): the complete mile-station network, the global event system, and deepening of the two wings [data:geometry/phasing.geojson#PHASE-003]. Phasing areas are recomputed in [metric:phase_1_area_sqm], [metric:phase_2_area_sqm], and [metric:phase_3_area_sqm].

### Global AI innovation event system and long-term operation (agent.6 response)

**Annual event system** (conceptual): the annual **Milepost Day** each September (echoing the call's implementation rhythm; includes open-source releases, testbed open days, and milestone-lighting ceremonies) and **Zero Open Day** each March (developer community and university linkage); **event branding**: "milepost lighting" as the core visual, with bilingual communication materials; **developer-community operation**: contributor profiles, an annual milestone report, hackathons, and a residency program; **scenario-open operation**: booking-based opening of test/validation scenarios, red-teaming, and safety-governance workshops; **public experience and landmark operation**: guided tours and renewal of exhibitions at the Centennial Mile Wall and Zero Milepost; **international communication and conversion**: the "Mile Zero" global narrative and the roadshow→landing-service→policy path. All events, investment, funding, and policy arrangements are conceptual and do not constitute confirmed government arrangements [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK].

## Metrics, Area Recalculation, and Compliance Matrix

Metrics fall into three categories: **spatial recomputation metrics** (directly recomputable from the submitted geometry): overall design area 1,141.3 ha [metric:site_area_sqm], green ratio about 23.5% [metric:green_ratio], public-space share about 9.3% [metric:public_space_ratio], and building footprint about 985,000 m² [metric:building_footprint_area_sqm]—road network, key-area totals, and phasing areas are recorded under their own metrics in `metrics.json`; **metrics pending official regulatory conditions**: floor area ratio [metric:floor_area_ratio] and building height [metric:building_height_m] (official green ratio likewise pending); **performance metrics pending professional calibration**: the AI innovation index [metric:ai_innovation_index] and talent density. Formulas, source files, and confidence for all known metrics are in `metrics.json`, and recalculation follows the unified depth requirement [depth:metrics_recalculation].

Task coverage is governed by `compliance_matrix.json`: the 16 tasks of announcement sections 1.3, 1.4, and 1.5 and the six agent tasks (agent.1–agent.6) are mapped one by one to report sections, layers, metrics, drawings, HTML pages, sources, assumptions, and self-checks; `standard_matrix.json` covers the five mandatory professional standards; `design_depth_matrix.json` marks all required design-depth items complete. The three matrices together ensure the proposal is a traceable, recomputable, reviewable evidence chain rather than slogans [depth:metrics_recalculation].

![Core metrics recalculation and evidence chain](assets/figures/metrics-evidence.png)

## Risk, Copyright, and Compliance

**Material legality**: this proposal uses only official public materials, repository-registered materials, and user-provided cleared materials; it does not use non-public planning drawings, non-public spatial data, internal control indicators, or personal private information [source:SOURCE-REGISTRY]. **Boundary risk**: provisional boundaries must not be treated as official redlines, approval bases, or precise-area bases; all spatial layers and metrics must be recomputed after official polygons are published [source:BOUNDARY-SOURCE]. **Regulatory risk**: floor area ratio, height, density, green ratio, redlines, and setbacks await official regulatory conditions; the proposal does not fabricate precision [standard:MOHURD-CONTROL-DETAILED-PLANNING]. **Privacy and ethics**: AI scenarios follow data minimization, public sources, explainability, and human review; urban agents do not replace planning approval or output unauthorized personal profiles. **Copyright**: naming, logo, fonts, images, cases, and corporate identities require cleared rights; for AI-generated content the author is responsible for facts, citations, and expression; the package license is COMMUNITY-DISPLAY-ONLY, with the full statement in `report/copyright_statement.md`. **Bilingual**: this proposal is the English translation of the primary Chinese report `proposal.md`; HTML, drawings, and text-bearing figures provide matching language versions. **Official endorsement**: this proposal does not claim official approval, approved regulatory plans, final ownership, confirmed building scale, or guaranteed implementation; all spatial landing, event operation, and policy mechanisms are conceptual suggestions, reference schemes, or materials for professional teams to deepen [source:AGENT-TASKBOOK].

## References

- Haidian Branch, Beijing Municipal Commission of Planning and Natural Resources: Qualification Pre-Announcement for the Centennial Jing-Zhang AI Innovation Belt International Urban Design Competition (2026-05-09)
- Excerpt of the agent-facing open-call taskbook for the "Centennial Jing-Zhang AI Innovation Belt Urban Design Open Call" (user-provided cleared material)
- Beijing Municipal Science & Technology Commission and Zhongguancun Administrative Committee: "Three Areas, Two Wings: Building a World-Class AI Agglomeration" (2026-04-03)
- Haidian District People's Government: "1+X+1" modern industrial system layout (2026-03-02)
- Ministry of Housing and Urban-Rural Development: Measures for the Administration of Urban Design (2017)
- Ministry of Housing and Urban-Rural Development: Measures for the Compilation, Review, and Approval of Regulatory Detailed Plans for Cities and Towns
- Ministry of Natural Resources: Guide to Land and Sea Use Classification for Territorial-Space Surveys, Planning, and Use Control (2023)
- OpenStreetMap Copyright and License (ODbL; background reference only)
- Repository site package `brief/site-package/`, public source registry `data/source_registry.json`, and processed materials `data/processed/`
- Complete machine index: `sources.json`, `metrics.json`, `compliance_matrix.json`, `standard_matrix.json`, `design_depth_matrix.json` [source:SITE-PACKAGE]
