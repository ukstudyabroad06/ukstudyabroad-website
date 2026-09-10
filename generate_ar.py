#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the Arabic (RTL) mirror of every English page, into ar/*.html.

Run this after generate.py (or via build_all.py, which runs both). Uses the
same shared templates and design system as the English site (build.py),
just with build_page_ar()/head_ar()/header_ar()/footer_ar() and Arabic
copy. The brand name "UK Study Abroad" is kept in Latin script throughout,
matching the client's existing brand usage; everything else is translated.
"""
from build import (
    ICONS, build_page_ar, decorative_panel, city_tile, check_list, whatsapp_link, EMAIL, WHATSAPP_DISPLAY,
    ACCENT_CYCLE, tint_icon, accent_card, glow_blob, page_hero, faq_section, arrow_icon,
)

WA_MSG_AR = "مرحبا UK Study Abroad، أود معرفة المزيد عن خدماتكم."

# ==========================================================================
# الرئيسية HOME
# ==========================================================================
home_body = f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <span class="hero-eyebrow">{ICONS['star']} استشارات UK Study Abroad</span>
      <h1>مسارك الكامل نحو <span>الدراسة في المملكة المتحدة</span>.</h1>
      <p class="lead">من الدورات القصيرة والتحضير لاختبار الأيلتس إلى القبول الجامعي وتوفير المقاعد الجامعية وبرنامجنا الأكاديمي المباشر عبر الإنترنت، نساعد الطلاب الطموحين من المملكة العربية السعودية على إيجاد المسار الصحيح للدراسة والنجاح في المملكة المتحدة.</p>
      <p style="margin:-14px 0 26px;color:var(--muted);font-size:0.98rem;">يضم فريقنا محاضرين وأساتذة حقيقيين من جامعات بريطانية، فكل خطوة في رحلتك مدعومة بخبرة أكاديمية حقيقية، وليست مجرد إجراءات ورقية.</p>
      <div class="hero-cta">
        <a class="btn btn-whatsapp" href="/ar/services.html">{ICONS['book']} استكشف خدماتنا</a>
        <a class="btn btn-outline-light" href="/ar/schools.html">المدارس والكليات</a>
      </div>
      <div class="hero-trust">
        <div><strong>5 خدمات</strong><span>شريك موثوق واحد للدراسة بالخارج</span></div>
        <div><strong>أكاديميون بريطانيون</strong><span>محاضرون وأساتذة حقيقيون في فريقنا</span></div>
        <div><strong>المملكة العربية السعودية</strong><span>دعم مباشر للعائلات والمدارس</span></div>
      </div>
    </div>
    <div class="hero-visual" data-reveal>
      <img src="/assets/images/logo-full-web.png" alt="UK Study Abroad" loading="eager">
      <div class="hero-badge">
        <div class="icon">{ICONS['cap']}</div>
        <div><strong>يُدرَّس على يد أكاديميين بريطانيين</strong><span>خبرة أكاديمية بريطانية حقيقية في فريقنا</span></div>
      </div>
    </div>
  </div>
</section>

<section class="stats-strip">
  <div class="container">
    <div class="grid grid-4">
      <div><strong>5 خدمات</strong><span>تغطي كل مرحلة من رحلتك</span></div>
      <div><strong>أساتذة بريطانيون</strong><span>محاضرون وأساتذة حقيقيون في فريقنا</span></div>
      <div><strong>من القبول حتى التخرج</strong><span>دعم من أول استفسار حتى التسجيل</span></div>
      <div><strong>المملكة العربية السعودية</strong><span>سوقنا الحالي</span></div>
    </div>
  </div>
</section>

<section class="bg-alt" style="position:relative;overflow:hidden;">
  {glow_blob("#14919b", top="-70px", left="-70px")}
  {glow_blob("#7c4dbb", bottom="-90px", right="-90px")}
  <div class="container" style="position:relative;z-index:1;">
    <div class="section-head center">
      <div class="eyebrow">كيف نساعدك</div>
      <h2>شريك واحد لرحلتك الكاملة نحو الدراسة في المملكة المتحدة.</h2>
      <p>تتطلب الدراسة بالخارج أكثر من قرار واحد. غالبا ما يحتاج الطلاب والعائلات إلى مساعدة في عدة أمور في وقت واحد: التحضير لاختبار اللغة الإنجليزية، واختيار التخصص المناسب، والتقديم للجامعة الصحيحة، وإيجاد تجارب أكاديمية ذات معنى على طول الطريق. تغطي معظم الاستشارات جزءا فقط من هذه الرحلة.</p>
      <p>يجمع UK Study Abroad كل ذلك في مكان واحد، من خلال الجمع بين الدعم العملي في التقديم والخبرة الأكاديمية البريطانية الحقيقية، حتى لا يضطر الطلاب والمدارس للتعامل مع عدة جهات مختلفة.</p>
      <p style="font-weight:600;">شريك واحد موثوق. في كل مرحلة من الرحلة.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">خدماتنا</div>
      <h2>كل ما تحتاجه للدراسة والنجاح في المملكة المتحدة</h2>
      <p>تصفح كل خدمة أدناه، أو راسلنا عبر واتساب وسنساعدك في إيجاد نقطة البداية المناسبة.</p>
    </div>
    <div class="grid grid-3">
      {accent_card('book', 'الدورات القصيرة', 'دورات عملية ومركزة تبني مهارات أكاديمية محددة وتعزز الثقة.', ACCENT_CYCLE[0], f'<a class="card-link" href="/ar/services.html#short-courses">اعرف المزيد {ICONS["arrow-right"]}</a>')}
      {accent_card('doc-check', 'القبول الجامعي', 'إرشاد واضح وصادق لاختيار الجامعات وإعداد طلب تقديم قوي.', ACCENT_CYCLE[1], f'<a class="card-link" href="/ar/services.html#recruitment">اعرف المزيد {ICONS["arrow-right"]}</a>')}
      {accent_card('cap', 'توفير المقاعد الجامعية', 'دعم في إيجاد وتأمين المقعد الجامعي المناسب في مؤسسة بريطانية.', ACCENT_CYCLE[2], f'<a class="card-link" href="/ar/services.html#degree-placement">اعرف المزيد {ICONS["arrow-right"]}</a>')}
      {accent_card('target', 'التحضير لاختبار الأيلتس', 'تحضير منظم يبني مهارات الاختبار والثقة للحصول على الدرجة المطلوبة.', ACCENT_CYCLE[0], f'<a class="card-link" href="/ar/services.html#ielts">اعرف المزيد {ICONS["arrow-right"]}</a>')}
      {accent_card('globe', 'برنامج التطوير المهني العالمي', 'برنامجنا الأكاديمي المباشر الرائد عبر الإنترنت، مع تجربة اختيارية في المملكة المتحدة.', ACCENT_CYCLE[1], f'<a class="card-link" href="/ar/services.html#global-career-programme">اعرف المزيد {ICONS["arrow-right"]}</a>')}
    </div>
    <div style="text-align:center;margin-top:36px;">
      <a class="btn btn-primary" href="/ar/services.html">عرض جميع خدماتنا {arrow_icon()}</a>
    </div>
  </div>
</section>

<section class="bg-alt" style="position:relative;overflow:hidden;">
  {glow_blob("#f0a93a", bottom="-90px", left="-80px")}
  <div class="container" style="position:relative;z-index:1;">
    <div class="section-head center">
      <div class="eyebrow">لماذا تختارنا العائلات</div>
      <h2>شريك واحد موثوق لكامل الرحلة</h2>
    </div>
    <div class="grid grid-2">
      {accent_card('cap', 'وصول أكاديمي بريطاني حقيقي', 'يضم فريقنا محاضرين وأساتذة حقيقيين من جامعات بريطانية، فتحصل العائلات على أكثر من مجرد مساعدة في الأوراق. يحصلون على خبرة أكاديمية مباشرة.', ACCENT_CYCLE[1])}
      {accent_card('doc-check', 'دعم كامل في التقديم', 'من اختيار التخصصات إلى تقديم طلب قوي، نرشد الطلاب خلال القبول الجامعي وتوفير المقاعد الجامعية من البداية حتى النهاية.', ACCENT_CYCLE[2])}
      {accent_card('book', 'تحضير للاختبارات واللغة', 'يبني التحضير المنظم لاختبار الأيلتس والدورات القصيرة المهارات العملية والثقة التي يحتاجها الطلاب قبل التقديم.', ACCENT_CYCLE[0])}
      {accent_card('users', 'شراكات موثوقة مع المدارس', 'نعمل مباشرة مع مديري المدارس والكليات في جميع أنحاء المملكة العربية السعودية، لنقدم لطلابهم فوائد حقيقية من خلال شراكتنا.', ACCENT_CYCLE[1])}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('users', 'المدارس والكليات', 'فوائد حقيقية لمستقبل طلابكم', 'gold')}</div>
      <div>
        <div class="eyebrow">المدارس والكليات</div>
        <h2>شراكة مبنية حول مستقبل طلابكم العالمي</h2>
        <p style="margin:16px 0 26px;">نعمل مباشرة مع مديري المدارس والكليات في جميع أنحاء المملكة العربية السعودية، من خلال الجمع بين الدورات القصيرة والقبول الجامعي وتوفير المقاعد الجامعية والتحضير لاختبار الأيلتس وبرنامج التطوير المهني العالمي، في شراكة مبنية حول ما يفيد طلابكم أكثر وهم يخططون لمستقبلهم في الدراسة بالخارج في المملكة المتحدة.</p>
        <div style="margin-bottom:28px;">
        {check_list([
            'دعم عملي يساعد طلابكم على التقدم بثقة نحو الجامعة ومسيرتهم المهنية',
            'وصول مباشر إلى خبرة أكاديمية بريطانية حقيقية من خلال فريقنا من المحاضرين والأساتذة',
            'شراكة تعاونية مصممة حول مدرستكم وطلابكم، وليست حلا واحدا يناسب الجميع',
        ])}
        </div>
        <a class="btn btn-primary" href="/ar/schools.html">كن شريكا معنا {arrow_icon()}</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div>
          <h2>هل أنت مستعد للتخطيط لخطوتك التالية؟</h2>
          <p>راسلنا لمعرفة المزيد عن خدماتنا، لعائلتك أو مدرستك.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link(WA_MSG_AR)}" target="_blank" rel="noopener">{ICONS['whatsapp']} راسلنا عبر واتساب الآن</a>
          <a class="btn btn-outline-light" href="mailto:{EMAIL}">{ICONS['mail']} راسلنا بالبريد الإلكتروني</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

build_page_ar(
    "index.html",
    "UK Study Abroad | استشارات الدراسة بالخارج للمملكة العربية السعودية",
    "UK Study Abroad شركة استشارات للدراسة بالخارج، تقدم دورات قصيرة، وخدمات القبول الجامعي، وتوفير المقاعد الجامعية، والتحضير لاختبار الأيلتس، وبرنامج التطوير المهني العالمي، وهو برنامج أكاديمي مباشر عبر الإنترنت مع تجربة اختيارية في المملكة المتحدة، للطلاب والمدارس في المملكة العربية السعودية.",
    "index.html",
    home_body,
)
print("HOME (ar) done")

# ==========================================================================
# من نحن ABOUT
# ==========================================================================
about_body = f"""
<main id="main">
{page_hero('من نحن', 'استشارة متكاملة للدراسة بالخارج، مبنية على خبرة أكاديمية بريطانية حقيقية.', 'يدعم UK Study Abroad الطلاب والمدارس في جميع أنحاء المملكة العربية السعودية من خلال الدورات القصيرة والقبول الجامعي وتوفير المقاعد الجامعية والتحضير لاختبار الأيلتس وبرنامجنا الأكاديمي المباشر عبر الإنترنت.', 'من نحن', lang='ar')}

