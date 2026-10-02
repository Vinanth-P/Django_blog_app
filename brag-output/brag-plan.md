# Brag Plan: Django Blog

## What is this app?
A full-stack blogging platform built entirely with Django — users register, log in, write posts, browse by author, and paginate through a live feed. No JS framework. Just Django doing its thing.

## The angle
Quiet dev pride. No hype, no buzzwords — just a real app that works: login, write, publish, read, paginate. The video shows the actual user flow, frame by frame, like a calm product demo from someone who knew exactly what they were building.

## Hook (first 2-3 seconds)
Title card appears on the steel-blue background:
"Django Blog."
One word at a time. Then the subtitle fades in:
"Write. Publish. Read."
Understated. No animation noise. Just the name, then what it does.

## Key moments (the middle)
- The home feed card sliding in: a post card with avatar, author name, date, and title — the real Django template rendered in styled HTML.
- Clicking into a post: the detail view — author byline, "Update / Delete" buttons visible (logged-in state), full content section.
- The "New Post" create form: a clean two-field form (Title + Content), a logged-in nav showing "New Post / Profile / Logout".

## Outro / punchline
Final scene: the steel-blue navbar visible at top. Then centered white text on the navbar color:
"Paginated. Authenticated. Deployed."
Brief hold, then a clean fade-out. No logo animation needed — the product *is* the statement.

## User flow worth showing
1. **Entry** — Home feed: post cards render with author avatar, name, date, title
2. **Key action** — Post detail: click in, see content, see Update/Delete (author controls)
3. **Result** — New Post form: the form that made it all possible

## Tone
- Preset: `polished`
- Creative direction: quiet dev-pride product film
- Interpretation: Long holds, restrained pacing, clean single-element reveals. The video respects the viewer's time. Typography does the heavy lifting. No gimmicks.

## Format: landscape — 1920x1080
## Duration: 20 seconds

## Visual identity (from the project)
- Background: `#fafafa` (body background)
- Accent / navbar: `#5f788a` (steel blue, `.bg-steel`)
- Text: `#444444` (headings), `#333333` (body)
- Article title link hover: `#428bca` (Bootstrap info blue)
- Content card: `#ffffff` with `1px solid #dddddd` border, `border-radius: 3px`
- Display font: Bootstrap 4 default (system sans-serif / Helvetica Neue) — use Inter as the video equivalent
- Body font: same — Inter
- Strongest visual element: The white post card with the circular author avatar on the left, the article title as a link, and the muted date — a very clean, recognizable pattern

## Share copy (draft)
Built a full blog platform with Django. Login, write, publish, paginate. Zero JS frameworks. Just Django doing its thing.

## Audio direction
- Role: warm professional bed
- Music: `happy-beats-business-moves-vol-9-by-ende-dot-app.mp3` (mid-energy, laid-back — matches polished restraint)
- Music treatment: fade in from 0s at volume 0.30; fade out gently over the last 1.5s
- Music cue guidance: Bundled preset at `<skill-dir>/assets/music/cues/happy-beats-business-moves-vol-9-by-ende-dot-app.music-cues.json`. Strong cues: 4.23s, 6.34s, 10.54s, 12.65s. Lock the post-card reveal to ~4.23s; lock the detail view reveal to ~10.54s; lock the form reveal to ~12.65s. Beat grid for staggered card elements: 1.07, 1.59, 2.12, 2.65.
- Audio-reactive treatment: subtle; use music RMS/bass to make the post card and background have a gentle breathing presence. No waveform or equalizer visuals.
- SFX posture: sparse, polished — 3 cues total
- Audio-coupled moments:
  - Scene 2 (post card reveal): `interface/drop_001.ogg` or `interface/drop_002.ogg` as the card slides in
  - Scene 3 (detail view): `interface/click_001.ogg` at simulated click moment
  - Scene 5 (outro text): `impact/impactBell_heavy_000.ogg` at settled reveal — low volume (0.55)
- Restraint rule: no punch sounds, no glitch sounds, nothing that feels chaotic or comedic — this is a polished, professional tone

