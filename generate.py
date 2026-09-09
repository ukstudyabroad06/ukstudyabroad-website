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
      <span class="hero-eyebrow">{ICONS['star']} UK Study Abroad Consultancy</span>
      <h1>Your complete pathway to <span>studying in the UK</span>.</h1>
      <p class="lead">From short courses and IELTS preparation to university recruitment, degree placement and our own live online to UK academic programme, we help ambitious students from Saudi Arabia find the right path to studying and succeeding in the UK.</p>
      <p style="margin:-14px 0 26px;color:var(--muted);font-size:0.98rem;">Our team includes genuine UK university lecturers and professors, so every step of your journey is backed by real academic expertise, not just paperwork.</p>
      <div class="hero-cta">
        <a class="btn btn-whatsapp" href="/services.html">{ICONS['book']} Explore Our Services</a>
        <a class="btn btn-outline-light" href="/schools.html">For Schools &amp; Colleges</a>
      </div>
      <div class="hero-trust">
        <div><strong>5 Services</strong><span>One Trusted Study Abroad Partner</span></div>
        <div><strong>UK Academics</strong><span>Real Lecturers &amp; Professors on Our Team</span></div>
        <div><strong>Saudi Arabia</strong><span>Direct Support for Families &amp; Schools</span></div>
      </div>
    </div>
    <div class="hero-visual" data-reveal>
      <img src="/assets/images/logo-full-web.png" alt="UK Study Abroad. Learn Online. Think Globally. Experience the UK." loading="eager">
      <div class="hero-badge">
        <div class="icon">{ICONS['cap']}</div>
        <div><strong>Taught by UK Academics</strong><span>Genuine UK university expertise on our team</span></div>
      </div>
    </div>
  </div>
</section>

