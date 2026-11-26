# Imagery guide

How every uWeed image looks and is produced: photography, engraving, collage, city images, campaign banners, category visuals and the explanatory graphics inside articles. Moved into this system on 25 November 2026 from the *uWeed Imagery Master Guide* (Google Docs), which is no longer maintained. The example pictures are in the asset group *Imagery examples*; each is named below where it belongs.

The README's *Imagery* holds the display rules (frames, cropping, fades) for category images, partner logos and hero banners. This section holds the look of the artwork. The mood, colour roles, people rules, visual hazards and the image prompt frame that apply to every picture are in *Visual identity*. Colours are named by their tokens; the token is the value.

## Formats at a glance

One table for every image family. Where any other text disagrees with it, this table is right and the other text is a mistake to fix.

| Image | Shape | Master size | File | Rules |
| --- | --- | --- | --- | --- |
| Blog featured image: effects and every other blog header | **3:2** landscape | **1800 × 1200 px** | full-colour sRGB PNG master; WebP and responsive sizes derived from it | this section; shown whole at 3:2 in the article header, the desktop card and the phone row (`BlogCard`, `ArticleRow`) |
| City featured image (city pages) | **3:2** | **1800 × 1200 px** production; the current set is delivered at 1536 × 1024 px | PNG | *City imagery* |
| Campaign email banner | **3:2** | **1800 × 1200 px** master; export **1200 × 800 px**, shown at 600 × 400 px in the 600 px email template | PNG | *Campaign email banners*; check the actual placement before export |
| Explanatory graphic inside an article | **3:2** | **1800 × 1200 px**; a separate mobile composition, also 3:2, when one bitmap cannot keep the text readable | sRGB PNG | *Explanatory graphics inside articles*, *Inline readability* |
| Portrait image inside an article | **4:5** portrait | **1200 × 1500 px** | full-colour sRGB PNG | *Images inside articles*; full width on a phone, at most 480 px wide on a desktop |
| Spot image inside an article | **1:1** square | **800 × 800 px** | full-colour sRGB PNG | *Images inside articles*; full width on a phone, 320 to 400 px wide on a desktop |
| Category image: category pages, category tiles, carousels, homepage category strip | **1:1** square | **1254 × 1254 px** | transparent RGBA PNG | README, *Imagery*, *Product category images*; *Category visuals* below |
| Partner brand logo | **2:1** | **1200 × 600 px** | transparent, unless a background is part of the logo | README, *Imagery*, *Partner brand logos* |
| Homepage banner: every banner in the hero, brand or campaign, 1 to 4 per language | phone **3:4**, desktop **21:9** | **1320 × 1760 px** and **2520 × 1080 px** | sRGB PNG master, clean (no text, logo or fade); the site serves it compressed as WebP or AVIF | README, *Imagery*, *Hero banner pictures* |
| Product photograph: product tile, product page, gallery and cart thumbnails | **1:1** square | **2000 × 2000 px** | transparent RGBA PNG | README, *Imagery*, *Product photographs* |
| Social feed post: single image and carousel slides on Instagram, Facebook and LinkedIn; Telegram channel posts | **4:5** portrait | **1080 × 1350 px** | sRGB JPG or PNG, under 8 MB | *Social formats* |
| Social story and reel cover: Instagram and Facebook Stories and Reels, Telegram stories | **9:16** | **1080 × 1920 px** | sRGB JPG or PNG | *Social formats* |
| Social profile picture: all four channels, shown as a circle | **1:1** | **1080 × 1080 px** | sRGB PNG | *Social formats*; README, *Logo* |
| Facebook page cover | about **2.7:1** | **1702 × 630 px** (twice 851 × 315) | sRGB JPG or PNG | *Social formats* |
| LinkedIn company page cover | about **6:1** | **1512 × 256 px** | sRGB JPG or PNG, under 3 MB | *Social formats* |

### Smaller copies

Every family has one master. Every smaller picture is a copy of it in **the same shape**: never a new crop, never a second file made by hand. The site makes the copies from the master (WebP or AVIF, keeping transparency where the master has it). Sizes are twice the on-screen size, so pictures stay sharp on high-resolution screens.

| Family | Master | Copies, and where each is used |
| --- | --- | --- |
| Product photograph | 1:1, 2000 × 2000 | 2000 × 2000 product page zoom (loaded only when opened) · 1200 × 1200 product page main picture · 688 × 688 product tile, desktop · 256 × 256 product tile, phone row · 152 × 152 gallery thumbnail · 128 × 128 cart thumbnail |
| Blog featured image | 3:2, 1800 × 1200 | 1800 × 1200 article header · 1200 × 800 featured card · 800 × 533 card on a desktop · 400 × 267 phone row and sidebar |
| Category image | 1:1, 1254 × 1254 | 800 × 800 category tile, desktop · 400 × 400 carousel and phone · 256 × 256 small category link |
| Partner brand logo | 2:1, 1200 × 600 | 600 × 300 brand row · 400 × 200 small logo |
| City featured image | 3:2, 1800 × 1200 | the blog copies |
| Campaign email banner | 3:2, 1800 × 1200 | 1200 × 800 email export |
| Portrait image inside an article | 4:5, 1200 × 1500 | 960 × 1200 on a desktop (480 px wide) · 780 × 975 full width on a phone |
| Spot image inside an article | 1:1, 800 × 800 | 800 × 800 on a desktop (up to 400 px wide) · 780 × 780 full width on a phone |

Product photographs taken before 25 November 2026 are portrait (for example 520 × 600 px). They still show whole in a square frame, with space at the sides, but a square thumbnail cuts them. Replace them with square masters as products are re-photographed.

All blog-family pictures share one 3:2 shape (decided 25 November 2026, replacing the earlier 16:9): one source file, the same cut everywhere, no place with its own crop.

### Uploading the master

Decided 26 November 2026, for every picture the website shows. Upload the master itself, never a copy: **PNG** for every picture (full-colour sRGB, or transparent RGBA where the table says so) and **SVG** for vector icons and logos. Upload at least the master size in *Formats at a glance*, at full quality: never a smaller file enlarged to that size, and never a file already compressed or converted to WebP or AVIF. The site's image optimiser (ShortPixel) compresses each upload and makes the WebP or AVIF copies. It can only shrink, so an undersized, enlarged or already compressed upload is what comes out blurred. Social formats go to the platforms as *Social formats* says.

### Social formats

Sizes decided on 26 November 2026 for uWeed's four channels: Instagram, Facebook, LinkedIn and Telegram (the brand icons in the footer). Two masters cover all four: one feed post and one vertical. The platforms make their own smaller copies, so upload the master as it is.

