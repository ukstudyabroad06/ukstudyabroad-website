#!/usr/bin/env python3
"""
UK Study Abroad — static site builder.

This script is a developer convenience only. It is NOT required for deployment —
the generated .html files are plain static output and are committed to the repo,
so Cloudflare Pages (and GitHub Pages) can serve them with zero build step.

Run `python3 build.py` after editing PAGES below to regenerate every page with a
consistent header, footer, SEO tags and floating WhatsApp button.
"""
import os
import re

SITE_NAME = "UK Study Abroad"
SITE_DOMAIN = "https://ukstudyabroad.co.uk"
SITE_TAGLINE = "Your Future, Our Mission"
WHATSAPP_NUMBER = "447792646769"  # no +, no spaces (wa.me format)
WHATSAPP_DISPLAY = "+44 7792 646769"
EMAIL = "info@ukstudyabroad.co.uk"
CURRENT_YEAR_PLACEHOLDER = "<span data-year></span>"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("destinations.html", "Destinations"),
    ("visa-ielts.html", "Visa & IELTS"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]

ICONS = {
    "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.29-1.39a9.9 9.9 0 0 0 4.75 1.21h.01c5.46 0 9.9-4.45 9.9-9.91C21.96 6.45 17.5 2 12.04 2Zm5.8 14.14c-.24.68-1.4 1.32-1.93 1.4-.5.08-1.12.11-1.8-.11-.42-.13-.96-.31-1.65-.6-2.9-1.25-4.79-4.16-4.94-4.35-.14-.2-1.18-1.57-1.18-3 0-1.42.75-2.12 1.01-2.41.27-.29.58-.36.78-.36.2 0 .39 0 .56.01.18.01.42-.07.66.5.24.58.82 2 .9 2.14.07.14.12.31.02.5-.1.19-.15.31-.29.48-.14.17-.3.37-.43.5-.14.14-.29.29-.12.58.17.29.75 1.24 1.62 2.01 1.11.99 2.05 1.3 2.34 1.44.29.14.46.12.63-.07.17-.2.72-.84.92-1.13.19-.28.38-.24.63-.14.26.1 1.65.78 1.93.92.29.14.48.2.55.32.07.11.07.65-.17 1.33Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 5c0 8.5 6.5 15 15 15l3-4-6-3-2 2c-2.5-1.2-4.8-3.5-6-6l2-2-3-6z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 22s7-6.6 7-12A7 7 0 1 0 5 10c0 5.4 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
    "arrow-up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
    "arrow-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "cap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 3 2 8l10 5 10-5-10-5Z"/><path d="M6 10.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-5.5"/><path d="M22 8v6"/></svg>',
    "doc-check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="m9.5 15 2 2 4-4"/></svg>',
    "passport": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="5" y="2.5" width="14" height="19" rx="2"/><circle cx="12" cy="10" r="2.5"/><path d="M8.5 16.5c0-1.5 1.5-2.5 3.5-2.5s3.5 1 3.5 2.5"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M21 12a8 8 0 1 1-3.4-6.5L21 4l-1 3.6A7.96 7.96 0 0 1 21 12Z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 3l7 3v6c0 4.5-3 8-7 9-4-1-7-4.5-7-9V6l7-3Z"/><path d="m9.5 12 2 2 3.5-3.5"/></svg>',
    "briefcase": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 12h18"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9.5h18M8 3v3M16 3v3"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5Z"/><path d="M4 5.5v15"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 4 6 4 9s-1.5 6.5-4 9c-2.5-2.5-4-6-4-9s1.5-6.5 4-9Z"/></svg>',
    "home-key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v9.5H18V10"/><circle cx="14" cy="14.5" r="1.6"/><path d="M15.4 15.9 18 18.5"/></svg>',
    "headset": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 13a8 8 0 0 1 16 0"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M20 19v1a3 3 0 0 1-3 3h-3"/></svg>',
    "check-circle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.5 2.5L16 9.5"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2 3.1 6.4 7 1-5 5 1.2 7-6.3-3.4L5.7 21.4l1.2-7-5-5 7-1L12 2Z"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="0.8" fill="currentColor"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 20.5S3.5 15 3.5 9a4.7 4.7 0 0 1 8.5-2.8A4.7 4.7 0 0 1 20.5 9c0 6-8.5 11.5-8.5 11.5Z"/></svg>',
    "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="8" r="5.5"/><path d="m8.5 12.5-1.5 8 5-2.5 5 2.5-1.5-8"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><path d="M2.5 20c0-3.5 3-5.5 6.5-5.5s6.5 2 6.5 5.5"/><circle cx="17.5" cy="9" r="2.6"/><path d="M15.5 14.7c2.6.3 4.5 2 4.5 5.3"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9.5"/><path d="m15 9-2 6-6 2 2-6 6-2Z"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
}