<section class="stats-strip">
  <div class="container">
    <div class="grid grid-4">
      <div><strong>5 Services</strong><span>Covering every stage of your journey</span></div>
      <div><strong>UK Faculty</strong><span>Real lecturers and professors on our team</span></div>
      <div><strong>Recruitment to Degree</strong><span>Support from first enquiry to enrolment</span></div>
      <div><strong>Saudi Arabia</strong><span>Our current focus market</span></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">How We Help</div>
      <h2>One partner for the whole journey to UK study.</h2>
      <p>Studying abroad involves more than one decision. Students and families often need help with several things at once: preparing for an English exam, choosing the right course, applying to the right university, and finding meaningful academic experiences along the way. Most consultancies only cover part of that journey.</p>
      <p>UK Study Abroad brings it together in one place, combining practical application support with genuine UK academic expertise, so students and schools do not have to juggle several different providers.</p>
      <p style="font-weight:600;">One trusted partner. Every stage of the journey.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Our Services</div>
      <h2>Everything you need to study and succeed in the UK</h2>
      <p>Explore each service below, or message us on WhatsApp and we will help you find the right starting point.</p>
    </div>
    <div class="grid grid-3">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['book']}</div><h3>Short Courses</h3><p>Focused, practical courses that build specific academic skills and confidence.</p><a class="card-link" href="/services.html#short-courses">Learn More {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['doc-check']}</div><h3>University Recruitment</h3><p>Clear, honest guidance choosing universities and preparing a strong application.</p><a class="card-link" href="/services.html#recruitment">Learn More {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>Degree Placement</h3><p>Support finding and securing the right degree place at a UK institution.</p><a class="card-link" href="/services.html#degree-placement">Learn More {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['target']}</div><h3>IELTS Preparation</h3><p>Structured preparation that builds the exam skills and confidence for a strong score.</p><a class="card-link" href="/services.html#ielts">Learn More {ICONS['arrow-right']}</a></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>Global Career Development Programme</h3><p>Our flagship live online academic module, with an optional UK experience.</p><a class="card-link" href="/services.html#global-career-programme">Learn More {ICONS['arrow-right']}</a></div>
    </div>
    <div style="text-align:center;margin-top:36px;">
      <a class="btn btn-primary" href="/services.html">See All Our Services {ICONS['arrow-right']}</a>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Why Families Choose Us</div>
      <h2>A single, trusted partner for the whole journey</h2>
    </div>
    <div class="grid grid-2">
      <div class="card" data-reveal>
        <div class="icon-wrap">{ICONS['cap']}</div>
        <h3>Genuine UK academic access</h3>
        <p>Our team includes real UK university lecturers and professors, so families get more than paperwork help. They get direct academic expertise.</p>
      </div>
      <div class="card" data-reveal>
        <div class="icon-wrap">{ICONS['doc-check']}</div>
        <h3>Complete application support</h3>
        <p>From choosing courses to submitting a strong application, we guide students through university recruitment and degree placement from start to finish.</p>
      </div>
      <div class="card" data-reveal>
        <div class="icon-wrap">{ICONS['book']}</div>
        <h3>Exam and language preparation</h3>
        <p>Structured IELTS preparation and short courses build the practical skills and confidence students need before they apply.</p>
      </div>
      <div class="card" data-reveal>
        <div class="icon-wrap">{ICONS['users']}</div>
        <h3>Trusted school partnerships</h3>
        <p>We work directly with school principals and colleges across Saudi Arabia, giving their students real benefits through our partnership.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('users', 'For Schools & Colleges', 'Real benefits for your students&rsquo; future', 'gold')}</div>
      <div>
        <div class="eyebrow">For Schools &amp; Colleges</div>
        <h2>A partnership built around your students&rsquo; global future</h2>
        <p style="margin:16px 0 26px;">We work directly with school principals and colleges across Saudi Arabia, combining short courses, university recruitment, degree placement, IELTS preparation and our Global Career Development Programme into a partnership built around what benefits your students most as they plan their study abroad future in the UK.</p>
        <div style="margin-bottom:28px;">
        {check_list([
            'Practical support that helps your students move confidently toward university and their careers',
            'Direct access to genuine UK academic expertise through our own team of lecturers and professors',
            'A collaborative partnership shaped around your school and your students, not a one size fits all package',
        ])}
        </div>
        <a class="btn btn-primary" href="/schools.html">Partner With Us {ICONS['arrow-right']}</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div>
          <h2>Ready to plan your next step?</h2>
          <p>Message us to learn more about our services, for your family or your school.</p>
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
    "UK Study Abroad | Study Abroad Consultancy for Saudi Arabia",
    "UK Study Abroad is a study abroad consultancy offering short courses, university recruitment, degree placement, IELTS preparation and the Global Career Development Programme, a live online academic module with an optional UK experience, for students and schools in Saudi Arabia.",
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
{page_hero('About Us', 'A complete study abroad consultancy, built around real UK academic expertise.', "UK Study Abroad supports students and schools across Saudi Arabia with short courses, university recruitment, degree placement, IELTS preparation and our own live online to UK academic programme.", 'About Us')}

