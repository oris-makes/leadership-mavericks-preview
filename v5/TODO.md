# Leadership Mavericks: homepage to-do list

Covers what is still needed for `v4/home.html` after the November 2026 reorder.
Placeholders on the page are in [square brackets]. Search the file for `[` to find them all.

## 0. Copy revision (13 November 2026): check these first
The copy now uses one repeated brand line: **"The partner you meet is the partner who finds your leader."** It appears in the hero, the partners heading, the contact intro and the footer.
- [ ] **Retention figure**: removed from the stats band and the hero eyebrow. If the firm tracks it, it can be added back.
- [ ] **Founding year**: the story says `[2018]`, taken from a directory listing (village.ai). Confirm.
- [ ] **Study cited in "How we do it"**: "In one study of 20,000 new hires, only 11% of failures came down to technical ability." This is Leadership IQ's widely quoted "Why New Hires Fail" study. Check you're comfortable citing it, or replace it with your own data.
- [x] **Capabilities headline numbers**: 25+ years of combined experience, 89 CXO placements
- [ ] **Capabilities sectors**: the rotating sectors are my draft (Technology, Financial Services, Healthcare, Pharma & Life Sciences, Manufacturing, Consumer & Retail, Energy & Infrastructure, Private Equity). Keep only the ones you have actually placed CXOs in.
- [ ] **Partner captions**: one fact each, in the format "Placed N leaders in [sector] since [year]"
- [x] **Shortlist time**: 3 weeks (filled in everywhere)
- [ ] **Shortlist size**: "[N] assessed candidates in 3 weeks"
- [ ] Old copy is backed up in the session scratchpad (`home.before-copy.html`) if you want to compare

## 1. Facts and numbers (copy blocked until these arrive)
- [ ] Hero proof line: confirm "100+ leadership searches · 30+ clients" is accurate
- [ ] How we do it, step 1: replace `[18 months]` (the horizon you plan a leader's goals over)
- [ ] How we do it, step 2: replace `[N]+ leaders` (typical size of a market map)
- [ ] How we do it, step 3: replace `[N] weeks` (typical time to shortlist)
- [x] Contact section reply time: one working week (intro line and thank-you message)
- [ ] "Where we search" line: list the 3–5 sectors and the regions you cover
- [ ] Services: check the four one-line descriptions, especially Bespoke Consulting (I guessed at its scope)
- [ ] Capabilities panel: fill in `[N]+ years` and `[India’s best-known companies]` in the headline, and confirm or edit the 18 items in the three lists (my draft)
- [ ] Story intro: confirm "We worked side by side for years before Leadership Mavericks had a name…" is true

## 2. Proof
- [ ] **Client logos are DUMMY.** The 10 logos (`assets/logo-*.svg`) are invented companies for design review. Replace them with 10 real logos (SVG preferred, or PNG on a transparent background), single colour or greyscale, with written permission to show each, and update the `logos` list in the page data.

## 3. Images (you're adding these)
- [ ] Social share image `assets/og-image.png`, 1200×630
- [ ] Check that the hero, services, story and partner images are final

## 4. Partner cards
- [ ] Sector or function focus for each partner (replaces `[Sector / function focus]`): Lakshmi, Monika, Saba, Panini
- [ ] LinkedIn URL for each partner (the arrow icons currently go to `#`)

## 5. Story section
- [ ] **The chapter text is DUMMY copy.** It claims more than a decade working together, a 2018 founding, and 100+ hires across eight sectors. The partners need to confirm or rewrite all of it.

## 7. Pages to build (the homepage already links to these)
- [ ] `about.html`: full story (the homepage no longer links to it; add a link once it exists)
- [ ] `services.html`: one section per service, with anchors `#executive-search`, `#market-mapping`, `#bespoke-consulting`, `#diversity-niche`
- [ ] `leaders.html`: for executives open to a move (what you do with profiles, how to send one, confidentiality)
- [ ] Once those pages exist, point the top nav (About Us, Services) at them instead of the section anchors on this page

## 8. Contact details and links
- [ ] Office address and city
- [ ] Phone number
- [ ] General inbox (placeholder: `hello@leadershipmavericks.com`)
- [ ] Company LinkedIn page URL (footer); add it to `sameAs` in the Organization schema in `<head>`

## 9. Forms (need a developer or form service)
- [ ] Contact form: connect to email or a CRM. It currently only shows the thank-you message.
- [ ] The contact heading promises "Meet Your Partner This Week." Confirm a partner can meet every new enquiry within the week.
- [ ] Decide who receives contact-form messages

## 10. Before launch
- [ ] Pick the serif (Momo Signature or Instrument Serif) and the tint palette (Now, A, B or C). Then remove the review-only switches: the first `<script>` block after the page data, the `.lm-review` and `.lm-fonttoggle` CSS, the unused palettes, and the unused font from the Google Fonts link
- [ ] Change the `og:image` and schema `logo` paths to full URLs on the live domain
- [ ] Add a favicon
- [ ] Search the file for `[` and confirm none are left
- [ ] Review on phone, tablet and desktop
