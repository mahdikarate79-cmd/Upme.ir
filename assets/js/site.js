(function () {
    'use strict';

    var COUNTER_URL = 'https://upmee.site/counter.php';
    var downloadCount = 700000;

    async function fetchCount() {
        try {
            var res = await fetch(COUNTER_URL);
            var data = await res.json();
            downloadCount = data.count || 700000;
            updateDisplay();
        } catch (e) {
            updateDisplay();
        }
    }

    async function trackDownload() {
        downloadCount += 1;
        updateDisplay();
        try {
            await fetch(COUNTER_URL, { method: 'POST' });
        } catch (e) {}
    }

    function updateDisplay() {
        var formatted = Number(downloadCount).toLocaleString('fa-IR');
        document.querySelectorAll('#nav-count, #hero-count, #footer-count').forEach(function (el) {
            el.textContent = el.id === 'hero-count' ? formatted + '+' : formatted;
        });
    }

    window.trackDownload = trackDownload;

    function initMusic() {
        var bgMusic = document.getElementById('bg-music');
        var musicToggle = document.getElementById('music-toggle');
        if (!bgMusic || !musicToggle) return;

        var musicIcon = musicToggle.querySelector('.music-icon');
        var isPlaying = false;
        var loaded = false;

        bgMusic.volume = 0.3;

        function ensureAudio() {
            if (!loaded) {
                bgMusic.src = '/background-music.mp3';
                loaded = true;
            }
        }

        musicToggle.addEventListener('click', function () {
            if (isPlaying) {
                bgMusic.pause();
                musicIcon.textContent = '🔇';
                musicToggle.classList.remove('playing');
                isPlaying = false;
                return;
            }
            ensureAudio();
            bgMusic.play().then(function () {
                isPlaying = true;
                musicIcon.textContent = '🔊';
                musicToggle.classList.add('playing');
            }).catch(function () {
                isPlaying = false;
                musicIcon.textContent = '🔇';
            });
        });
    }

    function initFaq() {
        document.querySelectorAll('.faq-question').forEach(function (btn) {
            btn.addEventListener('click', function () {
                var item = btn.parentElement;
                var isOpen = item.classList.contains('open');
                document.querySelectorAll('.faq-item').forEach(function (i) {
                    i.classList.remove('open');
                });
                document.querySelectorAll('.faq-question').forEach(function (b) {
                    b.setAttribute('aria-expanded', 'false');
                });
                if (!isOpen) {
                    item.classList.add('open');
                    btn.setAttribute('aria-expanded', 'true');
                }
            });
        });
    }

    function initBackToTop() {
        var backToTop = document.getElementById('back-to-top');
        if (!backToTop) return;

        window.addEventListener('scroll', function () {
            backToTop.classList.toggle('visible', window.scrollY > 500);
        }, { passive: true });

        backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    function initFadeIn() {
        var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        var fadeEls = document.querySelectorAll('.fade-in');

        if (reduceMotion) {
            fadeEls.forEach(function (el) { el.classList.add('visible'); });
            return;
        }

        if ('IntersectionObserver' in window) {
            var observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) entry.target.classList.add('visible');
                });
            }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

            fadeEls.forEach(function (el) { observer.observe(el); });
        } else {
            fadeEls.forEach(function (el) { el.classList.add('visible'); });
        }

        document.querySelectorAll('.hero .fade-in').forEach(function (el, i) {
            setTimeout(function () { el.classList.add('visible'); }, 120 * i);
        });
    }

    function initMobileNav() {
        var toggle = document.getElementById('nav-toggle');
        var menu = document.getElementById('nav-menu');
        if (!toggle || !menu) return;

        toggle.addEventListener('click', function () {
            var open = menu.classList.toggle('open');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });

        menu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                menu.classList.remove('open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        fetchCount();
        initMusic();
        initFaq();
        initBackToTop();
        initFadeIn();
        initMobileNav();
    });
})();
