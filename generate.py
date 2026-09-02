#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates every page of the UK Study Abroad website from shared templates."""
from build import (
    ICONS, build_page, decorative_panel, city_tile, check_list, whatsapp_link, EMAIL, WHATSAPP_DISPLAY
)

# ==========================================================================
# HOME
# ==========================================================================
home_body = f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <span class="hero-eyebrow">{ICONS['star']} Trusted UK Study Abroad Consultancy</span>
      <h1>Start your journey to a <span>UK university</span>, with confidence.</h1>
      <p class="lead">UK Study Abroad guides students step by step — from choosing the right course to landing in the United Kingdom. We're proudly supporting students from Saudi Arabia as our founding market, with plans to serve students across the region.</p>
      <div class="hero-cta">
        <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} Chat on WhatsApp</a>
        <a class="btn btn-outline-light" href="/contact.html">Book a Free Consultation</a>
      </div>
      <div class="hero-trust">
        <div><strong>Free</strong><span>Initial Consultation</span></div>
        <div><strong>Riyadh &amp; Jeddah</strong><span>Friendly Support Hours</span></div>
        <div><strong>End-to-End</strong><span>Application to Arrival</span></div>
      </div>
    </div>
    <div class="hero-visual" data-reveal>
      <img src="/assets/images/logo-full-web.png" alt="UK Study Abroad — Your Future, Our Mission" loading="eager">
      <div class="hero-badge">
        <div class="icon">{ICONS['shield']}</div>
        <div><strong>Visa &amp; IELTS Guidance</strong><span>Step-by-step support, explained simply</span></div>
      </div>
    </div>
  </div>
</section>

<section class="stats-strip">
  <div class="container">
    <div class="grid grid-4">
      <div><strong>2026</strong><span>Founded to serve Saudi students first</span></div>
      <div><strong>100%</strong><span>Free student counselling</span></div>
      <div><strong>1-on-1</strong><span>Dedicated application advisor</span></div>
      <div><strong>24-48h</strong><span>Response time on WhatsApp</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Why Choose Us</div>
        <h2>Honest guidance from people who know the UK system inside out.</h2>
        <p style="margin:16px 0 30px;">We built UK Study Abroad because too many talented students give up on their UK dream over confusing paperwork and unclear advice. Here's how we do it differently.</p>

        <div class="feature-row" data-reveal>
          <div class="icon-wrap">{ICONS['target']}</div>
          <div><h4>Course &amp; university matching</h4><p>We match your grades, budget and career goals to universities and courses where you'll genuinely thrive — not just wherever pays the highest commission.</p></div>
        </div>
        <div class="feature-row" data-reveal>
          <div class="icon-wrap">{ICONS['shield']}</div>
          <div><h4>Visa-first thinking</h4><p>Every recommendation we make considers your UK Student visa eligibility from day one, so there are no surprises later in the process.</p></div>
        </div>
        <div class="feature-row" data-reveal>
          <div class="icon-wrap">{ICONS['headset']}</div>
          <div><h4>Support in your time zone</h4><p>Message us on WhatsApp and get replies that respect Saudi Arabia working hours — no more waiting overnight for a UK office to open.</p></div>
        </div>
      </div>
      <div data-reveal>{decorative_panel('cap', 'Study. Explore. Grow. Succeed.', 'The four pillars behind every recommendation we make.')}</div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">What We Do</div>
      <h2>Complete support for every stage of your UK journey</h2>
      <p>From your very first question to settling into UK student life, our services cover the full journey — not just the parts that are easy to sell.</p>
    </div>
    <div class="grid grid-3">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['chat']}</div><h3>Free Counselling</h3><p>A no-obligation session to understand your goals, budget and academic background before we recommend anything.</p><a class="card-link" href="/services.html#counselling">Learn more {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['doc-check']}</div><h3>University Applications</h3><p>We help you shortlist universities, prepare your personal statement, and submit accurate UCAS or direct applications.</p><a class="card-link" href="/services.html#applications">Learn more {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['passport']}</div><h3>Student Visa Guidance</h3><p>Clear, step-by-step help with your CAS, financial evidence, IHS and Student Route visa application.</p><a class="card-link" href="/visa-ielts.html">Learn more {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['book']}</div><h3>IELTS &amp; English Prep</h3><p>Guidance on which English test you need, realistic score targets, and preparation resources that work.</p><a class="card-link" href="/visa-ielts.html#ielts">Learn more {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['award']}</div><h3>Scholarship Guidance</h3><p>We help you find and apply for university scholarships, bursaries and SACM-related funding options.</p><a class="card-link" href="/services.html#scholarships">Learn more {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['home-key']}</div><h3>Accommodation &amp; Arrival</h3><p>Accommodation shortlists, pre-departure briefings, and a checklist for your first weeks in the UK.</p><a class="card-link" href="/services.html#arrival">Learn more {ICONS['arrow-right']}</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Study Destinations</div>
      <h2>Popular UK cities for international students</h2>
      <p>Every city offers a different UK experience. We'll help you weigh cost of living, course options and community against what matters most to you.</p>
    </div>
    <div class="dest-list">
      {city_tile('London', 'Global finance, culture &amp; Russell Group universities', 0, 'Capital City')}
      {city_tile('Manchester', 'Vibrant, affordable, major research universities', 1, 'Best Value')}
      {city_tile('Birmingham', 'Central location, strong business schools', 2, 'Central Hub')}
      {city_tile('Edinburgh', 'Historic city, world-ranked institutions', 3, 'Historic Charm')}
      {city_tile('Coventry', 'Modern campuses, welcoming international community', 4, 'Community Focus')}
      {city_tile('Glasgow', 'Affordable living, strong engineering &amp; medicine', 5, 'Affordable Living')}
    </div>
    <div style="text-align:center;margin-top:40px;">
      <a class="btn btn-outline" href="/destinations.html">Explore All Destinations {ICONS['arrow-right']}</a>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('passport', 'UK Student Route Visa', 'CAS · Finances · IHS · Biometrics · Decision', 'gold')}</div>
      <div>
        <div class="eyebrow">Visa &amp; IELTS Guidance</div>
        <h2>We demystify the UK Student visa process, step by step</h2>
        <p style="margin:16px 0 26px;">The Student Route visa can feel overwhelming — financial evidence rules, CAS letters, biometric appointments. We break it into a clear checklist so you always know what's next.</p>
        <div style="margin-bottom:28px;">
        {check_list([
            'Understand CAS, financial requirements &amp; the Immigration Health Surcharge',
            'Know exactly which IELTS/UKVI score your course requires',
            'Prepare documents correctly the first time — fewer delays, fewer refusals',
        ])}
        </div>
        <a class="btn btn-primary" href="/visa-ielts.html">See the Full Visa Guide {ICONS['arrow-right']}</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Why Students Choose Us</div>
      <h2>What you can expect from working with us</h2>
    </div>
    <div class="grid grid-4">
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['chat']}</div><h3>Free, No-Pressure Advice</h3><p>An honest first conversation with no obligation to sign up for anything.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['headset']}</div><h3>Fast WhatsApp Replies</h3><p>Real answers within 24-48 hours, in Saudi Arabia-friendly hours.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['shield']}</div><h3>Visa-Aware Guidance</h3><p>Every recommendation accounts for your Student visa eligibility from day one.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['target']}</div><h3>Matched, Not Mass-Marketed</h3><p>Course and university suggestions based on your grades and goals — not a fixed list.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">From the Blog</div>
      <h2>Guides &amp; insights for your UK application</h2>
    </div>
    <div class="grid grid-3">
      <div class="post-card" data-reveal>
        <div class="post-media">{decorative_panel('passport', 'Visa Guide')}</div>
        <div class="post-body"><div class="post-meta"><span>Visas</span><span>2026</span></div><h3>UK Student Visa Guide for Saudi Students</h3><p>Everything you need to know about the Student Route visa — CAS, finances, IHS and timelines.</p><a class="card-link" href="/blog-visa-guide.html">Read Article {ICONS['arrow-right']}</a></div>
      </div>
      <div class="post-card" data-reveal>
        <div class="post-media">{decorative_panel('book', 'IELTS Guide')}</div>
        <div class="post-body"><div class="post-meta"><span>English Tests</span><span>2026</span></div><h3>IELTS Requirements for UK Universities</h3><p>What score you actually need, which test to book, and how it affects your visa application.</p><a class="card-link" href="/blog-ielts-guide.html">Read Article {ICONS['arrow-right']}</a></div>
      </div>
      <div class="post-card" data-reveal>
        <div class="post-media">{decorative_panel('compass', 'City Guide')}</div>
        <div class="post-body"><div class="post-meta"><span>Student Life</span><span>2026</span></div><h3>Top UK Cities for International Students</h3><p>A practical comparison of cost of living, community and university options across the UK.</p><a class="card-link" href="/blog-top-cities.html">Read Article {ICONS['arrow-right']}</a></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div>
          <h2>Ready to start your UK application?</h2>
          <p>Book a free, no-obligation consultation and get a clear plan for your course, visa and timeline.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} WhatsApp Us Now</a>
          <a class="btn btn-outline-light" href="mailto:{EMAIL}">{ICONS['mail']} Email Us</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