<section>
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">قصتنا</div>
        <h2>لماذا أسسنا UK Study Abroad</h2>
        <p style="margin-top:16px;">في كل عام، يكون آلاف الطلاب الموهوبين في جميع أنحاء المملكة العربية السعودية قادرين على ما هو أكثر بكثير مما يوفره مسار واحد فقط. وما يفتقر إليه كثير منهم ليس الطموح، بل شريك واحد موثوق يمكنه المساعدة في الخطوات العملية للدراسة بالخارج وتقديم خبرة أكاديمية بريطانية حقيقية على طول الطريق.</p>
        <p>تأسس UK Study Abroad ليجمع هذه العناصر معا. نحن ندعم الطلاب والمدارس من خلال الدورات القصيرة، والإرشاد في القبول الجامعي والتقديم، وتوفير المقاعد الجامعية، والتحضير لاختبار الأيلتس، إلى جانب برنامج التطوير المهني العالمي الخاص بنا، وهو برنامج أكاديمي مباشر عبر الإنترنت يقدمه مباشرة محاضرون وأساتذة من جامعات بريطانية، مع خيار مواصلة ذلك التعلم شخصيا في المملكة المتحدة.</p>
        <p>نبدأ برسالة مركزة، بدعم الطلاب والمدارس في المملكة العربية السعودية، لأننا نؤمن أن القيام بهذا بشكل صحيح أفضل من القيام به بشكل جزئي. ومع نمونا، نخطط لتقديم نفس مستوى الدعم للطلاب في جميع أنحاء المنطقة الأوسع.</p>
      </div>
      <div data-reveal>{decorative_panel('cap', 'أكاديمي. عالمي. حقيقي.', 'المبادئ التي توجه كل ما نقدمه.')}</div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">قيمنا</div>
      <h2>ما يوجه كل خدمة نقدمها</h2>
    </div>
    <div class="grid grid-4">
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['cap']}</div><h3>النزاهة الأكاديمية</h3><p>برنامج التطوير المهني العالمي لدينا مصمم ومقدم من أشخاص لديهم خبرة أكاديمية حقيقية في جامعات بريطانية، ولا يُسند أبدا لمدربين عامين.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['users']}</div><h3>عالمي بحق</h3><p>يتعلم الطلاب جنبا إلى جنب مع زملاء من دول أخرى، مما يبني الثقة والتفاهم بين الثقافات التي تتطلبها الدراسة والمسيرة المهنية العالمية.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['heart']}</div><h3>الصدق أولا</h3><p>نقدم نصيحة واضحة وصادقة حول أي الدورات والجامعات تناسب كل طالب حقا، وليس فقط الخيار الأسهل للتوصية به.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['target']}</div><h3>التركيز على النتائج</h3><p>نقيس النجاح من خلال النتائج التي يحققها طلابنا، من درجات الاختبارات إلى عروض الجامعات إلى البرامج المكتملة.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">فريقنا</div>
      <h2>الأشخاص وراء UK Study Abroad</h2>
      <p>فريق صغير بقيادة أكاديمية، ينضم إليه المزيد من محاضري وأساتذة الجامعات البريطانية مع نمو فريقنا.</p>
    </div>
    <div class="grid grid-4">
      <div class="team-card" data-reveal><div class="team-avatar">F</div><h4>المؤسس والمدير</h4><span class="role">الاستراتيجية والشراكات</span><p>يحدد اتجاه UK Study Abroad ويشرف على رحلة كل طالب، من أول استفسار حتى التسجيل وما بعده.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">A</div><h4>المسؤول الأكاديمي</h4><span class="role">محاضر جامعي بريطاني</span><p>يصمم ويقدم الوحدة الأكاديمية المباشرة عبر الإنترنت، بالاعتماد مباشرة على خبرة التدريس في الجامعات البريطانية.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">P</div><h4>مسؤول الشراكات</h4><span class="role">المدارس والكليات</span><p>يعمل مباشرة مع مديري المدارس والكليات لتقديم خدماتنا لطلابهم.</p></div>
      <div class="team-card" data-reveal><div class="team-avatar">S</div><h4>منسق تجربة الطالب</h4><span class="role">واتساب والاستفسارات</span><p>أول رد ودود ستحصل عليه عبر واتساب، وجهة اتصالك طوال فترة التقديم أو البرنامج.</p></div>
    </div>
    <p class="table-note" style="text-align:center;margin-top:24px;">يعكس هيكل الفريق الموضح نموذج التشغيل الحالي لدينا. يتم التحديث بأسماء ومسميات وظيفية ومؤهلات أكاديمية وصور حقيقية للموظفين مع نمو فريقكم الأكاديمي.</p>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div>
          <h2>لنتحدث عن مستقبل ابنك أو ابنتك العالمي</h2>
          <p>أخبرنا قليلا عن طفلك أو مدرستك، وسنوضح لك بصدق أي من خدماتنا هو الأنسب.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link(WA_MSG_AR)}" target="_blank" rel="noopener">{ICONS['whatsapp']} راسلنا عبر واتساب الآن</a>
          <a class="btn btn-outline-light" href="/ar/contact.html">صفحة التواصل</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# خدماتنا SERVICES
