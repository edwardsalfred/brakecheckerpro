# Brake Checker Pro — Website Build Brief

## Decisions Locked In

| Decision | Choice | Rationale |
|---|---|---|
| Product name on site | **Brake Checker Pro** | New brand the user gave; old site name retired |
| Price | **$89.99** | Confirmed from existing product page |
| Tagline | "**The patented solo brake test. Built by drivers, for drivers.**" | Replaces existing "tool you NEED" line |
| Primary color | `#E11D1D` (deepened brake red) | Keeps brand red, more legible than `#F50C0C` |
| Foundation | `#0F0F10` asphalt black | Premium feel for dark sections |
| Accent | `#FFB800` safety amber | Already in brand; reads as caution / safety |
| Display font | **Anton** | Industrial condensed, nobody in niche uses one |
| Body font | **Inter** | Modern, screen-optimized, neutral |
| Page count | **Single landing page** | DTC single-product play; everything on one scroll |
| Checkout | **Stripe Checkout** (hosted) | Fastest path to live with full PCI compliance |
| Hosting target | **Vercel** | Matches user's existing stack signals; supports Stripe API routes if needed |

---

## Site Architecture

**Single-page scroll with anchor navigation:**

1. **Sticky nav** — Logo · Buy · How It Works · Why It Pays · FAQ · price + Buy button
2. **Hero** — Tagline, sub, price, primary CTA, real cab-installed product image
3. **Trust strip** — Patented · Assembled in USA · DOT-Ready · Solo Operation
4. **Problem section** — "The pre-trip that gets drivers put out of service" — DOT/OOS framing
5. **How It Works** — 3-step illustrated process (Start engine → Install tool → Walk + inspect)
6. **Why It Pays** — ROI math callout (one prevented ticket vs. $89.99)
7. **What's Included / Specs** — Adjustable steel, fits all rigs, lifetime build
8. **Driver Reviews** — Real-voice testimonials (placeholder until client confirms real ones)
9. **FAQ** — DOT compliance, pedal compatibility, returns, shipping
10. **Final CTA** — Big buy block
11. **Sticky bottom buy bar** — Price + Buy, always visible on scroll
12. **Footer** — Contact (281-328-5339), Crosby TX, email, social slots, Chatbot Boy AI credit

---

## Content Framework

### Hero Options
**Option A (recommended — DOT pain):**
> **The patented solo brake test.**
> Catch air leaks and dead brake lights before DOT does. One driver. Ninety seconds. $89.99.

**Option B (ROI angle):**
> **One prevented out-of-service pays for it ten times over.**
> Brake Checker Pro is the patented steel rod that turns a two-person pre-trip into a solo walk-around.

**Option C (Built-by-drivers angle):**
> **Built by drivers, for drivers.**
> The only patented tool that lets you check brake lights and air leaks alone. Assembled in the USA.

**Going with A** — it's the strongest pain hook for the audience. ROI math gets its own section below.

### Section copy (drafted, edit-ready)

**Trust strip:**
PATENTED · ASSEMBLED IN USA · DOT-COMPLIANT WALKAROUND · ONE-DRIVER OPERATION

**Problem section H2:** "Every pre-trip you skip is a roadside ticket waiting."
Body: "FMCSA Part 393 requires functional brake lights and a sealed air system before you roll. The only way to verify both is to hold the brake pedal down while you walk the rig. Without a second driver, that's not happening. Brake Checker Pro is the patented steel rod that holds it for you, while you do the inspection that keeps your CSA score clean and your truck on the road."

**How It Works H2:** "Ninety seconds. Three steps. Done."
1. Start the engine, let air pressure build.
2. Wedge Brake Checker Pro between the brake pedal and seat bracket.
3. Walk the rig. Check every brake light. Listen for every leak. Roll out clean.

**ROI section H2:** "The math is simple."
Body: "An out-of-service violation costs the average owner-operator $500 to $2,000 in lost loads, fines, and downtime. Brake Checker Pro is $89.99. Prevent one ticket and the tool has paid for itself ten times over. Prevent two and you're funding the rest of your fleet."