<section>
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Our Story</div>
        <h2>Why we started UK Study Abroad</h2>
        <p style="margin-top:16px;">Every year, thousands of talented students across Saudi Arabia are capable of far more than a single pathway can offer. What many of them are missing is not ambition. It is one trusted partner who can help with the practical steps of studying abroad and provide genuine UK academic expertise along the way.</p>
        <p>UK Study Abroad was founded to bring these pieces together. We support students and schools with short courses, university recruitment and application guidance, degree placement and IELTS preparation, alongside our own Global Career Development Programme, a live online academic module taught directly by UK university lecturers and professors, with the option to continue that learning in person in the UK.</p>
        <p>We are starting with a focused mission, supporting students and schools in Saudi Arabia, because we believe doing this properly beats doing it half heartedly. As we grow, we plan to extend the same standard of support to students across the wider region.</p>
      </div>
      <div data-reveal>{decorative_panel('cap', 'Academic. International. Real.', 'The principles behind everything we deliver.')}</div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Our Values</div>
      <h2>What guides every service we deliver</h2>
    </div>
    <div class="grid grid-4">
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['cap']}</div><h3>Academic Integrity</h3><p>Our Global Career Development Programme is designed and delivered by people with genuine UK university academic experience, never outsourced to generic instructors.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['users']}</div><h3>Genuinely International</h3><p>Students learn alongside peers from other countries, building the cross cultural confidence that global study and careers require.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['heart']}</div><h3>Honesty First</h3><p>We give clear, honest advice about which courses and universities genuinely fit each student, never just the easiest option to recommend.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['target']}</div><h3>Outcome Focused</h3><p>We measure success by the outcomes our students achieve, from exam scores to university offers to completed programmes.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Our Team</div>
      <h2>People behind UK Study Abroad</h2>
      <p>A small, academically led team, with more UK university lecturers and professors joining our faculty as we grow.</p>
    </div>
    <div class="grid grid-4">
      <div class="team-card" data-reveal><div class="team-avatar">F</div><h4>Founder &amp; Director</h4><span class="role">Strategy &amp; Partnerships</span><p>Sets the direction for UK Study Abroad and oversees every student's journey, from first enquiry to enrolment and beyond.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">A</div><h4>Academic Lead</h4><span class="role">UK University Lecturer</span><p>Designs and teaches the live online academic module, drawing directly on UK university teaching experience.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">P</div><h4>Partnerships Lead</h4><span class="role">Schools &amp; Colleges</span><p>Works directly with school principals and colleges to bring our services to their students.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">S</div><h4>Student Experience Coordinator</h4><span class="role">WhatsApp &amp; Enquiries</span><p>The first friendly reply you will get on WhatsApp, and your contact throughout your application or programme.</p></div>
    </div>
    <p class="table-note" style="text-align:center;margin-top:24px;">Team structure shown reflects our current operating model. Update with real staff names, titles, academic credentials and photos as your faculty grows.</p>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div>
          <h2>Let's talk about your student's global future</h2>
          <p>Tell us a little about your child or your school, and we will explain honestly which of our services is the right fit.</p>
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
{page_hero('Our Services', 'Everything you need to study and succeed in the UK.', 'From short courses and IELTS preparation to university recruitment, degree placement and our own live academic programme, we support students at every stage of their UK study journey.', 'Services')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Who We Help</div>
      <h2>Built for ambitious, globally minded students</h2>
      <p>Our services are designed for international students who want more than a single pathway, currently welcoming students from schools and colleges across Saudi Arabia.</p>
    </div>
    <div class="grid grid-4">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>Academically Ambitious</h3><p>Students who want a genuine taste of UK university level thinking, not just extra homework.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>Globally Minded</h3><p>Students who want to build the international outlook that universities and employers increasingly expect.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['users']}</div><h3>Ready to Collaborate</h3><p>Students who are comfortable working alongside peers from other countries on shared academic tasks.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['target']}</div><h3>Planning Ahead</h3><p>Students starting to think seriously about their next step toward university and their career.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt" id="short-courses">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Short Courses</div>
        <h2>Build practical skills with a focused short course</h2>
        <p style="margin:16px 0 22px;">Our short courses are designed to build specific academic or practical skills over a condensed timeframe, ideal for students who want a meaningful head start without a long term commitment.</p>
        {check_list([
            'Flexible, focused courses on specific academic and practical skills',
            'Delivered online for easy access from anywhere',
            'A practical first step before a bigger academic commitment',
        ])}
      </div>
      <div data-reveal>{decorative_panel('book', 'Short Courses', 'A focused, practical head start')}</div>
    </div>
  </div>
</section>

<section id="recruitment">
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('doc-check', 'University Recruitment', 'Guidance through every step of the application')}</div>
      <div>
        <div class="eyebrow">University Recruitment</div>
        <h2>Clear, honest guidance through university applications</h2>
        <p style="margin:16px 0 22px;">Choosing the right course and university, and putting together a strong application, can be overwhelming without the right support. We guide students through the process step by step, from shortlisting universities to submitting a complete, well prepared application.</p>
        {check_list([
            'Help shortlisting universities and courses that genuinely fit each student',
            'Guidance on personal statements, references and application requirements',
            'Clear, honest advice with no pressure toward any particular institution',
        ])}
      </div>
    </div>
  </div>
</section>

<section class="bg-alt" id="degree-placement">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Degree Placement</div>
        <h2>Support finding the right degree place</h2>
        <p style="margin:16px 0 22px;">We help students identify and secure a place on the right undergraduate or postgraduate degree course at a UK institution, matching each student's goals, grades and interests to the right option.</p>
        {check_list([
            'Matching students to degree courses that fit their goals and grades',
            'Support through offers, conditions and enrolment',
            'Ongoing guidance right up to the start of the degree',
        ])}
      </div>
      <div data-reveal>{decorative_panel('cap', 'Degree Placement', 'The right course, at the right university')}</div>
    </div>
  </div>