# ==========================================================================
services_body = f"""
<main id="main">
{page_hero('خدماتنا', 'كل ما تحتاجه للدراسة والنجاح في المملكة المتحدة.', 'من الدورات القصيرة والتحضير لاختبار الأيلتس إلى القبول الجامعي وتوفير المقاعد الجامعية وبرنامجنا الأكاديمي المباشر، ندعم الطلاب في كل مرحلة من رحلتهم للدراسة في المملكة المتحدة.', 'خدماتنا', lang='ar')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">من نساعد</div>
      <h2>مصمم للطلاب الطموحين وذوي التفكير العالمي</h2>
      <p>خدماتنا مصممة للطلاب الدوليين الذين يريدون أكثر من مسار واحد، ونرحب حاليا بالطلاب من المدارس والكليات في جميع أنحاء المملكة العربية السعودية.</p>
    </div>
    <div class="grid grid-4">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>طموح أكاديميا</h3><p>طلاب يريدون تجربة حقيقية للتفكير على مستوى الجامعات البريطانية، وليس مجرد واجبات إضافية.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>بتفكير عالمي</h3><p>طلاب يريدون بناء النظرة العالمية التي تتوقعها الجامعات وأصحاب العمل بشكل متزايد.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['users']}</div><h3>مستعدون للتعاون</h3><p>طلاب مرتاحون للعمل جنبا إلى جنب مع زملاء من دول أخرى في مهام أكاديمية مشتركة.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['target']}</div><h3>يخططون للمستقبل</h3><p>طلاب بدأوا التفكير جديا في خطوتهم التالية نحو الجامعة ومسيرتهم المهنية.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt" id="short-courses">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">الدورات القصيرة</div>
        <h2>ابنِ مهارات عملية من خلال دورة قصيرة مركزة</h2>
        <p style="margin:16px 0 22px;">دوراتنا القصيرة مصممة لبناء مهارات أكاديمية أو عملية محددة خلال فترة زمنية مكثفة، وهي مثالية للطلاب الذين يريدون بداية قوية وذات معنى دون التزام طويل الأمد.</p>
        {check_list([
            'دورات مرنة ومركزة على مهارات أكاديمية وعملية محددة',
            'تقدم عبر الإنترنت لسهولة الوصول من أي مكان',
            'خطوة عملية أولى قبل التزام أكاديمي أكبر',
        ])}
      </div>
      <div data-reveal>{decorative_panel('book', 'الدورات القصيرة', 'بداية عملية ومركزة')}</div>
    </div>
  </div>
</section>

<section id="recruitment">
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('doc-check', 'القبول الجامعي', 'إرشاد خلال كل خطوة من التقديم')}</div>
      <div>
        <div class="eyebrow">القبول الجامعي</div>
        <h2>إرشاد واضح وصادق خلال التقديم للجامعات</h2>
        <p style="margin:16px 0 22px;">يمكن أن يكون اختيار التخصص والجامعة المناسبين، وإعداد طلب تقديم قوي، أمرا مربكا دون الدعم المناسب. نرشد الطلاب خلال هذه العملية خطوة بخطوة، من اختيار قائمة الجامعات المختصرة حتى تقديم طلب كامل ومُعد جيدا.</p>
        {check_list([
            'المساعدة في اختيار قائمة مختصرة من الجامعات والتخصصات التي تناسب كل طالب حقا',
            'إرشاد حول البيان الشخصي والتزكيات ومتطلبات التقديم',
            'نصيحة واضحة وصادقة دون ضغط تجاه أي مؤسسة بعينها',
        ])}
      </div>
    </div>
  </div>
</section>

<section class="bg-alt" id="degree-placement">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">توفير المقاعد الجامعية</div>
        <h2>دعم في إيجاد المقعد الجامعي المناسب</h2>
        <p style="margin:16px 0 22px;">نساعد الطلاب على تحديد وتأمين مقعد في التخصص الجامعي أو الدراسات العليا المناسب في مؤسسة بريطانية، من خلال مطابقة أهداف كل طالب ودرجاته واهتماماته مع الخيار الصحيح.</p>
        {check_list([
            'مطابقة الطلاب مع التخصصات الجامعية التي تناسب أهدافهم ودرجاتهم',
            'دعم خلال العروض والشروط والتسجيل',
            'إرشاد مستمر حتى بداية الدراسة الجامعية',
        ])}
      </div>
      <div data-reveal>{decorative_panel('cap', 'توفير المقاعد الجامعية', 'التخصص الصحيح، في الجامعة الصحيحة')}</div>
    </div>
  </div>
</section>

<section id="ielts">
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('target', 'التحضير لاختبار الأيلتس', 'تحضير عملي نحو درجة مستهدفة حقيقية')}</div>
      <div>
        <div class="eyebrow">التحضير لاختبار الأيلتس</div>
        <h2>تحضير منظم لاختبار الأيلتس</h2>
        <p style="margin:16px 0 22px;">غالبا ما يكون استيفاء متطلب اللغة الإنجليزية أول خطوة عملية نحو الدراسة في المملكة المتحدة. يبني تحضيرنا لاختبار الأيلتس مهارات الاختبار والثقة والتدريب الذي يحتاجه الطلاب للوصول إلى درجتهم المستهدفة.</p>
        {check_list([
            'تحضير منظم في القراءة والكتابة والاستماع والتحدث',
            'تدريب على مهام واقعية بأسلوب الاختبار مع تغذية راجعة',
            'خطة واضحة وعملية نحو الدرجة المستهدفة لكل طالب',
        ])}
      </div>
    </div>
  </div>
</section>

<section class="bg-alt" id="global-career-programme">
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">برنامجنا الرائد</div>
      <h2>برنامج التطوير المهني العالمي</h2>
      <p>تعلم عبر الإنترنت. فكر عالميا. عش تجربة المملكة المتحدة. وحدة أكاديمية مباشرة عبر الإنترنت يقدمها مباشرة محاضرون وأساتذة من جامعات بريطانية، مع خيار مواصلة التجربة شخصيا في المملكة المتحدة.</p>
    </div>
    <div class="split" style="margin-top:10px;">
      <div>
        <div class="eyebrow">المرحلة الأولى</div>
        <h3 style="margin:10px 0 14px;">الوحدة الأكاديمية عبر الإنترنت</h3>
        <p style="margin:0 0 22px;">يبدأ البرنامج بوحدة أكاديمية مباشرة قصيرة عبر الإنترنت يقدمها مباشرة محاضرون وأساتذة من جامعات بريطانية. الطلاب لا يشاهدون مقاطع فيديو مسجلة مسبقا، بل يتلقون التدريس في الوقت الفعلي من أكاديميين لديهم خبرة تدريس حقيقية في الجامعات البريطانية.</p>
        {check_list([
            'جلسات مباشرة يقدمها مباشرة محاضرون وأساتذة من جامعات بريطانية',
            'مجموعات دولية صغيرة حتى يتمكن كل طالب من المشاركة في النقاش',
            'مهارات أكاديمية ومهنية تُبنى من خلال عمل دراسي حقيقي، وليس أوراق عمل',
        ])}
      </div>
      <div data-reveal>{decorative_panel('cap', 'تدريس مباشر عبر الإنترنت', 'يقدمه مباشرة محاضرون من جامعات بريطانية')}</div>
    </div>
    <div class="split reverse" style="margin-top:56px;">
      <div class="split-media" data-reveal>{decorative_panel('globe', 'أسبوعان في المملكة المتحدة', 'استكمال اختياري للوحدة، وليس مخيما صيفيا')}</div>
      <div>
        <div class="eyebrow">المرحلة الثانية، اختيارية</div>
        <h3 style="margin:10px 0 14px;">تجربة المملكة المتحدة</h3>
        <p style="margin:0 0 22px;">يحصل الطلاب الذين يكملون الوحدة عبر الإنترنت على خيار السفر إلى المملكة المتحدة لتجربة حضورية مدتها أسبوعان خلال الصيف، لمواصلة تعلمهم على أرض الواقع بدلا من بدء شيء جديد. هذه ليست رحلة سياحية مبنية على شكل مخيم صيفي، بل استكمال لنفس البرنامج الأكاديمي، في البلد الذي صُمم من أجله.</p>
        {check_list([
            'أسبوعان في المملكة المتحدة، لمواصلة الوحدة الأكاديمية شخصيا',
            'يقدمه نفس الفريق الأكاديمي، وليس جهة سياحية منفصلة',
            'اختياري: يمكن للطلاب إكمال البرنامج الكامل عبر الإنترنت فقط إذا فضلوا ذلك',
        ])}
      </div>
    </div>
    <div style="margin-top:56px;">
      <div class="section-head center">
        <div class="eyebrow">المرحلة الثالثة</div>
        <h3>المشروع النهائي والشهادة</h3>
        <p>يكمل كل طالب مشروعا نهائيا يجمع تعلمه معا، ويتخرج بشهادة تقر بتطوره الأكاديمي والمهني.</p>
      </div>
      <div class="steps">
        <div class="step" data-reveal><h4>1. الوحدة الأكاديمية عبر الإنترنت</h4><p>تدريس مباشر من محاضرين وأساتذة جامعات بريطانية.</p></div>
        <div class="step" data-reveal><h4>2. التعاون الدولي</h4><p>عمل أكاديمي مشترك مع طلاب من دول أخرى.</p></div>
        <div class="step" data-reveal><h4>3. تطوير المهارات</h4><p>مهارات أكاديمية ومهنية وشخصية، تُبنى طوال البرنامج.</p></div>
        <div class="step" data-reveal><h4>4. تجربة المملكة المتحدة</h4><p>استكمال اختياري مدته أسبوعان للوحدة، في المملكة المتحدة.</p></div>
        <div class="step" data-reveal><h4>5. المشروع النهائي</h4><p>عمل واحد يجمع الوحدة بأكملها معا.</p></div>
        <div class="step" data-reveal><h4>6. الشهادة</h4><p>إقرار بتطور أكاديمي ومهني حقيقي.</p></div>
      </div>
    </div>
  </div>
</section>

{faq_section([
    ("ما الفرق بين خدماتكم؟", "تبني الدورات القصيرة والتحضير لاختبار الأيلتس مهارات أكاديمية ومهارات اختبار محددة. يساعد القبول الجامعي وتوفير المقاعد الجامعية الطلاب على اختيار وتأمين التخصص الجامعي المناسب. برنامج التطوير المهني العالمي هو برنامجنا الأكاديمي الخاص، يقدمه مباشرة محاضرون وأساتذة من جامعات بريطانية، مع تجربة اختيارية في المملكة المتحدة."),
    ("هل يجب أن أختار خدمة واحدة فقط؟", "لا. يجمع كثير من الطلاب بين عدة خدمات، مثل التحضير لاختبار الأيلتس مع القبول الجامعي، أو برنامج التطوير المهني العالمي مع دعم توفير المقاعد الجامعية لاحقا."),
    ("من يقوم فعليا بتدريس الوحدة الأكاديمية عبر الإنترنت؟", "يقوم محاضرون وأساتذة من جامعات بريطانية بتدريس كل جلسة مباشرة بأنفسهم."),
    ("هل تجربة المملكة المتحدة إلزامية؟", "لا. يمكن للطلاب إكمال الوحدة الأكاديمية الكاملة والحصول على شهادتهم عبر الإنترنت بالكامل. تجربة المملكة المتحدة لمدة أسبوعين هي استكمال اختياري للطلاب الذين يرغبون في توسيع تعلمهم شخصيا."),
    ("هل يساعد البرنامج في التقديم للجامعات؟", "برنامج التطوير المهني العالمي هو تطوير أكاديمي ومهني قائم بذاته، رغم أن كثيرا من الطلاب يجمعونه مع دعمنا في القبول الجامعي وتوفير المقاعد الجامعية عندما يكونون مستعدين للتقديم."),
    ("هل تعملون فقط مع طلاب في المملكة العربية السعودية؟", "المملكة العربية السعودية هي سوقنا التأسيسي وتركيزنا الحالي. نخطط لتوسيع خدماتنا لتشمل المزيد من الدول مع نمونا."),
], eyebrow="أسئلة شائعة عن خدماتنا", title="أسئلة شائعة حول خدماتنا")}

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>هل أنت مستعد لمعرفة المزيد؟</h2><p>راسلنا عبر واتساب للتحدث حول أي من خدماتنا هو الأنسب، لعائلتك أو مدرستك.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link(WA_MSG_AR)}" target="_blank" rel="noopener">{ICONS['whatsapp']} تحدث عبر واتساب</a>
          <a class="btn btn-outline-light" href="/ar/schools.html">المدارس والكليات</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# المدارس والكليات SCHOOLS & COLLEGES
# ==========================================================================
schools_body = f"""
<main id="main">
{page_hero('المدارس والكليات', 'شراكة مبنية لمديري المدارس', 'نعمل مباشرة مع مديري المدارس والكليات في جميع أنحاء المملكة العربية السعودية، لنجمع الدورات القصيرة والقبول الجامعي وتوفير المقاعد الجامعية والتحضير لاختبار الأيلتس وبرنامج التطوير المهني العالمي في شراكة مبنية حول مستقبل طلابكم العالمي.', 'المدارس والكليات', lang='ar')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">لماذا الشراكة معنا</div>
      <h2>كيف تفيد هذه الشراكة مستقبل طلابكم</h2>
      <p>شريك واحد موثوق أكاديميا يمكن لمدرستكم تقديمه بثقة، لمساعدة طلابكم على التقدم نحو الجامعة ومسيرتهم المهنية في المملكة المتحدة.</p>
    </div>
    <div class="grid grid-4">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['target']}</div><h3>دعم كامل، شريك واحد</h3><p>من الدورات القصيرة إلى القبول الجامعي وتوفير المقاعد الجامعية والتحضير لاختبار الأيلتس، نغطي الخدمات التي يحتاجها طلابكم لخطوتهم التالية، حتى لا تضطر مدرستكم لتنسيق عدة مزودين.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['award']}</div><h3>يعزز مكانتكم</h3><p>يضيف تقديم مسار حقيقي للدراسة في المملكة المتحدة نقطة تميز حقيقية لمدرستكم أو كليتكم بين أولياء الأمور.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['headset']}</div><h3>جهد أقل لفريقكم</h3><p>نصمم ونقدم الخدمات مباشرة. يساعدنا فريقكم فقط في الوصول إلى الطلاب المناسبين.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>نتائج حقيقية للطلاب</h3><p>يغادر الطلاب بتقدم عملي نحو أهدافهم، من درجات أيلتس أقوى إلى عروض جامعية وبرامج أكاديمية مكتملة.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('users', 'لمديري المدارس', 'شراكة يمكنكم الوقوف خلفها بثقة')}</div>
      <div>
        <div class="eyebrow">لمديري المدارس</div>
        <h2>كيف تعمل الشراكة</h2>
        <p style="margin:16px 0 22px;">نعلم أن وقت المدير محدود، لذا أبقينا جانبنا من هذا الأمر بسيطا. أنتم تقدمون خدماتنا لطلابكم وعائلاتهم. نحن نتولى كل شيء مباشرة: التدريس، والتحضير للاختبارات، والإرشاد في التقديم، ودعم التوفير الجامعي، كل ذلك ضمن شراكة واحدة مبنية حول مستقبل طلابكم.</p>
        {check_list([
            'نشارك معلومات واضحة وجاهزة للاستخدام لأولياء الأمور والطلاب',
            'مدرستكم ليست مسؤولة عن التدريس أو التقديم الأكاديمي',
            'نبقى على تواصل مباشر مع فريقكم طوال فترة الشراكة',
        ])}
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">ما يمكن أن تشمله شراكتكم</div>
      <h2>فوائد لمستقبل طلابكم في الدراسة العالمية</h2>
    </div>
    <div class="steps">
      <div class="step" data-reveal><h4>الدورات القصيرة</h4><p>دورات عملية ومركزة تبني مهارات أكاديمية محددة وتعزز الثقة.</p></div>
      <div class="step" data-reveal><h4>التحضير لاختبار الأيلتس</h4><p>تحضير منظم نحو الدرجة المستهدفة لكل طالب.</p></div>
      <div class="step" data-reveal><h4>القبول الجامعي</h4><p>إرشاد في اختيار الجامعات وإعداد طلبات تقديم قوية.</p></div>
      <div class="step" data-reveal><h4>توفير المقاعد الجامعية</h4><p>دعم في تأمين المقعد الجامعي المناسب في مؤسسة بريطانية.</p></div>
      <div class="step" data-reveal><h4>برنامج التطوير المهني</h4><p>برنامجنا الأكاديمي المباشر الرائد عبر الإنترنت، مع تجربة اختيارية في المملكة المتحدة.</p></div>
    </div>
    <div style="text-align:center;margin-top:36px;">
      <a class="btn btn-outline" href="/ar/services.html">شاهد نطاق خدماتنا الكامل {arrow_icon()}</a>
    </div>
  </div>
