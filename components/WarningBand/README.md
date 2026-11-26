Use `WarningBand` for the legal warning that advertising for smoking products and vapes must carry: a full-width band at the bottom of the banner, 10% of its area, a thick black frame and black text on white, like the warning on a cigarette pack.

```html
<div class="hero" style="position:relative">
  <img src="…" alt="…">
  <div class="uw-warning-band" role="note" lang="de">
    <div class="uw-warning-band__field">
      <p class="uw-warning-band__text">Das Rauchen dieses Produkts schädigt Ihre Gesundheit</p>
    </div>
  </div>
</div>
```

**When it is required** (compliance Part 6, D21; Art. 21 TabPG, Art. 15 TabPV):

- **Email campaign banners** that show or promote a smoking product or a vape.
- **Hero banners** (homepage, category, landing pages) that advertise a specific promotion, product or brand of these products.
- **Social posts, paid ads and Telegram** that show or promote them.

**Never** on product pages, product tiles or category listings: the product is presented there, not advertised, and the pack in the photo carries its own warning. Nor on a hero that only names a category for navigation. Never a hand-made band: every banner uses this one.

**The rules it builds in**

- **Size.** At least 10% of the banner's area (Art. 15(2)(a) TabPV). Full width at the bottom, so its height is 10% of the banner's height; the frame counts in the 10%.
- **Look.** Thick black frame (a tenth of the band's height), white field, black Neue Helvetica 75 Bold (or Helvetica Bold), centred, sentence case. Helvetica is the one exception to the type tokens, because it is the legal pack-warning look. Black on white is 21:1.
- **Text.** One line where it fits; two on narrow banners (phone heroes). The text scales with the band, never below legible: the law asks for a "leicht lesbare Schrift".
- **Language.** The language of the publication, set on the band with `lang`.

**The text, by product shown** (where several are shown, one `uw-warning-band__text` each):

| Product shown | DE | FR | EN |
| --- | --- | --- | --- |
| Flowers, hash, pollen, moonrock, joints, pre-rolls, tobacco-free CBD cigarettes | Das Rauchen dieses Produkts schädigt Ihre Gesundheit | Fumer ce produit nuit à votre santé | Smoking this product damages your health |
| CBD cigarettes with tobacco, rolling tobacco | Rauchen ist tödlich – hören Sie jetzt auf | Fumer tue – Arrêtez maintenant | Smoking kills – quit now |
| Vapes and e-liquids without nicotine | Dieses Produkt kann Ihre Gesundheit schädigen | Ce produit peut nuire à votre santé | This product can damage your health |
| Vapes and e-liquids with nicotine | Dieses Produkt kann Ihre Gesundheit schädigen und macht stark abhängig | Ce produit peut nuire à votre santé et crée une forte dépendance | This product can damage your health and is highly addictive |

The texts are copied word for word from compliance Part 6; change them there first, never here alone.

**Where it is drawn**

- **Homepage heroes:** the site draws the band over the picture with this markup and the `uw-warning-band` classes. The hero picture itself stays clean (*Imagery guide*, *Formats at a glance*).
- **Email banners:** email clients do not run this CSS, so the band is part of the banner image, drawn to the sizes below.

| Format | Size | Band | Frame | Text |
| --- | --- | --- | --- | --- |
| Homepage hero, desktop 21:9 | 2520 × 1080 px | 108 px | 11 px | about 37 px, one line |
| Homepage hero, phone 3:4 | 1320 × 1760 px | 176 px | 18 px | about 55 px, up to two lines |
| Campaign email banner 3:2 | 1800 × 1200 px (export 1200 × 800) | 120 px (80) | 12 px (8) | about 41 px (27), one line |

- Never cover the band with anything, never put the warning in the picture's own artwork instead, never shrink it below 10%, never change its colours to match a campaign.
- `role="note"` so a screen reader announces it as a note; the text is real text, never an image, on the site.
