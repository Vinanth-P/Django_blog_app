# Hyperframes Composition Brief: Django Blog

## Objective
Create a short 20-second polished brag video for Django Blog — a full-stack blogging platform built with Django. Quiet dev-pride tone. Show the real user flow: feed → detail → create.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 20 seconds

## Source Material
- Project root: `c:/Users/asus/OneDrive/Desktop/projects/django_project/`
- Primary files read: `blog/templates/blog/base.html`, `blog/templates/blog/home.html`, `blog/templates/blog/post_detail.html`, `blog/templates/blog/post_form.html`, `blog/static/blog/main.css`
- Product name: Django Blog
- Tagline / strongest claim: "Write. Publish. Read." — "Paginated. Authenticated. Deployed."
- Key UI or visual moment to recreate: The post card from `home.html` (avatar + author + date + title), the post detail view with Update/Delete buttons (logged-in state), and the New Post create form with the logged-in navbar.
- Copy that must appear verbatim:
  - "Django Blog"
  - "Write. Publish. Read."
  - "Paginated. Authenticated. Deployed."
  - "New Post" (navbar link)

## Creative Direction
- Tone preset: `polished`
- Creative direction: quiet dev-pride product film
- Interpretation: Long holds, restrained pacing, clean single-element reveals. No animation noise. Typography does the heavy lifting. The product earns the space.
- Angle: A real blog platform that works — login, write, publish, read, paginate. Show the flow, not the marketing. The video respects the viewer's time.
- Hook: "Django Blog." / "Write. Publish. Read." — white text on steel blue, clean fade-up
- Outro / punchline: "Paginated. Authenticated. Deployed." — three words, one line, fade to black
- Avoid:
  - Generic SaaS language ("streamline your workflow")
  - Abstract filler visuals or color washes
  - Unrelated visual redesign — stay within the project's own color palette

## Visual Identity
- Background: `#fafafa`
- Text: `#444444` headings, `#333333` body
- Accent: `#5f788a` (steel blue — navbar, scene backgrounds)
- Article title hover / link: `#428bca`
- Content card: `#ffffff` with `1px solid #dddddd` border, `border-radius: 3px`
- Display font: Inter (video equivalent of the Bootstrap 4 system stack)
- Body font: Inter
- Visual references from the project:
  - Circular 65px avatar (`article-img` class) on the left of each post card
  - Post card = white box, `10px 20px` padding, subtle border, `margin-bottom: 20px`
  - Steel-blue navbar with white-text links
  - Bootstrap 4 button classes: `btn btn-secondary btn-sm` (Update), `btn btn-danger btn-sm` (Delete), `btn btn-primary` (Submit)

## Storyboard
Use `brag-output/brag-plan.md` as the creative contract.

Scene summary:
1. Hook — 3s — "Django Blog." / "Write. Publish. Read." on steel-blue bg
2. The Feed — 5s — Post card slides in: avatar, author, date, title, content excerpt; beat-locked to 4.23s
3. Post Detail — 5s — Detail view: author byline, Update/Delete buttons, content; simulated cursor click; beat-locked reveal ~10.54s
4. New Post Form — 4s — Logged-in navbar + form with Title/Content fields + Submit; typing animation in title field; beat-locked ~12.65s
5. Outro — 3s — "Paginated. Authenticated. Deployed." on steel-blue; bell SFX; fade to black

## Audio
- Audio role: warm professional bed
- Audio arc: Fades in quietly at Scene 1, steady through Scenes 2-4, fades out gently over the last 1.5s of Scene 5
- Music: `assets/music/happy-beats-business-moves-vol-9-by-ende-dot-app.mp3`
- Music treatment: data-volume="0.30"; fade in from 0s; fade out from ~18.5s over 1.5s
- Music cue guidance: Bundled preset at `C:/Users/asus/.agents/skills/brag/assets/music/cues/happy-beats-business-moves-vol-9-by-ende-dot-app.music-cues.json`. Strong cues in window: 4.23s, 6.34s, 10.54s, 12.65s. Beat grid (114.84 BPM): 1.07, 1.59, 2.12, 2.65, 3.18, 3.70, 4.23, 4.75, 5.28, 5.80... Use these as timing hints only — readability and pacing come first.
- Audio-reactive treatment: subtle; use music RMS/bass to make the post card and scene background have a gentle breathing presence. No waveform/equalizer visuals, no strobing.
- Audio-coupled moments:
  - Scene 2 feed card reveal (~4.2s) — `interface/drop_001.ogg`, volume 0.70
  - Scene 3 simulated cursor click (~8.3s) — `interface/click_001.ogg`, volume 0.65
  - Scene 4 typing animation (~13.5s) — `keyboard/keypress-*.wav` (randomized 3-4 taps), volume 0.60
  - Scene 5 outro text settle (~17.4s) — `impact/impactBell_heavy_000.ogg`, volume 0.55
- SFX selection guidance: polished restraint — 4 cues total, no punch/glitch sounds; prefer drop and bell sounds that feel clean and professional
- SFX analysis guidance: `C:/Users/asus/.agents/skills/brag/assets/sfx/sfx-analysis.md`
- Exact SFX choice: Hyperframes should choose final filenames, timestamps, density, and volume based on the implemented animation
- Audio files: copy chosen music and SFX into `brag-output/composition/assets/`

## Hyperframes Instructions
Load `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`, and `hyperframes-cli`. This is `/brag`'s own workflow — do not enter the hyperframes entry-point intent interview or route into its generic promo/launch-video workflow. Prefer native Hyperframes conventions.

Requirements:
- Show at least one real UI element from the project (post card, detail view, or form — all three ideally).
- Keep all text readable — every text element fully settles before transition. No flashing text.
- Total duration: exactly 20 seconds.
- Include the music bed and 4 sparse polished SFX cues.
- Treat audio notes as guidance. Choose SFX after animation exists.
- Major reveals beat-locked to: 4.23s (feed card), 10.54s (detail reveal), 12.65s (form reveal). Mark each with `// beat-locked`.
- Typing animation SFX snap to beat grid (~13.5s area). Mark with `// beat-grid`.
- Run `npx hyperframes check` before render. Fix all errors.
- Render to `brag-output/brag.mp4`.
- Keep everything local.
