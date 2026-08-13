(() => {
  document.documentElement.classList.add("js");
  const root = document.querySelector(".review-walk-shell");
  if (!root) return;

  const steps = [...root.querySelectorAll("[data-step]")];
  const links = [...root.querySelectorAll("[data-step-link]")];
  const live = root.querySelector("[data-live]");
  if (!steps.length) return;

  const valid = new Set(steps.map((step) => step.id));
  const initialHash = location.hash.slice(1);
  let current = valid.has(initialHash) ? initialHash : steps[0].id;

  function show(id, focus = false, updateHash = true) {
    current = valid.has(id) ? id : steps[0].id;
    steps.forEach((step, index) => {
      const active = step.id === current;
      step.hidden = !active;
      step.setAttribute("aria-hidden", String(!active));
      const previous = step.querySelector("[data-prev]");
      const next = step.querySelector("[data-next]");
      if (previous) previous.disabled = index === 0;
      if (next) next.disabled = index === steps.length - 1;
      if (active && focus) step.querySelector("h3")?.focus();
    });
    links.forEach((link) => {
      link.setAttribute(
        "aria-current",
        link.getAttribute("href") === `#${current}` ? "step" : "false",
      );
    });
    const number = steps.findIndex((step) => step.id === current) + 1;
    if (live) live.textContent = `${number} / ${steps.length}`;
    if (updateHash) history.replaceState(null, "", `#${current}`);
  }

  steps.forEach((step, index) => {
    step.querySelector("[data-prev]")?.addEventListener("click", () => {
      show(steps[Math.max(0, index - 1)].id, true);
    });
    step.querySelector("[data-next]")?.addEventListener("click", () => {
      show(steps[Math.min(steps.length - 1, index + 1)].id, true);
    });
  });
  links.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      show(link.hash.slice(1), true);
    });
  });
  addEventListener("hashchange", () => {
    const id = location.hash.slice(1);
    if (valid.has(id)) show(id, true, false);
  });
  root.addEventListener("keydown", (event) => {
    if (event.target.closest("a, button, summary, details, input, textarea, select")) return;
    const index = steps.findIndex((step) => step.id === current);
    const destinations = {
      ArrowRight: steps[Math.min(steps.length - 1, index + 1)].id,
      ArrowLeft: steps[Math.max(0, index - 1)].id,
      Home: steps[0].id,
      End: steps.at(-1).id,
    };
    if (!destinations[event.key]) return;
    event.preventDefault();
    show(destinations[event.key], true);
  });

  // Preserve pre-existing dashboard deep links such as #baseline.
  show(current, false, !initialHash || valid.has(initialHash));
})();
