# DOT's website — source handoff (Nov 2026)

Latest version: "v5" preview (brand guide v2 applied). Not yet published to GitHub (repo dots-agency: main = edition 3).

## Build
python3 v3/build3.py            # template -> v3/dots-site-v3.html
python3 -I v3/build_mp.py site  # multi-page site in site/ (applies guide_v1.py + guide_v2.py)
python3 -I v3/inline.py site site-html   # self-contained, editable HTML pages
Scripts expect this folder at /home/claude (paths: /home/claude/v3, /home/claude/v2, /home/claude/sr).

## Rules in force
- Show previews first; publish/push only after approval.
- Layout guide v1 (buttons, key visual) and brand file "DOT's — Logo Symbol" (logo = signature only, green = button+logo, result sheet, KV on inner pages).
- Ask before writing anything to Supabase.

## Open items
- Result-sheet table uses index 100 for last year (no raw numbers yet).
- Unconfirmed copy: founder bio, Talent DRAFT rows, campaign ideas, ParTak results.
