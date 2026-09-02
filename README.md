# UK Study Abroad — Website

A fast, modern, static website for **UK Study Abroad** (`ukstudyabroad.co.uk`), an independent UK study-abroad consultancy launching with a focus on students in Saudi Arabia.

No framework, no build step required to run — plain HTML5, CSS3 and vanilla JavaScript. This means it deploys anywhere as static files (Cloudflare Pages, GitHub Pages, Netlify, any web host) with zero configuration.

---

## 1. What's in this repo

```
├── index.html                 Home
├── about.html                 About Us
├── services.html              Services
├── destinations.html          Study Destinations
├── visa-ielts.html            Visa & IELTS guidance
├── testimonials.html          Testimonials
├── blog.html                  Blog index
├── blog-visa-guide.html       Article: UK Student Visa Guide
├── blog-ielts-guide.html      Article: IELTS Requirements
├── blog-top-cities.html       Article: Top UK Cities
├── contact.html               Contact page + enquiry form
├── privacy-policy.html / terms.html / 404.html
├── assets/
│   ├── css/style.css          Single shared stylesheet (design system)
│   ├── js/main.js             Nav, FAQ accordion, scroll reveal, contact form
│   └── images/                Logo, favicons, social-share image (all web-optimised)
├── brand-assets/              High-resolution original logo files (for print/social — not used by the site)
├── build.py / generate.py     Optional dev tool that generated the HTML above (see §6)
├── _headers                   Cloudflare Pages config (security headers, caching)
├── robots.txt / sitemap.xml   Basic SEO
└── site.webmanifest
```

---

## 2. Before you go live — please do these 4 things

The site is fully designed and populated with real UK visa/IELTS facts, but a few things are intentionally placeholders you should update:

