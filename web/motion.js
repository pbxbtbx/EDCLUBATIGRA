/* One requestAnimationFrame loop per mounted scene; no frame counter affects scoring. */
window.AtigraMotion = (() => {
  let activeLoops = 0;
  function mount(root, options = {}) {
    const media = matchMedia("(prefers-reduced-motion: reduce)");
    let reduced = !!options.reduced || media.matches;
    let paused = !!options.paused,
      destroyed = false,
      frame = 0,
      last = 0;
    let progress = options.initial || 0,
      target = progress,
      phase = options.phase || 0;
    let pulse = 0,
      rewarded = 0,
      resolveCelebration = null,
      celebrationTimer = null;
    const mode = root.dataset.mode;
    const nodes = {
      ship: root.querySelector(".race-ship"),
      meteor: root.querySelectorAll(".meteor"),
      traveler: root.querySelector(".bridge-traveler"),
      explorer: root.querySelector(".explorer"),
      rings: root.querySelectorAll(".portal-ring"),
      core: root.querySelector(".portal-core"),
      dragon: root.querySelector(".mechanical-dragon"),
      wings: root.querySelectorAll(".dragon-wing"),
      stars: root.querySelector(".scene-stars"),
      shield: root.querySelector(".shield"),
      engine: root.querySelector(".engine-flame"),
      chunks: root.querySelectorAll(".rune"),
      parts: root.querySelectorAll(".dragon-parts span"),
      gems: root.querySelectorAll(".resource-grid span"),
      gates: root.querySelectorAll(".race-gate"),
      particles: root.querySelectorAll(".reward-particle"),
      objectives: root.querySelectorAll(".objective-light"),
      beam: root.querySelector(".collect-beam"),
      terrain: root.querySelector(".terrain-back"),
      charge: root.querySelector(".charge span"),
    };
    let width = root.clientWidth;
    const resize = new ResizeObserver(() => {
      width = root.clientWidth;
      paint();
    });
    resize.observe(root);
    function transform(node, value) {
      if (node) node.style.transform = value;
    }
    function paint() {
      const p = progress,
        bob = reduced ? 0 : Math.sin(phase * 2.2) * 3;
      root.style.setProperty("--motion-progress", p);
      root.style.setProperty("--shield", 0.18 + p * 0.82);
      root.style.setProperty("--glow", `${p * 32}px`);
      root.classList.toggle("scene-paused", paused);
      root.classList.toggle("scene-reduced", reduced);
      root.dataset.visualProgress = p.toFixed(4);
      if (nodes.stars)
        transform(
          nodes.stars,
          `translate3d(${reduced ? 0 : (-phase * 1.4) % 45}px,0,0)`,
        );
      if (nodes.terrain)
        transform(nodes.terrain, `translate3d(${-p * 30}px,0,0)`);
      if (mode === "castle") {
        nodes.meteor.forEach((node, i) => {
          const orbit = reduced ? 0 : Math.sin(phase * 0.7 + i * 2) * 5;
          transform(
            node,
            `translate3d(${width * (0.49 + i * 0.12 + p * 0.1)}px,${35 + i * 25 + orbit - pulse * 18}px,0) rotate(${-30 + (reduced ? 0 : phase * 9) + i * 40}deg) scale(${1 - pulse * 0.15})`,
          );
        });
        transform(nodes.shield, `scale(${1 + pulse * 0.08})`);
      }
      if (mode === "race") {
        transform(
          nodes.ship,
          `translate3d(${width * (0.08 + p * 0.73)}px,${bob}px,0) rotate(${-4 + (reduced ? 0 : Math.sin(phase) * 2)}deg)`,
        );
        transform(
          nodes.engine,
          `scaleX(${1 + (reduced ? 0 : Math.sin(phase * 17) * 0.12) + pulse * 0.35})`,
        );
        nodes.gates.forEach((node, i) =>
          node.classList.toggle(
            "passed",
            p >= (i + 1) / (nodes.gates.length + 1),
          ),
        );
      }
      if (mode === "bridge") {
        transform(
          nodes.traveler,
          `translate3d(${width * (0.08 + p * 0.73)}px,${bob * 0.45}px,0)`,
        );
        nodes.chunks.forEach((node, i) => {
          const local = Math.max(0, Math.min(1, p * nodes.chunks.length - i));
          node.style.opacity = 0.16 + 0.84 * local;
          transform(
            node,
            `translate3d(0,${(1 - local) * 25}px,0) scaleY(${0.35 + 0.65 * local})`,
          );
          node.classList.toggle("built", local >= 0.95);
        });
      }
      if (mode === "dragon") {
        transform(nodes.dragon, `translate3d(0,${bob * (0.3 + p)}px,0)`);
        nodes.wings.forEach((node, i) =>
          transform(
            node,
            `rotate(${(i ? -1 : 1) * (8 + p * 14 + (reduced ? 0 : Math.sin(phase * (2 + p)) * p * 15))}deg)`,
          ),
        );
        if (nodes.dragon)
          nodes.dragon.style.filter = `saturate(${0.2 + 0.8 * p})`;
        nodes.parts.forEach((node, i) => {
          const local = Math.max(0, Math.min(1, p * nodes.parts.length - i));
          node.style.opacity = 0.25 + 0.75 * local;
          transform(
            node,
            `rotate(${local * 180 + (reduced ? 0 : phase * 16 * local)}deg) scale(${0.7 + 0.3 * local})`,
          );
          node.classList.toggle("repaired", local >= 0.95);
        });
      }
      if (mode === "explore") {
        transform(
          nodes.explorer,
          `translate3d(${width * (0.06 + p * 0.72)}px,${bob * 0.35}px,0)`,
        );
        nodes.gems.forEach((node, i) => {
          const local = Math.max(0, Math.min(1, p * nodes.gems.length - i));
          transform(
            node,
            `translate3d(0,${-(local * 28) + (reduced ? 0 : Math.sin(phase * 2 + i) * 3)}px,0) scale(${1 - local * 0.8})`,
          );
          node.style.opacity = 1 - 0.9 * local;
          node.classList.toggle("collected", local >= 0.95);
        });
        if (nodes.beam) nodes.beam.style.opacity = reduced ? 0 : pulse * 0.55;
      }
      if (mode === "portal") {
        nodes.rings.forEach((node, i) =>
          transform(
            node,
            `rotate(${(i % 2 ? -1 : 1) * (reduced ? p * 100 : phase * (12 + i * 5))}deg) scale(${0.8 + p * 0.2})`,
          ),
        );
        if (nodes.core) {
          nodes.core.style.opacity = 0.15 + p * 0.8;
          transform(nodes.core, `scale(${0.4 + p * 0.6})`);
        }
      }
      if (nodes.charge) nodes.charge.style.height = `${p * 100}%`;
      nodes.objectives.forEach((node, i) =>
        node.classList.toggle(
          "lit",
          p >= (i + 1) / nodes.objectives.length - 0.006,
        ),
      );
      nodes.particles.forEach((node, i) => {
        const a = (i * Math.PI * 2) / nodes.particles.length;
        node.style.opacity = reduced ? 0 : pulse * 0.8;
        transform(
          node,
          `translate3d(${Math.cos(a) * (1 - pulse) * 75}px,${Math.sin(a) * (1 - pulse) * 45}px,0) scale(${pulse})`,
        );
      });
      options.onFrame?.(p, phase);
    }
    function tick(now) {
      frame = 0;
      activeLoops--;
      if (destroyed || paused || reduced || document.hidden) return;
      const dt = last ? Math.min(0.05, (now - last) / 1000) : 0;
      last = now;
      phase += dt;
      progress += (target - progress) * (1 - Math.exp(-9 * dt));
      if (Math.abs(target - progress) < 0.0001) progress = target;
      pulse = Math.max(0, pulse - dt * 1.6);
      paint();
      schedule();
    }
    function schedule() {
      if (!frame && !destroyed && !paused && !reduced && !document.hidden) {
        frame = requestAnimationFrame(tick);
        activeLoops++;
      }
    }
    function cancel() {
      if (frame) {
        cancelAnimationFrame(frame);
        frame = 0;
        activeLoops--;
      }
      last = 0;
    }
    function visibility() {
      cancel();
      if (!document.hidden) schedule();
    }
    function mediaChanged() {
      reduced = !!options.reduced || media.matches;
      cancel();
      if (reduced) progress = target;
      paint();
      schedule();
    }
    document.addEventListener("visibilitychange", visibility);
    media.addEventListener("change", mediaChanged);
    paint();
    schedule();
    return {
      setTarget(value, units = 0) {
        target = Math.max(0, Math.min(1, value));
        if (units > rewarded) {
          pulse = reduced ? 0 : 1;
          rewarded = units;
        }
        if (reduced) {
          progress = target;
          paint();
        }
        schedule();
      },
      pause(value) {
        paused = value;
        cancel();
        paint();
        schedule();
      },
      celebrate() {
        target = 1;
        pulse = reduced ? 0 : 1;
        root.classList.add("scene-complete");
        if (reduced || paused || document.hidden) {
          progress = 1;
          paint();
          return Promise.resolve();
        }
        schedule();
        return new Promise((resolve) => {
          resolveCelebration = resolve;
          celebrationTimer = setTimeout(() => {
            resolveCelebration = null;
            resolve();
          }, 480);
        });
      },
      destroy() {
        if (destroyed) return;
        destroyed = true;
        cancel();
        resize.disconnect();
        document.removeEventListener("visibilitychange", visibility);
        media.removeEventListener("change", mediaChanged);
        clearTimeout(celebrationTimer);
        resolveCelebration?.();
      },
    };
  }
  return { mount, activeLoops: () => activeLoops };
})();
