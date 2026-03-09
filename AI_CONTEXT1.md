# AI_CONTEXT.md — Soporte y Consultoría Marítima Website
**Last updated:** 2025 | **Status:** Ready for GitHub Pages deployment

---

## 🚀 Project Summary
One-page professional website for a Mexican nautical administrative services company.
**Company name:** Soporte y Consultoría Marítima
**Location:** Cancún, Quintana Roo, México
**Contact:** contacto@soportemaritimo.mx | +52 (998) 123 4567
**Domain:** soportemaritimo.mx (to be deployed)

---

## 📁 File Structure
```
/
└── index.html       ← ONLY file needed. 100% self-contained. No dependencies to install.
```

All CSS, JS, and images are embedded directly in `index.html`:
- Images are base64-encoded JPEGs (no external image URLs needed)
- Fonts loaded from Google Fonts CDN (fonts.googleapis.com)
- Icons loaded from Font Awesome CDN (cdnjs.cloudflare.com)
- NO Tailwind, NO frameworks, NO build step

---

## 🎨 Design System
**Color Palette:**
- `--navy: #0b1d3a` — Deep navy (main dark bg, footer, trust bar)
- `--navy2: #0d2548` — Slightly lighter navy
- `--teal-d: #0a4a5a` — Dark teal
- `--teal: #0e7090` — Main teal (accents, links, tab active)
- `--cyan: #0bbcd4` — Bright cyan (highlights, icons)
- `--cyan-lt: #22d3ee` — Light cyan (stats, decorative)
- `--gold: #f59e0b` — Gold (hero CTA button, hero h1 accent word)
- `--off: #f0f7f8` — Light background for sections
- `--hero-g` — Gradient: navy → teal → cyan (used on hero, exp section, card icons)

**Typography:**
- Headings: `Playfair Display` (serif, weights 600/700/800)
- Body: `Inter` (sans-serif, weights 300–700)

**Hero:**
- Background: real aerial boat photo (base64 embedded) with dark overlay gradient
- `linear-gradient(105deg, rgba(11,29,58,.92)→rgba(13,37,72,.85)→rgba(10,50,90,.70)→rgba(10,50,80,.55))`
- Right side card: zoomed boat photo (base64 embedded)

---

## 📄 Page Sections (in order)
1. **Navbar** — Fixed white bar, logo + nav links + "Contactar" CTA
2. **Hero** — Full screen, real boat photo bg, gold CTA button, hero card right with boat crop + "15+ años" badge
3. **Trust Bar** — Dark navy strip, 6 service highlights
4. **Servicios** (8 cards) — RPMN, Importación, Traducciones, CONANP, SEMAR, Inspección, Permisos, Navegación. Each has gradient image + icon overlay + link that activates matching tab below.
5. **Experiencia** — Dark gradient section, boat photo left, stats right (12+ años, 1200+ trámites, 98%, 15+ puertos)
6. **Trámites Detallados** — 8-tab system. TABS CRITICAL: panels use `display:none/block` (NOT CSS class only) to prevent stacking. showPanel() function manages this.
7. **Beneficios** — Dark navy bg, 4-col grid of 8 cards with teal bottom-bar hover effect. Last card says "Quintana Roo" (NOT "Cobertura Nacional")
8. **Proceso** — 4 steps with connecting line
9. **Contacto** — 2-col layout, contact info left, form right with JS validation
10. **Footer** — Dark navy, 4-col, social links

---

## ⚠️ Known Issues Fixed (do NOT revert)
- **Tabs stacking:** Each tab panel uses `p.style.display = 'none'` in JS AND CSS `.panel{display:none}`. Both needed.
- **Images:** All images are base64-embedded. No external URLs. Do NOT switch back to Unsplash URLs (they were unreliable).
- **No Tailwind:** Pure CSS only. No CDN for Tailwind. Removing it eliminated console warnings.
- **"Quintana Roo"** in beneficios card #8 (was "Cobertura Nacional" — family gave feedback to change it).
- **White text on dark backgrounds:** All dark sections (hero, exp-bg, ben-bg, tbar, footer) use white/rgba(255,255,255,x) text for legibility.

---

## 🔧 Key JavaScript Functions
```javascript
showPanel(id, btn)    // Switches tab panels — sets display:none on ALL, then display:block on selected
activateTab(id)       // Called from service card links — finds matching tab button and calls showPanel
submitForm()          // Validates form fields fn/fe/fs2/fm, shows toast on success
toggleMenu()          // Mobile nav open
closeMenu()           // Mobile nav close
```
**Form field IDs:** `fn` (nombre), `fe` (email), `ft` (telefono), `fs2` (tipo trámite), `fm` (mensaje)
**Note:** Select is `id="fs2"` (not "fs") to avoid conflicts.

---

## 🌐 SEO Included
- `<title>` with keywords
- `<meta description>` 
- `<meta keywords>` including "Quintana Roo, Cancún"
- `<link rel="canonical" href="https://soportemaritimo.mx/">`
- Open Graph tags (og:title, og:description, og:type, og:url)
- Schema.org JSON-LD (`ProfessionalService` type)
- All images have `alt` attributes
- Semantic HTML: `<nav>`, `<article>`, `<footer>`, `role` attributes, `aria-label`

---

## 🚀 Deployment Instructions

### Option A: GitHub Pages (free)
```bash
# 1. Create repo on github.com (public or private)
# 2. In terminal:
mkdir soporte-maritimo && cd soporte-maritimo
git init
git branch -M main
# Copy index.html into this folder, then:
git add index.html
git commit -m "feat: Soporte y Consultoría Marítima website v1.0"
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
# 3. GitHub → Settings → Pages → Deploy from branch → main → / (root) → Save
# URL will be: https://TU_USUARIO.github.io/TU_REPO/
```

### Option B: Custom Domain (soportemaritimo.mx)
```bash
# After GitHub Pages is live, add custom domain:
# GitHub → Settings → Pages → Custom domain → type: soportemaritimo.mx → Save
# Then in your domain registrar (GoDaddy/Namecheap/etc), add DNS records:
#   A record:     @ → 185.199.108.153
#   A record:     @ → 185.199.109.153
#   A record:     @ → 185.199.110.153
#   A record:     @ → 185.199.111.153
#   CNAME record: www → TU_USUARIO.github.io
# HTTPS is automatic via GitHub Pages (Let's Encrypt)
```

### Option C: Hostinger / cPanel
```
1. Login to Hostinger / cPanel
2. File Manager → public_html → Upload index.html
3. Done — site is live at your domain
```

### Option D: Netlify (drag & drop, free)
```
1. Go to netlify.com → Log in
2. Drag the index.html file onto the Netlify dashboard
3. Get instant URL, then connect your domain in settings
```

---

## 📋 Pending / Future Improvements (client feedback)
- [ ] Replace placeholder contact info (email, phone, address) with real data
- [ ] Add real WhatsApp link: `href="https://wa.me/529981234567"`
- [ ] Add Google Analytics or similar
- [ ] Consider adding a testimonials/reviews section
- [ ] Add real social media profile URLs (Facebook, Instagram, LinkedIn)
- [ ] Consider multilingual version (EN/ES) for foreign boat owners

---

## 🔄 How to Resume This Project with Another AI
Give the AI this file + the index.html and say:
> "This is a single-file HTML website for Soporte y Consultoría Marítima. Read AI_CONTEXT.md for full context. [Your change request here]."

The AI should edit index.html directly — no build tools, no packages, just HTML/CSS/JS.
