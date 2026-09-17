/* =====================================================================
   个人展示平台 · 交互脚本
   - 明暗主题切换（记忆用户选择）
   - 导航滚动样式 & 移动端菜单
   - 滚动浮现动画
   - 摄影画廊灯箱
   - 摄影 / 项目 分类筛选
   ===================================================================== */

(function () {
  "use strict";

  /* ---------- 年份 ---------- */
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- 主题切换 ---------- */
  const toggle = document.getElementById("themeToggle");
  const root = document.documentElement;
  const saved = localStorage.getItem("theme");
  if (saved === "dark" || saved === "light") {
    root.setAttribute("data-theme", saved);
  } else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    root.setAttribute("data-theme", "dark");
  }
  function syncToggle() {
    const t = root.getAttribute("data-theme");
    if (toggle) toggle.textContent = t === "dark" ? "☀️" : "🌙";
  }
  syncToggle();
  if (toggle) {
    toggle.addEventListener("click", function () {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      syncToggle();
    });
  }

  /* ---------- 导航：滚动样式 + 移动端菜单 ---------- */
  const nav = document.getElementById("nav");
  const burger = document.getElementById("navBurger");
  const links = document.getElementById("navLinks");

  window.addEventListener("scroll", function () {
    if (nav) nav.classList.toggle("is-scrolled", window.scrollY > 10);
  });

  if (burger && links) {
    burger.addEventListener("click", function () {
      links.classList.toggle("is-open");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("is-open");
      });
    });
  }

  /* ---------- 滚动浮现动画 ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("is-visible");
    });
  }

  /* ---------- 分类筛选（通用，支持多个 .filters 区块） ---------- */
  document.querySelectorAll(".filters").forEach(function (filterGroup) {
    const buttons = filterGroup.querySelectorAll(".filter");
    const section = filterGroup.closest("section");
    if (!section) return;
    const grid = section.querySelector(".gallery, .projects");
    if (!grid) return;
    const items = grid.querySelectorAll(".gallery__item, .project-card");

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        buttons.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        const cat = btn.getAttribute("data-filter");
        items.forEach(function (item) {
          const match = cat === "all" || item.getAttribute("data-cat") === cat;
          item.classList.toggle("is-hidden", !match);
        });
      });
    });
  });

  /* ---------- 摄影画廊灯箱 ---------- */
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightboxImg");
  const lightboxClose = document.getElementById("lightboxClose");

  document.querySelectorAll(".gallery__item img").forEach(function (img) {
    img.addEventListener("click", function () {
      if (!lightbox || !lightboxImg) return;
      lightboxImg.src = img.src;
      lightboxImg.alt = img.alt;
      lightbox.classList.add("is-open");
      lightbox.setAttribute("aria-hidden", "false");
    });
  });
  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove("is-open");
    lightbox.setAttribute("aria-hidden", "true");
  }
  if (lightboxClose) lightboxClose.addEventListener("click", closeLightbox);
  if (lightbox) lightbox.addEventListener("click", function (e) {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeLightbox();
  });
})();