</section>

<section id="ielts">
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('target', 'IELTS Preparation', 'Practical preparation toward a real target score')}</div>
      <div>
        <div class="eyebrow">IELTS Preparation</div>
        <h2>Structured preparation for the IELTS exam</h2>
        <p style="margin:16px 0 22px;">Meeting the English language requirement is often the first practical step toward studying in the UK. Our IELTS preparation builds the exam skills, confidence and practice students need to reach their target score.</p>
        {check_list([
            'Structured preparation across reading, writing, listening and speaking',
            'Practice with realistic exam style tasks and feedback',
            'A clear, practical plan toward each student&rsquo;s target score',
        ])}
      </div>
    </div>
  </div>
</section>

<section class="bg-alt" id="global-career-programme">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Our Flagship Programme</div>
      <h2>Global Career Development Programme</h2>
      <p>Learn Online. Think Globally. Experience the UK. A live online academic module taught directly by UK university lecturers and professors, with the option to continue the experience in person in the UK.</p>
    </div>
    <div class="split" style="margin-top:10px;">
      <div>
        <div class="eyebrow">Stage One</div>
        <h3 style="margin:10px 0 14px;">The online academic module</h3>
        <p style="margin:0 0 22px;">The programme opens with a short, live online academic module delivered directly by UK university lecturers and professors. Students are not watching pre-recorded videos. They are taught in real time by academics with genuine UK university teaching experience.</p>
        {check_list([
            'Live sessions taught directly by UK university lecturers and professors',
            'Small, international cohorts so every student can take part in discussion',
            'Academic and professional skills built through real coursework, not worksheets',
        ])}
      </div>
      <div data-reveal>{decorative_panel('cap', 'Live Online Teaching', 'Delivered directly by UK university lecturers')}</div>
    </div>
    <div class="split reverse" style="margin-top:56px;">
      <div class="split-media" data-reveal>{decorative_panel('globe', 'Two Weeks in the UK', 'An optional continuation of the module, not a summer camp')}</div>
      <div>
        <div class="eyebrow">Stage Two, Optional</div>
        <h3 style="margin:10px 0 14px;">The UK experience</h3>
        <p style="margin:0 0 22px;">Students who complete the online module have the option to travel to the UK for a two week in person experience over the summer, continuing their learning on the ground rather than starting something new. This is not a sightseeing trip built around a summer camp format. It is a continuation of the same academic programme, in the country it is designed around.</p>
        {check_list([
            'Two weeks in the UK, continuing the academic module in person',
            'Delivered by the same academic team, not a separate holiday provider',
            'Optional: students can complete the full programme online only if preferred',
        ])}
      </div>
    </div>
    <div style="margin-top:56px;">
      <div class="section-head center">
        <div class="eyebrow">Stage Three</div>
        <h3>Final project and certificate</h3>
        <p>Every student completes a final project that brings their learning together, and graduates with a certificate recognising their academic and professional development.</p>
      </div>
      <div class="steps">
        <div class="step" data-reveal><h4>1. Online Academic Module</h4><p>Live teaching from UK university lecturers and professors.</p></div>
        <div class="step" data-reveal><h4>2. International Collaboration</h4><p>Shared academic work with students from other countries.</p></div>
        <div class="step" data-reveal><h4>3. Skills Development</h4><p>Academic, professional and interpersonal skills, built throughout.</p></div>
        <div class="step" data-reveal><h4>4. UK Experience</h4><p>An optional two week continuation of the module, in the UK.</p></div>
        <div class="step" data-reveal><h4>5. Final Project</h4><p>One piece of work that brings the whole module together.</p></div>
        <div class="step" data-reveal><h4>6. Certificate</h4><p>Recognition of genuine academic and professional development.</p></div>
      </div>
    </div>
  </div>
</section>