build_page(
    "index.html",
    "UK Study Abroad | UK University Admissions &amp; Visa Consultants for Saudi Students",
    "UK Study Abroad helps students in Saudi Arabia apply to UK universities, prepare for the Student Route visa, and plan their move to the UK. Free consultation via WhatsApp.",
    "index.html",
    home_body,
)
print("HOME done")

# ==========================================================================
# ABOUT
# ==========================================================================
def page_hero(eyebrow, title, desc, current_label):
    return f"""<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Home</a> <span>/</span> <span>{current_label}</span></div>
    <div class="eyebrow" style="background:rgba(255,255,255,.12);color:var(--gold-400);">{eyebrow}</div>
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</section>"""

about_body = f"""
<main id="main">
{page_hero('About Us', 'Built to make the UK feel within reach.', "UK Study Abroad is an independent education consultancy helping students plan, apply and prepare for university life in the United Kingdom — with Saudi Arabia as our founding market.", 'About Us')}

<section>
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Our Story</div>
        <h2>Why we started UK Study Abroad</h2>
        <p style="margin-top:16px;">Every year, thousands of talented students across Saudi Arabia consider studying in the United Kingdom — and every year, many give up before they even apply, overwhelmed by conflicting advice, confusing visa paperwork, and agents who push whichever university pays the best commission.</p>
        <p>UK Study Abroad exists to fix that. We built a consultancy around one simple idea: give students honest, visa-aware guidance from the very first conversation, in the same time zone they live in, without the pressure and confusion that usually comes with this journey.</p>
        <p>We're starting with a focused mission — supporting students in Saudi Arabia — because we believe doing one thing properly beats doing everything half-heartedly. As we grow, we plan to extend the same standard of support to students across the wider region.</p>
      </div>
      <div data-reveal>{decorative_panel('compass', 'Study. Explore. Grow. Succeed.', 'The four pillars behind everything we do — taken directly from our founding promise to students.')}</div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Our Values</div>
      <h2>What guides every recommendation we make</h2>
    </div>
    <div class="grid grid-4">
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['heart']}</div><h3>Honesty First</h3><p>We only recommend universities and courses that genuinely fit your grades, budget and goals.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['shield']}</div><h3>Visa-Aware Advice</h3><p>Every suggestion accounts for your Student visa eligibility from the very first conversation.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['headset']}</div><h3>Always Reachable</h3><p>WhatsApp-first support that respects Saudi Arabia working hours and replies quickly.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['target']}</div><h3>Outcome-Focused</h3><p>We measure success by successful visas and happy students, not the number of applications filed.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Our Team</div>
      <h2>People behind UK Study Abroad</h2>
      <p>A small, focused team covering counselling, admissions and visa guidance — with more specialists joining as we grow.</p>
    </div>
    <div class="grid grid-4">
      <div class="team-card" data-reveal><div class="team-avatar">F</div><h4>Founder &amp; Lead Consultant</h4><span class="role">Strategy &amp; Partnerships</span><p>Sets the direction for UK Study Abroad and oversees every student's journey end to end.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">A</div><h4>Admissions Specialist</h4><span class="role">University Applications</span><p>Matches students to courses and manages the university application process.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">V</div><h4>Visa &amp; Immigration Advisor</h4><span class="role">Student Route Guidance</span><p>Guides students through CAS, financial evidence and the visa application itself.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">S</div><h4>Student Support Officer</h4><span class="role">WhatsApp &amp; Pre-Departure</span><p>The first friendly reply you'll get on WhatsApp, and your contact for pre-departure prep.</p></div>
    </div>
    <p class="table-note" style="text-align:center;margin-top:24px;">Team structure shown reflects our current operating model — update with real staff names, titles and photos as your team grows.</p>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div>
          <h2>Let's talk about your UK plans</h2>
          <p>Tell us your grades, budget and course interests — we'll tell you honestly what's realistic and what to do next.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} WhatsApp Us Now</a>
          <a class="btn btn-outline-light" href="/contact.html">Contact Page</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

def faq_section(faqs, eyebrow="FAQs", title="Frequently asked questions"):
    items = "\n".join(
        f"""<div class="faq-item">
  <button class="faq-q" aria-expanded="false"><span>{q}</span><span class="plus"></span></button>
  <div class="faq-a"><p>{a}</p></div>
