# Brake Checker Pro — Landing Site

Premium single-product landing page for the Brake Checker Pro patented solo brake-light and air-leak test tool. Built for truck drivers. Sells via Stripe.

## What's Here

```
BrakeCheckerPro/
├── vercel.json              # Vercel deploy config (publish dir = site/)
├── netlify.toml             # Netlify alternative
├── README.md                # This file
├── research/                # Client-facing research deliverables
│   ├── 01-client-brand.md
│   ├── 02-competitor-analysis.md
│   ├── 03-build-brief.md
│   └── 04-quality-audit.md
└── site/                    # Publish directory
    ├── index.html
    ├── competitive-analysis.html  # Client report (noindex)
    ├── robots.txt
    ├── sitemap.xml
    ├── css/styles.css
    ├── js/main.js
    └── assets/
        ├── logo-nav.png
        └── product/         # Real product photos
```

## Local Preview

From the project root:

```bash
cd site
python -m http.server 8080
```

Then open http://localhost:8080.

## Step 1: Set Up Stripe (required before going live)

The site is wired to a Stripe Payment Link. You need to create your Stripe account first.

1. **Create a Stripe account** at https://stripe.com (free, takes 5 minutes).
2. **Add your product** in the Stripe dashboard → Products → New product:
   - Name: Brake Checker Pro
   - Price: $89.99
   - Description: Patented solo brake-light and air-leak inspection tool for truck drivers.
   - Add a product image (use `site/assets/product/product-3.png`).
3. **Create a Payment Link** in the Stripe dashboard → Payment Links → New:
   - Select your Brake Checker Pro product.
   - Enable "Collect shipping address" (you need this to ship the tool).
   - Optionally enable Apple Pay, Google Pay, and Link.
   - Optionally add a "Shipping rate" so customers see shipping cost at checkout.
   - Click Create. Stripe gives you a URL like `https://buy.stripe.com/abc123xyz`.
4. **Drop the URL into `site/index.html`.** Find every instance of `STRIPE_LINK_HERE` (there are six in the file) and replace with your Payment Link URL.
   - On Mac/Linux: `sed -i '' 's|STRIPE_LINK_HERE|https://buy.stripe.com/YOUR_LINK|g' site/index.html`
   - On Windows PowerShell: `(Get-Content site/index.html) -replace 'STRIPE_LINK_HERE','https://buy.stripe.com/YOUR_LINK' | Set-Content site/index.html`

Until that's done, the Buy buttons will pop up an alert reminding you to configure Stripe.

## Step 2: Deploy to Vercel

The fastest path. Free for this site.

1. Push the project to a GitHub repo.
2. Go to https://vercel.com and click "Add New → Project".
3. Import the GitHub repo. Vercel reads `vercel.json` and publishes `site/` automatically.
4. Done. You get a `*.vercel.app` URL immediately.

## Step 3: Connect Your Domain

In the Vercel project settings → Domains:
1. Add `brakecheckerpro.com` (or whichever domain you bought).
2. Update your domain registrar's nameservers per Vercel's instructions.
3. Vercel issues HTTPS automatically.

## Alternative: Netlify

If you'd rather use Netlify, the `netlify.toml` is already configured. Drag the project folder to https://app.netlify.com/drop or connect the GitHub repo. Publish dir is set to `site/`.

## Editing the Site

### Replace placeholder testimonials with real reviews
In `site/index.html`, find the section marked `<!-- REPLACE WITH REAL REVIEWS -->`. There are three review blocks. Update the quote, the initials in `.avatar`, and the name + meta line.

Remove the placeholder note at the bottom of the section once real reviews are in.

### Swap the demo video
The current demo video lives at `site/assets/video/demo.mp4` (~9MB, 1280×720, 30 seconds — pulled from your existing site and re-encoded for web). The poster frame is `site/assets/video/poster.jpg`.

To replace with a new video:
1. Drop a new `.mp4` file at `site/assets/video/demo.mp4` (H.264 + AAC, faststart enabled, ideally under 10MB).
2. Optionally update the poster frame at `site/assets/video/poster.jpg` (or change the path in the `<video poster="...">` tag in `site/index.html`).
3. If you'd rather use YouTube/Vimeo, replace the `<video>` tag inside `.video-wrap` with an iframe embed.

### Update contact info
Search `site/index.html` for `sales@brakecheckerpro.com` and `281-328-5339` and replace with the email and phone you want public on the new domain.

## Performance Notes

- Fonts (Anton, Inter) load from Google Fonts with preconnect hints.
- All product images are self-hosted in `site/assets/product/` — no third-party CDN dependencies.
- CSS and JS are unminified for readability. For maximum speed, you can minify both with any standard tool, but the site is already well under 100KB transferred on first load.

## Browser Support

Modern evergreen browsers (Chrome, Safari, Edge, Firefox). Mobile Safari and Chrome Android tested. No IE11 support.

## Credits

Created by [Chatbot Boy AI](https://www.chatbotboy.ai/).