{faq_section([
    ("What is the difference between your services?", "Short courses and IELTS preparation build specific academic and exam skills. University recruitment and degree placement help students choose and secure the right university course. The Global Career Development Programme is our own academic programme, delivered directly by UK university lecturers and professors, with an optional experience in the UK."),
    ("Do I have to choose only one service?", "No. Many students combine services, for example IELTS preparation alongside university recruitment, or the Global Career Development Programme alongside degree placement support later on."),
    ("Who actually teaches the online academic module?", "UK university lecturers and professors teach every live session directly."),
    ("Is the UK experience compulsory?", "No. Students can complete the full academic module and earn their certificate entirely online. The two week UK experience is an optional continuation for students who want to extend their learning in person."),
    ("Does the programme help with university applications?", "The Global Career Development Programme is academic and professional development in its own right, though many students combine it with our university recruitment and degree placement support when they are ready to apply."),
    ("Do you only work with students in Saudi Arabia?", "Saudi Arabia is our founding market and current focus. We plan to extend our services to more countries as we grow."),
], eyebrow="Services FAQs", title="Common questions about our services")}

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Ready to find out more?</h2><p>Message us on WhatsApp to talk through which of our services is the right fit, for your family or your school.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} Chat on WhatsApp</a>
          <a class="btn btn-outline-light" href="/schools.html">For Schools &amp; Colleges</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# SCHOOLS & COLLEGES
# ==========================================================================
schools_body = f"""
<main id="main">
{page_hero('Schools &amp; Colleges', 'A partnership built for school principals', 'We work directly with school principals and colleges across Saudi Arabia, bringing short courses, university recruitment, degree placement, IELTS preparation and our Global Career Development Programme together in a partnership built around your students&rsquo; global future.', 'Schools & Colleges')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Why Partner With Us</div>
      <h2>How this partnership benefits your students&rsquo; future</h2>
      <p>A single, academically credible partner your school can offer with confidence, helping your students move toward university and their careers in the UK.</p>
    </div>
    <div class="grid grid-4">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['target']}</div><h3>Complete Support, One Partner</h3><p>From short courses to university recruitment, degree placement and IELTS preparation, we cover the services your students need for their next step, so your school does not have to coordinate several providers.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['award']}</div><h3>Strengthens Your Profile</h3><p>Offering a genuine pathway to UK study adds a real point of distinction for your school or college among parents.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['headset']}</div><h3>Low Effort for Your Team</h3><p>We design and deliver the services directly. Your staff simply help us reach the right students.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>Real Student Outcomes</h3><p>Students leave with practical progress toward their goals, from stronger IELTS scores to university offers and completed academic programmes.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('users', 'For School Principals', 'A partnership you can stand behind with confidence')}</div>
      <div>
        <div class="eyebrow">For School Principals</div>
        <h2>How the partnership works</h2>
        <p style="margin:16px 0 22px;">We know a principal's time is limited, so we have kept our side of this simple. You introduce our services to your students and families. We handle everything directly: teaching, exam preparation, application guidance and university placement support, all under one partnership built around your students&rsquo; future.</p>
        {check_list([
            'We share clear, ready to use information for parents and students',
            'Your school is not responsible for teaching or academic delivery',
            'We stay in direct contact with your team throughout the partnership',
        ])}
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">What Your Partnership Can Include</div>
      <h2>Benefits for your students&rsquo; global study future</h2>
    </div>
    <div class="steps">
      <div class="step" data-reveal><h4>Short Courses</h4><p>Practical, focused courses that build specific academic skills and confidence.</p></div>
      <div class="step" data-reveal><h4>IELTS Preparation</h4><p>Structured preparation toward each student&rsquo;s target score.</p></div>
      <div class="step" data-reveal><h4>University Recruitment</h4><p>Guidance choosing universities and preparing strong applications.</p></div>
      <div class="step" data-reveal><h4>Degree Placement</h4><p>Support securing the right degree place at a UK institution.</p></div>
      <div class="step" data-reveal><h4>Global Career Programme</h4><p>Our flagship live online academic module, with an optional UK experience.</p></div>
    </div>
    <div style="text-align:center;margin-top:36px;">
      <a class="btn btn-outline" href="/services.html">See Our Full Range of Services {ICONS['arrow-right']}</a>
    </div>
  </div>
</section>

{faq_section([
    ("What does our school need to provide?", "Mainly your help introducing our services to students and families. We design and deliver the academic content, exam preparation and application support directly."),
    ("Is there a cost to the school?", "There is no cost to your school to become a partner. Ask us on WhatsApp for the current arrangement for students and families."),
    ("Can we see your services before recommending them to parents?", "Yes. We are happy to walk your team through a full outline of our services before you introduce them to families."),
    ("Do you only work with schools in Saudi Arabia?", "Saudi Arabia is our founding market and current focus. We plan to extend school partnerships to more countries as we grow."),
], eyebrow="Partner FAQs", title="Questions school principals ask us")}

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Interested in partnering with us?</h2><p>Message us on WhatsApp and we will walk you through our services in detail, principal to principal.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link('Hi, I am a school principal interested in partnering with UK Study Abroad.')}" target="_blank" rel="noopener">{ICONS['whatsapp']} WhatsApp Us</a>
          <a class="btn btn-outline-light" href="/contact.html">Contact Us</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# ELIGIBILITY & FAQS
# ==========================================================================
faqs_body = f"""
<main id="main">
{page_hero('Eligibility &amp; FAQs', 'Everything parents and students ask us', 'Practical answers on eligibility, our services, the UK experience and how the certificate works, in plain English.', 'FAQs')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">Eligibility</div>
      <h2>Who we can help</h2>
    </div>
    <div class="grid grid-3">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>Any Academic Stage</h3><p>We support students at different stages, from those preparing with a short course or IELTS, to those ready for university recruitment, degree placement or our own academic programme.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>Saudi Arabia, Currently</h3><p>We are currently welcoming students and school partners across Saudi Arabia, with plans to extend to more countries over time.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['book']}</div><h3>Comfortable in English</h3><p>Sessions are taught in English. Students should be comfortable following and taking part in academic discussion in English.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Format &amp; Timing</div>
        <h2>How the online module actually runs</h2>
        <p style="margin:16px 0 22px;">Live sessions are held online and scheduled with Saudi Arabia time zones in mind, so students can join from home or school without disrupting their regular studies.</p>
        {check_list([
            'Live, scheduled sessions, not pre-recorded videos',
            'Small international cohorts so every student can take part',
            'A manageable weekly time commitment alongside regular school work',
        ])}
      </div>
      <div data-reveal>{decorative_panel('cap', 'Live Online Sessions', 'Scheduled with Saudi Arabia time zones in mind')}</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('globe', 'Travelling to the UK', 'Guidance for the optional two week experience')}</div>
      <div>
        <div class="eyebrow">The UK Experience</div>
        <h2>Travel, safeguarding and logistics</h2>
        <p style="margin:16px 0 22px;">The UK experience is a short, two week visit, not a course of study, so it does not require a UK Student visa. Saudi nationals should check current UK visa requirements for a short visit well ahead of travel. We share full, up to date guidance directly with enrolled families closer to the travel dates.</p>
        {check_list([
            'A two week visit, continuing the academic module in person',
            'Clear safeguarding and duty of care arrangements throughout the trip',
            'Detailed travel information shared directly with enrolled families',
        ])}
      </div>
    </div>
  </div>