</div>"""
        for q, a in faqs
    )
    return f"""<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">{eyebrow}</div>
      <h2>{title}</h2>
    </div>
    <div style="max-width:820px;margin:0 auto;">
      {items}
    </div>
  </div>
</section>"""


# ==========================================================================
# SERVICES
# ==========================================================================
services_body = f"""
<main id="main">
{page_hero('Our Services', 'End-to-end support for your UK application', 'From your first question to your first week on campus — here is exactly how UK Study Abroad supports you at every stage.', 'Services')}

<section>
  <div class="container">
    <div class="grid grid-2">

      <div class="card" id="counselling" data-reveal>
        <div class="icon-wrap">{ICONS['chat']}</div>
        <h3>Free Counselling &amp; Course Selection</h3>
        <p style="margin-bottom:18px;">A relaxed, no-obligation conversation to understand your grades, budget, career goals and preferred UK cities before we suggest anything.</p>
        {check_list(['30-45 minute consultation via WhatsApp call or video', 'Honest shortlist of 3-5 realistic universities', 'Clear next-step plan with no pressure to commit'])}
      </div>

      <div class="card" id="applications" data-reveal>
        <div class="icon-wrap">{ICONS['doc-check']}</div>
        <h3>University Application Support</h3>
        <p style="margin-bottom:18px;">We help you build a strong application — not just a submitted one — so you present your best self to admissions teams.</p>
        {check_list(['UCAS or direct university application guidance', 'Personal statement review and feedback', 'Document checklist: transcripts, certificates, references'])}
      </div>

      <div class="card" data-reveal>
        <div class="icon-wrap">{ICONS['passport']}</div>
        <h3>Student Visa (Student Route) Guidance</h3>
        <p style="margin-bottom:18px;">Once your CAS is issued, we walk you through the Student Route visa application so nothing is left to guesswork.</p>
        {check_list(['CAS review and financial requirement explanation', 'Immigration Health Surcharge (IHS) and fee breakdown', 'Biometric appointment and document checklist'])}
        <a class="card-link" href="/visa-ielts.html">See the full visa guide {ICONS['arrow-right']}</a>
      </div>

      <div class="card" id="ielts" data-reveal>
        <div class="icon-wrap">{ICONS['book']}</div>
        <h3>IELTS &amp; English Test Guidance</h3>
        <p style="margin-bottom:18px;">We help you understand exactly which English test and score your course and visa require — and how to prepare realistically.</p>
        {check_list(['UKVI IELTS vs Academic IELTS explained', 'CEFR B1/B2 requirements by course level', 'Recommended preparation resources and timelines'])}
        <a class="card-link" href="/visa-ielts.html#ielts">See IELTS details {ICONS['arrow-right']}</a>
      </div>

      <div class="card" id="scholarships" data-reveal>
        <div class="icon-wrap">{ICONS['award']}</div>
        <h3>Scholarship &amp; Funding Guidance</h3>
        <p style="margin-bottom:18px;">We help you identify and apply for university scholarships, merit bursaries and relevant funding routes.</p>
        {check_list(['University-specific scholarship shortlists', 'Guidance on SACM-related funding questions', 'Application timeline planning around funding deadlines'])}
      </div>

      <div class="card" id="arrival" data-reveal>
        <div class="icon-wrap">{ICONS['home-key']}</div>
        <h3>Accommodation &amp; Pre-Departure Support</h3>
        <p style="margin-bottom:18px;">Once your visa is approved, we help you prepare for departure and your first weeks on campus.</p>
        {check_list(['Accommodation shortlist near your university', 'Pre-departure checklist: banking, SIM, essentials', 'Airport arrival and first-week orientation tips'])}
      </div>

    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">How It Works</div>
      <h2>Your journey with us, in four steps</h2>
    </div>
    <div class="steps">
      <div class="step" data-reveal><h4>Free Consultation</h4><p>Share your grades, budget and goals. We tell you honestly what's realistic.</p></div>
      <div class="step" data-reveal><h4>Course &amp; University Match</h4><p>We shortlist universities and help you submit strong applications.</p></div>
      <div class="step" data-reveal><h4>Visa &amp; IELTS Support</h4><p>Once accepted, we guide your English test and Student Route visa application.</p></div>
      <div class="step" data-reveal><h4>Pre-Departure &amp; Arrival</h4><p>Accommodation, checklists, and support for your first weeks in the UK.</p></div>
    </div>
  </div>
</section>

{faq_section([
    ("Is the initial consultation really free?", "Yes. Your first consultation is completely free and comes with no obligation to use our other services."),
    ("Do you guarantee university admission or a visa?", "No consultancy can honestly guarantee admission or a visa decision — those are made by universities and UK Visas &amp; Immigration. What we guarantee is honest guidance and thorough preparation to give you the strongest possible application."),
    ("Do you charge a fee for your services?", "Our fee structure depends on the level of support you need. We'll always explain any costs clearly and in advance — ask us on WhatsApp for current pricing."),
    ("Can you help even if I haven't chosen a course yet?", "Absolutely — that's exactly what the free consultation is for. Many students start with us before they've decided on a course or university."),
])}

