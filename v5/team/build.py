"""Builds the partner profile pages: v5/team/<slug>/index.html.

Edit the PARTNERS data below and run:  python team/build.py   (from v5/)
The pages are generated; edits made directly to index.html are overwritten on the next build.
Bios are written from the partner pages on leadershipmavericks.com/teams/<name>/ (facts only; quotes are verbatim).
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
A = '../../assets/'
HOME = '../../home.html'

PARTNERS = [
    dict(
        slug='lakshmi-prasanna', first='Lakshmi', name='Lakshmi Prasanna', role='Founding Partner',
        photo='partner-lakshmi.png', illo=('partner-lakshmi-illustration.svg', 757, 921),
        email='lakshmi@leadershipmavericks.com', phone='+91 99454 48258',
        linkedin='https://www.linkedin.com/in/mavericklakshmi',
        quote='Being a maverick is mastering your skills to such an extent that you are ready for any challenge.',
        bio=[
            'Lakshmi is a strategic partner to her clients on succession planning and executive search, with more than two decades of data-driven search behind her.',
            'She began her career as an entrepreneur before moving into search with Korn Ferry International and Heidrick &amp; Struggles. Before co-founding Leadership Mavericks, she led the Technology Practice for India at Stanton Chase.',
            'Her searches span telecom, semiconductors, e-commerce and hardware, and her practice keeps growing into new sectors.',
            'She holds dual degrees in sociology and psychology and is an alumna of the Symbiosis Centre for Management and Human Resource Development (SCMHRD).',
        ],
        focus=['Succession planning', 'Executive search'],
        previously=['Stanton Chase, Technology Practice India', 'Heidrick &amp; Struggles', 'Korn Ferry International'],
        education=['Dual degrees in sociology and psychology', 'SCMHRD'],
        sectors=['Telecom', 'Semiconductor', 'E-commerce', 'Hardware'],
    ),
    dict(
        slug='monika-pathak', first='Monika', name='Monika Pathak', role='Founding Partner',
        photo='partner-monika.png', illo=('partner-monika-illustration.svg', 827, 764),
        email='monika@leadershipmavericks.com', phone='+91 98101 39824',
        linkedin='https://www.linkedin.com/in/maverickmonika',
        quote='As a boutique search firm, our strength is personalized, high-quality search with faster turnaround times.',
        bio=[
            'Monika is a talent advisor with more than two decades in leadership search, and she backs every search with clear evaluation frameworks and data.',
            'At Cisco she led leadership hiring across Engineering, Sales and Services, including talent strategy and demand planning. Before Cisco, she led the global technology practice at Heidrick &amp; Struggles and at Stanton Chase.',
            'Her work covers IT, IT services, telecom, consulting and e-commerce. She co-founded Leadership Mavericks to offer search that is hands-on and built around each client.',
            'She holds a bachelor’s degree in philosophy from Lady Shri Ram College, Delhi University.',
        ],
        focus=['Leadership search', 'Talent strategy'],
        previously=['Cisco, leadership hiring', 'Heidrick &amp; Struggles, global technology practice', 'Stanton Chase'],
        education=['BA Philosophy, Lady Shri Ram College, Delhi University'],
        sectors=['IT', 'IT Services', 'Telecom', 'Consulting', 'E-commerce'],
    ),
    dict(
        slug='saba-alam', first='Saba', name='Saba Alam', role='Senior Partner',
        photo='partner-saba.png', illo=('partner-saba-illustration.svg', 878, 901),
        email='saba@leadershipmavericks.com', phone='+91 99717 19776',
        linkedin='https://www.linkedin.com/in/noorussaba',
        quote='To me, being a maverick means being a critical thinker who doesn’t just go with the crowd.',
        bio=[
            'Saba has spent more than two decades in talent hiring, much of it on CXO roles in finance and HR.',
            'Before Leadership Mavericks she worked at Egon Zehnder, LinkedIn and Heidrick &amp; Struggles.',
            'She is a leadership hiring generalist across start-ups, technology and non-technology businesses, education and social enterprise, with a particular focus on the start-up and ed-tech ecosystems.',
            'She holds a bachelor’s degree in commerce and an MBA from Devi Ahilya Vishwavidyalaya, Indore.',
        ],
        focus=['CXO hiring in finance and HR', 'Leadership hiring'],
        previously=['Egon Zehnder', 'LinkedIn', 'Heidrick &amp; Struggles'],
        education=['B.Com and MBA, Devi Ahilya Vishwavidyalaya, Indore'],
        sectors=['Start-ups', 'Ed-tech', 'Technology', 'Education', 'Social enterprise'],
    ),
    dict(
        slug='panini-balaji', first='Panini', name='Panini Balaji', role='Senior Partner',
        photo='partner-panini.png', illo=('partner-panini-illustration.svg', 772, 849),
        email='panini@leadershipmavericks.com', phone='+91 97409 06487',
        linkedin='https://www.linkedin.com/in/paninibalaji',
        quote='In a transactional world, I choose relationships.',
        bio=[
            'Panini is a talent evangelist, a diversity and inclusion advocate and a connector, with more than 20 years in talent.',
            'She spent fourteen years at Allegis, including as Head of HR, and helped establish Allegis Partners in India. Earlier in her career she worked in Silicon Valley.',
            'She grew up in Banaras and is an alumna of Banaras Hindu University (BHU). She joined Leadership Mavericks as a partner.',
        ],
        focus=['Diversity &amp; inclusion', 'Talent advisory'],
        previously=['Allegis, Head of HR', 'Allegis Partners India', 'Silicon Valley, USA'],
        education=['Banaras Hindu University (BHU)'],
        sectors=[],
    ),
]

ARROW = '<svg width="36" height="12" viewBox="0 0 40 12" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M0 6h38M33 1l5 5-5 5"></path></svg>'
OUT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"></path></svg>'
OUT18 = OUT.replace('width="16" height="16"', 'width="18" height="18"')


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def page(p):
    esc = html.escape
    tel = 'tel:' + p['phone'].replace(' ', '')
    illo, iw, ih = p['illo']
    others = [o for o in PARTNERS if o['slug'] != p['slug']]
    lead = ' class="lead"'
    bio = ''.join(f'<p{lead if i == 0 else ""} data-reveal style="--d:{i}">{t}</p>' for i, t in enumerate(p['bio']))
    tags = ''
    if p['sectors']:
        tags = (f'<div data-reveal style="--d:{len(p["bio"])}"><h3 class="sr">Sectors</h3>'
                '<ul class="p-tags">' + ''.join(f'<li>{s}</li>' for s in p['sectors']) + '</ul></div>')
    cards = ''.join(f'''
      <a class="p-card" href="../{o['slug']}/index.html" data-reveal style="--d:{i}">
        <div class="p-card-media">
          <img class="p-card-photo" src="{A}{o['photo']}" alt="" width="360" height="288" loading="lazy">
          <span class="p-card-illo"><img src="{A}{o['illo'][0]}" alt="" width="{o['illo'][1]}" height="{o['illo'][2]}" loading="lazy"></span>
        </div>
        <div class="p-card-info"><div><h3>{o['name']}</h3><p>{o['role']}</p></div>{OUT18}</div>
      </a>''' for i, o in enumerate(others))
    desc = f"{p['name']}, {p['role']} at Leadership Mavericks. " + html.unescape(p['bio'][0]).split('. ')[0].rstrip('.') + '.'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['name']} — Leadership Mavericks</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="Leadership Mavericks">
<meta property="og:title" content="{p['name']}, {p['role']} — Leadership Mavericks">
<meta property="og:image" content="{A}{p['photo']}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","name":"{p['name']}","jobTitle":"{p['role']}","worksFor":{{"@type":"Organization","name":"Leadership Mavericks"}},"email":"mailto:{p['email']}","telephone":"{p['phone']}","sameAs":["{p['linkedin']}"]}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300..700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="../team.css">
</head>
<body>

<header class="p-top">
  <div class="wrap p-top-in">
    <a class="p-logo" href="{HOME}" aria-label="Leadership Mavericks home"><img src="{A}logo.png" alt="Leadership Mavericks"></a>
    <nav class="p-nav" aria-label="Primary">
      <a href="{HOME}">Home</a>
      <a href="{HOME}#team">About Us</a>
      <a href="{HOME}#services">Services</a>
      <a class="p-nav-cta" href="{HOME}#contact">Contact Us</a>
    </nav>
    <button type="button" class="p-menu-btn" aria-expanded="false" aria-controls="p-mnav" aria-label="Open menu">
      <svg class="i-open" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h16"></path></svg>
      <svg class="i-close" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>
    </button>
  </div>
  <nav id="p-mnav" class="p-mnav" aria-label="Mobile" hidden>
    <a href="{HOME}">Home</a>
    <a href="{HOME}#team">About Us</a>
    <a href="{HOME}#services">Services</a>
    <a class="p-mcta" href="{HOME}#contact">Contact Us</a>
  </nav>
</header>

<section class="p-head" aria-labelledby="p-name">
  <svg class="p-grain" width="100%" height="100%" aria-hidden="true">
    <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"></feTurbulence><feColorMatrix values="0 0 0 0 0.11  0 0 0 0 0.10  0 0 0 0 0.09  0 0 0 .09 0"></feColorMatrix></filter>
    <rect width="100%" height="100%" filter="url(#grain)"></rect>
  </svg>
  <div class="wrap p-head-in">
    <nav aria-label="Breadcrumb"><p class="p-crumb rise" style="--d:0ms"><a href="{HOME}#team">The Mavericks</a><span aria-hidden="true">/</span><span aria-current="page">{p['name']}</span></p></nav>
    <div class="p-portrait rise" style="--d:60ms">
      <div class="p-portrait-disc"><img src="{A}{p['photo']}" alt="Photo of {p['name']}" width="360" height="288"></div>
      <div class="p-avatar"><img src="{A}{illo}" alt="" width="{iw}" height="{ih}"></div>
    </div>
    <div class="rise" style="--d:120ms">
      <p class="p-eyebrow">{p['role']}</p>
      <h1 id="p-name" class="p-name">{p['name']}</h1>
    </div>
    <figure class="p-quote rise" style="--d:180ms">
      <blockquote><p><span class="p-qmark" aria-hidden="true">“</span>{p['quote']}<span class="p-qmark" aria-hidden="true">”</span></p></blockquote>
    </figure>
    <div class="p-actions rise" style="--d:240ms">
      <a class="btn btn-ink" href="mailto:{p['email']}">Email {p['first']}{ARROW}</a>
      <a class="btn btn-line" href="{p['linkedin']}" target="_blank" rel="noopener">LinkedIn{OUT}<span class="sr"> (opens in a new tab)</span></a>
    </div>
  </div>
</section>

<main>
<section class="p-body" aria-labelledby="about-h">
  <div class="wrap p-grid">
    <aside class="p-side" data-reveal aria-label="{p['first']} at a glance">
      <div class="p-side-card">
        <div class="p-side-role"><span>{p['role']}</span><span>Leadership Mavericks</span></div>
        <dl class="p-facts">
          <div><dt>Focus</dt><dd><ul class="p-chips">{''.join(f'<li>{i}</li>' for i in p['focus'])}</ul></dd></div>
          <div><dt>Previously</dt><dd><ul class="p-ticks">{''.join(f'<li>{i}</li>' for i in p['previously'])}</ul></dd></div>
          <div><dt>Education</dt><dd><ul class="p-plain">{''.join(f'<li>{i}</li>' for i in p['education'])}</ul></dd></div>
        </dl>
      </div>
      <ul class="p-contact" aria-label="Contact {p['first']}">
        <li><a href="mailto:{p['email']}"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="M3.5 6.5L12 13l8.5-6.5"></path></svg><span>{p['email']}</span></a></li>
        <li><a href="{tel}"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a1 1 0 01-1 1A16 16 0 014 5a1 1 0 011-1z"></path></svg><span>{p['phone']}</span></a></li>
        <li><a href="{p['linkedin']}" target="_blank" rel="noopener"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 11-.01 5 2.5 2.5 0 01.01-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.06c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.77 2.65 4.77 6.1V21h-4v-4.9c0-1.17-.02-2.68-1.63-2.68-1.64 0-1.89 1.28-1.89 2.6V21h-4z"></path></svg><span>LinkedIn</span>{OUT}<span class="sr"> (opens in a new tab)</span></a></li>
      </ul>
    </aside>
    <div class="p-bio">
      <h2 id="about-h" class="h2" data-reveal>About {p['first']}</h2>
      {bio}
      {tags}
    </div>
  </div>
</section>

<section class="p-others" aria-labelledby="others-h">
  <div class="wrap">
    <h2 id="others-h" class="h2" data-reveal>The Other Mavericks</h2>
    <div class="p-cards">{cards}
    </div>
  </div>
</section>

<section class="p-cta" aria-labelledby="cta-h">
  <h2 id="cta-h" data-reveal>Ready To Look Beyond The Obvious?</h2>
  <p data-reveal style="--d:1">Tell {p['first']} about the role. The partner who takes your brief runs your search.</p>
  <div class="p-actions" data-reveal style="--d:2">
    <a class="btn btn-ink" href="mailto:{p['email']}">Email {p['first']}{ARROW}</a>
    <a class="btn btn-line" href="{tel}">Call {p['phone']}</a>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div class="f-top">
      <div>
        <img src="{A}logo.png" alt="Leadership Mavericks">
        <p>Open to your next leadership role? <a href="{HOME}#contact" style="color:var(--paper);font-weight:500;text-decoration:underline;text-underline-offset:5px">Share your profile with us</a></p>
      </div>
      <div>
        <nav class="f-nav" aria-label="Footer">
          <a href="{HOME}#services">Services</a>
          <a href="{HOME}#team">About Us</a>
          <a href="{HOME}#contact">Contact Us</a>
          <a href="#">LinkedIn</a>
        </nav>
        <address>[Office address, City]<br>[Phone number] <span aria-hidden="true" style="margin:0 6px">·</span> <a href="mailto:[hello@leadershipmavericks.com]">[hello@leadershipmavericks.com]</a></address>
      </div>
    </div>
    <div class="f-base"><span>© 2026 Leadership Mavericks</span><span>Executive search. Independent thinking.</span></div>
  </div>
</footer>

<script>
(function () {{
  var btn = document.querySelector('.p-menu-btn'), nav = document.getElementById('p-mnav');
  if (btn && nav) btn.addEventListener('click', function () {{
    var open = btn.getAttribute('aria-expanded') !== 'true';
    btn.setAttribute('aria-expanded', open); btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    nav.hidden = !open;
  }});
  if (!('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('js');
  var io = new IntersectionObserver(function (es) {{
    es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.setAttribute('data-in', ''); io.unobserve(e.target); }} }});
  }}, {{ rootMargin: '0px 0px -8% 0px', threshold: 0.12 }});
  document.querySelectorAll('[data-reveal]').forEach(function (el) {{ io.observe(el); }});
}})();
</script>
</body>
</html>
'''


for p in PARTNERS:
    d = ROOT / p['slug']
    d.mkdir(exist_ok=True)
    (d / 'index.html').write_text(page(p), encoding='utf-8', newline='\n')
    print('wrote', d.relative_to(ROOT.parent) / 'index.html')
