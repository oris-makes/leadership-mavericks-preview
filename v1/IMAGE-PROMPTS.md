# v1 — Image prompts (Indian context, women-led)

These prompts cover every photograph on `home.html`: the existing ones get replacements and the one missing image gets a new prompt. Leadership Mavericks is an Indian executive search firm founded and led by women. Every image should show modern professional India, with women as the decision-makers in the frame.

| # | Slot | Status | File | Generate at |
|---|------|--------|------|-------------|
| 1 | Hero (right half of the header) | Replace | `assets/india/hero.png` | 1200 × 1250 |
| 2 | "Where every search begins." banner | Replace | `assets/india/banner.png` | 2400 × 930 |
| 3 | Services → 01 Executive search | Replace | `assets/india/service-executive-search.png` | 1200 × 900 (4:3) |
| 4 | Services → 02 Market mapping | Replace | `assets/india/service-market-mapping.png` | 1200 × 900 (4:3) |
| 5 | Services → 03 Bespoke consulting | Replace | `assets/india/service-bespoke-consulting.png` | 1200 × 900 (4:3) |
| 6 | Services → 04 Diversity & niche searches | Replace | `assets/india/service-diversity.png` | 1200 × 900 (4:3) |

The two image sets live in separate folders with matching filenames: `assets/original/` (the first set) and `assets/india/` (this set). The **Images: Original | India** switch at the bottom-left of `home.html` flips between them. To swap in a regenerated image, overwrite the file of the same name in `assets/india/`.

---

## Brand style block (paste at the start of every prompt)

> Editorial documentary photograph for a women-led Indian executive search firm. Set in contemporary urban India (a Bengaluru, Mumbai or Gurugram office or studio), understated and premium, never touristy. Indian professionals with natural, true-to-life skin tones and features. Women hold the room: they lead, decide and direct, and they're shown as senior and assured, not decorative. Wardrobe is modern Indian business: tailored blazers, handloom cotton or silk saris in muted tones, structured kurtas, minimal gold or silver jewellery. Soft natural window light, late morning, warm. Muted warm colour grade: cream highlights (#F8F6F0 / #E9E5D6), warm teak and paper midtones, deep plum-maroon shadows (#311023 / #4A1D37), with fabrics in plum, wine, ivory, charcoal and sand. Low saturation, gentle film grain, shallow depth of field. Candid, calm, quietly confident. No text, no logos, no watermark, no border, no rounded corners, full-bleed.

**Negative prompt (all images):** Western or stock-generic office, Caucasian subjects, men leading while women look on, woman taking notes for a man, stereotypes (Taj Mahal, festival décor, heavy bridal jewellery, rangoli, yoga), bright saturated colours, blue corporate tint, neon, HDR, glossy stock smiles, handshake cliché, posed group looking at the camera, readable text or brand names, logos, watermark, white border, rounded corners, lightened or airbrushed skin, distorted hands, extra fingers.

**Keep it consistent:** use the same light, grade and wardrobe palette across all six images so they read as one shoot. Vary age (30s to 60s), region and body type across the set.

---

## 1. Hero

**File:** `assets/india/hero.png` · 1200 × 1250 (near-square, shown in a tall column with `object-fit: cover`)

**Says:** "Strong leadership starts with the right people."

> [Brand style block] A boardroom in a light-filled Bengaluru office with a warm teak table, a softly blurred exposed-brick or lime-plaster wall, and a dark screen switched off. A senior Indian woman leader in her mid-fifties stands at the head of the table, in a charcoal blazer over an ivory silk blouse with a slim gold watch. She's leaning in and pointing to a line on a printed candidate profile laid in front of a seated colleague. Seated are a woman in her forties in a muted plum handloom sari, reading closely, and a man in a dark suit at the edge of the frame, partly cropped and listening. There's a laptop, papers, steel tumblers or white cups of filter coffee, and reading glasses on the table. She's clearly the one running the decision. Keep the main figures in the central vertical third so a tall or square crop still works. Near-square portrait orientation.

## 2. Banner: "Where every search begins."