<section>
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Not sure where to start?</h2><p>Message us on WhatsApp and we'll point you in the right direction — no forms, no pressure.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} Chat on WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# DESTINATIONS
# ==========================================================================
destinations_body = f"""
<main id="main">
{page_hero('Study Destinations', 'Why the UK — and where to study', 'Explore what makes the United Kingdom one of the world&rsquo;s top study destinations, and compare the cities and universities that could become your new home.', 'Study Destinations')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Why Study in the UK</div>
      <h2>What makes a UK degree worth it</h2>
    </div>
    <div class="grid grid-4">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['award']}</div><h3>Globally Recognised</h3><p>UK degrees are respected by employers and universities worldwide, backed by centuries of academic tradition.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['calendar']}</div><h3>Shorter Courses</h3><p>Bachelor's degrees typically take 3 years and Master's just 1 year — saving time and tuition cost versus many other countries.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['briefcase']}</div><h3>Graduate Work Route</h3><p>Eligible graduates can apply for the Graduate visa to work in the UK after finishing their studies, subject to current immigration rules.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>Multicultural Cities</h3><p>Study alongside students from around the world in cities with established Arabic-speaking and Saudi student communities.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Popular Cities</div>
      <h2>Where students choose to study</h2>
      <p>Every city offers a different balance of cost, culture and course options. We'll help you weigh them against your own priorities.</p>
    </div>
    <div class="dest-list">
      {city_tile('London', 'Global finance &amp; Russell Group universities', 0, 'Capital City')}
      {city_tile('Manchester', 'Vibrant, affordable, major research universities', 1, 'Best Value')}
      {city_tile('Birmingham', 'Central location, strong business schools', 2, 'Central Hub')}
      {city_tile('Edinburgh', 'Historic city, world-ranked institutions', 3, 'Historic Charm')}
      {city_tile('Coventry', 'Modern campuses, welcoming international community', 4, 'Community Focus')}
      {city_tile('Glasgow', 'Affordable living, strong engineering &amp; medicine', 5, 'Affordable Living')}
      {city_tile('Leeds', 'Large student population, strong law &amp; business', 6, 'Student Hub')}
      {city_tile('Sheffield', 'Friendly city, respected engineering faculties', 7, 'Engineering Hub')}
      {city_tile('Cardiff', "Compact capital, growing international intake", 8, 'Compact Capital')}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Popular Courses</div>
      <h2>What Saudi students commonly study in the UK</h2>
    </div>
    <div class="grid grid-3">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['briefcase']}</div><h3>Business &amp; MBA</h3><p>Management, finance, marketing and MBA programmes at universities with strong industry links.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['heart']}</div><h3>Medicine &amp; Health Sciences</h3><p>Medicine, dentistry, pharmacy and allied health courses — note that medicine places are highly competitive and entry requirements are strict.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['target']}</div><h3>Engineering</h3><p>Mechanical, civil, electrical and petroleum engineering at universities with accredited programmes.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>Computer Science &amp; AI</h3><p>Computer science, data science and artificial intelligence courses at universities investing heavily in tech faculties.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['doc-check']}</div><h3>Law</h3><p>LLB and LLM programmes, including routes for students planning to convert qualifications back home.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['compass']}</div><h3>Architecture &amp; Design</h3><p>Architecture, interior design and urban planning courses with strong studio-based teaching.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">University Options</div>
      <h2>A general guide to UK university types</h2>
      <p>This is general information to help you understand your options — not an exclusive partner list. We'll recommend specific universities once we know your grades and goals.</p>
    </div>
    <div class="split">
      <div>
        <h3 style="margin-bottom:14px;">Russell Group Universities</h3>
        <p style="margin-bottom:18px;">A group of 24 research-intensive, highly ranked UK universities — often more competitive to enter, with strong global recognition.</p>
        <div class="uni-pill-list">
          <span class="uni-pill">University of Manchester</span>
          <span class="uni-pill">University of Birmingham</span>
          <span class="uni-pill">University of Glasgow</span>
          <span class="uni-pill">University of Leeds</span>
          <span class="uni-pill">University of Sheffield</span>
          <span class="uni-pill">Queen Mary University of London</span>
        </div>
      </div>
      <div>
        <h3 style="margin-bottom:14px;">Modern &amp; Teaching-Focused Universities</h3>
        <p style="margin-bottom:18px;">Often more accessible entry requirements, strong career support, and a genuine focus on international student experience.</p>
        <div class="uni-pill-list">
          <span class="uni-pill">Coventry University</span>
          <span class="uni-pill">University of Hertfordshire</span>
          <span class="uni-pill">Northumbria University</span>
          <span class="uni-pill">University of Sunderland</span>
          <span class="uni-pill">University of East London</span>
          <span class="uni-pill">Teesside University</span>
        </div>
      </div>
    </div>
    <p class="table-note" style="margin-top:26px;">University names above are shown as general examples of well-known UK institutions and do not imply an existing partnership. Update this list with your confirmed partner universities.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Not sure which city or course fits you?</h2><p>Book a free consultation and we'll help you narrow it down based on your grades, budget and goals.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} WhatsApp Us</a>
          <a class="btn btn-outline-light" href="/contact.html">Book Consultation</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# VISA & IELTS
# ==========================================================================
visa_body = f"""
<main id="main">
{page_hero('Visa &amp; IELTS Guidance', 'The UK Student visa, explained simply', 'A clear, step-by-step look at the Student Route visa process and English language requirements &mdash; based on official UK government guidance.', 'Visa &amp; IELTS')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">The Process</div>
      <h2>Five stages of a UK Student visa application</h2>
    </div>
    <div class="timeline">
      <div class="timeline-item" data-reveal>
        <span class="tag">Stage 1</span>
        <h4>Get your university offer &amp; CAS</h4>
        <p>Once you accept an unconditional offer and meet the university's conditions, your UK sponsor institution issues a Confirmation of Acceptance for Studies (CAS) — a unique reference number required for your visa application.</p>
      </div>
      <div class="timeline-item" data-reveal>
        <span class="tag">Stage 2</span>
        <h4>Prove your English language ability</h4>
        <p>Most applicants must prove English proficiency to at least CEFR level B2 for degree-level courses (B1 for below-degree courses), usually via a Secure English Language Test (SELT) such as UKVI IELTS, unless exempt.</p>
      </div>
      <div class="timeline-item" data-reveal>
        <span class="tag">Stage 3</span>
        <h4>Show your financial evidence</h4>
        <p>You'll need to show you can cover your course fees and living costs, with the required funds held in your account for a consecutive 28-day period ending within 31 days of your application date.</p>
      </div>
      <div class="timeline-item" data-reveal>
        <span class="tag">Stage 4</span>
        <h4>Submit your application &amp; biometrics</h4>
        <p>Apply online up to 6 months before your course start date (if applying from outside the UK), pay the visa fee and Immigration Health Surcharge, then attend a biometric appointment at a visa application centre.</p>
      </div>
      <div class="timeline-item" data-reveal>
        <span class="tag">Stage 5</span>
        <h4>Receive your decision &amp; prepare to travel</h4>
        <p>Applications from outside the UK are usually decided within around 3 weeks. Once approved, we'll help you with a pre-departure checklist covering accommodation, banking, and your first days on campus.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Costs &amp; Requirements</div>
      <h2>What a Student visa costs (at a glance)</h2>
    </div>
    <div class="table-scroll">
      <table class="info-table">
        <thead><tr><th>Item</th><th>Typical Cost / Requirement</th></tr></thead>
        <tbody>
          <tr><td>Student visa application fee (from outside the UK)</td><td>£558</td></tr>
          <tr><td>Immigration Health Surcharge (IHS)</td><td>£776 per year of your visa</td></tr>
          <tr><td>Living cost financial evidence &mdash; London courses</td><td>£1,529 per month (up to 9 months)</td></tr>
          <tr><td>Living cost financial evidence &mdash; outside London</td><td>£1,171 per month (up to 9 months)</td></tr>
          <tr><td>Course fees requirement</td><td>Full amount shown on your CAS (or first year's fees if paying in instalments)</td></tr>
          <tr><td>Application window (from outside the UK)</td><td>Up to 6 months before your course starts</td></tr>
          <tr><td>Typical processing time (from outside the UK)</td><td>Around 3 weeks</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Figures shown reflect official UK government guidance at the time this page was published. Visa fees, financial thresholds and rules change periodically — we always confirm the latest requirements with you directly, and you can verify current figures on gov.uk at any time.</p>
  </div>
</section>

<section id="ielts">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">English Language Requirement</div>
        <h2>Which IELTS score do you actually need?</h2>
        <p style="margin:16px 0 22px;">Your required English level depends on your course level, not a single fixed number. Here's how it generally breaks down:</p>
        {check_list([
            'Degree-level courses (Bachelor&rsquo;s, Master&rsquo;s): equivalent to CEFR level B2',
            'Below degree-level (foundation, pathway courses): equivalent to CEFR level B1',
            'You may be exempt if you hold a UK degree, or a degree taught in English assessed by Ecctis',
            'Most applicants take an approved Secure English Language Test (SELT), such as UKVI IELTS',
        ])}
        <p>Your university may also accept its own English assessment for degree-level entry, provided it meets the B2 standard. We'll confirm exactly which test and score your chosen course requires before you book anything.</p>
      </div>
      <div data-reveal>{decorative_panel('book', 'IELTS UKVI', 'CEFR B1 &mdash; B2, depending on course level')}</div>
    </div>
  </div>
</section>

{faq_section([
    ("Do I need a UK visa consultant, or can I apply myself?", "You can apply for a Student visa yourself &mdash; the process doesn't legally require an agent. Many students choose support because the financial evidence rules and documentation are easy to get wrong, and a small mistake can cause delays or refusal."),
    ("What happens if my financial evidence doesn't meet the 28-day rule?", "Your application can be refused if the required funds haven't been held for a full, continuous 28-day period ending within 31 days of your application. We help you plan this timeline carefully in advance."),
    ("Can my family accompany me on a Student visa?", "Dependants are only permitted in specific circumstances under current UK immigration rules, mainly for postgraduate research students or government-sponsored students. We'll explain whether this applies to your situation."),
    ("Is the Graduate visa still available after I finish my degree?", "Yes, eligible graduates can currently apply for the Graduate visa to work in the UK after their studies. Note that the standard duration is due to change from 2 years to 18 months for new applicants (non-PhD) from 1 January 2027 &mdash; we'll keep you updated on how this affects your timeline."),
], eyebrow="Visa FAQs", title="Common visa &amp; IELTS questions")}

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Ready to check your visa eligibility?</h2><p>Send us your course offer or ask us anything about the process &mdash; we'll reply on WhatsApp within 24-48 hours.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link('Hi, I have a question about the UK Student visa process.')}" target="_blank" rel="noopener">{ICONS['whatsapp']} Ask on WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# TESTIMONIALS (kept content-free of fabricated reviews — see note below)
# ==========================================================================
# This page intentionally does not include any student quotes: we only
# publish real, verified reviews (with permission) once we have them. Update
# this page directly once your first cohort of students is ready to share
# feedback — a `testimonial()` helper and card styling already exist in
# build.py/style.css and can be reused at that point.
testimonials_body = f"""
<main id="main">
{page_hero('Testimonials', "We're just getting started", 'UK Study Abroad launched to serve students in Saudi Arabia, and we only publish real, verified reviews from students we&rsquo;ve actually worked with — never invented ones. This page will fill up as our first cohort completes their journey.', 'Testimonials')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">In the Meantime</div>
      <h2>What you can expect from working with us</h2>
    </div>
    <div class="grid grid-4">
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['chat']}</div><h3>Free, No-Pressure Advice</h3><p>An honest first conversation with no obligation to sign up for anything.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['headset']}</div><h3>Fast WhatsApp Replies</h3><p>Real answers within 24-48 hours, in Saudi Arabia-friendly hours.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['shield']}</div><h3>Visa-Aware Guidance</h3><p>Every recommendation accounts for your Student visa eligibility from day one.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['target']}</div><h3>Matched, Not Mass-Marketed</h3><p>Course and university suggestions based on your grades and goals — not a fixed list.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Want to be our first success story?</h2><p>Book a free consultation and let's talk about your UK university plans.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} WhatsApp Us</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

def post_card(icon, panel_label, category, date, title, desc, href):
    return f"""<div class="post-card" data-reveal>
  <div class="post-media">{decorative_panel(icon, panel_label)}</div>
  <div class="post-body"><div class="post-meta"><span>{category}</span><span>{date}</span></div><h3>{title}</h3><p>{desc}</p><a class="card-link" href="{href}">Read Article {ICONS['arrow-right']}</a></div>
</div>"""

POSTS = [
    dict(icon='passport', panel='Visa Guide', category='Visas', date='2026', slug='blog-visa-guide.html',
         title='UK Student Visa Guide for Saudi Students (2026)',
         desc="Everything you need to know about the Student Route visa — CAS, finances, IHS and timelines."),
    dict(icon='book', panel='IELTS Guide', category='English Tests', date='2026', slug='blog-ielts-guide.html',
         title='IELTS Requirements for UK Universities: What You Need to Know',
         desc="What score you actually need, which test to book, and how it affects your visa application."),
    dict(icon='compass', panel='City Guide', category='Student Life', date='2026', slug='blog-top-cities.html',
         title='Top UK Cities for International Students',
         desc="A practical comparison of cost of living, community and university options across the UK."),
]

# ==========================================================================
# BLOG (index)
# ==========================================================================
blog_cards = "\n".join(
    post_card(p['icon'], p['panel'], p['category'], p['date'], p['title'], p['desc'], "/" + p['slug'])
    for p in POSTS
)

blog_body = f"""
<main id="main">
{page_hero('Blog', 'Guides &amp; insights for your UK journey', 'Practical, plain-English articles to help you plan your application, visa and move to the United Kingdom.', 'Blog')}

<section>
  <div class="container">
    <div class="grid grid-3">
      {blog_cards}
    </div>
    <p class="table-note" style="text-align:center;margin-top:36px;">More articles coming soon. Have a question you'd like us to cover? <a href="/contact.html" style="color:var(--teal-700);font-weight:700;">Send us a message</a>.</p>
  </div>
</section>
</main>
"""

build_page(
    "blog.html",
    "Blog | UK Study Abroad",
    "Guides and insights on UK student visas, IELTS requirements and student life, written for students applying from Saudi Arabia.",
    "blog.html",
    blog_body,
)
print("BLOG index done")


def blog_post_page(slug, title, category, date, read_time, intro, body_html, related_slugs):
    related = [p for p in POSTS if p['slug'] in related_slugs]
    related_html = "\n".join(
        post_card(p['icon'], p['panel'], p['category'], p['date'], p['title'], p['desc'], "/" + p['slug'])
        for p in related
    )
    content = f"""
<main id="main">
<section class="page-hero" style="padding-bottom:56px;">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Home</a> <span>/</span> <a href="/blog.html">Blog</a> <span>/</span> <span>{category}</span></div>
    <div class="eyebrow" style="background:rgba(255,255,255,.12);color:var(--gold-400);">{category} &middot; {date} &middot; {read_time} read</div>
    <h1 style="max-width:820px;">{title}</h1>
  </div>
</section>
<section>
  <div class="container">
    <article class="post-content">
      <p style="font-size:1.1rem;color:var(--gray-700);">{intro}</p>
      {body_html}
      <hr class="divider">
      <p style="font-size:0.9rem;color:var(--gray-500);">Have questions about your own situation? <a href="/contact.html" style="color:var(--teal-700);font-weight:700;">Get in touch</a> or message us directly on <a href="{whatsapp_link()}" target="_blank" rel="noopener" style="color:var(--teal-700);font-weight:700;">WhatsApp</a>.</p>
    </article>
  </div>
</section>
<section class="bg-alt">
  <div class="container">
    <div class="section-head center"><div class="eyebrow">Keep Reading</div><h2>Related articles</h2></div>
    <div class="grid grid-3">{related_html}</div>
  </div>
</section>
</main>
"""
    build_page(slug, f"{title} | UK Study Abroad Blog", f"{title} — a practical guide from UK Study Abroad.", "blog.html", content)


# ---- Post 1: Visa Guide ----
blog_post_page(
    "blog-visa-guide.html",
    "UK Student Visa Guide for Saudi Students (2026)",
    "Visas", "2026", "6 min",
    "If you're planning to study in the United Kingdom, understanding the Student Route visa early will save you time, stress and money. Here's a plain-English walkthrough of how it works.",
    f"""
<h2>1. Get your CAS from your university</h2>
<p>Before you can apply for a visa, your UK university (a licensed student sponsor) must issue you a Confirmation of Acceptance for Studies (CAS) — a unique reference number confirming your place on the course. This is usually issued once you've met any conditions on your offer, such as final grades or a tuition deposit.</p>

<h2>2. Prove your English language ability</h2>
<p>Most applicants need to demonstrate English proficiency equivalent to CEFR level B2 for degree-level study, or B1 for below-degree courses. This is usually done through an approved Secure English Language Test (SELT) such as UKVI IELTS, unless you're exempt — for example, if you already hold a UK degree.</p>

<h2>3. Show you can financially support yourself</h2>
<p>You'll need to show evidence of funds covering your course fees (as stated on your CAS) plus a monthly living cost allowance — currently around £1,529 per month for courses in London, or £1,171 per month outside London, for up to 9 months. This money generally needs to sit in your account for a continuous 28-day period, ending within 31 days of your application date.</p>

<h2>4. Submit your application and pay the fees</h2>
<p>You can apply online up to 6 months before your course starts if you're applying from outside the UK. Along with the visa application fee, you'll need to pay the Immigration Health Surcharge (IHS), which gives you access to the NHS during your stay.</p>

<h2>5. Attend your biometric appointment</h2>
<p>As part of your application, you'll usually need to visit a visa application centre to provide fingerprints and a photo (biometric information).</p>

<h2>6. Wait for your decision</h2>
<p>Processing times vary, but applications from outside the UK are often decided within around 3 weeks. Once approved, you'll receive your visa vignette and can start planning your travel.</p>

<blockquote>Fees and financial requirements change periodically. Always confirm the latest figures on gov.uk, or ask us directly — we track these updates so you don't have to.</blockquote>
""",
    ["blog-ielts-guide.html", "blog-top-cities.html"],
)
print("BLOG post: visa guide done")

# ---- Post 2: IELTS Guide ----
blog_post_page(
    "blog-ielts-guide.html",
    "IELTS Requirements for UK Universities: What You Need to Know",
    "English Tests", "2026", "5 min",
    "English test scores are one of the most common sources of confusion for students applying to the UK. Here's how to figure out exactly what you need.",
    f"""
<h2>Which test do you actually need?</h2>
<p>For your visa application, the UK Home Office requires a Secure English Language Test (SELT) from an approved provider — most commonly UKVI IELTS (also called IELTS for UKVI). This is different from the standard "Academic" or "General Training" IELTS you may take for other purposes, so always check which version your university and visa application require before booking.</p>

<h2>What score do you need?</h2>
<p>Requirements are generally tied to your course level:</p>
<ul>
<li><strong>Degree-level courses</strong> (Bachelor's, Master's and above): equivalent to CEFR level B2</li>
<li><strong>Below degree-level courses</strong> (foundation or pathway programmes): equivalent to CEFR level B1</li>
</ul>
<p>Many universities also set their own minimum overall band score and minimum scores per skill (reading, writing, listening, speaking) — so it's worth checking your specific course page or asking your admissions team directly.</p>

<h2>Are you exempt from taking a test?</h2>
<p>You may not need to sit an English test if you already hold a bachelor's degree or higher taught in English (subject to an assessment from Ecctis for non-UK degrees), or a relevant UK qualification such as GCSEs or A-levels.</p>

<h2>How should you prepare?</h2>
<p>Give yourself enough runway — most students benefit from at least 6-8 weeks of focused preparation, particularly for the writing and speaking sections. Book your test early enough that you have time to retake it if needed, without delaying your CAS or visa timeline.</p>

<blockquote>Don't overspend on test preparation before you know your target score. We'll help you confirm the exact requirement for your course first.</blockquote>
""",
    ["blog-visa-guide.html", "blog-top-cities.html"],
)
print("BLOG post: ielts guide done")

# ---- Post 3: Top Cities ----
blog_post_page(
    "blog-top-cities.html",
    "Top UK Cities for International Students",
    "Student Life", "2026", "6 min",
    "Choosing where to study in the UK is about far more than league tables. Here's a practical look at some of the most popular cities for international students.",
    f"""
<h2>London</h2>
<p>Home to some of the world's most recognised universities, plus unmatched career and networking opportunities. Living costs are higher than the rest of the UK, which is reflected in the visa financial requirement (£1,529/month vs £1,171/month elsewhere).</p>

<h2>Manchester</h2>
<p>A large, diverse student city with a lower cost of living than London, strong transport links, and a well-established international student community.</p>

<h2>Birmingham</h2>
<p>Centrally located with excellent rail connections to the rest of the UK, home to respected business schools and a growing international population.</p>

<h2>Edinburgh &amp; Glasgow</h2>
<p>Scotland's two largest cities offer historic campuses, strong research reputations, and generally lower living costs than London — plus a distinct cultural experience within the UK.</p>

<h2>Coventry &amp; Sheffield</h2>
<p>Both offer modern campuses, a lower cost of living, and universities known for being genuinely welcoming to international and first-generation students.</p>

<h2>How to choose</h2>
<p>Weigh these factors: total cost of living against your budget, the specific course strength at each university (not just city reputation), the size of the existing Arabic-speaking or Saudi student community, and how easily you can travel home for holidays. We help students compare all of this side by side before making a final decision.</p>
""",
    ["blog-visa-guide.html", "blog-ielts-guide.html"],
)
print("BLOG post: top cities done")

# ==========================================================================
# CONTACT
# ==========================================================================
contact_body = f"""
<main id="main">
{page_hero('Contact Us', "Let's talk about your UK plans", "Reach out on WhatsApp for the fastest reply, or send us a message using the form below. We aim to respond within 24-48 hours.", 'Contact')}

<section>
  <div class="container">
    <div class="contact-grid">
      <div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['whatsapp']}</div>
          <div><h4>WhatsApp</h4><p>Fastest way to reach us — chat with a real advisor.</p><a class="value" href="{whatsapp_link()}" target="_blank" rel="noopener">{WHATSAPP_DISPLAY}</a></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['mail']}</div>
          <div><h4>Email</h4><p>For documents, applications and anything non-urgent.</p><a class="value" href="mailto:{EMAIL}">{EMAIL}</a></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['clock']}</div>
          <div><h4>Response Hours</h4><p>We reply in Saudi Arabia-friendly hours (AST), typically within 24-48 hours on WhatsApp and email.</p></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['pin']}</div>
          <div><h4>Who We Serve</h4><p>Currently supporting students across the Kingdom of Saudi Arabia — Riyadh, Jeddah, Dammam and beyond.</p></div>
        </div>
      </div>

      <div class="form-card" data-reveal>
        <h3 style="margin-bottom:8px;">Send us a message</h3>
        <p style="margin-bottom:26px;font-size:0.94rem;">Tell us a little about your goals and we'll get back to you with clear next steps.</p>
        <form id="contact-form">
          <input type="hidden" name="access_key" value="YOUR_WEB3FORMS_ACCESS_KEY">
          <input type="hidden" name="subject" value="New enquiry from ukstudyabroad.co.uk">
          <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
          <div class="form-row">
            <div class="field"><label for="name">Full Name</label><input type="text" id="name" name="name" required placeholder="Your full name"></div>
            <div class="field"><label for="phone">WhatsApp / Phone Number</label><input type="tel" id="phone" name="phone" required placeholder="+966 5X XXX XXXX"></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="email">Email Address</label><input type="email" id="email" name="email" required placeholder="you@example.com"></div>
            <div class="field"><label for="interest">I'm Interested In</label>
              <select id="interest" name="interest">
                <option>Free Consultation</option>
                <option>University Application</option>
                <option>Student Visa Guidance</option>
                <option>IELTS Guidance</option>
                <option>Scholarships</option>
                <option>Something Else</option>
              </select>
            </div>
          </div>
          <div class="field"><label for="message">Your Message</label><textarea id="message" name="message" required placeholder="Tell us about your grades, budget and preferred course or city..."></textarea></div>
          <button type="submit" class="btn btn-primary btn-block">Send Message</button>
          <div class="form-status"></div>
          <p class="form-note">By submitting, you agree to be contacted by UK Study Abroad via email, phone or WhatsApp about your enquiry. We do not share your information with third parties.</p>
        </form>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# 404
