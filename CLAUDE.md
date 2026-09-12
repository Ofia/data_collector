# Trabajando en Santa Teresa

## Resume here
Pivot direction and stack are locked (see below). No app code written yet.
Next session: design worker onboarding + employer search screens/flows,
then start scaffolding the Expo project.

## What this is
Started as a one-page worker-signup form (QR flyer → static HTML → Supabase).
**Pivoting to a mobile app**: a marketplace connecting local workers (Santa
Teresa, Costa Rica — many from Nicaragua, low tech-comfort but all on
Instagram/WhatsApp) with employers who need to hire them. Workers build a
profile (not just a phone number). Employers search/filter and contact.

Free for now. Possible future monetization: credits to unlock contacts, or a
monthly subscription for employers. Not decided — don't build billing yet.

## Legacy assets (pre-pivot, still live)
- `index.html` — static worker signup form, deployed via GitHub Pages at
  `https://ofia.github.io/trabajo-en-santa-teresa/`. Writes directly to
  Supabase from the browser using the anon/publishable key.
- `flyer.html` — printable A4 flyer with a QR code pointing at the form.
- `generate_qr.py` — regenerates `worker_signup_qr.png` from the URL above.
- These stay as-is for now (flyer campaign may still be running). They are
  not part of the new app's codebase — treat as a separate legacy funnel,
  possibly a data source to migrate later.

## Supabase
- Project: `workers-data-collector` (id `oajtkvzgsjdwtfmqsccs`, region
  us-east-1).
- Table `public.workers` (RLS enabled): `id, created_at, name, whatsapp,
  job_type, specialties[], tools[], availability, hourly_rate, selfie_url`.
- No `employers` table yet, no auth yet — the legacy form inserts anonymously.

## New app — direction (locked so far)
- No native iOS app (avoids Apple Developer fee + review) — see Tech
  decisions below for how iPhone users are still covered via web export.
- Two user types: **workers** (build a profile) and **employers** (search
  and contact).
- Auth: Supabase Auth, Google sign-in or email/password.
- Aesthetic: **not** generic-AI (no default rounded-everything, no purple
  gradients). Reference points: Slack, VS Code. Should feel like a real
  tool, not a template.
- Must stay usable for non-technical users — plain flows, big touch targets,
  Spanish-first copy (see existing form for tone/fields).

## Tech decisions (locked)
- **Expo (React Native + TypeScript)** as a *universal* app: one codebase
  exports to (a) an Android app for the Google Play Store, and (b) a
  responsive website (via `react-native-web`) that works in any mobile
  browser — including iPhone Safari. This avoids the Apple Developer
  Program fee ($99/yr) and App Store review entirely; iPhone users and
  anyone who doesn't want to install anything just get a URL.
- Single app, single codebase, one role picker (`worker` / `employer`)
  right after signup — not two separate apps.
- Supabase stays the backend: Auth (Google + email/password), Postgres for
  `profiles` / `worker_details` / `employer_details`, Storage for photos.
- Styling: NativeWind (Tailwind syntax for React Native) for a consistent
  flat, Slack/VS Code look — no gradients, no pill-shaped everything.
- Search is plain Postgres `WHERE` filters on `worker_details` — no
  search-engine service, this is one small town's worth of workers.

## Open decisions
- Exact screens/flows for worker onboarding and employer search (design
  next).
- Where the web export gets hosted (likely reuses existing GitHub Pages
  habit, or Vercel — not decided).
- Contact-gating schema for future credits/subscription — log the event,
  don't build the paywall yet.
- Trust/safety review process (manual queue vs. anything automated) —
  manual to start.