</section>

{faq_section([
    ("ماذا تحتاج مدرستنا لتقديمه؟", "بشكل أساسي مساعدتكم في تقديم خدماتنا للطلاب والعائلات. نحن نصمم ونقدم المحتوى الأكاديمي والتحضير للاختبارات ودعم التقديم مباشرة."),
    ("هل هناك تكلفة على المدرسة؟", "لا توجد تكلفة على مدرستكم لتصبحوا شريكا. اسألونا عبر واتساب عن الترتيب الحالي للطلاب والعائلات."),
    ("هل يمكننا الاطلاع على خدماتكم قبل التوصية بها لأولياء الأمور؟", "نعم. يسعدنا اطلاع فريقكم على وصف كامل لخدماتنا قبل تقديمها للعائلات."),
    ("هل تعملون فقط مع مدارس في المملكة العربية السعودية؟", "المملكة العربية السعودية هي سوقنا التأسيسي وتركيزنا الحالي. نخطط لتوسيع شراكات المدارس لتشمل المزيد من الدول مع نمونا."),
], eyebrow="أسئلة الشركاء", title="أسئلة يطرحها مديرو المدارس")}

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>مهتمون بالشراكة معنا؟</h2><p>راسلونا عبر واتساب وسنشرح لكم خدماتنا بالتفصيل، من مدير إلى مدير.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link('مرحبا، أنا مدير مدرسة ومهتم بالشراكة مع UK Study Abroad.')}" target="_blank" rel="noopener">{ICONS['whatsapp']} راسلنا عبر واتساب</a>
          <a class="btn btn-outline-light" href="/ar/contact.html">تواصل معنا</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# الأهلية والأسئلة الشائعة FAQS