def whatsapp_link(message="Hi UK Study Abroad, I'd like to know more about studying in the UK."):
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def head(title, description, path, og_image="assets/images/og-image.jpg", extra=""):
    canonical = f"{SITE_DOMAIN}/{path}" if path != "index.html" else SITE_DOMAIN + "/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>document.documentElement.classList.add('js')</script>
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE_DOMAIN}/{og_image}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_DOMAIN}/{og_image}">

<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/images/favicon-192.png">
<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#1b2951">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
{extra}
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "{SITE_NAME}",
  "alternateName": "UK Study Abroad Consultancy",
  "url": "{SITE_DOMAIN}",
  "logo": "{SITE_DOMAIN}/assets/images/logo-full-web.png",
  "description": "UK Study Abroad helps students, with an initial focus on Saudi Arabia, apply to UK universities, secure student visas, and prepare for life and study in the United Kingdom.",
  "email": "{EMAIL}",
  "areaServed": ["Saudi Arabia", "United Kingdom"],
  "sameAs": []
}}
</script>
</head>
"""


def header(active):
    ARIA_CURRENT = ' aria-current="page"'
    links = "\n".join(
        f'<a href="/{href}"{ARIA_CURRENT if href == active else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a href="/index.html" class="brand">
      <img src="/assets/images/logo-icon-web.png" alt="UK Study Abroad logo" width="46" height="46">
      <span class="brand-text">
        <span class="brand-name">UK Study Abroad</span>
        <span class="brand-tag">{SITE_TAGLINE}</span>
      </span>
    </a>
    <nav class="main-nav" aria-label="Primary">
      {links}
    </nav>
    <div class="header-actions">
      <a class="phone-link" href="tel:+{WHATSAPP_NUMBER}">
        {ICONS['phone']}
        {WHATSAPP_DISPLAY}
      </a>
      <a class="btn btn-primary" href="{whatsapp_link()}" target="_blank" rel="noopener">
        {ICONS['whatsapp']}<span class="btn-label">WhatsApp Us</span>
      </a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""


def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/images/logo-full-web.png" alt="UK Study Abroad" width="220">
        <p>Independent UK study-abroad consultancy helping students plan, apply and get visa-ready for university life in the United Kingdom — with dedicated support for students applying from Saudi Arabia.</p>
        <div class="footer-social" aria-label="Social media">
          <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1"/></svg></a>
          <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 9h3V5h-3a4 4 0 0 0-4 4v2H7v4h3v7h4v-7h3l1-4h-4V9a1 1 0 0 1 1-1Z"/></svg></a>
          <a href="#" aria-label="TikTok"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 4v10.5a3.5 3.5 0 1 1-3-3.46"/><path d="M14 4c0 2.5 2 4.5 4.5 4.5"/></svg></a>
          <a href="{whatsapp_link()}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICONS['whatsapp']}</a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Explore</h5>
        <ul>
          <li><a href="/about.html">About Us</a></li>
          <li><a href="/services.html">Our Services</a></li>
          <li><a href="/destinations.html">Study Destinations</a></li>
          <li><a href="/testimonials.html">Testimonials</a></li>
          <li><a href="/blog.html">Blog</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul>
          <li><a href="/services.html#counselling">Free Consultation</a></li>
          <li><a href="/services.html#applications">University Applications</a></li>
          <li><a href="/visa-ielts.html">Visa Guidance</a></li>
          <li><a href="/visa-ielts.html#ielts">IELTS Preparation</a></li>
          <li><a href="/services.html#scholarships">Scholarships</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Get in Touch</h5>
        <div class="contact-line">{ICONS['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="contact-line">{ICONS['whatsapp']}<a href="{whatsapp_link()}" target="_blank" rel="noopener">{WHATSAPP_DISPLAY}</a></div>
        <div class="contact-line">{ICONS['pin']}<span>Registered office: GoDaddy domain ukstudyabroad.co.uk — serving students across the Kingdom of Saudi Arabia (Riyadh · Jeddah · Dammam) and beyond.</span></div>
        <a href="/contact.html" class="btn btn-outline btn-sm" style="margin-top:8px;">Contact Us</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; {CURRENT_YEAR_PLACEHOLDER} UK Study Abroad. All rights reserved.</p>
      <div class="legal-links">
        <a href="/privacy-policy.html">Privacy Policy</a>
        <a href="/terms.html">Terms of Use</a>
      </div>
    </div>
  </div>
</footer>

<div class="float-actions">
  <button class="back-to-top" aria-label="Back to top">{ICONS['arrow-up']}</button>
  <a class="whatsapp-float" href="{whatsapp_link()}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
    {ICONS['whatsapp']}
  </a>
</div>

<script src="/assets/js/main.js"></script>
</body>
</html>
"""