# ==========================================================================
notfound_body = f"""
<main id="main">
<section class="error-page">
  <div class="container">
    <div class="code">404</div>
    <h1 style="margin:10px 0 16px;">This page has moved on to better things.</h1>
    <p style="margin-bottom:30px;">The page you're looking for doesn't exist or may have been renamed. Let's get you back on track.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
      <a class="btn btn-primary" href="/index.html">Back to Home</a>
      <a class="btn btn-outline" href="/contact.html">Contact Us</a>
    </div>
  </div>
</section>
</main>
"""
build_page("404.html", "Page Not Found | UK Study Abroad", "The page you're looking for could not be found.", "", notfound_body)
print("404 done")

# ==========================================================================
# PRIVACY POLICY (basic, editable)
# ==========================================================================
legal_wrap = lambda title, current, body: f"""
<main id="main">
{page_hero('Legal', title, 'Last updated: September 2026.', current)}
<section><div class="container"><article class="post-content">{body}</article></div></section>
</main>
"""

privacy_body = """
<p>UK Study Abroad ("we", "us", "our") respects your privacy. This page explains, in general terms, how we collect and use information when you use this website or contact us via WhatsApp, email or our contact form.</p>
<h2>Information We Collect</h2>
<p>When you submit our contact form or message us directly, we may collect your name, email address, phone/WhatsApp number, and any details you choose to share about your study plans.</p>
<h2>How We Use Your Information</h2>
<p>We use the information you provide to respond to your enquiry, offer consultation and application support, and — with your consent — send you relevant updates about our services.</p>
<h2>Data Sharing</h2>
<p>We do not sell your personal information. We may share necessary details with UK universities or visa application services strictly as part of delivering the services you request from us.</p>
<h2>Your Rights</h2>
<p>You can ask us at any time to access, correct, or delete the personal information we hold about you by contacting us at the email address on our Contact page.</p>
<p style="margin-top:30px;font-size:0.85rem;color:var(--gray-500);"><em>This is a general-purpose placeholder policy. Please review it with a qualified legal advisor and update it to reflect your actual data practices, tools (such as your chosen form provider) and any applicable Saudi Arabian or UK data protection requirements before publishing this site live.</em></p>
"""
build_page("privacy-policy.html", "Privacy Policy | UK Study Abroad", "How UK Study Abroad collects, uses and protects your personal information.", "", legal_wrap("Privacy Policy", "Privacy Policy", privacy_body))
print("PRIVACY done")

