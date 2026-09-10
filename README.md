# UK Study Abroad — Website

A fast, modern, static website for **UK Study Abroad** (`ukstudyabroad.co.uk`), a study abroad consultancy offering short courses, university recruitment and application support, degree placement, IELTS preparation and the Global Career Development Programme, a live online academic module taught directly by UK university lecturers and professors, with an optional two week in person experience in the UK. Currently focused on students, parents and schools in Saudi Arabia.

The site is fully bilingual: every page exists in English (site root) and Arabic (`/ar/`), with a language switcher in the header of both versions. See section 7 for details.

No framework, no build step required to run — plain HTML5, CSS3 and vanilla JavaScript. This means it deploys anywhere as static files (Cloudflare Pages, GitHub Pages, Netlify, any web host) with zero configuration.

---

## 1. What's in this repo

```
├── index.html                 Home (English)
├── about.html                 About Us
├── services.html               Our Services (short courses, recruitment, degree placement, IELTS, Global Career Development Programme)
├── schools.html                Schools & Colleges (partnership pitch for principals)
├── faqs.html                  Eligibility & FAQs
├── testimonials.html          Student Experiences
├── blog.html                  Insights (blog index, ready for future articles)
├── contact.html               Contact page + enquiry form
├── privacy-policy.html / terms.html / 404.html
├── ar/                        Arabic version of every page above (see §7), same filenames, e.g. ar/about.html
├── assets/
│   ├── css/style.css          Single shared stylesheet (design system, includes RTL rules for the Arabic site)
│   ├── js/main.js             Nav, FAQ accordion, scroll reveal, contact form
│   └── images/                Logo, favicons, social-share image (all web-optimised)
├── brand-assets/              High-resolution original logo files (for print/social — not used by the site)
├── build.py                   Shared templates/helpers (header, footer, page shell) for both languages
├── generate.py                Generates the English pages listed above
├── generate_ar.py             Generates the Arabic pages inside ar/
├── _headers                   Cloudflare Pages config (security headers, caching)
├── robots.txt / sitemap.xml   Basic SEO (sitemap includes hreflang alternate links for both languages)
└── site.webmanifest
```

---

## 2. Before you go live — please do these things

1. **Testimonials** (`testimonials.html` and `ar/testimonials.html`) — these pages intentionally have no quotes yet. Only add real, verified feedback from students who have actually completed the programme. Never publish invented reviews, in either language.
2. **Team section** (`about.html` and `ar/about.html`) — generic role placeholders (Founder & Programme Director, Academic Lead, Partnerships Lead, Student Experience Coordinator). Update with real names once ready, or leave generic if you prefer not to name staff yet. Update both language versions together.
3. **Contact form** (`contact.html` and `ar/contact.html`) — both send through [Web3Forms](https://web3forms.com) using the same access key already set on the hidden `access_key` field. If you ever need to change it, get a new key at web3forms.com with `info@ukstudyabroad.co.uk` and swap the value in `contact.html`, `ar/contact.html`, `generate.py`, and `generate_ar.py` so it survives a regeneration.
4. **Insights articles** (`blog.html` and `ar/blog.html`) — currently teaser pages with no published articles. Add real articles as `blog_post_page()` calls in `generate.py` (and their Arabic translation in `generate_ar.py`) when you have genuine content ready (see §4).

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
- **Structural changes** (new page, changed navigation, redesigned header/footer): this site was generated from `build.py` (shared header/footer/design-system templates, used by both languages) plus `generate.py` (English page content) and `generate_ar.py` (Arabic page content). Edit those Python files, then regenerate both:
  ```bash
  python3 generate.py
  python3 generate_ar.py
  git add .
  git commit -m "Update site content"
  git push
  ```
  This keeps every page's header, footer and styling perfectly consistent in both languages. If you only change `build.py` (shared layout), rerun both generators so English and Arabic output stay in sync. If you only change `generate.py`, you only need to rerun that one (same for `generate_ar.py`). You never have to touch these files again if you're only editing existing page text — plain HTML edits work fine too, just remember to make the same edit in both `page.html` and `ar/page.html` if the change should apply to both languages.

## 5. Local preview

To preview the site on your own computer before pushing:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080/index.html` in your browser.

## 6. Notes on design choices

- **No stock photography** is used anywhere — all visuals are built from your logo and CSS/SVG illustrations, so there are zero image licensing concerns.
- **Colors** are sampled directly from your official logo (navy, teal, purple, gold).
- **Fonts:** Playfair Display (headings) + Inter (body) via Google Fonts for English; Cairo (headings) + Tajawal (body) via Google Fonts for Arabic.
- The design is fully responsive (mobile, tablet, desktop) and includes basic on-page SEO (meta descriptions, Open Graph tags, JSON-LD structured data, sitemap).

---

## 7. Bilingual site (English + Arabic)

The whole site is available in English (site root, e.g. `/about.html`) and Arabic (`/ar/` subfolder, e.g. `/ar/about.html`), with every page mirroring its counterpart 1:1. A language switcher in the header (labelled "العربية" on English pages, "English" on Arabic pages) links each page directly to its translated counterpart, not just to the other language's homepage.

**How it's built:**

- `build.py` contains English helpers (`head()`, `header()`, `footer()`, `build_page()`) and Arabic counterparts (`head_ar()`, `header_ar()`, `footer_ar()`, `build_page_ar()`). The Arabic versions output `<html lang="ar" dir="rtl">`, an Arabic nav menu, and Arabic ARIA labels/WhatsApp text.
- `generate.py` builds the English pages at the repo root; `generate_ar.py` builds the Arabic pages into `ar/`. Both import their shared helpers from `build.py`, so a layout change made once in `build.py` and then regenerated with both scripts stays consistent everywhere.
- **RTL layout:** the design is built on CSS Grid/Flexbox, which mirrors automatically under `direction: rtl`, so only a small, additive block of RTL-specific overrides was needed in `assets/css/style.css` (physical `left`/`right` positioning, text alignment, and flipping directional icons such as arrows). This means the Arabic site shares the exact same stylesheet as the English site, just with the RTL block applying automatically via the `dir="rtl"` attribute.
- **SEO:** every page in both languages carries `hreflang` alternate tags (`en`, `ar`, `x-default`) in the `<head>`, and `sitemap.xml` lists both language versions of every URL with matching `hreflang` links, so search engines correctly serve each visitor the right language version.
- **Content:** every English page was professionally translated into Arabic by hand, not machine-translated boilerplate, keeping the same structure, sections, and calls to action so both versions feel equally complete. The brand name "UK Study Abroad" is kept in Latin script on Arabic pages (as is standard practice for brand names), with all surrounding content in Arabic.
- The Arabic contact form uses the same Web3Forms access key as the English form, so both languages deliver enquiries to the same inbox. If you ever rotate the Web3Forms key, update it in `contact.html`, `ar/contact.html`, `generate.py`, and `generate_ar.py`.

**Adding new content later:** if you add a new page or section, write the English version in `generate.py` and, when ready, its Arabic translation in `generate_ar.py` using the same `build_page_ar()` pattern, then regenerate both.
