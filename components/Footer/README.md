Use `Footer` at the bottom of every page. It carries `.on-dark`, so links, buttons and focus rings inside it switch to their dark-surface treatment automatically. Redesigned 16 November 2026, mobile first.

```jsx
<Footer
  contact={{ heading: "Kontakt", items: [
    { icon: "mail", label: "hello@uweed.ch", href: "mailto:hello@uweed.ch" },
    { icon: "phone", label: "+41 44 505 76 66", href: "tel:+41445057666" },
    { icon: "message-circle", label: "Live-Chat öffnen", onClick: openChat, haspopup: "dialog" },
    { icon: "clock", label: "Mo bis Fr, 9:00 bis 17:00" },
    { icon: "link", label: "Zur Kontaktseite", href: "/kontakt/" },
  ] }}
  columns={[
    { heading: "Online CBD Shop", links: [{ label: "CBD Öl", href: "/cbd-shop/cbd-oel/" }, …, { label: "Alle Marken", href: "/marken/" }] },
    { heading: "CBD Wissen", links: […] },
    { heading: "Service & Hilfe", links: […] },
  ]}
  social={{ links: [{ network: "instagram", label: "uWeed auf Instagram", href: "…" }, …] }}
  reviews={{ content: <ReviewsBadge /> }}
  locale={{ controls: [
    { label: "Sprache", value: "Deutsch", flag: <FlagDE />, onClick: openLanguage },
    { label: "Währung", value: "CHF", flag: <FlagCH />, onClick: openCurrency },
  ] }}
  payments={{ methods: [{ label: "TWINT", src: "…" }, …] }}
  memberships={{ items: [{ label: "IG Hanf", href: "…", src: "…" }, { label: "MedCan", href: "…", src: "…" }] }}
  legalLinks={[{ label: "Impressum", href: "/impressum/" }, …, { label: "Cookie-Einstellungen", onClick: openCookies }]}
  disclaimer={<><b>Verkauf nur an Personen ab 18 Jahren.</b> Alle Produkte enthalten unter 1% THC …</>}
  copyright="© 2026 Digital Hive GmbH"
/>
```

**What it carries, in this order.** The order is the same at every width and in the DOM, so a screen reader and a keyboard meet the footer the way the eye does.

1. **Navigation** (`<nav aria-label="Fusszeile">`): `Kontakt` first, then three link columns: Online CBD Shop, CBD Wissen, Service & Hilfe.
2. **Trust and settings**: Folge uns, Bewertungen, Sprache und Währung, then Sicher bezahlen with Mitglied bei.
3. **Bottom**: the white logo with the legal links (Impressum, AGB, Datenschutzrichtlinie, Cookie-Richtlinie, Cookie-Einstellungen), the age and legal disclaimer, then the copyright with "Nach oben".

**One markup, CSS only.** Below `lg` (992px) everything stacks; each link column is a disclosure, its heading holding a button with `aria-expanded`, all closed at first. `Kontakt` is never collapsed: a closed accordion is not the first thing a visitor meets. From `lg` the four navigation blocks are four equal columns, the buttons are gone and every list is open; the trust band is four equal columns too. Never `<details>`, and never a second copy of the links for one of the widths.

- **Surface and text.** `dark-blue`, all text pure `white` (18.72:1). Green stays on the purchase path; pink never appears.
- **Rows are 44px on a phone** and 32px from `lg` with a fine pointer. The contact rows use the same size as the links: the contact page link is a plain row with the `link` icon, not a bold or underlined call to action. Only the live-chat row, which opens a window rather than a page, is underlined.
- **Icons** are 20px in contact rows, 24px in the 44px social circles, 16px in the pills and "Nach oben". Social icons are Tabler's `brand-*` line icons in white, never the networks' own colours. Social links carry `rel="nofollow noopener"`, as do membership links.
- **Language and currency** are the header's controls: a white pill with a round 20px flag, a small `medium-gray` label over the value, and a chevron. Both open the same picker as the header; the footer never has its own. They stay on one line from `lg`.
- **Payment marks and membership logos** are white one-colour files placed straight on the dark blue, with no chip or tile behind them. Each file is a 2:1 canvas (1200 × 600) with its margin built in, so all marks line up without per-logo tweaks: payment marks show 28px high, membership logos 44px high. Without a file, the name shows as white text in the same box. The files and their alt texts in DE, FR and EN are listed in the sheet *uWeed Footer Logos – DE, FR, EN*; the file names change per language (zahlung-, paiement-, payment-), the artwork does not. Payment methods today: TWINT, PostFinance Pay, Visa, Mastercard, Apple Pay, Google Pay, QR-Rechnung. Members: IG Hanf Schweiz and MedCan.
- **Reviews** take the REVIEWS.io *badge-modern* widget (an iframe) as `reviews.content`. Its shape: a black frame with rounded corners; inside, a white panel with five black stars, the average ("4.85 Durchschnittlich") and the count ("686 Bewertungen"); below it, a black strip with the REVIEWS.io mark. The slot is 160px wide and keeps 126px of height free, so nothing jumps when the widget loads late. The preview draws this shape with the figures of November 2026; in the shop the widget brings its own. If the widget is not on the page at all, leave the block out rather than showing an empty frame.
- **No address and no SEO paragraph.** The legal address is in the Impressum (UWG Art. 3 para. 1 lit. s); boilerplate text in a footer adds nothing to search.
- **Menus per language.** Columns are passed in per language; a link may exist in one language and not another.
- Focus is the `.on-dark` ring: 3px `white` at 2px offset.