# ==========================================================================
faqs_body = f"""
<main id="main">
{page_hero('الأهلية والأسئلة الشائعة', 'كل ما يسأل عنه أولياء الأمور والطلاب', 'إجابات عملية حول الأهلية وخدماتنا وتجربة المملكة المتحدة وكيفية عمل الشهادة، بوضوح تام.', 'الأسئلة الشائعة', lang='ar')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">الأهلية</div>
      <h2>من يمكننا مساعدته</h2>
    </div>
    <div class="grid grid-3">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>أي مرحلة أكاديمية</h3><p>ندعم الطلاب في مراحل مختلفة، من المستعدين بدورة قصيرة أو تحضير للأيلتس، إلى الجاهزين للقبول الجامعي أو توفير المقاعد الجامعية أو برنامجنا الأكاديمي الخاص.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>المملكة العربية السعودية، حاليا</h3><p>نرحب حاليا بالطلاب وشركاء المدارس في جميع أنحاء المملكة العربية السعودية، مع خطط للتوسع إلى المزيد من الدول مع مرور الوقت.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['book']}</div><h3>مرتاح في اللغة الإنجليزية</h3><p>تُقدَّم الجلسات باللغة الإنجليزية. يجب أن يكون الطلاب مرتاحين لمتابعة والمشاركة في النقاش الأكاديمي باللغة الإنجليزية.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">الصيغة والتوقيت</div>
        <h2>كيف تسير الوحدة عبر الإنترنت فعليا</h2>
        <p style="margin:16px 0 22px;">تُعقد الجلسات المباشرة عبر الإنترنت وتُجدول مع مراعاة التوقيت في المملكة العربية السعودية، بحيث يمكن للطلاب الانضمام من المنزل أو المدرسة دون تعطيل دراستهم المعتادة.</p>
        {check_list([
            'جلسات مباشرة ومجدولة، وليست مقاطع فيديو مسجلة مسبقا',
            'مجموعات دولية صغيرة حتى يتمكن كل طالب من المشاركة',
            'التزام زمني أسبوعي معقول إلى جانب العمل المدرسي المعتاد',
        ])}
      </div>
      <div data-reveal>{decorative_panel('cap', 'جلسات مباشرة عبر الإنترنت', 'مجدولة مع مراعاة التوقيت في المملكة العربية السعودية')}</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split reverse">
      <div class="split-media" data-reveal>{decorative_panel('globe', 'السفر إلى المملكة المتحدة', 'إرشادات لتجربة الأسبوعين الاختيارية')}</div>
      <div>
        <div class="eyebrow">تجربة المملكة المتحدة</div>
        <h2>السفر والسلامة واللوجستيات</h2>
        <p style="margin:16px 0 22px;">تجربة المملكة المتحدة هي زيارة قصيرة مدتها أسبوعان، وليست برنامجا دراسيا، لذا فهي لا تتطلب تأشيرة طالب في المملكة المتحدة. ينبغي على المواطنين السعوديين التحقق من متطلبات التأشيرة البريطانية الحالية للزيارات القصيرة قبل السفر بوقت كاف. نشارك إرشادات كاملة ومحدثة مباشرة مع العائلات المسجلة قرب مواعيد السفر.</p>
        {check_list([
            'زيارة مدتها أسبوعان، لمواصلة الوحدة الأكاديمية شخصيا',
            'ترتيبات واضحة للسلامة ورعاية الطلاب طوال الرحلة',
            'معلومات سفر تفصيلية تُشارك مباشرة مع العائلات المسجلة',
        ])}
      </div>
    </div>
  </div>
</section>

{faq_section([
    ("هل أحتاج إلى تأشيرة طالب لتجربة المملكة المتحدة؟", "لا. تجربة المملكة المتحدة هي زيارة قصيرة مدتها أسبوعان بدلا من برنامج دراسي، لذا فهي لا تتطلب تأشيرة طالب بريطانية. مع ذلك، ينبغي على المواطنين السعوديين التحقق من أحدث متطلبات التأشيرة البريطانية للزيارات القصيرة، ونحن نرشد العائلات المسجلة خلال ذلك مباشرة."),
    ("ما إجراءات السلامة المتبعة خلال رحلة المملكة المتحدة؟", "يخضع الطلاب للإشراف طوال تجربة المملكة المتحدة من قبل فريقنا، مع ترتيبات واضحة لرعاية الطلاب والسلامة. نشارك التفاصيل الكاملة مع أولياء الأمور قبل السفر."),
    ("هل الشهادة معترف بها من الجامعات؟", "تقر الشهادة بالتطور الأكاديمي والمهني الحقيقي الذي تم إنجازه في البرنامج. وهي دليل على مشاركة أكاديمية بريطانية حقيقية، وليست مؤهلا جامعيا أو مسارا مضمونا للقبول."),
    ("هل يمكن للطالب إكمال البرنامج دون السفر إلى المملكة المتحدة؟", "نعم. يمكن إكمال الوحدة الأكاديمية عبر الإنترنت والمشروع النهائي بالكامل عبر الإنترنت، مع منح نفس الشهادة عند الإكمال. تجربة المملكة المتحدة هي استكمال اختياري."),
    ("كيف نسجل؟", "راسلونا عبر واتساب أو البريد الإلكتروني وسنوضح المواعيد الحالية والصيغة والخطوات التالية لعائلتكم أو مدرستكم."),
], eyebrow="أسئلة عامة", title="أسئلة شائعة إضافية")}

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>هل لا يزال لديك سؤال؟</h2><p>اسألنا مباشرة عبر واتساب وسنرد في أقرب وقت ممكن.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link(WA_MSG_AR)}" target="_blank" rel="noopener">{ICONS['whatsapp']} اسأل عبر واتساب</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# تجارب الطلاب STUDENT EXPERIENCES
# (No fabricated reviews — only real, verified feedback gets published here,
# once available. Mirrors the policy on the English testimonials page.)
# ==========================================================================
testimonials_body = f"""
<main id="main">
{page_hero('تجارب الطلاب', 'لا زلنا في البداية', 'انطلق UK Study Abroad لخدمة الطلاب والمدارس في المملكة العربية السعودية عبر خدماتنا للدراسة بالخارج، ونحن ننشر فقط آراء حقيقية وموثقة من طلاب عملنا معهم فعلا. ستمتلئ هذه الصفحة مع إكمال المزيد من الطلاب لخدماتنا.', 'تجارب الطلاب', lang='ar')}