## Storyboard

### Scene 1 — Hook — 3s
Steel-blue background (`#5f788a`). Centered white text:
"Django Blog" — appears at 0.3s with a soft fade-up (0.4s ease).
"Write. Publish. Read." — fades in at 1.4s, slightly smaller, lighter opacity.
Both lines hold until the transition.
Sequential/interaction: none
Audio intent: music fades in gently; quiet and professional
Audio-coupled idea: none — let the music carry
Music: warm bed, fade in
Transition mood: soft crossfade → Scene 2

### Scene 2 — The Feed — 5s (start: ~3.2s, beat-locked to 4.23s for card arrival)
Light gray background (`#fafafa`). A single post card slides up from slightly below:
- White card with `1px solid #ddd` border and subtle shadow
- Left: circular avatar (65px, placeholder profile image)
- Right: author name (link), date "October 02, 2026", article title as an `<h2>` link, first 2 lines of content
The card arrives at ~4.23s (beat-locked), settles for 3+ seconds of readable hold.
Paginator row faintly visible at bottom (First / Previous / 1 / Next / Last buttons).
Sequential/interaction: none — single card reveal
Audio intent: warm, slightly brightening as the product appears
Audio-coupled idea: `interface/drop_001.ogg` at card arrival (~4.2s)
Music: vol-9 bed, volume 0.30
Transition mood: clean slide → Scene 3

### Scene 3 — Post Detail — 5s (start: ~8.2s, beat-locked to ~10.54s for content reveal)
Same light gray background. The post detail card appears:
- Same card format, but now showing the author byline at top
- Crucially: two small buttons visible — "Update" (grey) and "Delete" (red) — showing the logged-in author state
- Post title as `<h2>`, content text below
A simulated cursor click moment (very brief, 0.2s opacity flash on a "Read Post" link) transitions in — simulates navigating from the feed.
Sequential/interaction: yes — cursor click on title at start of scene, then detail card reveals
Audio intent: confident; the product delivers
Audio-coupled idea: `interface/click_001.ogg` at cursor click moment (~8.3s)
Music: vol-9 bed, steady
Transition mood: soft crossfade → Scene 4

### Scene 4 — New Post Form — 4s (start: ~13.1s, beat-locked to ~12.65s)
Steel-blue navbar at top (same as Scene 1). Navbar shows: "Django Blog | Home | About | New Post | Profile | Logout" — the logged-in state.
Below: white form card with:
- "Title" input field (with placeholder text "My First Post")
- "Content" textarea (with sample text "This blog was built with Django...")
- A "Submit" button (Bootstrap primary blue)
Text types into Title at ~13.5s — 3-4 characters, with subtle keyboard SFX if Hyperframes supports a typing animation; otherwise the field appears pre-filled.
Sequential/interaction: yes — title field types out "My Fi..." to show the form in active use
Audio-coupled idea: `keyboard/keypress-*.wav` for the typing animation (randomized, 3-4 key taps)
Audio intent: purposeful — this is where things get made
Music: vol-9 bed, steady
Transition mood: clean fade → Scene 5

### Scene 5 — Outro — 3s (start: ~17.1s, beat-locked to ~23.17s? — hold for full 3s)
Steel-blue background. Centered white text fades in:
"Paginated. Authenticated. Deployed."
One line. Holds for 2.5 seconds. Then soft fade to black.
Sequential/interaction: none
Audio intent: confident resolution; the bell SFX punctuates the reveal
Audio-coupled idea: `impact/impactBell_heavy_000.ogg` at text settle (~17.4s), volume 0.55
Music: vol-9 bed fades out over last 1.5s (from ~18.5s)
Transition mood: fade to black

**Total duration:** 3 + 5 + 5 + 4 + 3 = **20 seconds** ✓

**Music mood for this video:** mid-energy, laid-back, warm corporate
**Audio summary:** Vol-9 bed fades in quietly, three sparse polished SFX mark the card arrival, the cursor click, and the outro bell — then music fades under the final text.