terms_body = """
<p>These Terms of Use govern your use of the UK Study Abroad website. By using this site, you agree to these terms.</p>
<h2>Educational Guidance, Not a Guarantee</h2>
<p>UK Study Abroad provides counselling and application support. We do not control, and cannot guarantee, decisions made by universities or by UK Visas &amp; Immigration.</p>
<h2>Accuracy of Information</h2>
<p>We aim to keep visa, IELTS and university information accurate and up to date, but rules and fees can change. Always confirm time-sensitive details directly with us or via official government sources before making decisions.</p>
<h2>Intellectual Property</h2>
<p>All content on this site, including our logo and branding, belongs to UK Study Abroad unless otherwise stated.</p>
<h2>Contact</h2>
<p>Questions about these terms can be sent to us via our Contact page.</p>
<p style="margin-top:30px;font-size:0.85rem;color:var(--gray-500);"><em>This is a general-purpose placeholder. Please review it with a qualified legal advisor before publishing this site live.</em></p>
"""
build_page("terms.html", "Terms of Use | UK Study Abroad", "Terms of use for the UK Study Abroad website.", "", legal_wrap("Terms of Use", "Terms of Use", terms_body))
print("TERMS done")

build_page(
    "contact.html",
    "Contact Us | UK Study Abroad",
    "Get in touch with UK Study Abroad via WhatsApp, email or our contact form to start your UK university application.",
    "contact.html",
    contact_body,
)
print("CONTACT done")