- **Feed post, 4:5 (1080 × 1350 px).** Meta's recommended feed shape, and accepted by LinkedIn and Telegram. Not 3:4: Instagram does not take 3:4 for ads, so 4:5 keeps every post usable later as a paid ad. Not square: since January 2025 the Instagram profile grid shows tall 3:4 tiles, which cut a square at the sides.
- **Story and reel cover, 9:16 (1080 × 1920 px).** One file serves organic and paid.
- **Profile picture, 1:1 (1080 × 1080 px).** The uWeed mark, per the README's *Logo* rules.
- **Covers.** Facebook page cover 1702 × 630 px; LinkedIn company cover 1512 × 256 px (LinkedIn's current Page spec; many guides still give the older 1128 × 191).

**Focus zones.** As for the homepage banners: the key element (the face, the product, the mark) and any text sit inside the zone; the rest of the canvas may carry the picture.

- **Feed post:** the centred 3:4 area, 1012 × 1350 px. The Instagram profile grid cuts about 34 px from each side.
- **Story and reel:** everything except the top 14%, the bottom 35% and 6% on each side, where the platforms place their buttons and captions (Meta's guidance). A reel cover also shows on the profile grid as a centred 3:4 crop.
- **Profile picture:** the central circle.
- **Facebook cover:** the middle three quarters of the width; phones cut the sides.
- **LinkedIn cover:** the centre and right; the logo covers the bottom left.

**Look.** Not defined yet: it is set when uWeed posts on social media again. Until then the brand tokens, the README's *Logo* rules and this guide apply, and compliance rules hold for every caption and every word on a picture.

## Scope

Consolidated 20 October 2026 (last edited 16 November 2026). Use this section as the imagery brief for uWeed. It covers featured blog collages, effects articles, city images, campaign email banners, category concepts and explanatory graphics inside articles. It records the current rules, the examples that explain them and the limits of each rule.

The shared identity is premium photography, tactile brand-colour paper and detailed editorial engraving. Composition depends on placement. Effects headers use their specific two-photo structure. Inline illustrations use the lighter collage system updated on 20 October 2026 below: centred composition, torn-paper title, optional subtitle, small original smile-u favicon and genuine engraved linework. Category assets use the paper-free, fine navy engraving direction selected on 12 November 2026; see Category visuals for the current rules and review status.

### How to apply the rules

  - Identify the placement and article before choosing a composition. Apply the shared identity, then the relevant family rules, then any explicitly recorded article exception.
  - The latest specific instruction takes precedence over an older general example. Never extend an exception to neighbouring articles or another visual family.
  - Use examples to understand composition and drawing technique. Some older raster studies contain superseded logos, separators or labels; their captions identify those limits.
  - If a required source, logo or article brief is unavailable, record the gap. Do not invent an approved decision or substitute a different reference.

| Visual family | Current scope |
| --- | --- |
| Effects blog header | 6–7 paper pieces; normally 2 contextual photos and 1 engraving. Two named head-topic exceptions. |
| Other blog headers | Shared collage identity; subject, scene or comparison composition chosen for the topic. |
| City header | Recognisable city photography transitions continuously into fine green engraving of the same scene; large integrated city name and a small white logo at the bottom right. |
| Campaign email | Shared materials and signature; message comes from the approved campaign brief. |
| Category hero | Category-led material/product cutouts; example remains a proposal. |
| Inline explanatory graphic | Light editorial collage; centred title, optional subtitle, small favicon, detailed engraving and responsive type. |

## Shared identity and brand assets

Use supplied original uWeed artwork. The horizontal logo contains the distinctive smile-u mark; it must not be reconstructed with a font, redrawn by AI or replaced by a generated approximation. Preserve geometry, letter spacing, proportions and clear space. Select an existing approved colourway that is already present in the visual, with sufficient contrast.

### Fixed logo geometry

For header and campaign signatures other than the city-specific exception, measure visible logo artwork rather than transparent padding. At 1800 px canvas width, the horizontal logo is 427 px wide, with a 39 px top inset and 50 px right inset; scale these measurements with canvas width. City images use the later, smaller white bottom-right logo direction in City imagery. Inline explanatory illustrations use the supplied small smile-u favicon at bottom-right, not the horizontal wordmark or this header-logo geometry.

Reserve the top-right logo area before laying out the content. Adjust paper or drawings around the logo, never its size or anchor. In collages, use a small integrated torn-paper area with clear space; avoid a large empty colour surface, separate badge, capsule or corner tab. The logo paper counts within the effects piece total.

### Palette

| Family | Dark ink / logo | Main paper | Light paper |
| --- | --- | --- | --- |
| Blue | Navy `dark-blue` | Cobalt `medium-blue` | Lavender `light-blue` |
| Green | Dark green `dark-green` | Green `medium-green` | Mint `light-green` |
| Pink | Dark pink `dark-pink` | Pink `medium-pink` | Blush `light-pink` |
| Neutral | Navy `dark-blue` | White `white` | White `white` |

There is no fixed topic-to-colour mapping. Recombine approved colours with readable contrast; pale tints are backgrounds, not text. Effects paper uses the blue, green and pink families, navy and white. New engravings use monochrome navy ink; the 21 October clarification supersedes coloured engraving treatments in older examples. Orange may remain naturally inside a photograph, such as the silk sleep mask or countdown timer; it is not a fourth effects paper family. The earlier broad brand palette also contains orange and red, but that does not override this later effects restriction. Graphic colour choices do not redefine website UI colour roles.

Use the original approved logo assets: the logo kit is in this system (*Logo*, asset group *Logos*); the original brand kit and its usage guide: <https://drive.google.com/file/d/1D7Iu1DPYXnKvEJZbWX7MJEo91gNi60FJ/view>. Choose the existing approved SVG or PNG colourway that matches the collage. Source a missing colourway from that kit rather than inventing or redrawing it.

## Photography and engraving

### Photographic finish

Use credible people, places, materials and proportions, with natural skin tones, realistic colours, soft-to-moderate contrast and matched exposure. Keep the visual premium and relevant to the article. Avoid decorative cannabis-leaf repetition, cheap leaf stamps and generic cannabis props added merely to signal the category. Genuine hemp material or a leaf on relevant packaging may remain when the article calls for it.

For named products, use authentic packshots, labels and retail packaging. A generic study is not an accurate catalogue product image. Do not imply a product benefit, medical outcome or geographic detail that the article and source material do not support.

### Drawing language

“Botanical engraving” describes the technique, not a mandatory botanical subject. Use a sophisticated antique copperplate or natural-history finish: fine contours, close hatching, dimensional modelling, tonal depth and rich material or terrain detail. Mountains, mechanisms, objects, plants and conceptual subjects can share this drawing language. Sport S3’s mountains are the positive detail benchmark.

Do not flatten drawings into sparse line icons, impose a blanket 20–30% detail reduction, or force plants into every image. Judge density by meaning, legibility and premium finish. Tabler icons are a separate optional element for inline explanations; they do not replace detailed editorial drawings.

### Complementary meaning

Photography and engraving must represent different objects or subjects. The engraving adds a clear complementary concept rather than redrawing a photographed bottle, pill, landmark or other object. Figurative drawings are useful where their connection is understandable. Do not rely on an explanation in chat to make an otherwise obscure rope, tram platform or unrelated prop communicate the article.

Effects engravings contain no words, labels or captions unless explicitly requested for that image. The Überdosis dial is an explicit text exception. Existing accepted German labels in older head-topic images remain untouched during title-only localisation.

When people appear in an effects photograph, the engraving must not also contain human faces, figures, silhouettes or separate hands and gestures. An isolated liver-organ drawing is an explicitly accepted article subject. This effects rule must not be retroactively imposed on every inline scientific illustration.

**Example:** `assets/Imagery examples/effects-sport-s3-detail-reference.png` (group *Imagery examples*)

*Sport S3: the exact retained panel from the original comparison board. This is the detail and balance reference, not a new regeneration. Its recovered panel is 697 × 480 px, not a production-resolution master.*

## Effects collage structure

Use 6–7 physical collage pieces in total. Count the title paper and logo paper within the total. Count paper pieces, not the number of objects drawn on a single paper.

| Piece | Count | Purpose |
| --- | --- | --- |
| Contextual photographs | 2 | One dominant scene and one supporting scene. |
| Engraving paper | 1 | One coherent drawing area, targeting about 20% of the whole image. |
| Article title paper | 1 | White torn-paper label, bottom-left. |
| Brand-colour papers | 2–3 | Plain strips or broader shapes, including the small integrated logo area. |

The 20% engraving area is a composition guide, not a precise measured ratio of Sport S3. No additional fixed photo-area ratios were agreed. The dominant photo may alternate left or right. Keep the title bottom-left and the authentic logo at its fixed top-right anchor.

### Two complete photographic pieces

  - Each photo is a contextual crop showing its subject with an immediate setting. It is not an isolated item or person overlay. The full body or full object need not be visible.
  - Only one photographic piece may contain humans. Two or more people may share that main scene. The supporting photo must contain no person, portrait, separate hands or body-detail view, including reflections.
  - The two photos need distinct settings or surface patterns. Avoid repeating plants and stone steps, bedding or another obvious background pattern in both.
  - Do not create detached photo fragments around the logo or through gaps between papers. Close joins using the existing paper pieces, without adding more pieces.

### Photo joins and torn edges

The photos may touch naturally along a short part of their boundaries, up to 50% of either adjoining photographic side. This is a boundary-length limit, not a photo-area ratio. A join around one third of the side is a practical target, not an additional mandatory rule.

Do not insert a continuous narrow coloured separator strip, spine or gutter between every pair of photos. Stagger the torn shapes naturally. Existing broad engraving-paper corners and title or base papers can interrupt the contact at its ends. Maintain the 6–7 total rather than adding a divider.

Use clearly visible, natural torn-paper marks between pieces. Effects photos are complete photographic paper crops with torn boundaries. The older generic ban on photo panels and preference for clean subject cutouts does not govern this later effects-specific structure.

## Effects examples and title treatment

**Example:** `assets/Imagery examples/effects-schlaf.png` (group *Imagery examples*)

*Schlaf: sleeping woman in a complete bedding photograph, a separate contrasting orange silk mask in its fabric setting, and one moon-and-cloud engraving. No landscape. Orange belongs to the real photo, not the paper palette.*

Use white naturally torn paper with comfortable padding, a deliberate small angle where useful, and uppercase heavy Poppins ExtraBold-like navy title lettering. Blog titles are short article phrases or questions, usually one or two lines; approximately 2–5 words or 30 characters is guidance, not a hard limit. Do not embed blog category tags. Keep a consistent apparent type scale.

Rounded corner title cutouts, connected title-row cutouts and coloured title labels are superseded for collage headers. Inline illustrations now also use tactile torn-paper titles under their lighter collage rules; the earlier rounded-title studies are historical references.

For new compositions, shorten or rephrase an overlong title before shrinking type. Paper width may be planned to fit the chosen wording. For the current French and English copies, preserve the accepted German paper and artwork; adjust title wording, line breaks and fitting only.

**Example:** `assets/Imagery examples/effects-schmerzen.png` (group *Imagery examples*)

*Schmerzen: sofa scene, separate hot-water-bottle scene and a lumbar-spine engraving. This older accepted raster retains a separator shape; future compositions follow the later natural-contact rule above.*

## Effects article exceptions

Only Nebenwirkungen and Gegenanzeigen use the expressly approved one-photo structure with a larger coherent engraving. Do not extend this treatment to supporting topics such as Medikamente or Antidepressiva. A single enlarged drawing paper may contain several related objects while remaining one piece.

| Article | Specific instruction |
| --- | --- |
| Nebenwirkungen | Keep the dominant daytime-drowsiness photo; use a larger grouped engraving for potential side effects. Remove the unhelpful second photo. |
| Gegenanzeigen | One doctor consultation with a non-pregnant adult patient and a larger caution engraving. The non-pregnant request is specific to this image. |
| Medikamente | Restore the standard two-photo structure; interlocking gears provide the distinct figurative engraving. |
| Antidepressiva | Standard two-photo structure; detailed antique balance with empty pans. Do not duplicate medicine packaging in the engraving. |
| Überdosis | The dial must explicitly communicate dose and being over the limit. DOSIS and ZU VIEL are the agreed text exception; no invented numerical dose threshold. |
| Leber | Non-clinical contextual photos plus an unlabelled liver-organ engraving and small caution sign. Convey informed caution about potential liver risk. |
| Schwangerschaft | Pregnant woman as main subject is allowed because pregnancy is the topic. Empty cradle is the supporting photo; a few toys form the engraving. |
| Abhängigkeit | The article asks about dependence on CBD itself. Keep a questioning, sober framing; do not imply established addiction or depict recovery from other substances. |

CBD Öl Wirkung was explicitly skipped because the article will retire. Do not generate it merely because it remains published in the topical map.

**Example:** `assets/Imagery examples/effects-nebenwirkungen-exception.png` (group *Imagery examples*)

*Nebenwirkungen: an approved head-topic exception with one photo and a larger grouped engraving. The German engraving labels are legacy content, not a new instruction to label other engravings.*

**Example:** `assets/Imagery examples/effects-gegenanzeigen-exception.png` (group *Imagery examples*)

*Gegenanzeigen: the other approved head-topic exception. Do not copy this structure into Medikamente or Antidepressiva.*

## Article meaning and accepted subjects

Use the topical map and the article’s actual question before selecting a concept. These subjects record the retained effects artwork; they are not a stock list to repeat on other pages.

| Article | Retained visual meaning |
| --- | --- |
| Wirkung | Couple examining CBD information, notebook scene and endocannabinoid-system engraving. Legacy human engraving predates the later no-human-drawing rule. |
| Macht CBD high | Mirror-checking adult, CBD packaging and unlit joint, and a conceptual distorted-room engraving. Packaging leaf was expressly retained. |
| Schlaf | Sleep scene, orange silk mask and moon/clouds. |
| Angst | Preoccupied man, household letters/planner and anatomical brain. Rope, tram and maze concepts were not retained. |
| Schmerzen | Sofa scene, hot-water bottle and lumbar spine. |
| Sexualität | Couple in one sofa scene, separate bottle scene and oyster with pearl. No engraved couple. |
| Gewicht | Meal preparation, bathroom scale and measuring tape. |
| Arthrose | Woman on outdoor steps, walking stick beside an indoor chair and joint engraving. Distinct contexts; no photo sliver by the logo. |
| Depression | Withdrawn woman in a bedroom, empty rain-wet bench and rain cloud. |
| Sport | Original Sport S3 runner, shoe context and detailed Alpine mountain drawing. |
| Parkinson | Clinician/patient hand assessment together, unoccupied rollator and metronome. |
| ADHS | Distracted work scene, orange visual timer in a separate setting and tangled thread. Blue/lavender paper. |
| Nebenwirkungen | Drowsiness photograph and larger grouped potential-side-effect drawings. |
| Gegenanzeigen | Non-pregnant consultation photo and larger grouped warning drawing. |
| Medikamente | Pharmacist consultation, medicine-organiser/list scene and interlocking gears. |
| Antidepressiva | Mental-health consultation, separate medicine scene and empty antique balance. |
| Überdosis | Adult seeking advice by phone, tipped bottle/spill scene and explicitly excessive dose dial. |
| Leber | Adult reading CBD packaging, separate bottle/water scene and liver with caution. |
| Kinder | Father and child reading together, separate wooden rocking horse and storybook engraving. |
| Schwangerschaft | Pregnant woman, empty cradle and toy engraving. |
| Abhängigkeit | Thoughtful woman inspecting a closed CBD bottle, separate CBD-flower jar and intact chain. Title asks whether CBD is addictive. |

## City imagery

City imagery — current direction, confirmed 16 November 2026. Begin with the city, not a reusable landscape template: research what the place stands for and choose a recognisable local landmark, characteristic setting, cultural feature or other meaningful motif. Vary the subject, viewpoint and composition by city; do not default to a riverfront or the same background in every image. Keep a consistent uWeed visual treatment across the series.

Build a single continuous, recognisable scene that gradually transitions from realistic, full-colour photography on the left into a precise green-toned, high-quality engraving of the SAME scene on the right. Carry the actual forms and perspective across the transition; avoid abrupt splits or separate unrelated illustrations. The engraving should have refined contours, fine hatching and dimensional detail. Use the restrained light-green finish of the chosen Zürich image for CBD city pages. Verify the landmark and geography before production; generated imagery is not evidence of geographic accuracy.

### City typography and title integration

Set the city name large and confident in the established Poppins direction, in dark green, using the Morges and Genève images as visual scale references. Prioritise an equally strong visual presence across the series rather than fitting every city to the same fixed width. Keep the city name on one line where possible; reduce its size only as needed for a long name, without stretching, cropping or sacrificing legibility. Do not make short names excessively large simply because extra width is available.

Place the smaller supporting line directly above the city name, left-aligned with it: “CBD in” for German and English; “CBD à” for French. Preserve the current, lighter supporting-line weight shown in the approved Luzern image: in the four-way comparison on 16 November, option 1/current was retained. The heavier medium, semi-bold and bold studies were not selected. Match the visual reference rather than assuming an unverified numeric font weight.

Let a meaningful element of the scene interact naturally with the title where appropriate, while keeping every letter readable. The Genève water jet and the Montreux statue’s raised hand are examples. Do not force the same overlap into every city or invent a landmark for this purpose.

Carry the illustration into the city-name letterforms: the left side starts predominantly solid dark green, then fine engraved hatching gradually becomes visible inside the letters toward the illustrated side. Match the Zürich reference; preserve sharp letter outlines and strong contrast. This internal texture is distinct from a landmark overlapping in front of the lettering, and both treatments may be used together.

Use the authentic approved white horizontal uWeed logo, small at the bottom right and with enough contrast against the image. Preserve the original logo asset and proportions; never redraw it, substitute text, or add a badge. City images are landscape 3:2; use 1536 × 1024 px PNG for this current image set. Avoid torn paper, title boxes, chips, artificial collage edges and unrelated decorative elements. These city-specific decisions supersede earlier city collage, complementary-subject and top-right logo rules, without changing other imagery families.

Approved visual references: Zürich lettering texture and overall direction — https://drive.google.com/file/d/1OHdYVsQ_S3atWNTsjOxM0uwaLsTlsIIu/view; current lighter “CBD in” weight — https://drive.google.com/file/d/1KlKy3XzAWNu91TcKIJDHOgGFq72-nyCS/view; title scale and landmark interaction — https://drive.google.com/file/d/1jYTj1ek8SnZC4ORVUDdKirA0D6WwKrhe/view and https://drive.google.com/file/d/1wF2dp9tDLy80PtH5WBvMQDL3XyhptETJ/view; Morges title scale — https://drive.google.com/file/d/1QQzydzCQaERzmFoXU8jE4mcRecebLXwT/view.

### Historical city collage references (superseded)

| City | Photo reference | Complementary engraving |
| --- | --- | --- |
| Basel | Rhine and Münster | Fasnacht mask, drum and piccolo |
| Bern | Aare and old town | Clock detail and rose branches |
| Biel | Old-town fountain | Watchmaking and lake imagery |
| Zürich | Grossmünster and Limmat | Polybahn and façade detail |

For each language, use the appropriate local city name and supporting line while preserving the city-specific scene, composition and visual hierarchy. German and English use “CBD in”; French uses “CBD à”. Check accents, spelling, full-word legibility and alignment for each image. The older table and collage study below are historical references, not requirements for the continuous-scene treatment.

**Example:** `assets/Imagery examples/city-collage-historical.png` (group *Imagery examples*)

*Historical city collage study from the featured-image guide. Its paper, title, logo placement and complementary-engraving rules have been superseded by the chosen continuous-scene direction above.*

Current city-image masters: City Images – Photo to Engraving – Nov 2026, organised into DE, FR and EN folders — https://drive.google.com/drive/folders/1_96n2lkEJCLVo0mjVfdmAqSvCVswOLi0. Use the latest assets in those folders as the working references; the earlier city collage set is historical. City-image decisions do not alter effects, categories or other imagery families.

## Other blog headers and campaign imagery

### Generic blog compositions

The earlier shared collage family supports subject-led, continuous-scene and comparison compositions. Hero placement may be left, right or central while the title and logo stay anchored. Clean complete photographic subject cutouts may share a paper-and-engraving environment. Avoid framed photo windows and detached photographic fragments in this generic treatment.

Generic collages have no fixed three-to-four-piece cap. The later effects standard specifically requires contextual photo pieces and supersedes that cutout-only treatment for effects articles. Do not collapse these two scopes into one contradictory rule.

**Example:** `assets/Imagery examples/blog-subject-led-collage-historical.png` (group *Imagery examples*)

*Earlier subject-led collage study. It demonstrates the generic family, not the later two-contextual-photo effects recipe.*

**Example:** `assets/Imagery examples/blog-comparison-composition.png` (group *Imagery examples*)

*Comparison composition reference. It is a material/layout study; do not reuse its blog wording as campaign copy.*

### Campaign email banners

Use the same premium photographic, paper and editorial-engraving materials for product-, category- or lifestyle-led campaigns. The approved campaign brief supplies the title, key message and offer. There is no generic 2–5-word limit for campaign headlines. Verify the full approved wording at mobile display size.

Use the white torn-paper title bottom-left and authentic horizontal logo top-right. Put supporting copy, conditions and clickable CTAs in native email blocks where appropriate. Do not add photographic insets or rounded logo backings merely because older boards show them.

Shared master: 3:2 at 1800 × 1200 px. Standard email export from the shared guide: 1200 × 800 px, displayed at 600 × 400 px in the then-current 600 px-wide template. Check the actual campaign placement before export; later campaign-specific formats do not change the effects header ratio. A homepage campaign banner is not a resized email banner: it is a banner in the hero, made to the hero format (README, *Imagery*, *Hero banner pictures*).

## Category visuals

### Category direction — 12 November 2026

Selected engraving benchmark: CBD Blüten, option 2 “Finer detail”. Retain the original navy copperplate / natural-history style with more precise contours, fine form-following hatching, detailed veins and dimensional shading. Use the reference for the quality of linework and the balance of illustration to product; adapt the subject and scale to each category. Navy `dark-blue` remains the single engraving ink. Avoid coloured washes, flat iconography and heavy simplified outlines.

Paper-free composition: category visuals no longer use the torn-paper piece or white torn edge beneath the products. Keep the photograph, the applicable packaging and a complementary engraved subject as freestanding elements on a genuinely transparent 1:1 square canvas. Preserve the existing category-specific packaging, branding and subject decisions; packaging-free accessory exceptions still apply. Category tile framing: use the same 1254 × 1254 canvas throughout. Aim for approximately 8–10% clear transparent space at the top and bottom and at least about 8% at the sides, allowing modest optical adjustments for different silhouettes. Align the visible product base near 91% of canvas height and check the set side by side at equal display size. Narrow compositions may have more side space. Balance apparent product scale rather than stretching each silhouette to identical width; preserve natural object proportions, complete engravings and all labels. The website category heading remains outside the image. Render the whole square using contain, without cropping away the built-in margins. This category-tile rule also applies inside a wide homepage category strip; the strip itself can be full width.

Scope and status — 12 November 2026: the user authorised in-place replacement of the 23 CBD/CBG category assets, retaining their existing filenames and Drive links. The remaining Vaping, Headshop and planned tobacco images are held while the relevant vertical direction is settled. Apply the square format and spacing rule to their future revisions. Saving assets is separate from website publication. These category rules supersede older paper-underlay and portrait-format instructions; blog headers, city images, campaign imagery and inline illustrations retain their own formats and paper rules.

**Example:** `assets/Imagery examples/category-cbd-blueten-reference.png` (group *Imagery examples*)

*Selected CBD Blüten reference: finer-detail engraving and paper-free composition. The package details are illustrative, not a live offer.*

Category decisions agreed on 21 October 2026 supersede the historical proposal below. Use K05 Bold typographic for flower packaging, K07 Technical index for hash, and K06 Tactile relief for oils. Packaging design may differ by category. For the 12 November rollout, CBD and CBG packaging share the green family: dark green `dark-green`, green `medium-green` and mint `light-green`, with the existing cream/white neutrals and navy engraving. CBD vape belongs to Vaping; all accessories belong to Headshop. Vaping and Headshop colour identities remain to be defined; do not present suggested palettes as approved. The earlier flower images remain review studies; the 12 November CBD Blüten example is selected as the engraving-style reference.

Concentrate category studies — 22 October 2026: the current topical map has four German categories: CBD Hash, CBD Pollen, CBD Kristalle, and the combined Wax, Crumble & Shatter category. Create one featured asset per category; wax, crumble and shatter share one image. Use the current 1:1 / 1254 × 1254 transparent paper-free composition, original small package-coloured smile-u, clear category-first label hierarchy, discreet inline grams / CBD percentage / illustrative reference-price row, and complementary fine navy monochrome copperplate engraving without text. Keep the K07 technical-index grid direction selected for hash. These first concentrate studies propose: hash on a single clear-dome blister card with real pressed resin and engraved screw press; pollen in a technical-index pouch with real loose kief and engraved mesh sieve; wax/crumble/shatter with a technical-index concentrate jar, three distinguishable photographed material textures and engraved botanical extraction apparatus; crystals with a technical-index glass jar, white crystalline isolate material and engraved precision balance. The jar adaptations and engraving subjects are review proposals, not additional universal rules or final approvals. No duplicated photographed object in engraving, generic cannabis-leaf filler, full wordmark, invented health/quality claims or prominent price badges. Product-like data are illustrative references, not actual private-label listings. Archive: New Style Collage Oct 26 / Categories — https://drive.google.com/drive/folders/1BLJnBVb9BVik22xmiTNpJGWSbs4H_psi. All category images are stored directly in this parent folder. The numbered category subfolders and nested flower-version folders were emptied and removed on 22 October 2026. Preserve existing file IDs and links when reorganising or revising images.

Remaining category studies — 22 October 2026

Category file organisation — updated 23 October 2026: keep the 31 current/category-review PNGs directly inside New Style Collage Oct 26 / Categories — https://drive.google.com/drive/folders/1BLJnBVb9BVik22xmiTNpJGWSbs4H_psi. Their filenames now match the approved SEO filenames in the category image spreadsheet — https://docs.google.com/spreadsheets/d/1qUQbAmyHPw3HBZbH_sK88EtQpQ_kbSqEZchHFph4N3s/edit. The 16 historical flower studies are preserved only in the subfolder Archive – nicht veröffentlichen — https://drive.google.com/drive/folders/1dkLZO4QBwn9dns2yxTPKHlGs5a9DRHEm. They retain archive-v1- or archive-r2- filename prefixes and must not go live. This single Archive folder is the exception to the flat current-image organisation; do not recreate category or packaging-concept subfolders. The spreadsheet separates current images from the archive, records the actual filename and full Drive URL, and lists the WooCommerce ID from the Topical Map's WP Object ID column first. Missing IDs remain blank and flagged; planned pages keep their status, and an ID is not publication approval. Preserve image bytes and Drive file IDs when moving or renaming so existing links remain valid. This folder decision applies to category imagery only; city and blog organisation is unchanged.

Created 15 German category featured-image studies: 12 active categories (CBD Joints, CBD Samen, CBD Kosmetik, Hanftee, Hanfkapseln, CBD Vape, Einweg Vape, CBD Liquid, Rauchzubehör, Drehpapier, Filtertips and CBG Shop) and three planned categories (Pre-Rolls, CBD Zigaretten and Tabak). The three planned studies do not imply that their pages are live. Retired or redirected Pets, CBN and individual CBG categories are excluded; CBG Shop is the retained active parent. An additional packaging-free grinder study is stored with the accessory images; it is not counted as a newly verified topical-map category. The current category archive therefore contains 15 mapped-category studies plus one separate grinder study for this remaining-category set.

Use the current 1254 × 1254 square format (1:1) and true transparency outside the composition. This 12 November sizing rule supersedes the original portrait format. The usual paper-free composition combines concept packaging, a realistic product/material group and one complementary fine navy monochrome copperplate engraving. An oil/vape carton can serve as the packaging while the bottle/device serves as the product. For cosmetics use the pump package, cream smear and aloe engraving only; do not add an unnecessary outer carton or paper base. The photographic product and engraved subject must be different. Engraving style remains detailed antique natural-history/technical etching, not necessarily a botanical subject. No text in the engraving by default. Category-specific exception agreed on 22 October 2026: head shop/Rauchzubehör and grinder images have NO retail packaging. Do not invent retail packaging, printed product-information labels, reference prices or title chips for these accessories. For the packaging-free headshop assortment, brand BOTH the grinder lid and the storage container using the original supplied artwork. Center a matching-family favicon on the circular top face of a lid, projected naturally in perspective. On the green storage container, use the dark-green favicon centered on the horizontal lid top; remove the old navy side icon. If branding is placed on the storage container's vertical side instead, use the horizontal uWeed logo in matching green rather than a side favicon. The standalone blue grinder also needs a centered light-blue original favicon on the leaned lid face. These are requested product-branding exceptions; do not print the mark on the central internal magnet. Use a realistic colourful, thoughtfully designed product assortment for head shop, one item of each kind, and a realistic grinder for the grinder study, with complementary fine navy process engraving and no torn-paper base. The exception changes component count as needed; do not force packaging onto either accessory.

Packaging retains the category as the dominant title, a smaller subtitle, the original small package-coloured smile-u printed top-right, balanced lower label spacing and one discreet information row with equal styling for quantity / relevant specification / illustrative price. Do not add a full wordmark, separate floating logo or title chip. Unit and specification depend on the category; a CBD percentage is not mandatory. Keep authentic formats: pre-roll cartons/cases, cigarette flip-top pack, seed card/vial, cosmetic pump, a square-front tea-bag carton, a rigid actiTube-type filter box, a horizontal fold-over rolling-tobacco pouch, capsule jar, vape cartons/devices and a rolling-paper booklet. The tea/filter/tobacco formats and packaging-free head shop/grinder direction were requested on 22 October 2026; resulting revised images remain review studies until selected. Other new adaptations, subjects and colour choices are review proposals, not new universal packaging rules. Existing K05 flowers, K07 hash and K06 oils selections remain in force. All prices, strengths and quantities on concept packaging are illustrative references, not actual private-label SKUs or live offers.

Category-specific naming: use HANFTEE and HANFKAPSELN without a CBD prefix, cannabinoid-content claim or dosing/health promise. Seeds use count and Saatgut rather than potency or yield claims. Accessories use count/material/size without cannabinoid claims. Cosmetic labels use volume and product type without clinical promises. CBG Shop uses one parent-category assortment showing CBG oil, hash, seeds and flowers together, all clearly identified as CBG. Balance the four formats instead of letting the flower pouch dominate. This is an explicit category-specific exception to the default component count; adapt the packaging/product groups to the assortment. Do not create separate redirected CBG category assets or print one weight, strength or price as if it applied to the entire range. Preserve adult catalogue presentation and add no people, invented certifications or benefit claims.

Complementary engraving directions — updated 22 October 2026: joints—papermaking deckle and fibre spool; Pre-Rolls—manual rolling mechanism; CBD Zigaretten—cellulose fibres; seeds—seedling and roots; cosmetics—aloe specimen; Hanftee—tea bags and/or loose herbal blend, with brewed tea in a colourful designed ceramic cup as the real photograph and a square tea-bag carton; capsules—precision caliper; vape—etched vapour ribbons; disposable vape—hourglass; liquid—merging drops; head shop/Rauchzubehör—the current review study uses a recognisable stocked open-front shop-shell engraving behind the colourful photographed accessories, showing the broader smoking/tobacco/vape assortment; papers—a material-source engraving of acacia gum arabic and rice, hemp and flax fibre specimens, replacing the rejected rolling-process imagery; filtertips—porous charcoal, with real filters and a rigid filter box; Tabak—whole leaves representing blend sources as the engraving, with real Feinschnitt in front of a horizontal rolling-tobacco pouch; grinder—actual grinder without packaging, with a process engraving of coarse material passing between cutting teeth and emerging finer. Use the established detailed navy copperplate style without engraving text. Complement the photographed objects; do not duplicate their exterior form in the engraving. These 22 October corrections supersede the earlier teapot, generic gear and tobacco-flower motifs for the affected categories.

Further category refinements — 22 October 2026: Hanftee retains its square carton and tea-bag/herbal engraving; replace the transparent glass cup with a colourful opaque design ceramic cup with brewed tea visible at its opening. Head shop uses distinct designed accessories without retail packaging: one grinder, one storage container, one pipe, one ashtray, one lighter and one rolling tray; a grinder lid belongs to the same product, not a second product. Include the original favicon on the grinder lid and use matching green branding on the storage container. Top-centred lid branding uses the favicon; side branding on the storage container uses the horizontal logo. Use the approved original colourway and source, not a generic smiley. The grinder follows the paper-free category direction; do not add a coloured underlay beneath it. On activated-charcoal filters, print the supplied horizontal uWeed logo in its approved dark green directly on the real filter wrappers, following their cylindrical perspective and leaving endcaps clear. This is a filter-specific exception to the usual small-mark-only concept branding rule; the separate storage-container side-logo exception applies only when that placement is chosen. Do not add full wordmarks across all category packages. Rolling-paper engraving now represents material sources: gum arabic from acacia as the adhesive example, with rice, hemp and flax as examples of paper raw materials. Show recognisable gum exudate/tears on an acacia twig, a rice panicle, hemp stem fibres with restrained identifying leaf, and a flax specimen. These are category material examples, not a claim that every paper or this illustrative package contains all four; verify any SKU-specific ingredient wording against its actual data. Gum arabic is not arabica coffee. Replace both rejected isolated-cone and rolling-process studies; no finished joints, rolling diagrams, arrows or engraving captions in the current material direction. Source references for materials: OCB Rice — https://ocb.net/ocbproducto/rice/ ; SWM Rolling Papers — https://www.swmintl.com/products/rolling-papers/ . Head shop is the broad junction of smoking, tobacco and vape accessories, not a cannabis-only category. The approved photographic product designs and original lid branding are retained. Abstract roller-mechanism, lock/key and materials/connector engraving studies were rejected as unclear representations. Following the user's request to step back and consider a shop shell, the current review image uses one coherent architectural copperplate engraving of an open-front stocked specialist shop: shelves of water pipes and vaping devices, rolling-paper and filter displays, and a glass display counter. The concept should read as a shop at first glance, with recognisable assortment groups rather than arbitrary symbolic objects. The six real colourful foreground products are reduced/rebalanced to leave the shop visible, maintaining one of each photographic type, blue grinder-lid favicon and green top-lid storage favicon, without a torn-paper base. Stock inside the shop is contextual assortment, not an instruction to duplicate the exact photographic product designs or add extra foreground cutouts. Any contextual product repetition within the shop study is a scoped review exception, not a new universal engraving rule. Maintain the broad category meaning, detailed navy style, no engraving text and genuine transparent 1:1 square canvas for new exports. This is a new composition study awaiting review, not a final approval. Source inspiration: specialist headshop shelving and assortment structure, https://www.wernersheadshop.ch/de/ ; https://www.tamar.ch/de/headshop/bong-pfeifenzubehoer ; https://www.jelly-joker-kassel.de/headshop/ . Do not reproduce a real retailer's branding or exact storefront. The other category visuals were retained at that time. The 12 November paper-free engraving direction applies to future revisions; it does not authorise automatic replacement or publication. The rolling-paper material engraving is separate from this headshop rethink.

Oil category application — updated 22 October 2026: create FOUR category assets only: CBD Öl (main category), Vollspektrum, Breitspektrum, and ONE category image for oils by concentration. The concentration image combines 5%, 10%, 20%, 30%, 40% and 50% in one illustration; use 5–50% consistently on carton and bottle, not separate category images by strength. Retain visible engraved flowing movement linking the drops along a rising curved path; subtle motion lines alone must not disappear at thumbnail scale. Preserve the transparent 1:1 / 1254 × 1254 paper-free composition, K06 tactile-relief ivory carton, photographic amber dropper bottle, small package-coloured original smile-u mark and fine navy monochrome engraving. Use millilitres in the discreet inline information row; keep volume, CBD value/range and illustrative price equally styled and label content vertically balanced. Main CBD Öl: the confirmed complete carrier-source list is coconut/MCT, sunflower oil (Sonnenblumenöl), and hemp-seed oil. Show three smaller recognisable botanical specimen vignettes of balanced visual weight; no extra carrier and no engraving captions. Keep the main package label generic. The user approved the main CBD Öl image on 22 October 2026. Preserve its established composition and packaging; the 12 November paper-free engraving direction applies to future revisions. Both spectrum packages use the spectrum name as the largest label and CBD ÖL as the smaller subtitle, on carton and bottle. Vollspektrum retains the conceptual oil-content engraving showing THC present and must always be included and shown alongside the other oil-category assets. Final full-spectrum correction: remove the outside italic mit THC caption, its underline and its callout line; retain the CBD, CBG and THC constituent labels inside the engraved oil drop. Breitspektrum uses a different, text-free engraving showing multiple included constituents and a separate excluded component; the revised figurative study uses an etched oil drop made of interlocking sections, with one removed section clearly separated from the matching gap. The former magnifying-lens study is superseded. This subject is a study for this category, not a new universal engraving rule. No added letters, abbreviations, numbers, labels or captions in the broad-spectrum engraving; package text remains. Constituent symbols are conceptual, not chemical formulae, laboratory evidence or quantitative THC claims. The limited labels already used in the full-spectrum study and the percentage labels in the concentration image are placement-specific exceptions to the default no-text engraving rule; do not generalise those exceptions to other engravings. The current CBD oil category set uses the green/mint family consistently; concentration does not change the colour family. Prices remain illustrative reference prices, not live offers or actual concept-product listings. The four oil category visuals are the final selected set following the requested full-spectrum caption removal on 22 October 2026. Keep these four current oil-image files directly in Categories; do not create a separate oil subfolder. Send any separately superseded oil variants to Trash rather than treating them as current files. Saving final assets does not authorise automatic website publication. Current location: New Style Collage Oct 26 / Categories — https://drive.google.com/drive/folders/1BLJnBVb9BVik22xmiTNpJGWSbs4H_psi. The old eight-image archive folder was deleted as explicitly requested on 22 October 2026; the current oil set contains four image files in the shared Categories folder.

Category tile assets use a 1:1 square canvas, with the current revised set exported uniformly at 1254 × 1254 px as transparent RGBA PNGs. This 12 November update replaces the former 2:3 / 1024 × 1536 production format. The usual paper-free composition combines a detailed e-commerce photograph of the product/material, a finished retail-style package and a complementary engraving. The documented packaging-free accessory exceptions remain valid. The engraving adds a different dimension rather than redrawing the photographed subject: for example cultivation architecture/light, terrain, sorting or trimming tools. Keep the rich antique copperplate/natural-history drawing technique; a botanical subject is not mandatory.

The category heading stays in the website layout; do not add a separate title chip or floating logo to these category cutouts. On concept packages, the CATEGORY NAME is the largest and clearest label; a strain or product name is an optional smaller subtitle. Keep quantity (grams for flowers/hash, millilitres for oils), CBD percentage and the reference price together in one discreet information row, using the same font size, weight, colour and baseline for all three values. No prominent price, retail sticker, price badge or separate price panel. Redistribute the printed content vertically after removing the wordmark: move the smaller product/strain subtitle, separator and information row slightly lower, leaving a comfortable short gap above the product window rather than an empty former-logo slot. Judge the entire package balance; preserve the category title hierarchy, applicable product/packaging groups and complementary engraving. This 21 October clarification supersedes the earlier price-removal default. Do not use the full uWeed wordmark on these category concept packages. Use the approved small original smile-u/favicon in the package colour family at the top-right of the printable package face, just below the top edge or pouch zip area; it must be printed on the package, not float outside it. At the historical 1024 × 1536 px reference size, use approximately 65 px visible mark width on a roughly 600 px-wide pouch. Keep the supplied mark geometry; do not invent an emoji, add a surrounding badge or use the full wordmark. This package-only rule does not alter logos on blog headers, city images or other placements. Oils use the K06 amber dropper bottle plus tactile embossed ivory carton. Flowers use pouches; hash uses a pouch or a single round clear blister dome on a backing card, following the real Swiss Premium Pollen format. Use authentic packaging when representing a named catalogue SKU; concept packaging must not be presented as an actual private-label listing.

Category transparency: apart from the relevant category components (packaging where applicable, photographed material and engraved subject), the canvas must be completely transparent. Remove background haze, colour gradients, glow, vignettes, floor surfaces and unwanted shadows outside the subjects. Preserve clean natural edges and transparent air between engraved leaves. Check the exported RGBA PNG alpha channel, not only the rendered preview; a decorative background must not be mistaken for transparency.

Engraving colour rule, clarified 21 October 2026: use a single monochrome navy ink `dark-blue`, as in the CBD Blüten specimen. Do not add coloured washes, gold resin, coloured powder, gradients or multicoloured fills inside the engraved subject. Rich contours, fine hatching, tonal depth and detailed natural-history/copperplate rendering remain required. Colour richness comes from photography and packaging. This applies to new illustration work; it does not authorise automatic replacement of older accepted artwork.

Small Buds revision: replace the fine sieve, which suggests pollen/hash production, with a clearly readable engraved size-comparison ruler or scale labelled Standard / Small Buds / Trim. Its pointer marks Small Buds. These functional comparison labels are an explicitly requested exception to the usual text-free engraving rule. Keep the photographic material as small intact flower buds, clearly different from whole standard buds and leaf-dominant trim.

**Example:** `assets/Imagery examples/category-proposal-historical.png` (group *Imagery examples*)

*Historical category proposal recovered from the earlier guide. Its landscape format and unfinished branding policy are superseded by the current square export, packaging and category-specific rules above.*

Do not apply effects piece counts, one-human-photo rules or medical imagery by default to category assets. Distinguish whole flowers, small intact buds and leaf-dominant trim accurately. Product and category visuals must not become interchangeable generic hemp-leaf artwork.

## Images inside articles

Decided 26 November 2026. A picture inside an article sits in the text column (at most `measure` wide) and takes one of three shapes; no other shape is used inside an article, and no 16:9.

- **Explanatory graphic, 3:2:** full column width on every screen (*Explanatory graphics inside articles*, below).
- **Portrait image, 4:5:** full width on a phone; at most 480 px wide on a desktop, centred, so it is never taller than the screen.
- **Spot image, 1:1:** full width on a phone; 320 to 400 px wide on a desktop, between paragraphs.

Each shape has one master (*Formats at a glance*); the page shows it at the width the placement needs, from the copies the site makes. How portrait and spot images look, and whether they carry a mark or text, is not set yet: it is settled on approved examples (*Visual identity*, opening note and section 4). Until then *Visual identity* sections 1, 3, 5 and 6 apply.

## Explanatory graphics inside articles

Inline explanatory illustrations: current direction, agreed 20 October 2026. Use the centred composition selected as layout 2, with a title above the explanatory content and an optional subtitle only when it adds information. Choose a sequence, comparison, annotation, Q&A or takeaway according to what the reader needs to understand. The relationship controls the content arrangement; the light collage identity remains consistent. Keep the agreed 3:2 canvas and distribute content naturally across its width and height, with balanced margins and no large accidental empty lower area. Keep drawings modest in scale; improve spacing rather than enlarging every element.

### Titles and containers

Titles use a wide, shallow tactile torn-paper piece, Poppins uppercase with positive tracking, and a compact hierarchy that leaves the explanation prominent. Retained title options are gently tilted white paper with a restrained colour under-edge, or dark brand-colour paper with white lettering. A subtitle may appear directly on white or on its own smaller torn-paper piece. Paper treatments and line breaks follow the content and available space.

Title and subtitle use ONE brand-colour family per illustration. Select blue, green or pink according to the visual; blue is not mandatory. Use the dark family tone for the main paper with white lettering and its light tone for subtitle paper with dark family lettering. Blue: `dark-blue` / `light-blue`; green: `dark-green` / `light-green`; pink: `dark-pink` / `light-pink`. White title paper can carry dark family lettering and a same-family colour under-edge. Do not mix a blue title with a green subtitle. For the flower comparison, replace mint subtitle paper with light blue `light-blue`.

Derive typography from the site scale in this system (Typography, the H3 and Lead styles), rather than choosing sizes independently for each image. Inline title maps to the H3 visual token: Poppins 700, 21 px at 375 px mobile viewport to 30 px at 1280 px desktop viewport, line height 1.20; uppercase uses +0.04em tracking. The optional subtitle maps to Lead: DM Sans 400, 17–19 px, line height 1.55, normal tracking. This is a component-size mapping, not an instruction to change the article’s semantic heading level.

Three illustration-paper treatments remain available, chosen to suit the content rather than enforced as a fixed formula: (1) open engraved subjects directly on white; (2) open subjects with restrained partial colour-paper accents, where subjects can extend freely beyond paper edges; (3) related subjects sharing one continuous torn-paper shape. Individual accent papers do not need to enclose each drawing or repeat a uniform card shape. Keep the collage light; do not import the effects header’s 6–7-piece count or two-photo requirement.

**Example:** `assets/Imagery examples/inline-rounded-title-historical.png` (group *Imagery examples*)

*Historical rounded-title exploration. Current inline titles follow the 20 October 2026 torn-paper system above; this board does not define current title shapes, signature or layout.*

**Example:** `assets/Imagery examples/inline-container-historical.png` (group *Imagery examples*)

*Historical container exploration. Use it only as a reference for information relationships; the current light collage treatments and centred layout take precedence over card shapes.*

Use original Tabler icons on a 24 px grid, with 2 px strokes and rounded ends. Check Tabler for a missing symbol before proposing a custom addition. Use editorial drawings for detailed subjects. Secondary marks may vary in brand colour but remain subordinate; they never replace the original primary logo.

The inline signature is the supplied original smile-u favicon/mark, small and subordinate in the bottom-right corner. Position the VISIBLE artwork, not its transparent file padding. Use a right and bottom edge inset of 1% of canvas width, or 25% of the visible mark height if that is larger. At 1536 × 1024 px this is approximately 16 px; at 1800 × 1200 px it is 18 px. Keep the mark’s existing small size and authentic proportions. Use the existing approved asset in the selected family; do not redraw it or use the full wordmark. This is an inline-only rule and does not alter header, city or campaign logo geometry.

Optional editorial notes belong at bottom-left, in brand dark grey `dark-gray` rather than the title’s blue, green or pink. Keep them visually subordinate, in DM Sans regular at the existing readable note size. Match their visible lower/left inset to the footer margin, preserve at least the established readable text minimum at displayed size, and add no note unless it serves the explanation. Reserve the footer while composing the content. Do not allow artwork or labels to collide with the corner signature or note.

The earlier inline boards below are historical functional-layout references; their title containers, logo size/location and proportions are superseded by the current written rules. This editorial exception does not alter site UI tokens or header/city logo rules.

Engraving quality: use the originally retained botanical/natural-history copperplate technique—fine drawn contours, visible parallel and cross-hatching, delicate tonal modelling and restrained colour washes over linework. Botanical describes the drawing technique, not a required subject. Avoid photorealistic packshot rendering, glossy or volumetric 3D forms, thick cartoon outlines, saturated plastic-looking colour and exaggerated orange pistils. Fine detail is welcome when it clarifies the subject. Do not confuse detailed 3D-looking rendering with engraved illustration.

## Explanatory layout library

| Family | Retained arrangements | Mobile approach |
| --- | --- | --- |
| Sequence | 1 horizontal capsules; 5 illustrated route | Stack the steps as needed. |
| Comparison | 1 paired angled cards; 5 circular panels | Stack panels if side-by-side labels become too small. |
| Annotated | 1 open callouts; 2 numbered key; 3 detail zooms | Use a numbered key below the illustration when callouts crowd. |
| Q\\&A | 1 speech bubbles; 3 open editorial columns; 4 illustrated answer | Read question → illustration → answer clearly. |
| Takeaway | 2 typographic; 3 illustrated; 4B tilted rounded panel on navy | Retain the arrangement when possible; wrap and increase height. |

These retained options form a flexible library, not a requirement to use every layout in every article. Numbers refer to the historical exploration boards. The following examples show selected arrangements, with their original sample content. Their wording is not a scientific or product brief.

Keep content truthful and editorially checked. A process arrow must describe a real relationship; an illustrated route is not automatically a cycle. Do not imply equivalence, medical effects or precise mechanisms merely because a diagram layout makes them easy to draw.

## Sequence examples

Use horizontal capsules for a short step sequence. Use the illustrated route when each main stage benefits from a recognisable editorial drawing, including the middle processing stage. In the retained route, the dotted path curves above the first connection and below the second; keep it clear of labels and drawings. Show a start and end rather than a repeating cycle unless the content actually is cyclical.

**Example:** `assets/Imagery examples/inline-sequence-1-capsules.png` (group *Imagery examples*)

*Sequence 1: historical horizontal-capsule sample. Current inline paper titles, centred composition and small bottom-right favicon take precedence.*

**Example:** `assets/Imagery examples/inline-sequence-5-illustrated-route.png` (group *Imagery examples*)

*Sequence 5: illustrated route. Every main step is illustrated; the path must not cross labels.*

## Comparison examples

Use paired angled cards for a focused comparison and circular panels for a compact set of distinct alternatives. Keep labels and evidence comparable across items. Whole flowers, small buds and trim must remain materially distinguishable, not three decorative copies of the same bud.

**Example:** `assets/Imagery examples/inline-comparison-1-angled-cards.png` (group *Imagery examples*)

*Comparison 1: paired angled cards. Shape and colour may vary; retain readable information hierarchy.*

**Example:** `assets/Imagery examples/inline-comparison-5-circular-panels.png` (group *Imagery examples*)

*Comparison 5: circular panels. Stack or reflow for mobile when labels cannot remain readable.*

## Annotated illustration examples

Use open callouts when labels have enough room. Use a numbered key when surrounding labels become crowded, especially on mobile. Detail zooms are also retained when a small feature needs explanation. Every callout must point to the correct feature, with a clear reading order.

**Example:** `assets/Imagery examples/inline-annotated-1-open-callouts.png` (group *Imagery examples*)

*Annotated 1: open callouts. Preserve space around the central drawing and reserve the current logo area.*

**Example:** `assets/Imagery examples/inline-annotated-2-numbered-key.png` (group *Imagery examples*)

*Annotated 2: numbered key. Annotated 3, detail zooms, remains an equally valid retained arrangement.*

## Question and answer examples

Keep the question and its answer visually connected. Retained arrangements are speech bubbles, open editorial columns and illustrated answers. The mobile reading order is question, illustration where useful, then answer. An illustration should explain the answer rather than decorate a disconnected text block.

**Example:** `assets/Imagery examples/inline-qa-1-speech-bubbles.png` (group *Imagery examples*)

*Q&A 1: historical speech-bubble arrangement. Apply the current inline title and small bottom-right favicon rules.*

**Example:** `assets/Imagery examples/inline-qa-4-illustrated-answer.png` (group *Imagery examples*)

*Q&A 4: illustrated answer. Q&A 3, open editorial columns, is also retained.*

## Key takeaway examples

Use a typographic statement for a clear central conclusion, an illustrated takeaway when the drawing adds meaning, or the retained 4B tilted rounded panel on navy. Keep the takeaway concise and preserve any necessary qualification. On mobile, wrap the wording and increase height rather than shrinking it into unreadable text.

**Example:** `assets/Imagery examples/inline-takeaway-2-typographic.png` (group *Imagery examples*)

*Takeaway 2: typographic statement. Keep titles and supporting prose distinct.*

**Example:** `assets/Imagery examples/inline-takeaway-3-illustrated.png` (group *Imagery examples*)

*Takeaway 3: illustrated takeaway. The 4B tilted rounded panel on navy is also retained.*

## Inline readability and responsive behaviour

Use 3:2 for the current inline illustration system, for example an 1800 × 1200 px production source; 1536 × 1024 px studies are review assets. Preserve the full composition with responsive width and automatic height; do not crop diagrams. Prepare a separate mobile composition when required, keeping the same 3:2 ratio and visual identity.

Measure text at its actual displayed size, not at the export resolution. Apply the site’s fluid H3 and Lead tokens to the inline title and optional subtitle: title 21–30 px and subtitle 17–19 px between 375 and 1280 px viewports; body remains at least 16 px, short labels 14 px and metadata 13 px. Raster images do not inherit CSS clamp() or reflow automatically. Calculate artwork font size = target displayed font size × source canvas width / displayed image width, then check the real article width. If one bitmap cannot maintain both desktop and mobile targets, supply a separately arranged mobile asset; never merely shrink the desktop artwork until lettering becomes unreadable. Wrap the title and adjust paper height when necessary. Prefer editable text over AI-rendered lettering for exact production typography.

Sequences stack vertically; comparisons stack panels where necessary; annotated diagrams move labels to a numbered key; Q&A preserves question-to-answer reading order; takeaways wrap and grow. Keep the same visual language when the arrangement changes.

**Example:** `assets/Imagery examples/inline-desktop-mobile-reflow.png` (group *Imagery examples*)

*Historical desktop/mobile study: open callouts become a numbered key. The study demonstrates reflow; apply the current signature in production.*

The earlier site inspection found an approximately 723 px desktop article column, with about 952 px at the largest CSS layout and 336–406 px available on 360–430 px phone screens. These describe that inspected template, not a current site-wide audit. Dedicated mobile artwork requires template support; no template or site settings are changed by this guide.

Keep essential information in the article text as well as in the image. Supply accurate descriptive alt text in the page language. Do not make packaging microtext or tiny embedded labels carry essential information.

## Production files and title only localisation

| Asset | Master / delivery |
| --- | --- |
| Blog and city collage | 3:2, 1800 × 1200 px production source; full-colour sRGB PNG. |
| Current effects review archive | 20 images at 1536 × 1024 px, plus the recovered Sport S3 panel at 697 × 480 px. These are review assets, not production-resolution masters. |
| Campaign email | Shared 1800 × 1200 master; 1200 × 800 export for the referenced template, unless the campaign placement specifies otherwise. |
| Inline explanatory graphic | 3:2, for example 1800 × 1200 px; full-colour sRGB PNG, with a separate mobile composition when needed. |
| Standalone photograph | High-quality JPEG; PNG where transparency is required. |
| Category / brand / product | Placement-specific format; do not assume the blog ratio. |

### Exact language copies

Use German as the selected visual master. French and English copies change only the article title on its existing white collage paper. Preserve photographs, people, objects, engraving, colours, seams, logo, canvas, crop and paper shape. Adjust wording and meaningful line breaks inside the same title area. Do not silently repair older imagery or translate labels inside engraving or photographed packaging during this task. This is the current header-copy rule. Inline explanatory graphics have a separate localisation scope: translate the briefed titles, labels and explanatory prose, then apply the relevant mobile and language reflow rules.

Use Swiss German spelling, French accents including capitals and British English. A title that is already identical, such as CBD & SPORT or CBD & PARKINSON, needs an identical copy rather than a needless visual edit. Record each language file against its German source.

### Editable source and derivatives

For future production, retain separate text, original logo, photography, paper and engraving layers where available. The current generated review images are flattened rasters; do not describe them as layered design sources or separate vector engravings. Enlarging a small study does not create a genuine production master.

Keep the uploaded original. Derive responsive sizes and WebP from that original rather than another compressed copy. The existing site script was expected to create responsive/WebP variants; this guide does not audit or change it. Keep title and logo in responsive 3:2 frames without fixed-height or square crops that cut them off.

## Filenames alt text and archive

Use article-first, descriptive filenames in the page language: article topic plus one visible distinguishing detail. Use 3–6 words and fewer than 60 characters, lowercase ASCII and hyphens. Omit uweed and language suffixes unless needed to avoid a genuine filename collision. Transliterate accents in filenames.

Examples: cbd-schlafen-schlafmaske.png, cbd-sommeil-masque-nuit.png and cbd-sleep-eye-mask.png. Track review/version status separately from the delivery filename. Preserve the actual file extension: PNG originals remain .png; use .webp or .avif only after a real format conversion.

The filename identifies the article topic and actual image, not a site-wide keyword target. Do not append cbd-shop to unrelated effects imagery. The Topical Map tab is the image-metadata register: column P is Featured Image Name, column Q is Image Alt Text, and column B remains the page identifier. Match entries by article and language.

Alt text describes visible subjects and their context in the page language, without implying unseen product use, medical outcomes or geographic details. Use 8–15 words, typically 80–120 characters, with natural topic wording rather than repeated keywords. Essential information belongs in surrounding text. Decorative images can use empty alt text when appropriate.

Archive location: New Style Collage Oct 26 / Blog / Effects Network / DE, FR and EN. Cities remain in their existing separate folder. The imagery examples are in this system, asset group *Imagery examples*; the superseded Blog Featured batches and separate blog References folder have been removed.

Generate one article at a time by default unless a batch is requested. Present concepts in words first when requested. After review, record agreed takeaways here and distinguish shared rules from article-specific exceptions. Save approved images under Blog / [Network] / [Language]; do not replace an approved image with a rejected trial.

Archive verified 18 October 2026: 21 DE + 21 FR + 21 EN PNGs (63 total). FR/EN change only the title lettering; Sport and Parkinson are exact copies. Existing engraving labels remain unchanged.

| Folder | Location |
| --- | --- |
| German effects | <https://drive.google.com/drive/folders/1iwLKouEqOQYyecTrEQet6JCokw-TGaLK> |
| French effects | <https://drive.google.com/drive/folders/1UbfAAv7vCP5j0UeFz4PMM0y9ZviQC1U3> |
| English effects | <https://drive.google.com/drive/folders/1ADdKONGNwtUfXk8YRgBSUIuze_V7-f3t> |
| Cities | <https://drive.google.com/drive/folders/1W3hjpr6gyxo5N4_s2Zdb_JPmnAgRjLJy> |

## Briefing future AI

Attach this section with the relevant approved visual example, the exact original logo colourway and the article or placement brief. Give the AI an explicit family and mode: new composition, revision of a specified element, or title-only localisation. Do not ask it to infer all three from a subject name.

### Required brief fields

  - Placement and family; article URL or identifier; language; exact visible title; actual article question and intended meaning.
  - Approved source image or reference; required photo subjects and engraving concept; palette; standard structure or named exception.
  - Canvas and output format; authentic logo file; elements that must remain fixed; exact scope of the requested change.
  - Filename and destination; review status; any unresolved placement decision.

### Effects composition prompt

Create a premium uWeed effects collage in the supplied reference style. Use 6–7 physical pieces total: two complete contextual photographic crops, one coherent detailed antique engraving around 20%, one white title paper and two or three plain brand-colour papers including the small logo area. Only the main photo may show people; no human drawing when a photo has people. The secondary photo has a distinct context. The engraving adds a different, understandable concept and contains no text unless expressly authorised. Allow only a short natural photo join, no longer than half either adjoining side, without a continuous separator. No detached photo slivers. Use the supplied exact logo at the fixed top-right geometry and the exact title bottom-left. Apply only the named article exception, if any.

### Title localisation prompt

Use the supplied German image as the immutable visual master. Replace only the article-title lettering inside the existing white paper with the supplied French or English title. Preserve all pixels outside the title area, including photographs, engraving, text within photographs/engravings, colours, seams, logo, canvas and crop. Preserve the paper outline and angle. Fit natural line breaks and correct accents; do not redesign.

### Inline explanation prompt

Create one clear inline explanation in the current centred 3:2 light-collage system. Use a wide shallow torn-paper Poppins title, optional DM Sans subtitle, same-family dark/light title papers, modest detailed copperplate engravings and the supplied small original bottom-right smile-u favicon. Choose open subjects, partial paper accents or a shared paper shape according to the content. Distribute content naturally over the canvas. Derive displayed typography from the site H3 and Lead tokens; supply a mobile reflow when a single raster cannot meet the text sizes. Keep every fact, arrow and callout grounded in the supplied content.

## Review checklist and boundaries

  - Meaning: the visual communicates the actual article question and does not require a separate explanation to justify unrelated imagery.
  - Structure: the correct family rules and named exceptions are applied. Effects standard has 6–7 pieces, two photos, one engraving and one human-bearing photo at most.
  - Subjects: photo contexts differ; engraving does not duplicate photographed objects; no stray photo fragments; no unrequested engraving text.
  - Finish: rich, dimensional copperplate drawing, credible photography, clear natural torn seams and readable hierarchy.
  - Branding: original logo artwork, approved matching colourway, fixed top-right visible bounds, small integrated logo area and white bottom-left title where required.
  - Language: exact title, correct spelling and accents, meaningful line breaks, no text or imagery changes outside the authorised title area.
  - Delivery: correct native dimensions and honest master/review status; article-first filename; language folder; source mapping and accessible files.
  - Display: check the real header/card/mobile or email context. Keep titles and logos inside uncropped frames; preserve entire explanatory diagrams.

At the earlier visual scale check, short titles, logos and subjects remained clear at 600 px email and 360 px mobile widths; 240 px was the practical minimum for the complete treatment. At 160 px the logo was very small, and at 120 px the subject alone remained useful. These were uniform study scalings, not current live-site or inbox tests. Fine engraving may read as texture at small sizes.

### Decisions still required

Still open: the campaign email banner, to be settled from approved examples. Two versions disagree today: *Campaign email banners* above puts the title on white torn paper and the logo in the picture, while the `monthly-newsletter` skill keeps the banner free of text and sets the headline in Klaviyo. Follow neither as final until an example is approved; *Visual identity* section 4 then records the result. Link previews. Facebook, LinkedIn and Telegram show a shared uweed.ch page at 1.91:1 (1200 × 630 px) from its og:image, so a 3:2 blog picture loses 129 px at the top and the bottom and can lose part of the logo top-right or the title bottom-left. Decided on 26 November 2026 to leave it as it is for now (the platforms crop; cosmetic only) and not to change the artwork. When it is taken up, the preferred fix is for the site to make a 1200 × 630 copy of the featured image with the whole picture fitted and `white` bands at the sides, used only in the og:image tag, so the site and the pictures stay unchanged; the look of social posts (*Social formats*); review of the completed category image set; editable production-source workflow and any necessary blog rebuilds at 1800 × 1200; implementation of dedicated mobile inline artwork. The small top-right favicon, inline price typography and transparent category composition were approved on 21 October 2026; the torn-paper base was retired for category visuals on 12 November 2026. The current seven flower category assets are saved under New Style Collage Oct 26 / Categories: https://drive.google.com/drive/folders/1BLJnBVb9BVik22xmiTNpJGWSbs4H_psi. This set includes the main category, Indoor, Outdoor, Greenhouse, Small Buds, Trim, and combined Moonrocks & Ice Rocks. Earlier flower studies are historical references kept in the separate Archive – nicht veröffentlichen folder, with archive-v1- or archive-r2- filename prefixes. They are excluded from the current-image list and must not be published. Keep the main CBD Blüten subtitle/data block lower as requested; do not publish assets automatically.

## Remaining blog imagery outside effects

The earlier topical-map coverage review identified 27 remaining German blog topics outside the effects set: 23 published and 4 planned. Their language siblings total 77 active pages: DE 27, FR 26 and EN 24. This is the recorded topical-map inventory, not an instruction to generate new pictures in this task. No new concepts or images are commissioned by this list. Here, missing means that no approved image in the new style was verified in that batch; it does not mean the live article has no featured image. Planned pages need an approved brief before choosing an image concept.

| Network | Article / DE page | DE | FR | EN |
| --- | --- | --- | --- | --- |
| SCIENCE | Cannabidiol (CBD) | Published | Published | Published |
| CBG | Cannabigérol (CBG) | Published | Published | Published |
| CBN | Cannabinol (CBN) | Published | Published | Published |
| SCIENCE | Tetrahydrocannabinol (THC) | Planned | Planned | Planned |
| SCIENCE | CBD vs. THC | Published | Published | Published |
| LEGAL | CBD Legal | Published | Published | Published |
| LEGAL | CBD Driving | Published | Published | Published |
| LEGAL | THC Body | Published | Published | Published |
| OILS | CBD Oil Strength | Published | Published | Retired |
| OILS | CBD Extraction | Published | Published | Published |
| OILS | CBD Pharmacy | Published | Published | Not mapped |
| FLOWERS | Indoor vs Outdoor | Published | Published | Published |
| OILS | Best CBD Oils | Published | Retired | Retired |
| OILS | CBD Oil Usage | Published | Published | Published |
| OILS | CBD Dosage | Published | Published | Published |
| PETS | CBD Dosage Animals | Published | Published | Published |
| VAPE | Puff Recycling | Published | Published | Published |
| ACCESSORIES | How to roll a joint | Published | Published | Published |
| FLOWERS | CBD Storage | Published | Published | Published |
| SCIENCE | CBD Study | Published | Published | Published |
| SCIENCE | Entourage Effect | Planned | Planned | Planned |
| HEMP | Hemp | Published | Published | Published |
| CONCENTRATES | Kief | Published | Published | Published |
| SCIENCE | Terpenes | Published | Published | Published |
| FLOWERS | Sativa vs Indica | Published | Published | Published |
| LEGAL | Swiss Cannabis | Planned | Planned | Planned |
| SCIENCE | 420 | Planned | Planned | Planned |

Recorded exclusions from the merged blog guide: CBD Oil Legal; Types of CBD; CBD Carrier Oils; CBD Oil vs CBD Flowers; CBD Oil vs Capsules; CBD Oil Storage; CBD Not Working; Hemp oil vs CBD oil vs Cannabis oil. These German topics were marked retired in the recorded map review. CBD Oil Benefits / CBD Öl Wirkung was explicitly excluded by the user, even though its map row still said Published. The blog hub (All Blog Articles, UTILITY) is a listing page and is excluded from the article counts; brief it separately if a header is needed. Do not turn excluded, retired or already covered pages into a fresh queue automatically. Check the current topical map and editorial instructions before starting remaining articles.

## Reference sources and precedence

The visual examples in this document are existing design studies and selected effects images. They show the established materials and layouts; they are not new concept generations. Captions identify proposals and legacy details. Current written rules in the relevant section take precedence over visible historical inconsistencies.

Advancing with “next” retained the selected version for the review sequence. The archive preserves those selections. It does not certify every older raster against rules introduced later; for example, the Wirkung torso and the small figure inside Kinder’s storybook predate the later human-engraving restriction. Do not repair such legacy details while performing a title-only language copy.

  - Explanatory Graphics Guide, 9 October 2026: historical functional layout pack. The 20 October 2026 inline decisions supersede its rounded title blocks, large wordmark, flexible ratio and older surface treatments. Retain useful explanatory relationships and the original fine engraved drawing technique.
  - Featured Image Rules, updated through 14 October 2026: shared 3:2 family, city and campaign treatments, fixed title/logo, production guidance and category proposal.
  - Fixed logo and city engraving clarifications, 13 October 2026: historical collage-era guidance. For current city images, the 15–16 November continuous-scene direction and small white bottom-right signature in City imagery supersede the older complementary-subject and fixed top-right city-logo rules. Other image families retain their applicable guidance.
  - Effects review decisions, 15–17 October 2026: contextual two-photo structure, piece count, human limits, no duplicate subjects, engraving finish, natural partial joins, palette and article exceptions.
  - Localisation clarification, 18 October 2026: retain selected German artwork and change only the title paper’s wording for French and English. This does not authorise imagery cleanup or translation of engraving labels.

Topical map: <https://docs.google.com/spreadsheets/d/1Odixd6kcvJWj8-1HP7wBm3znsURyNU0EOUeRRIwJY-s/edit>

The blog collage rules, scoped article decisions, saved-set notes and remaining-article inventory are consolidated in this guide. This section is the single maintained source for future imagery work.

## Category educational examples

These historical version-4 applications show category education rather than category hero policy. Retain the meaningful differences between whole flowers, small intact buds and leaf-dominant trim, together with genuine engraved subject drawings. For new inline production, the 20 October light-collage title, optional subtitle, same-family papers and small bottom-right favicon rules supersede these rounded information bands and footer signatures. These examples do not finalise category hero policy.

**Example:** `assets/Imagery examples/category-education-cultivation.png` (group *Imagery examples*)

*Category education: indoor, greenhouse and outdoor cultivation. Choose a recognisable subject illustration rather than a generic repeated leaf.*

**Example:** `assets/Imagery examples/category-education-flowers-buds-trim.png` (group *Imagery examples*)

*Category education: whole flowers, small buds and trim. The actual flower/material drawings are central to the explanation.*

**Example:** `assets/Imagery examples/category-education-oil-ingredients.png` (group *Imagery examples*)

*Category education: CBD ingredient, carrier oil and product information. Historical illustrative sample; verify product facts for the actual brief.*

## Additional retained arrangements

These complete the retained inline layout library shown earlier. The sample text is not a product or scientific content brief. Apply current typography, logo and readability rules in new production.

**Example:** `assets/Imagery examples/inline-annotated-3-detail-zooms.png` (group *Imagery examples*)

*Annotated 3: detail zooms. Use a magnified feature when it adds information that the full view cannot show clearly.*

**Example:** `assets/Imagery examples/inline-qa-3-editorial-columns.png` (group *Imagery examples*)

*Q&A 3: open editorial columns. Preserve an obvious question-to-answer reading order.*

**Example:** `assets/Imagery examples/inline-takeaway-4b-navy-panel.png` (group *Imagery examples*)

*Takeaway 4B: tilted rounded panel on navy. Keep the tilt gentle and the statement readable.*