<section>
  <div class="container">
    <div class="section-head center">
      <div class="eyebrow">في هذه الأثناء</div>
      <h2>ما يمكن أن تتوقعه من البرنامج</h2>
    </div>
    <div class="grid grid-4">
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['cap']}</div><h3>أكاديميون بريطانيون حقيقيون</h3><p>كل جلسة يقدمها مباشرة محاضر أو أستاذ من جامعة بريطانية.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['headset']}</div><h3>ردود سريعة عبر واتساب</h3><p>إجابات حقيقية خلال 24 إلى 48 ساعة، في أوقات مناسبة للمملكة العربية السعودية.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['target']}</div><h3>نتيجة أكاديمية حقيقية</h3><p>مشروع نهائي مكتمل وشهادة، وليس مجرد حضور.</p></div>
      <div class="card value-card" data-reveal><div class="icon-wrap" style="margin:0 auto 20px;">{ICONS['heart']}</div><h3>صادقون منذ اليوم الأول</h3><p>ننشر فقط آراء حقيقية وموثقة، ولا نختلقها أبدا.</p></div>
    </div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-banner" data-reveal>
      <div class="container-inner">
        <div><h2>هل تريد أن تكون قصة نجاحنا الأولى؟</h2><p>راسلنا عبر واتساب ولنتحدث عن برنامج التطوير المهني العالمي.</p></div>
        <div class="cta-actions">
          <a class="btn btn-whatsapp" href="{whatsapp_link(WA_MSG_AR)}" target="_blank" rel="noopener">{ICONS['whatsapp']} راسلنا عبر واتساب</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ==========================================================================