build_page(
    "testimonials.html",
    "Student Testimonials | UK Study Abroad",
    "Read what students say about applying to UK universities and securing their Student visa with UK Study Abroad's guidance.",
    "testimonials.html",
    testimonials_body,
)
print("TESTIMONIALS done")

build_page(
    "visa-ielts.html",
    "UK Student Visa &amp; IELTS Guidance | UK Study Abroad",
    "A clear guide to the UK Student Route visa process, costs, financial requirements and IELTS/English language requirements for students applying from Saudi Arabia.",
    "visa-ielts.html",
    visa_body,
)
print("VISA-IELTS done")

build_page(
    "destinations.html",
    "Study Destinations &amp; UK Universities | UK Study Abroad",
    "Compare popular UK study cities, courses and university types for international students, including guidance tailored to students from Saudi Arabia.",
    "destinations.html",
    destinations_body,
)
print("DESTINATIONS done")

build_page(
    "services.html",
    "Our Services | UK Study Abroad",
    "Explore UK Study Abroad's full range of services: free counselling, university applications, Student Route visa guidance, IELTS support, scholarships and pre-departure help.",
    "services.html",
    services_body,
)
print("SERVICES done")

build_page(
    "about.html",
    "About Us | UK Study Abroad",
    "Learn how UK Study Abroad helps students in Saudi Arabia apply to UK universities with honest, visa-aware guidance from a dedicated team.",
    "about.html",
    about_body,
)
print("ABOUT done")
