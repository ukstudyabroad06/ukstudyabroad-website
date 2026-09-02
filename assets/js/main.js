/* UK Study Abroad — main.js */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    initHeader();
    initMobileNav();
    initFaq();
    initReveal();
    initBackToTop();
    initYear();
    initContactForm();
  });

  // Sticky header shadow on scroll
  function initHeader() {
    var header = document.querySelector(".site-header");
    if (!header) return;
    function onScroll() {
      if (window.scrollY > 12) header.classList.add("scrolled");
      else header.classList.remove("scrolled");
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Mobile nav toggle
  function initMobileNav() {
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.querySelector(".main-nav");
    if (!toggle || !nav) return;
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("open");
      toggle.classList.toggle("active", isOpen);
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      document.body.style.overflow = isOpen ? "hidden" : "";
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.classList.remove("active");
        document.body.style.overflow = "";
      });
    });
  }

  // FAQ accordion
  function initFaq() {
    document.querySelectorAll(".faq-item").forEach(function (item) {
      var q = item.querySelector(".faq-q");
      if (!q) return;
      q.addEventListener("click", function () {
        var wasOpen = item.classList.contains("open");
        item.parentElement.querySelectorAll(".faq-item").forEach(function (i) {
          i.classList.remove("open");
          var qq = i.querySelector(".faq-q");
          if (qq) qq.setAttribute("aria-expanded", "false");
        });
        if (!wasOpen) {
          item.classList.add("open");
          q.setAttribute("aria-expanded", "true");
        }
      });
    });
  }

  // Scroll reveal animation
  function initReveal() {
    var items = document.querySelectorAll("[data-reveal]");
    if (!items.length) return;
    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("in-view"); });
      return;
    }
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.05, rootMargin: "0px 0px 60px 0px" }
    );
    items.forEach(function (el) { observer.observe(el); });

    // Safety net: if anything is somehow never observed as visible
    // (e.g. very short pages, edge-case browsers), reveal it after a delay
    // so content is never permanently hidden.
    setTimeout(function () {
      items.forEach(function (el) { el.classList.add("in-view"); });
    }, 2500);
  }

  // Back to top button
  function initBackToTop() {
    var btn = document.querySelector(".back-to-top");
    if (!btn) return;
    window.addEventListener(
      "scroll",
      function () {
        if (window.scrollY > 500) btn.classList.add("show");
        else btn.classList.remove("show");
      },
      { passive: true }
    );
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Auto-update footer year
  function initYear() {
    document.querySelectorAll("[data-year]").forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  // Contact form (Web3Forms — free, no backend required)
  // Sign up at https://web3forms.com to get a free Access Key, then replace
  // "YOUR_WEB3FORMS_ACCESS_KEY" in contact.html with your real key.
  function initContactForm() {
    var form = document.getElementById("contact-form");
    if (!form) return;
    var statusEl = form.querySelector(".form-status");
    var submitBtn = form.querySelector('button[type="submit"]');

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var accessKey = form.querySelector('input[name="access_key"]');
      if (!accessKey || accessKey.value.indexOf("YOUR_") === 0) {
        showStatus(
          "error",
          "Form is not fully configured yet — please contact us directly via WhatsApp or email (see the buttons above) while the site owner finishes setup."
        );
        return;
      }

      var originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.textContent = "Sending...";

      var formData = new FormData(form);
      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        body: formData,
        headers: { Accept: "application/json" },
      })
        .then(function (res) { return res.json(); })
        .then(function (data) {
          if (data.success) {
            showStatus("success", "Thank you! Your message has been sent. Our team will contact you within 24 hours.");
            form.reset();
          } else {
            showStatus("error", "Something went wrong. Please try again or reach us on WhatsApp.");
          }
        })
        .catch(function () {
          showStatus("error", "Network error. Please try again or reach us on WhatsApp.");
        })
        .finally(function () {
          submitBtn.disabled = false;
          submitBtn.textContent = originalText;
        });
    });

    function showStatus(type, message) {
      if (!statusEl) return;
      statusEl.className = "form-status " + type;
      statusEl.textContent = message;
      statusEl.style.display = "block";
    }
  }
})();