**File:** `assets/india/banner.png` · 2400 × 930 (shown as a full-width background with `background-size: cover`; a maroon stats panel covers the bottom)

> [Brand style block] Very wide, close overhead crop of a pale table covered in printed charts, talent-market tables and candidate shortlists (all illegible), with a brass magnifying glass and a phone face-down. The hands of four Indian women of different ages reach into the frame: one wears a handloom-sleeved kurta and writes with a pen, one has a thin gold bangle and points at a chart, one in a charcoal blazer cuff holds a pencil, and one wears a plum knit with a silver ring and rests on a shortlist. It's an active working session. Keep the top 40% of the frame lighter and less busy, because a headline sits there. Panoramic 2.6:1.

## 3. Executive search

**File:** `assets/india/service-executive-search.png` · 1200 × 900 · 4:3

**Says:** "Board, CXO and senior leadership hires, run end to end by a partner."

> [Brand style block] Close crop at a teak desk by a window. We see the hands and forearms of a senior Indian woman partner, with a deep wine silk sari pallu over a charcoal blazer sleeve and a slim gold watch. She's turning over one printed candidate profile (illegible) from a short, neat stack. A brass magnifying glass, a closed dark leather notebook, a fountain pen and a white cup of filter coffee sit nearby, softly out of focus. The mood is quiet scrutiny and the judgement of someone who has done this for twenty years. 4:3 landscape.

## 4. Market mapping

**File:** `assets/india/service-market-mapping.png` · 1200 × 900 · 4:3

**Says:** "A clear view of the talent pool and competitor teams before you hire."

> [Brand style block] Over-the-shoulder shot of an Indian woman in her thirties, in an ivory structured kurta with her hair in a low bun, working at a laptop on a warm table. The screen shows a muted, abstract map of India and Asia with clusters of small dusty-rose and cream dots and no readable text or UI. Her left hand holds a pencil over a printed version of the same map, marked with handwritten circles. A glass of cutting chai sits beside it. Analytical, focused, calm. 4:3 landscape.

## 5. Bespoke consulting (missing)

**File:** `assets/india/service-bespoke-consulting.png` · 1200 × 900 · 4:3

**Says:** organisation design, compensation benchmarking, leadership structuring, and support for talent acquisition teams.

> [Brand style block] Three-quarter overhead crop of a teak meeting table. Two Indian women, one in her fifties in a muted plum handloom sari and one in her thirties in a charcoal blazer, are arranging plain cream paper cards into a hierarchy, an organisation chart taking shape between them. The older woman places one card in the centre while the younger one adjusts the row beneath. A printed compensation table (illegible), a fountain pen and a brass paperweight are on the table. Soft daylight from the left, with a faint jaali-screen shadow pattern across one corner. Collaborative, deliberate, expert. 4:3 landscape.


## 6. Diversity & niche searches

**File:** `assets/india/service-diversity.png` · 1200 × 900 · 4:3

**Says:** "Searches for under-represented and hard-to-find leadership profiles."

> [Brand style block] Candid waist-up shot of three Indian professionals standing together in a sunlit atrium of an older Mumbai building, with arches and lime-plaster walls softly blurred behind them. At the centre, a woman in her forties with short grey-streaked hair, in a wine-coloured blazer, holds open a folded paper map and points to a spot on it. On either side, a younger woman in an ivory kurta with a sand dupatta and a man in a charcoal shirt lean in to look. They're from visibly different regions and backgrounds. The feeling: finding a route others missed. Nobody looks at the camera. 4:3 landscape.

---

## After generating

- Update the `alt` text in `home.html` to describe the new images. For example, change the hero's "Leaders reviewing documents together around a table" to "A senior woman partner leading a shortlist review with colleagues".
- Check the hero at mobile width (`min-height: 420px`, full width). The lead woman should still be in frame.

## Not for generation

- **Partner portraits** (`partner-*.png`): these are the real founders and partners, so use real photographs only. If you reshoot, use a 4:5 crop, head-and-shoulders framing, natural light and a plain cream or stone (#D8CDD3) backdrop, with the same warm grade as the set above.
- **Logo:** use the brand file only.
