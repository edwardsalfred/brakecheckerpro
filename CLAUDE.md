# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Single-product marketing landing page for Brake Checker Pro (patented solo brake-light and air-leak test tool). Static HTML/CSS/JS — **no build step, no framework, no package manager**. Checkout is handled externally by a Shopify cart permalink.

## Commands

Local preview (from repo root):
```powershell
cd site
python -m http.server 8080
# open http://localhost:8080
```

There is no lint, test, or build command — files are served as-is.

Deploy: `git push` to the connected Vercel project. `vercel.json` sets `outputDirectory: site` and Vercel builds with zero config. `netlify.toml` mirrors the same headers as a backup target.

## Architecture

**Two-tier layout.** The repo root holds tooling and deliverables; **only `site/` ships**. Everything else (`research/`, `scripts/`, root-level PNGs) is internal.

- `site/index.html` (~450 lines) — the landing page. All sibling HTML files (`privacy.html`, `terms.html`, `shipping.html`, `returns.html`, `competitive-analysis.html`) are standalone pages that reuse the same CSS/JS.
- `site/css/styles.css` (~970 lines) — one stylesheet, unminified by design (README explicitly favors readability; total payload is already <100KB).
- `site/js/main.js` (~120 lines) — one IIFE handling: scrolled-nav state, sticky buy-bar visibility (between hero bottom and footer), mobile nav drawer, reveal-on-scroll via IntersectionObserver (with two timed fallbacks at 600ms and 3s in case observation misses), smooth anchor scroll with nav-height offset, and a developer safety-net for buy-link misconfiguration.

**Checkout is a Shopify cart permalink.** Every real Buy button has `href="https://brakecheckerpro.myshopify.com/cart/50064538894573:1"` and the marker attribute `data-buy`. The JS in `main.js` watches `[data-buy]` clicks and intercepts if the href is missing or doesn't start with `http` — a safety net, not a content gate. The variant ID `50064538894573` is hardcoded; to change product/variant or migrate to a custom storefront domain, find/replace the URL across `site/`. The same URL also lives in the JSON-LD `Product.offers.url` in `index.html` `<head>` and **the price `$79.99` is hardcoded separately in the JSON-LD `Product.offers.price`** — update both if pricing changes. The homepage nav button (`href="#buy"`, no `data-buy`) is intentionally a scroll-to-CTA anchor, not a real Buy link.

**Reveal animations.** Adding `class="reveal"` to any element opts it into the IntersectionObserver fade-in. The two fallback timers exist because earlier versions had elements stuck invisible on slow scroll/iOS — don't remove them without verifying on mobile Safari.

## Caching headers (both `vercel.json` and `netlify.toml`)

- `/assets/*` → `max-age=31536000, immutable` (1 year, hash-busting required if you replace an asset at the same path — bump the `?v=` query on the `<link>` tag, as already done with `styles.css?v=2`).
- `*.html` → `max-age=0, must-revalidate`.

## Repo-only directories (never deployed)

- `research/` — markdown client deliverables (brand brief, competitor analysis, build brief, quality audit).
- `scripts/` — one-off Python utilities for image processing (favicon, logo bg removal). Not part of the runtime pipeline.
- `verify-*.png` at repo root — gitignored Playwright/agent screenshots. Safe to delete.

## Conventions

- Contact info (`sales@brakecheckerpro.com`, `281-328-5339`) is hardcoded in HTML — search both if it changes.
- Mobile breakpoint is **720px** (used in `main.js` resize handler and throughout `styles.css`).
- Fonts are Anton (display) + Inter (body) from Google Fonts with preconnect. Brand colors anchor on `#0F0F10` (theme-color) and a red accent.
- No IE11 support; targeting modern evergreen browsers only.
