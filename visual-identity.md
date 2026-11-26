# Visual identity

How every uWeed picture should feel and what it must never show, whatever kind of visual it is and wherever it appears: website, email, social and, later, print. Decided on 26 November 2026; it replaces the visual sections that used to be in the `uweed-copy-rules` skill, which now covers words only.

Where to find the rest: the size and shape of every picture is in *Imagery guide*, *Formats at a glance*. How each kind of picture is made (collage, engraving, city images, category visuals, explanatory graphics) is in the *Imagery guide*. Colours are named by their tokens; the token is the value.

**New placements are settled on examples.** For a kind of picture that has no rule yet, make examples first, agree on one, then write its rule here and in the *Imagery guide* from the approved image. Until then, sections 1, 3, 5 and 6 already apply.

## 1. Mood

Every picture is **happy, modern, warm and premium**. Natural light, real materials, credible people and places. A uWeed picture feels like a good day: never like a pharmacy, never like a discount shop.

The mood is the same for every kind of visual below. It says how a picture feels, not how it is made.

## 2. Kinds of visuals

| Kind | What it is | Typical use |
| --- | --- | --- |
| Lifestyle photography | People and moments, with products in use or nearby | Homepage banners, campaigns, social |
| Product still life | The products as the subject: packshots, flat lays, details | Category visuals, product photographs, campaigns |
| Photo and engraving collage | uWeed's editorial look: photography combined with `dark-blue` engraving | Blog featured images, city images (*Imagery guide*) |
| Explanatory graphics | Diagrams, sequences and comparisons inside articles | Blog (*Imagery guide*) |

Choose the kind by purpose and placement. A campaign may use different kinds across its placements, as long as the mood and the colours hold.

## 3. Colour in pictures

One dominant colour family per picture, and at most one accent family. Never blue, green and pink as equals.

| Family | Tokens | Role in pictures |
| --- | --- | --- |
| Blue | `dark-blue`, `medium-blue`, `light-blue` | The brand, and the default |
| Green | `dark-green`, `medium-green`, `light-green` | Product-led moments, "CBD shop" |
| Pink | `dark-pink`, `medium-pink`, `light-pink` | Lifestyle and softer themes |
| Orange | `medium-orange`, `light-orange` | Accent only, never dominant |
| Red | `medium-red` | Never in pictures: alerts in the interface only |
| Grey | `dark-gray`, `medium-gray`, `light-gray` | Neutrals and surfaces |

These roles are for pictures. The website interface has its own, stricter colour roles (README, *Colour*), and each shop vertical keeps its own family (README, *Vertical colours*).

## 4. Logo and text in the picture

The logo is always the authentic asset (README, *Logo*), never redrawn, retyped or recoloured outside its approved colourways. Whether a picture carries text depends on its placement: either the text belongs to the picture, or the page or the email sets it on top and the picture stays clean.

| Placement | Logo or mark in the picture | Text in the picture |
| --- | --- | --- |
| Homepage banner | None | None: the page adds the title, subtitle and buttons (README, *Hero banner pictures*) |
| Blog featured image | Horizontal logo, top right | A short title naming the entities the article covers, on white torn paper, bottom left |
| City featured image | Small white logo, bottom right | "CBD in" (French: "CBD à") above the city name |
| Explanatory graphic | smile-u mark, bottom right | Title and labels |
| Category image | smile-u on the packaging | The category name on the packaging; the heading stays in the interface |
| Product photograph | None: the real packaging only | None |
| Email banner, social post and story, any new placement | Set from approved examples | Set from approved examples |

Positions, insets, type and sizes for each placement are in the *Imagery guide*. When a picture is generated, any title or logo it carries is added or checked against the real asset and the exact approved wording, never left to the generator.

## 5. People

People shown are clearly adults, and nothing in a picture appeals to minors (TabPG Art. 18; compliance Part 6). Generated people are fictional: never a real or recognisable person. A photograph of a real person is used only with that person's consent.

## 6. Never (visual hazards)

- The stoner look: a green leaf on black, Rasta colours, smoke clouds as the subject, 420 symbols, tie-dye, psychedelic patterns, aggressive neon.
- Decorative cannabis-leaf silhouettes, and black backgrounds with green accents.
- Hands rolling joints, unless the campaign is about joints.
- Medical cues: pills, droppers framed clinically, lab coats as the subject.
- Cartoonish or emoji-like styles.
- Copyrighted characters, brands and other protected work.
- The Eiffel Tower at night (a daytime silhouette only).
- Promotion pictures for smoking products and vapes without the legal warning band (compliance Part 6; the band is a design-system component).

## 7. Image prompt frame

For any generated picture: one paragraph in English, 120 to 200 words, in five blocks in this order, with no bullets inside the prompt. Each prompt stands on its own; it never refers to another.

1. **Kind and composition:** which kind of visual (section 2), the scene, and where the text-safe area sits if the placement sets text on top.
2. **Product handling:** "Use the attached product images as the central subject; do not generate substitute cannabis products." If none are attached: "Render the product types described below as restrained, realistic editorial still life, never cartoonish, never psychedelic." (Delete whichever does not apply.)
3. **Creative slot:** what is shown, and the moment or story that carries the theme.
4. **Palette and mood:** the dominant family and the accent with their hex values, and the mood from section 1.
5. **Standing rules:** text and logo only as the placement's row in section 4 allows, otherwise none; no branded packaging other than attached real packaging; fictional adults only; none of the visual hazards; the aspect ratio and size from *Formats at a glance*.

The *Imagery guide*, *Briefing future AI*, adds the family-specific prompts (effects collages, title localisation, inline explanations) on top of this frame.