def decorative_panel(icon_key, big_label, small_label="", variant="brand"):
    """A photo-free decorative panel used in place of stock photography."""
    bg = {
        "brand": "var(--grad-hero)",
        "gold": "linear-gradient(135deg, var(--purple-700), var(--navy-800))",
    }.get(variant, "var(--grad-hero)")
    return f"""<div class="art-panel" style="background:{bg};">
  <div class="art-panel-pattern"></div>
  <div class="art-panel-icon">{ICONS[icon_key]}</div>
  <strong>{big_label}</strong>
  {f'<span>{small_label}</span>' if small_label else ''}
</div>"""


SKYLINE_SVG = '''<svg class="skyline" viewBox="0 0 400 140" preserveAspectRatio="none" fill="currentColor" aria-hidden="true">
<rect x="0" y="70" width="34" height="70"/><rect x="38" y="40" width="26" height="100"/>
<rect x="68" y="85" width="30" height="55"/><rect x="102" y="20" width="22" height="120"/>
<rect x="128" y="60" width="34" height="80"/><rect x="166" y="45" width="20" height="95"/>
<polygon points="186,45 196,15 206,45"/><rect x="210" y="75" width="30" height="65"/>
<rect x="244" y="30" width="24" height="110"/><rect x="272" y="65" width="34" height="75"/>
<rect x="310" y="50" width="22" height="90"/><rect x="336" y="80" width="30" height="60"/>
<rect x="370" y="35" width="26" height="105"/>
</svg>'''

CITY_GRADIENTS = [
    "linear-gradient(160deg, var(--navy-800), var(--teal-700))",
    "linear-gradient(160deg, var(--purple-700), var(--navy-800))",
    "linear-gradient(160deg, var(--teal-700), var(--purple-600))",
    "linear-gradient(160deg, var(--navy-900), var(--purple-500))",
    "linear-gradient(160deg, var(--teal-600), var(--navy-800))",
    "linear-gradient(160deg, var(--purple-600), var(--teal-700))",
    "linear-gradient(160deg, var(--navy-800), var(--gold-500))",
    "linear-gradient(160deg, var(--purple-700), var(--teal-600))",
]


def city_tile(name, tagline, i):
    grad = CITY_GRADIENTS[i % len(CITY_GRADIENTS)]
    return f"""<div class="city-tile" style="background:{grad};">
  <div class="pattern"></div>
  {SKYLINE_SVG}
  <div class="cap">{ICONS['cap']}</div>
  <h4>{name}</h4>
  <span>{tagline}</span>
</div>"""


def check_list(items):
    lis = "\n".join(
        f'<li class="check-item"><span class="check-icon">{ICONS["check-circle"]}</span><span>{item}</span></li>'
        for item in items
    )
    return f'<ul class="check-list">\n{lis}\n</ul>'


def build_page(path, title, description, active, body, extra_head=""):
    html = head(title, description, path, extra=extra_head) + "<body>\n" + header(active) + body + footer()
    out_path = os.path.join(os.path.dirname(__file__), path)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("built", path)