# رؤى INSIGHTS (blog index — no posts yet, mirrors English blog.html)
# ==========================================================================
blog_body = f"""
<main id="main">
{page_hero('رؤى', 'أدلة حول التطور الأكاديمي العالمي', 'مقالات عملية حول التطور الأكاديمي ومهارات المسيرة المهنية العالمية والتحضير للتدريس الجامعي البريطاني. مقالات جديدة في الطريق.', 'رؤى', lang='ar')}

<section>
  <div class="container">
    <div class="grid grid-3">
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['cap']}</div><h3>المهارات الأكاديمية</h3><p>ما يساعد الطلاب الطموحين فعلا على بناء تفكير أكاديمي بمستوى الجامعة، من أشخاص يدرّسون في جامعات بريطانية.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['users']}</div><h3>مهارات المسيرة المهنية العالمية</h3><p>التواصل والعمل الجماعي والثقة بين الثقافات، ولماذا تقدرها الجامعات وأصحاب العمل بشدة.</p></div>
      <div class="card" data-reveal><div class="icon-wrap">{ICONS['globe']}</div><h3>الحياة كطالب دولي</h3><p>رؤى صادقة وعملية حول الدراسة والسفر دوليا، من فريقنا الأكاديمي.</p></div>
    </div>
    <p class="table-note" style="text-align:center;margin-top:36px;">مقالاتنا الأولى في الطريق. هل لديك سؤال تريد منا تناوله؟ <a href="/ar/contact.html" style="color:var(--teal-700);font-weight:700;">أرسل لنا رسالة</a>.</p>
  </div>
</section>
</main>
"""

# ==========================================================================
# تواصل معنا CONTACT
# ==========================================================================
contact_body = f"""
<main id="main">
{page_hero('تواصل معنا', 'لنتحدث عن مستقبل ابنك أو ابنتك العالمي', 'تواصل معنا عبر واتساب لأسرع رد، أو أرسل لنا رسالة باستخدام النموذج أدناه. نهدف إلى الرد خلال 24 إلى 48 ساعة.', 'تواصل معنا', lang='ar')}

<section>
  <div class="container">
    <div class="contact-grid">
      <div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['whatsapp']}</div>
          <div><h4>واتساب</h4><p>أسرع طريقة للتواصل معنا. تحدث مباشرة مع فريقنا.</p><a class="value" href="{whatsapp_link(WA_MSG_AR)}" target="_blank" rel="noopener">{WHATSAPP_DISPLAY}</a></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['mail']}</div>
          <div><h4>البريد الإلكتروني</h4><p>للأسئلة التفصيلية وشراكات المدارس وأي أمر غير عاجل.</p><a class="value" href="mailto:{EMAIL}">{EMAIL}</a></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['clock']}</div>
          <div><h4>ساعات الرد</h4><p>نرد في أوقات مناسبة للمملكة العربية السعودية، عادة خلال 24 إلى 48 ساعة عبر واتساب والبريد الإلكتروني.</p></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="icon-wrap">{ICONS['pin']}</div>
          <div><h4>من نخدم</h4><p>نرحب حاليا بالطلاب وشركاء المدارس في جميع أنحاء المملكة العربية السعودية.</p></div>
        </div>
      </div>

      <div class="form-card" data-reveal>
        <h3 style="margin-bottom:8px;">أرسل لنا رسالة</h3>
        <p style="margin-bottom:26px;font-size:0.94rem;">أخبرنا قليلا عن طالبك أو مدرستك وسنعاود التواصل معك بخطوات واضحة تالية.</p>
        <form id="contact-form">
          <input type="hidden" name="access_key" value="fac1cb50-58f2-4bea-a973-c5e221bec7d1">
          <input type="hidden" name="subject" value="استفسار جديد من ukstudyabroad.co.uk">
          <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
          <div class="form-row">
            <div class="field"><label for="name">الاسم الكامل</label><input type="text" id="name" name="name" required placeholder="اسمك الكامل"></div>
            <div class="field"><label for="phone">رقم واتساب / الهاتف</label><input type="tel" id="phone" name="phone" required placeholder="+966 5X XXX XXXX"></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="email">البريد الإلكتروني</label><input type="email" id="email" name="email" required placeholder="you@example.com"></div>
            <div class="field"><label for="interest">أنا مهتم بـ</label>
              <select id="interest" name="interest">
                <option>الدورات القصيرة</option>
                <option>القبول الجامعي والتقديم للجامعات</option>
                <option>توفير المقاعد الجامعية</option>
                <option>التحضير لاختبار الأيلتس</option>
                <option>برنامج التطوير المهني العالمي</option>
                <option>شراكة مع مدرسة أو كلية</option>
                <option>شيء آخر</option>
              </select>
            </div>
          </div>
          <div class="field"><label for="message">رسالتك</label><textarea id="message" name="message" required placeholder="أخبرنا عن أهدافك ومدرستك وما ترغب في معرفته..."></textarea></div>
          <button type="submit" class="btn btn-primary btn-block">إرسال الرسالة</button>
          <div class="form-status"></div>
          <p class="form-note">بالإرسال، فإنك توافق على أن يتواصل معك UK Study Abroad عبر البريد الإلكتروني أو الهاتف أو واتساب بخصوص استفسارك. نحن لا نشارك معلوماتك مع أطراف ثالثة.</p>
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
    <h1 style="margin:10px 0 16px;">انتقلت هذه الصفحة إلى أمور أفضل.</h1>
    <p style="margin-bottom:30px;">الصفحة التي تبحث عنها غير موجودة أو ربما تم تغيير اسمها. دعنا نعيدك إلى المسار الصحيح.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
      <a class="btn btn-primary" href="/ar/index.html">العودة إلى الرئيسية</a>
      <a class="btn btn-outline" href="/ar/contact.html">تواصل معنا</a>
    </div>
  </div>
</section>
</main>
"""
build_page_ar("404.html", "الصفحة غير موجودة | UK Study Abroad", "لم يتم العثور على الصفحة التي تبحث عنها.", "", notfound_body)
print("404 (ar) done")

# ==========================================================================
# سياسة الخصوصية PRIVACY POLICY
# ==========================================================================
legal_wrap_ar = lambda title, current, body: f"""
<main id="main">
{page_hero('قانوني', title, 'آخر تحديث: سبتمبر 2026.', current, lang='ar')}
<section><div class="container"><article class="post-content">{body}</article></div></section>
</main>
"""