**FAQ:**
- Will it fit my truck? (Yes — adjustable for free-swinging and floor-mounted pedals, all class 7-8.)
- Is it DOT-approved? (Brake Checker Pro is a driver-side tool. It helps you comply with FMCSA Part 393 brake light and air system requirements.)
- How long does it last? (Steel construction. We've had drivers using the same unit for 5+ years.)
- Returns? (30-day no-questions return on unused tools.)
- Shipping? (Ships from Crosby, Texas. 2-5 business days continental US.)

### SEO Targets
- **Meta title:** Brake Checker Pro | Patented Solo Brake Light & Air Leak Test Tool
- **Meta description:** The patented steel tool that lets one truck driver pre-trip brake lights and air leaks alone. Prevents DOT out-of-service violations. $89.99, assembled in USA.
- **Primary H1:** Match the hero
- **Image alt text:** Every product image gets a "Brake Checker Pro installed in semi-truck cab" pattern with variations

---

## Conversion Playbook

**Primary goal:** Stripe Checkout completion at $89.99.

**Stripe integration plan:**
- Use **Stripe Checkout** (hosted page). Fastest, fully PCI-compliant, supports Apple Pay / Google Pay / Link out of the box.
- Two implementation modes (pick at build):
  1. **Static-link mode (zero backend):** Create a Stripe Payment Link in dashboard → paste URL into the Buy buttons. Cheapest, no server needed. Ideal for shipping today.
  2. **Server mode (Vercel function):** Tiny `/api/checkout` route that creates a Checkout Session. More flexible (quantities, line items, metadata). Required if we add upsells later.
- **Default to static link mode** unless user wants quantities or upsells now.

**Lead-capture fallback:**
- Email signup at the footer for drivers who aren't ready to buy ("Get the pre-trip checklist PDF" — lead magnet placeholder).

**Sticky bottom buy bar:** Always-visible on mobile and desktop after the hero scrolls past. Price + Buy. Biggest single conversion lever.

**Trust signals on page:**
- Patented badge (visual)
- Assembled in USA flag accent
- Real driver reviews (placeholder slots)
- Stripe secure-checkout lock icon near Buy buttons
- 30-day return promise

---

## What to AVOID (pulled directly from competitor weaknesses)

| Don't | Why |
|---|---|
| Generic stock testimonials | Existing site does this. Reviewers can spot template avatars from a mile. |
| Quote-only pricing | Redline does this. Kills DTC conversion. Show the price. |
| Sterile black-and-white catalog feel | Iowa 80 does this. Audience reads it as commodity. |
| Big enterprise navy + corporate type | Redline does this. Reads B2B-only. |
| Cluttered specs above benefits | J.J. Keller does this. Lead with the why. |
| Em-dashes in copy | Skill rule. Use periods, commas, colons. |
| Fake reviews | The single biggest trust-killer in this niche. Ship empty before fake. |

---

## Open Questions for Client (the ones that change the build)

1. **Stripe:** Do you have a Stripe account set up? If yes, do you want to create a Payment Link in the dashboard (fastest), or should I wire up a server-side checkout endpoint?
2. **Founder photo / name:** Do you have a portrait or name we should use for the "Built by drivers, for drivers" section? If not, I'll keep it text-only.
3. **Real customer testimonials:** Do you have any real driver quotes, names, and trucks? If not, I'll mark placeholder slots and you can drop them in later.
4. **Demo video:** Any chance of a 30-second clip of the tool installed and a driver walking the rig? Marks the highest-conversion slot on the page.
5. **Old domain:** Do you want this new build to replace `brakelightandairleakcheckertool.com`, or to live at a new domain like `brakecheckerpro.com`?
6. **Shipping zones:** US only, or international? Affects what's shown on the FAQ and Stripe checkout.

---

## HARD STOP — Approval Checkpoint

Before I build, please review the brief and answer the questions above (especially the Stripe one — that determines how Buy buttons get wired).

**Once you green-light, the build runs in this order:**
1. Scaffold HTML/CSS/JS with the design system
2. Drop in the real product photos
3. Wire Stripe Buy buttons (static link or server-side based on your answer)
4. GSAP scroll animations + sticky buy bar + mobile drawer
5. Quality audit in browser (Playwright)
6. Hand off with deploy instructions

**Ready to build?**