</section>

{faq_section([
    ("Do I need a student visa for the UK experience?", "No. The UK experience is a short, two week visit rather than a course of study, so it does not require a UK Student visa. Saudi nationals should still check the latest UK visa requirements for short visits, and we guide enrolled families through this directly."),
    ("What safeguarding is in place during the UK trip?", "Students are supervised throughout the UK experience by our team, with clear duty of care and safeguarding arrangements. We share full details with parents before travel."),
    ("Is the certificate recognised by universities?", "The certificate recognises genuine academic and professional development completed on the programme. It is evidence of real UK academic engagement, not a university qualification or guaranteed entry pathway."),
    ("Can a student complete the programme without travelling to the UK?", "Yes. The online academic module and final project can be completed entirely online, with the same certificate awarded on completion. The UK experience is an optional continuation."),
    ("How do we enrol?", "Message us on WhatsApp or email and we will explain current dates, format and next steps for your family or your school."),
])}

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Still have a question?</h2><p>Ask us directly on WhatsApp and we will reply as soon as we can.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link()}" target="_blank" rel="noopener">{ICONS['whatsapp']} Ask on WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# STUDENT EXPERIENCES (kept content-free of fabricated reviews, see note below)
# ==========================================================================
# This page intentionally does not include any student quotes: we only
# publish real, verified reviews (with permission) once we have them. Update
# this page directly once your first cohort of students is ready to share
# feedback. A `testimonial()` helper and card styling already exist in
# build.py/style.css and can be reused at that point.
testimonials_body = f"""
<main id="main">
{page_hero('Student Experiences', "We're just getting started", 'UK Study Abroad launched to serve students and schools in Saudi Arabia across our study abroad services, and we only publish real, verified feedback from students we have actually worked with. This page will fill up as more students complete our services.', 'Student Experiences')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">In the Meantime</div>
      <h2>What you can expect from the programme</h2>
    </div>
    <div class="grid grid-4">
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['cap']}</div><h3>Genuine UK Academics</h3><p>Every session is taught directly by a UK university lecturer or professor.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['headset']}</div><h3>Fast WhatsApp Replies</h3><p>Real answers within 24 to 48 hours, in Saudi Arabia friendly hours.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['target']}</div><h3>A Real Academic Outcome</h3><p>A completed final project and a certificate, not just attendance.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['heart']}</div><h3>Honest From Day One</h3><p>We only publish feedback that is real and verified, never invented.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>Want to be our first success story?</h2><p>Message us on WhatsApp and let's talk about the Global Career Development Programme.</p></div>
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

POSTS = []

# ==========================================================================
# INSIGHTS (blog index)
# ==========================================================================
blog_cards = "\n".join(
    post_card(p['icon'], p['panel'], p['category'], p['date'], p['title'], p['desc'], "/" + p['slug'])
    for p in POSTS
)

blog_body = f"""
<main id="main">
{page_hero('Insights', 'Guides on global academic development', 'Practical articles on academic development, global career skills and preparing for UK university teaching. New articles are on their way.', 'Insights')}