1. **Testimonials** (`index.html`, `testimonials.html`) — currently sample quotes, clearly marked. Replace with real, verified student reviews before publishing.
2. **Team section** (`about.html`) — generic role placeholders (Founder, Admissions Specialist, etc.). Update with real names/titles once ready, or leave generic if you prefer not to name staff yet.
3. **Contact form** (`contact.html`) — needs a free [Web3Forms](https://web3forms.com) access key to actually send emails (takes 2 minutes, no backend needed):
   - Go to web3forms.com → enter `info@ukstudyabroad.co.uk` → get your Access Key by email.
   - Open `contact.html`, find `value="YOUR_WEB3FORMS_ACCESS_KEY"` and replace it with your real key.
   - Until you do this, the form shows a friendly message directing visitors to WhatsApp/email instead of failing silently.
4. **University partner list** (`destinations.html`) — shown as general examples, not a claim of partnership. Update with your actual confirmed partner universities.

---

## 3. Deploy: GitHub → Cloudflare Pages → GoDaddy DNS

This is the exact order you asked for. Total time: ~20 minutes plus DNS propagation (can take up to 24-48 hours, though it's often much faster).

### Step 1 — Push this code to GitHub

1. Create a new **empty** repository at [github.com/new](https://github.com/new) — name it e.g. `ukstudyabroad-website`. Don't add a README/license (this folder already has one).
2. From inside this folder, run:
   ```bash
   git init
   git add .
   git commit -m "Initial site: UK Study Abroad"
   git branch -M main
   git remote add origin https://github.com/YOUR-GITHUB-USERNAME/ukstudyabroad-website.git
   git push -u origin main
   ```

### Step 2 — Create a Cloudflare Pages project

1. Sign up / log in at [dash.cloudflare.com](https://dash.cloudflare.com) (free plan is enough).
2. Go to **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Authorize Cloudflare to access GitHub, then select your `ukstudyabroad-website` repo.
4. Build settings — since this is plain static HTML, use:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Build output directory:** `/`
5. Click **Save and Deploy**. Cloudflare builds and gives you a live URL like `ukstudyabroad-website.pages.dev` within a minute or two — open it and click through the site to confirm everything works.

> **Note:** Cloudflare Pages automatically serves clean, extension-less URLs for static HTML sites — `/about.html` is already reachable at both `/about.html` and `/about` with no configuration needed. An earlier version of this repo included a custom `_redirects` file to force this, which actually conflicted with Cloudflare's own automatic behavior and caused a "Latest build failed — infinite loop detected" error. That file has been removed; if you still have it locally, delete it, commit, and push again.

### Step 3 — Point your GoDaddy domain to Cloudflare

This is the standard, most reliable way to use a GoDaddy-registered domain with Cloudflare Pages (free SSL, full CDN performance, and proper support for the root domain `ukstudyabroad.co.uk` with no `www`):

1. **Add your domain to Cloudflare** (separate from the Pages project): Cloudflare dashboard → **Add a Site** → enter `ukstudyabroad.co.uk` → choose the **Free** plan. Cloudflare scans existing DNS records and shows you two nameservers, e.g. `xxx.ns.cloudflare.com` and `yyy.ns.cloudflare.com`.
2. **Update nameservers at GoDaddy:**
   - Log into [godaddy.com](https://godaddy.com) → **My Products** → find `ukstudyabroad.co.uk` → **DNS** → **Nameservers** → **Change**.
   - Select "I'll use my own nameservers" and enter the two Cloudflare nameservers exactly as shown.
   - Save. GoDaddy will warn this can take time to propagate — that's normal.
3. Back in Cloudflare, wait for the dashboard to show the domain as **Active** (it emails you too — usually within a few hours, sometimes up to 24-48h).
4. **Attach the domain to your Pages project:** Workers & Pages → your project → **Custom domains** → **Set up a custom domain** → enter `ukstudyabroad.co.uk`, then repeat and add `www.ukstudyabroad.co.uk` too. Cloudflare automatically creates the correct DNS records since the domain now lives on Cloudflare.
5. Cloudflare issues a free SSL certificate automatically (usually within minutes). Once done, `https://ukstudyabroad.co.uk` will serve this site directly.

**Don't want to move DNS to Cloudflare?** You can alternatively keep GoDaddy as your DNS host and just add a `CNAME` record there pointing `www` to your `*.pages.dev` address, plus a redirect from the root domain to `www`. This works but the root domain (`ukstudyabroad.co.uk` with no `www`) is trickier to support this way, and you lose Cloudflare's CDN/performance benefits on the DNS layer — the nameserver method above is what we recommend and what most guides assume.

### Step 4 — Final checks

- Visit `https://ukstudyabroad.co.uk` and `https://www.ukstudyabroad.co.uk` — both should load over HTTPS with a padlock.
- Test the WhatsApp button, the contact form, and click through every nav link on both desktop and mobile.
- Submit `https://ukstudyabroad.co.uk/sitemap.xml` to [Google Search Console](https://search.google.com/search-console) so Google starts indexing the site.

---

## 4. Making updates after launch

**Every push to your `main` branch on GitHub automatically redeploys the site on Cloudflare Pages** — typically live within a minute, with no manual steps.

- **Small text/content edits:** open the relevant `.html` file directly and edit it, or ask your developer/AI assistant to do it, then `git commit` + `git push`.
- **Structural changes** (new page, changed navigation, redesigned header/footer): this site was generated from `build.py` (shared header/footer/design-system templates) and `generate.py` (page content). Edit those Python files, then regenerate:
  ```bash
  python3 generate.py
  git add .
  git commit -m "Update site content"
  git push
  ```
  This keeps every page's header, footer and styling perfectly consistent. You never have to touch `build.py`/`generate.py` again if you're only editing existing page text — plain HTML edits work fine too.

## 5. Local preview

To preview the site on your own computer before pushing:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080/index.html` in your browser.

## 6. Notes on design choices

- **No stock photography** is used anywhere — all visuals are built from your logo and CSS/SVG illustrations, so there are zero image licensing concerns.
- **Colors** are sampled directly from your official logo (navy, teal, purple, gold).
- **Fonts:** Playfair Display (headings) + Inter (body) via Google Fonts, matching the elegant serif wordmark in your logo.
- The design is fully responsive (mobile, tablet, desktop) and includes basic on-page SEO (meta descriptions, Open Graph tags, JSON-LD structured data, sitemap).
