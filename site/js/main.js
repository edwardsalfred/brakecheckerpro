// Brake Checker Pro — interactions

(function() {
  'use strict';

  const nav = document.querySelector('.nav');
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelectorAll('.nav-links a');
  const stickyBuy = document.querySelector('.sticky-buy');
  const heroSection = document.querySelector('.hero');
  const footEl = document.querySelector('.foot');

  // Scrolled nav state
  function onScroll() {
    if (window.scrollY > 40) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }

    // Show sticky buy bar after scrolling past hero, hide once footer is in view
    if (heroSection && stickyBuy) {
      const heroBottom = heroSection.offsetTop + heroSection.offsetHeight;
      const pastHero = window.scrollY > heroBottom - 100;
      const footerInView = footEl ? footEl.getBoundingClientRect().top < window.innerHeight - 40 : false;
      if (pastHero && !footerInView) {
        stickyBuy.classList.add('visible');
      } else {
        stickyBuy.classList.remove('visible');
      }
    }
  }

  // Mobile nav drawer
  function closeNav() {
    nav.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-open');
  }
  function toggleNav() {
    const isOpen = nav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.classList.toggle('nav-open', isOpen);
  }

  if (navToggle) {
    navToggle.addEventListener('click', toggleNav);
  }
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (nav.classList.contains('open')) closeNav();
    });
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('open')) closeNav();
  });
  window.addEventListener('resize', () => {
    if (window.innerWidth > 720 && nav.classList.contains('open')) closeNav();
  });

  // Scroll listener
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Reveal-on-scroll
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    revealEls.forEach(el => io.observe(el));

    // Fallback: settle anything in 2x viewport after 600ms
    setTimeout(() => {
      const vh = window.innerHeight * 2;
      revealEls.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < vh) el.classList.add('visible');
      });
    }, 600);

    // Final fallback: force reveal everything after 3s
    setTimeout(() => {
      revealEls.forEach(el => el.classList.add('visible'));
    }, 3000);
  } else {
    revealEls.forEach(el => el.classList.add('visible'));
  }

  // Smooth anchor scrolling with header offset
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId.length <= 1) return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const navHeight = nav ? nav.offsetHeight : 80;
        const top = target.getBoundingClientRect().top + window.scrollY - navHeight - 16;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // Safety net: alert if a Buy link is missing a real checkout URL.
  document.querySelectorAll('[data-buy]').forEach(btn => {
    btn.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (!href || !href.startsWith('http')) {
        e.preventDefault();
        alert('Buy link not configured. Update the Shopify cart URL in the HTML.');
      }
    });
  });

})();