<section>
  <div class="container">
    <div class="grid grid-3">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>Academic Skills</h3><p>What genuinely helps ambitious students build university level academic thinking, from people who teach at UK universities.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['users']}</div><h3>Global Career Skills</h3><p>Communication, teamwork and cross cultural confidence, and why universities and employers value them so highly.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>Life As an International Student</h3><p>Honest, practical insights on studying and travelling internationally as a teenager, from our own academic team.</p></div>
    </div>
    <p class="table-note" style="text-align:center;margin-top:36px;">Our first articles are on their way. Have a question you would like us to cover? <a href="/contact.html" style="color:var(--teal-700);font-weight:700;">Send us a message</a>.</p>
  </div>
</section>
</main>
"""

build_page(
    "blog.html",
    "Insights | UK Study Abroad",
    "Articles on academic development, global career skills and preparing for UK university teaching, from UK Study Abroad's Global Career Development Programme.",
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


# Blog posts will be added here once the first Insights articles are written.
# The blog_post_page() helper above is ready to use: call it with a slug,
# title, category, date, read time, intro and body HTML once you have real
# articles on academic development, global career skills or the UK experience.

# ==========================================================================
# CONTACT
# ==========================================================================
contact_body = f"""
<main id="main">
{page_hero('Contact Us', "Let's talk about your student's global future", "Reach out on WhatsApp for the fastest reply, or send us a message using the form below. We aim to respond within 24 to 48 hours.", 'Contact')}