privacy_body = """
<p>يحترم UK Study Abroad ("نحن"، "لنا") خصوصيتك. توضح هذه الصفحة، بشكل عام، كيف نجمع ونستخدم المعلومات عند استخدامك لهذا الموقع، أو التسجيل في إحدى خدماتنا، أو التواصل معنا عبر واتساب أو البريد الإلكتروني أو نموذج التواصل.</p>
<h2>المعلومات التي نجمعها</h2>
<p>عند إرسال نموذج التواصل أو مراسلتنا مباشرة، قد نجمع اسمك وبريدك الإلكتروني ورقم هاتفك أو واتساب ومدرسة طالبك وأهدافه الدراسية وأي تفاصيل أخرى تختار مشاركتها.</p>
<h2>كيف نستخدم معلوماتك</h2>
<p>نستخدم المعلومات التي تقدمها للرد على استفسارك، وتقديم الخدمة التي سجلت فيها، وبموافقتك، إرسال تحديثات ذات صلة حول خدماتنا.</p>
<h2>مشاركة البيانات</h2>
<p>نحن لا نبيع معلوماتك الشخصية. قد نشارك التفاصيل الضرورية مع فريقنا الأكاديمي، أو إدارات القبول الجامعي، أو مزودي السفر والإقامة في المملكة المتحدة، وذلك فقط كجزء من تقديم الخدمة التي سجلت فيها.</p>
<h2>حقوقك</h2>
<p>يمكنك أن تطلب منا في أي وقت الوصول إلى المعلومات الشخصية التي نحتفظ بها عنك أو تصحيحها أو حذفها، من خلال التواصل معنا عبر البريد الإلكتروني الموضح في صفحة التواصل.</p>
<p style="margin-top:30px;font-size:0.85rem;color:var(--gray-500);"><em>هذه سياسة عامة نموذجية. يرجى مراجعتها مع مستشار قانوني مؤهل وتحديثها لتعكس ممارساتكم الفعلية في التعامل مع البيانات، والأدوات المستخدمة (مثل مزود النموذج الذي تختارونه)، وأي متطلبات سعودية أو بريطانية معمول بها لحماية البيانات، قبل نشر هذا الموقع بشكل فعلي.</em></p>
"""
build_page_ar("privacy-policy.html", "سياسة الخصوصية | UK Study Abroad", "كيف يجمع UK Study Abroad معلوماتك الشخصية ويستخدمها ويحميها.", "", legal_wrap_ar("سياسة الخصوصية", "سياسة الخصوصية", privacy_body))
print("PRIVACY (ar) done")

terms_body = """
<p>تحكم شروط الاستخدام هذه استخدامك لموقع UK Study Abroad. باستخدامك لهذا الموقع، فإنك توافق على هذه الشروط.</p>
<h2>خدماتنا، وليست ضمانا</h2>
<p>يقدم UK Study Abroad خدمات للدراسة بالخارج تشمل الدورات القصيرة، والقبول الجامعي ودعم التقديم، وتوفير المقاعد الجامعية، والتحضير لاختبار الأيلتس، وبرنامج التطوير المهني العالمي. إكمال أي دورة أو برنامج أو دعم تقديم نقدمه لا يضمن القبول في أي جامعة، أو درجة اختبار معينة، أو أي نتيجة مهنية محددة.</p>
<h2>دقة المعلومات</h2>
<p>نسعى للحفاظ على دقة وتحديث معلومات الخدمات والسفر والأهلية، لكن التفاصيل قد تتغير. يرجى دائما تأكيد التفاصيل الحساسة للوقت معنا مباشرة قبل اتخاذ القرارات.</p>
<h2>الملكية الفكرية</h2>
<p>جميع المحتويات على هذا الموقع، بما في ذلك شعارنا وهويتنا التجارية، ملك لـ UK Study Abroad ما لم يُذكر خلاف ذلك.</p>
<h2>التواصل</h2>
<p>يمكن إرسال الأسئلة حول هذه الشروط إلينا عبر صفحة التواصل.</p>
<p style="margin-top:30px;font-size:0.85rem;color:var(--gray-500);"><em>هذا نص عام نموذجي. يرجى مراجعته مع مستشار قانوني مؤهل قبل نشر هذا الموقع بشكل فعلي.</em></p>
"""
build_page_ar("terms.html", "شروط الاستخدام | UK Study Abroad", "شروط استخدام موقع UK Study Abroad.", "", legal_wrap_ar("شروط الاستخدام", "شروط الاستخدام", terms_body))
print("TERMS (ar) done")

build_page_ar(
    "contact.html",
    "تواصل معنا | UK Study Abroad",
    "تواصل مع UK Study Abroad عبر واتساب أو البريد الإلكتروني أو نموذج التواصل لمعرفة المزيد عن خدماتنا للدراسة بالخارج.",
    "contact.html",
    contact_body,
)
print("CONTACT (ar) done")

build_page_ar(
    "testimonials.html",
    "تجارب الطلاب | UK Study Abroad",
    "اقرأ ما يقوله الطلاب والمدارس عن دورات UK Study Abroad القصيرة، والقبول الجامعي، وتوفير المقاعد الجامعية، والتحضير لاختبار الأيلتس، وبرنامج التطوير المهني العالمي.",
    "testimonials.html",
    testimonials_body,
)
print("TESTIMONIALS (ar) done")

build_page_ar(
    "faqs.html",
    "الأهلية والأسئلة الشائعة | UK Study Abroad",
    "إجابات عن أسئلة الأهلية والصيغة والسفر والشهادة حول خدمات UK Study Abroad، بما في ذلك برنامج التطوير المهني العالمي.",
    "faqs.html",
    faqs_body,
)
print("FAQS (ar) done")

build_page_ar(
    "schools.html",
    "المدارس والكليات | UK Study Abroad",
    "كن شريكا مع UK Study Abroad لتقديم فوائد حقيقية لمستقبل طلابكم العالمي في المملكة المتحدة، من خلال الدورات القصيرة والقبول الجامعي وتوفير المقاعد الجامعية والتحضير لاختبار الأيلتس وبرنامج التطوير المهني العالمي.",
    "schools.html",
    schools_body,
)
print("SCHOOLS (ar) done")

build_page_ar(
    "services.html",
    "خدماتنا | UK Study Abroad",
    "دورات قصيرة، وقبول جامعي، وتوفير مقاعد جامعية، وتحضير لاختبار الأيلتس، وبرنامج التطوير المهني العالمي، وهو برنامج أكاديمي مباشر عبر الإنترنت مع تجربة اختيارية في المملكة المتحدة.",
    "services.html",
    services_body,
)
print("SERVICES (ar) done")

build_page_ar(
    "about.html",
    "من نحن | UK Study Abroad",
    "UK Study Abroad شركة استشارات للدراسة بالخارج تقدم دورات قصيرة، وقبولا جامعيا، وتوفير مقاعد جامعية، وتحضيرا لاختبار الأيلتس، وبرنامج التطوير المهني العالمي، يقدمه مباشرة محاضرون وأساتذة من جامعات بريطانية.",
    "about.html",
    about_body,
)
print("ABOUT (ar) done")

build_page_ar(
    "blog.html",
    "رؤى | UK Study Abroad",
    "مقالات حول التطور الأكاديمي ومهارات المسيرة المهنية العالمية والتحضير للتدريس الجامعي البريطاني، من برنامج التطوير المهني العالمي التابع لـ UK Study Abroad.",
    "blog.html",
    blog_body,
)
print("BLOG (ar) done")
