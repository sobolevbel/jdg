# CLAUDE.md

Community guide "ИП в Польше" (running a sole proprietorship / JDG in Poland).
MkDocs Material site published to GitHub Pages: <https://sobolevbel.github.io/jdg/>
(English mirror at `/en/`). Content language is Russian (canonical) + English mirror.
There is **no custom domain** — the github.io URL above is the only canonical one.

## Build and checks

```shell
pip install -r requirements.txt
python -m mkdocs build     # must produce zero warnings
python -m mkdocs serve     # local preview at :8000
```

- Lint: `mdl -s .github/workflows/markdown_linter_rules.rb docs/.`
- CI on every PR: mdl lint, mkdocs build, markdown-link-check, alt-text check
  (rejects `![]`, `![N]` and filename-like alts).
- Verify every new external link returns 200 (`curl -sI`) before adding — the CI
  link checker fails the PR otherwise.

## Bilingual structure (mkdocs-static-i18n, suffix mode)

- `page.md` = Russian (default), `page.en.md` = English. **Every content change
  must update both files in the same PR** (or explicitly note «нужен перевод»).
- New page: add to `nav:` (Russian label) **and** to `nav_translations:` in
  `mkdocs.yml`.
- Anchors differ per language: Russian headings are transliterated by slugify
  (check with `python -c "from slugify import slugify; print(slugify('Заголовок'))"`),
  English anchors come from the English headings. Never copy RU anchors into EN links.
- Renaming/removing a page: add `redirect_maps` entries for **both** the `.md`
  and `.en.md` variants.
- The i18n plugin replaces `page.title` with the nav label — theme code must
  prefer `page.meta.title`.

## Page conventions

- Frontmatter: `title` (SEO title), `description`, `tags`. Single H1. No trailing
  punctuation in headings (MD026).
- Be conservative with headings: anchors are generated from them, and both other
  guide pages and external sources (Telegram chats, search results) link to those
  anchors. Prefer keeping an existing heading as is; if renaming is truly needed,
  grep `docs/` for the old anchor and update inbound links — external links will
  still break, so rename rarely.
- Code blocks are **indented**, not fenced (MD046 is set to `indented`).
- Links are reference-style `[1]` collected at the bottom of the file, numbered
  sequentially. Link text must be descriptive — never «тут»/«здесь»/"here".
- Screenshots: `docs/images/<page-slug>/` — one directory per owning page,
  named exactly like its `.md` file (images reused by other pages stay in the
  owner's directory). Filenames: lowercase ASCII snake_case, extension as-is;
  step sequences are `NN_short_slug.ext` (zero-padded, slug from the alt text);
  when a page has several sequences, prefix each: `rwn_02_katalog.png`,
  `epity_05_dane.jpg`. Never repeat the directory name in the filename. Alt
  text in Russian, describing the screen and the actionable element (≤ ~120
  chars, no «Скриншот»/"image of"); frames via screely.com (Plain Window,
  Regular, white background, 4 px padding); blur personal data before
  committing.
- Admonitions `!!! info/tip/note/warning/example` are used heavily.
- The support button («Поддержите наш гайд чашкой кофе ♥») is injected
  automatically below the content of every page (except `support.md`) by the
  `content` block override in `overrides/main.html` — never add it manually.
- Every user-facing change gets a bullet in `docs/whatsnew.md` **and**
  `docs/whatsnew.en.md` (current-month section, newest month on top).

## Facts and figures

- Amounts, limits and rates change every year (ZUS bases in January, pension
  waloryzacja in March, GUS life-expectancy tables in April, etc.). Always verify
  against official sources (zus.pl, podatki.gov.pl, biznes.gov.pl, stat.gov.pl,
  lexlege.pl for statutes) and state the year explicitly («на 2026 год»).
- Notes forwarded from the Telegram chat often contain stale numbers or pre-2016
  legal rules — fact-check before publishing.
- The `/verify-guide-numbers` skill audits all time-sensitive figures against
  official sources. When adding a new figure to the guide, add it to the skill's
  registry.

## SEO and theme code

- `overrides/main.html`: og tags, `hreflang x-default`, TechArticle JSON-LD.
- `hooks/seo_faq_schema.py`: FAQPage JSON-LD for the FAQ page.
- Code and comments in scripts/hooks/workflows: **English only**.
- The minify plugin strips attribute quotes in built HTML — account for that when
  grepping `site/`.

## Git and PRs

- Work in a feature branch, open a PR to `master`. **Merge only when the owner
  explicitly asks.** The repo uses merge commits (no fast-forward).
- The gh CLI token lacks the `workflow` scope: PRs touching `.github/workflows/`
  cannot be merged via `gh pr merge` — merge locally
  (`git merge --no-ff <branch>` on master, then push).
- Pushing to a PR author's fork requires
  `git push https://x-access-token:$(gh auth token)@github.com/<fork>.git` —
  the SSH key has no access to forks.
- Community links: main chat [t.me/JDG_PBH](https://t.me/JDG_PBH), contributors
  chat link in README.