<section>
  <div class="container">
    <div class="contact-grid">
      <div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['whatsapp']}</div>
          <div><h4>WhatsApp</h4><p>The fastest way to reach us. Chat directly with our team.</p><a class="value" href="{whatsapp_link()}" target="_blank" rel="noopener">{WHATSAPP_DISPLAY}</a></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['mail']}</div>
          <div><h4>Email</h4><p>For detailed questions, school partnerships and anything non-urgent.</p><a class="value" href="mailto:{EMAIL}">{EMAIL}</a></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['clock']}</div>
          <div><h4>Response Hours</h4><p>We reply in Saudi Arabia friendly hours (AST), typically within 24 to 48 hours on WhatsApp and email.</p></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['pin']}</div>
          <div><h4>Who We Serve</h4><p>Currently welcoming students and school partners across the Kingdom of Saudi Arabia.</p></div>
        </div>
      </div>

      <div class="form-card" data-reveal>
        <h3 style="margin-bottom:8px;">Send us a message</h3>
        <p style="margin-bottom:26px;font-size:0.94rem;">Tell us a little about your student or your school and we will get back to you with clear next steps.</p>
        <form id="contact-form">
          <input type="hidden" name="access_key" value="fac1cb50-58f2-4bea-a973-c5e221bec7d1">
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
                <option>Short Courses</option>
                <option>University Recruitment &amp; Applications</option>
                <option>Degree Placement</option>
                <option>IELTS Preparation</option>
                <option>The Global Career Development Programme</option>
                <option>School or College Partnership</option>
                <option>Something Else</option>
              </select>
            </div>
          </div>
          <div class="field"><label for="message">Your Message</label><textarea id="message" name="message" required placeholder="Tell us about your goals, your school and what you would like to know..."></textarea></div>
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
<p>UK Study Abroad ("we", "us", "our") respects your privacy. This page explains, in general terms, how we collect and use information when you use this website, enrol in one of our services, or contact us via WhatsApp, email or our contact form.</p>
<h2>Information We Collect</h2>
<p>When you submit our contact form or message us directly, we may collect your name, email address, phone/WhatsApp number, your student's school and study goals, and any other details you choose to share.</p>
<h2>How We Use Your Information</h2>
<p>We use the information you provide to respond to your enquiry, deliver the service you have enrolled in, and, with your consent, send you relevant updates about our services.</p>
<h2>Data Sharing</h2>
<p>We do not sell your personal information. We may share necessary details with our academic delivery team, university admissions teams, or UK travel and accommodation providers strictly as part of delivering the service you have enrolled in.</p>
<h2>Your Rights</h2>
<p>You can ask us at any time to access, correct, or delete the personal information we hold about you by contacting us at the email address on our Contact page.</p>
<p style="margin-top:30px;font-size:0.85rem;color:var(--gray-500);"><em>This is a general-purpose placeholder policy. Please review it with a qualified legal advisor and update it to reflect your actual data practices, tools (such as your chosen form provider) and any applicable Saudi Arabian or UK data protection requirements before publishing this site live.</em></p>
"""
build_page("privacy-policy.html", "Privacy Policy | UK Study Abroad", "How UK Study Abroad collects, uses and protects your personal information.", "", legal_wrap("Privacy Policy", "Privacy Policy", privacy_body))
print("PRIVACY done")

terms_body = """
<p>These Terms of Use govern your use of the UK Study Abroad website. By using this site, you agree to these terms.</p>
<h2>Our Services, Not a Guarantee</h2>
<p>UK Study Abroad provides study abroad services including short courses, university recruitment and application support, degree placement, IELTS preparation and our Global Career Development Programme. Completion of any course, programme or application support we provide does not guarantee admission to any university, a specific exam score, or any specific career outcome.</p>
<h2>Accuracy of Information</h2>
<p>We aim to keep service, travel and eligibility information accurate and up to date, but details can change. Always confirm time-sensitive details directly with us before making decisions.</p>
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
    "Get in touch with UK Study Abroad via WhatsApp, email or our contact form to learn more about our study abroad services.",
    "contact.html",
    contact_body,
)
print("CONTACT done")

build_page(
    "testimonials.html",
    "Student Experiences | UK Study Abroad",
    "Read what students and schools say about UK Study Abroad's short courses, university recruitment, degree placement, IELTS preparation and Global Career Development Programme.",
    "testimonials.html",
    testimonials_body,
)
print("TESTIMONIALS done")

build_page(
    "faqs.html",
    "Eligibility &amp; FAQs | UK Study Abroad",
    "Eligibility, format, travel and certificate questions answered about UK Study Abroad's services, including the Global Career Development Programme.",
    "faqs.html",
    faqs_body,
)
print("FAQS done")

build_page(
    "schools.html",
    "Schools &amp; Colleges | UK Study Abroad",
    "Partner with UK Study Abroad to give your students real benefits for their global study future in the UK, through short courses, university recruitment, degree placement, IELTS preparation and our Global Career Development Programme.",
    "schools.html",
    schools_body,
)
print("SCHOOLS done")

build_page(
    "services.html",
    "Our Services | UK Study Abroad",
    "Short courses, university recruitment, degree placement, IELTS preparation and the Global Career Development Programme, a live online academic module with an optional UK experience.",
    "services.html",
    services_body,
)
print("SERVICES done")

build_page(
    "about.html",
    "About Us | UK Study Abroad",
    "UK Study Abroad is a study abroad consultancy offering short courses, university recruitment, degree placement, IELTS preparation and the Global Career Development Programme, taught directly by UK university lecturers and professors.",
    "about.html",
    about_body,
)
print("ABOUT done")
