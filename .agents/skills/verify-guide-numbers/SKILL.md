---
name: verify-guide-numbers
description: Audit every time-sensitive figure in the guide (ZUS contributions, health insurance tiers, VAT/tax limits, pension amounts, benefit rates, IKE/IKZE limits) against official Polish sources and update RU+EN pages where stale. Use when asked to "проверить цифры" / "обновить суммы", at the start of a new year, or after Polish law changes.
---

# Verify guide numbers

Audit the registry below against official sources, update stale values in both
language versions, recompute derived examples, and open a PR with an old→new table.

## Process

1. **Establish context.** Note today's date. Polish figures update on a schedule:
   - **Before January**: check published regulations and ministerial notices for
     next year's minimum wage, prognozowane przeciętne wynagrodzenie,
     30-krotność and IKE/IKZE limits. Their January effective date does not mean
     publication must wait until January. Derive ZUS bases and the chorobowe cap;
   - **~late January**: GUS announces average enterprise-sector salary for Q4 →
     składka zdrowotna tiers for ryczałt payers (valid Jan–Dec). The Feb–Jan
     contribution year applies to skala/liniowy health minima instead;
   - **March 1**: pension/benefit waloryzacja → minimalna emerytura;
   - **April 1**: GUS life-expectancy tables (divisor in the pension formula);
   - ad-hoc: VAT rules (KSeF rollout), tax scale changes.
2. **Verify each registry row** with WebSearch/WebFetch. Prefer official sources
   (zus.pl, podatki.gov.pl, stat.gov.pl, gov.pl, lexlege.pl for statutes);
   poradnikprzedsiebiorcy.pl/wskazniki is an acceptable secondary source.
   Never update a legal amount from a single non-government source.
3. **Grep the listed files** for the current value; also grep for the old year
   marker (e.g. `на 2026`, `w 2026`, `in 2026`) to find prose that needs the year
   bumped, not just the number.
4. **Update RU and EN together.** Each `page.md` has a `page.en.md` mirror with
   the same figures. Match each file's existing number formatting exactly
   (some files use `9.228,64 zł`, others `1 441,80 zł`; EN files use `1,441.80 zł`).
5. **Recompute derived values** (section below) — never swap a base number
   without recalculating the examples built on it.
6. **Wrap up**: add whatsnew bullets (RU+EN), run `python -m mkdocs build`
   (zero warnings) and `mdl -s .github/workflows/markdown_linter_rules.rb docs/.`,
   verify any newly added links with `curl -sI` (expect 200), then branch + PR.
   The PR body must contain a table: figure | old | new | source link.
   Do not merge without the owner's explicit request.
7. **Maintain this registry.** If the guide gained new time-sensitive figures
   (hint: `grep -rn "zł\|злот\|20[0-9][0-9]" docs --include='*.md'`), add rows
   here in the same PR.

For advance updates, retain the current year's tables and examples. Add a
separate dated section for the next year, distinguishing published inputs,
calculations under current rates, and amounts awaiting publication. Never mix
new social contributions with old health contributions into a next-year total.
Round each monthly contribution to grosz (decimal half-up) before summing;
annual examples multiply the rounded monthly amount by the paid months.
If the user asks for a local diff without publication, stop after local checks:
do not commit, push, or open a PR.

### 2027 preparation — checked 2026-11-25

The 2026 registry below remains the current-year baseline. The following values
are separate additions in `zus.md`, `zus_chorobowe.md`, `emerytura.md` and their
English mirrors, not replacements of 2026 amounts.

| Figure | 2026 | 2027 | Status / source |
|---|---|---|---|
| Minimum wage | 4 806 zł | 4 950 zł | Published; effective 1 Jan 2027, [DU/2026/1213](https://api.sejm.gov.pl/eli/acts/DU/2026/1213/text.pdf) |
| Projected average salary for ZUS | 9 420 zł | 10 033 zł | Published, [MP/2026/1098](https://api.sejm.gov.pl/eli/acts/MP/2026/1098/text.pdf); no longer awaiting a budget estimate |
| Preferencyjne / Duży base | 1 441,80 / 5 652,00 zł | 1 485,00 / 6 019,80 zł | 30% minimum wage / 60% announced projected salary |
| Emerytalna pref / duży | 281,44 / 1 103,27 zł | 289,87 / 1 175,06 zł | 19.52% |
| Rentowa pref / duży | 115,34 / 452,16 zł | 118,80 / 481,58 zł | 8% |
| Wypadkowa pref / duży | 24,08 / 94,39 zł | 24,80 / 100,53 zł | At 1.67%; check the payer's rate, including the insurance year from April |
| Mandatory social pref / duży, excluding FP/FS and health | 420,86 / 1 649,82 zł | 433,47 / 1 757,17 zł | Sum rounded components; [current ZUS rules](https://www.zus.pl/pl/firmy/rozliczenia-z-zus/skladki-na-ubezpieczenia) |
| Chorobowa pref / duży | 35,32 / 138,47 zł | 36,38 / 147,49 zł | 2.45%, voluntary |
| Social with chorobowa pref / duży, excluding FP/FS and health | 456,18 / 1 788,29 zł | 469,85 / 1 904,66 zł | Sum rounded components |
| Chorobowa for 12 paid months, pref / duży | 423,84 / 1 661,64 zł | 436,56 / 1 769,88 zł | Rounded monthly contribution × 12 |
| Pension contributions for 12 paid months, pref / duży | 3 377,28 / 13 239,24 zł | 3 478,44 / 14 100,72 zł | Rounded monthly contribution × 12 |
| Chorobowe monthly base cap | 23 550 zł | 25 082,50 zł | 250% announced projected salary |
| Annual emerytalne/rentowe cap | 282 600 zł | 300 990 zł | Published, MP/2026/1098 |
| Benefit-blocking arrears threshold | 48,06 zł | 49,50 zł | 1% minimum wage; arrears must exceed the threshold |
| Minimum zdrowotna, skala/liniowy | 432,54 zł for Feb 2026–Jan 2027 | 445,50 zł for Feb 2027–Jan 2028 | 9% minimum wage under current rules; Jan 2027 remains 432,54 zł |
| IKE | 28 260 zł | 30 099 zł | Published, [MP/2026/1081](https://api.sejm.gov.pl/eli/acts/MP/2026/1081/text.pdf) |
| IKZE standard / JDG | 11 304 / 16 956 zł | 12 039,60 / 18 059,40 zł | Published, [MP/2026/1062](https://api.sejm.gov.pl/eli/acts/MP/2026/1062/text.pdf) |

Still pending as of the check date:

- **FP/FS:** the [2027 budget bill](https://api.sejm.gov.pl/sejm/term10/processes/3150)
  has not passed. At an unchanged combined 2.45%, FP/FS would be 147,49 zł,
  and Duży ZUS with FP/FS would be 1 904,66 zł without chorobowa or 2 052,15 zł
  with it, excluding health. These are conditional, not approved totals.
- **Ryczałt health:** GUS Q4 2026 enterprise salary including profit payments,
  then ZUS tables for Jan–Dec 2027. Do not use the projected salary of 10 033 zł.
  Recompute all combined totals and Maksym's annual example only after this.
- **Pensions:** March 2027 indexation / minimum pension and the GUS life table
  effective April 2027. Keep the 2026 pension amount example and divisor.

Derived 2027 examples: Duży benefit base 6 019,80 × 86.29% = 5 194,49 zł;
sick pay about 138,52 zł/day, maternity about 4 234 zł per 30 days,
break-even still about 13 days. These assume 12 full months at the new base,
not an automatic benefit increase in January; actual benefits use insured
history. The five-month art. 48a example becomes about 7 678 zł before 13.71%.
The 25-year contribution-only example becomes 352 518 zł, without indexation;
do not present it as an approved future pension.

## Registry of time-sensitive figures

Values in the "2026" column are what the guide states as of 2026-07 — they are
the grep targets, not eternal truths.

### Base indicators (everything else derives from these)

| Figure | 2026 | Source | Updates |
|---|---|---|---|
| Prognozowane przeciętne wynagrodzenie | 9 420 zł | ZUS / ustawa budżetowa | Jan |
| Minimum wage (minimalne wynagrodzenie) | 4 806 zł | gov.pl rozporządzenie | Jan (check for a mid-year raise too) |
| Avg enterprise salary Q4 (GUS, for zdrowotna) | 9 228,64 zł | stat.gov.pl komunikat | late Jan |

### ZUS contributions — files: `zus.md`, `zus_chorobowe.md`, `emerytura.md` (+ `.en.md`)

| Figure | 2026 | Notes |
|---|---|---|
| Duży ZUS base (60% of prognozowane) | 5 652,00 zł | |
| Preferencyjne base (30% of min wage) | 1 441,80 zł | |
| Emerytalna duży / pref | 1 103,27 / 281,44 zł | 19,52% of base |
| Rentowa duży / pref | 452,16 / 115,34 zł | 8% |
| Wypadkowa duży / pref | 94,39 / 24,08 zł | 1,67% |
| Fundusz Pracy (duży only) | 138,47 zł | 2,45% |
| Chorobowa duży / pref | 138,47 / 35,32 zł | 2,45% |
| Społeczne total duży / pref | 1 649,82 / 420,86 zł | table in `zus.md` |
| Row totals A+B+C in `zus.md` table | 2 286,64 / 2 618,87 / 3 283,33 etc. | recompute all cells |
| Chorobowe base cap (250% of prognozowane) | 23 550 zł | `zus_chorobowe.md` |
| 30-krotność annual cap | 282 600 zł | `emerytura.md` |

### Składka zdrowotna (ryczałt tiers) — files: `zus.md` (+ example), `faq.md`, `wfirma_routine.md`

| Figure | 2026 |
|---|---|
| Bases 60% / 100% / 180% of Q4 salary | 5 537,18 / 9 228,64 / 16 611,55 zł |
| Contributions (9% of base) | 498,35 / 830,58 / 1 495,04 zł |
| Income thresholds | 60 000 / 300 000 zł (stable so far) |

### Taxes — files: `taxes.md`, `declarations_vat.md`, `registration_vat.md`, `faq.md`, `index.md`

| Figure | 2026 | Notes |
|---|---|---|
| VAT exemption limit | 240 000 zł | raised from 200 000 in 2026 |
| Skala: kwota wolna / threshold / rates | 30 000 zł / 120 000 zł / 12%+32% | changes rarely |
| Ryczałt rates (IT = 12%) | 2–17% | changes rarely |
| VAT standard rate | 23% | |
| VAT refund deadlines | 40 days standard for periods from February 2026; 25 / 180 days in specific cases | `infakt_routine.md` (+ `.en.md`); verify with podatki.gov.pl, art. 87 VAT |
| Cash-payment limit between firms | 15 000 zł | `faq.md` |
| KSeF mandatory dates/thresholds | rollout 2026 | `declarations_vat.md`, `taxes.md` — verify current schedule |

### Pension — file: `emerytura.md` (+ `.en.md`)

| Figure | 2026 | Updates |
|---|---|---|
| Minimalna emerytura | 1 978,49 zł brutto | Mar 1 (waloryzacja) |
| GUS life expectancy at 65 / 60 | 222,7 / 268,9 months | Apr 1 |
| IKE limit | 28 260 zł | Jan |
| IKZE limit standard / JDG | 11 304 / 16 956 zł | Jan |

### Benefits — file: `zus_chorobowe.md` (+ `.en.md`)

| Figure | 2026 | Notes |
|---|---|---|
| Minimum maternity benefit floor | 1 000 zł net | świadczenie rodzicielskie level |
| Arrears threshold blocking benefits | 1% of min wage (~48 zł) | recompute from min wage |

### Legalization — file: `legalization.md` (+ `.en.md`)

| Figure | 2026 | Notes |
|---|---|---|
| Income criterion per family member | 823 zł net/month | kryterium dochodowe (pomoc społeczna), rozporządzenie RM Dz.U. 2024 poz. 1044; revised every 3 years, next revision for 2028. Do NOT check migrant.wsc.mazowieckie.pl "Stabilne i regularne źródło dochodu" — that glossary still shows pre-2025 amounts (776/600 zł) as of Aug 2026 |
| Income criterion for a person living alone | 1 010 zł net/month | same rozporządzenie; both unchanged for 2026 |
| 12 avg monthly salaries by voivodship | 85 606,80 / 91 759,44 / 113 867,28 zł (warm.-maz. / łódzkie / maz., 2024 data) | new GUS obwieszczenie every November — update figures AND the `[4]`/`[20]` link. Not applied to citizens of Ukraine with PESEL UKR running a CEIDG JDG (art. 142 ust. 1 pkt 3 exemption kept after the specustawa wind-down of 5.03.2026) — re-check that exemption still holds |
| Opłata skarbowa for the decision | 340 zł | rarely changes; for applications filed from 5.03.2026 it is not refunded on refusal/discontinuation (noted on the page) |
| Private insurance policy minimum | 30 000 EUR | rarely changes |

### Partner terms — file: `accounting.md` (+ `.en.md`)

| Figure | As of 2026-08 | Notes |
|---|---|---|
| Legal Tax Level pricing | 225 zł netto/month (276,75 zł brutto), 1 200 zł netto per 6 months prepaid | commercial terms, NOT verifiable against official sources — confirm with the owner/partner; the page dates them («Условия на август 2026 года») |
| Biuro rachunkowe typical price range | 150–300 zł/month | rough market range, update only if far off |

### Rarely changing (check yearly, expect no change)

- De minimis aid limit 300 000 EUR / 3 years — `zus_vacation.md`
- Insurance record for minimum pension 20/25 years — `emerytura.md`
- Retirement age 60/65 — `emerytura.md`
- Benefit percentages (80% sick pay, 100%+70% / 81,5% maternity, 13,71% deduction) — `zus_chorobowe.md`
- Ulga na start 6 months, preferencyjne 24 months — `zus.md`, `zus_ulga_na_start.md`, `zus_obnizone_skladki.md`

## Derived values that must be recomputed by hand

- `zus.md` — the «Максим» zdrowotna example: monthly amounts, yearly sum
  (`11 295,88`), underpayment (`6 644,60`), and the yearly total (`17 940,48`).
- `zus_chorobowe.md` — benefit base `5 652 × 86,29% = 4 877 zł`; daily sick pay
  `≈ 130 zł`; yearly cost `~1 662 / ~424 zł`; break-even `~13 days`; maternity
  `≈ 3 975 zł`; the art. 48a example `5 652 + (10 000 − 5 652) × 5/12 ≈ 7 464 zł`.
- `emerytura.md` — the 25-year example `1 103,27 × 12 × 25 ≈ 331 000 zł` and
  `331 000 / 222,7 ≈ 1 490 zł`; per-year capital `~3 377 / ~13 239 zł`.
- `faq.md` and `index.md` (cost table) — the rough ZUS ranges (~500 / ~900–1300 /
  from ~2300 as of 2026) are approximations; update only if they drift far from
  reality, and keep both pages consistent.
- `wfirma_routine.md` (+ `.en.md`) — the 2026 health contribution of 498,35 zł
  and its deductible half of 249,18 zł; the first Ulga na Start payment example
  also uses 498,35 zł. Await GUS before adding a 2027 version.
- `index.md` — the "Что важно в 2026 году" block (KSeF dates, VAT limit
  240 000 zł, ZUS vacation) is a snapshot of current changes: refresh its
  contents each year and swap in whatever is newly relevant.

## Registry of legal bases (check act status via the Sejm ELI API)

Pages also cite statutes and regulations that can be repealed or renumbered.
Check each act's status with:

    curl -s https://api.sejm.gov.pl/eli/acts/DU/<year>/<position>

and look at `status` / `inForce` (expect `IN_FORCE`). ISAP web pages block
non-browser fetches with a CAPTCHA — use the API, not WebFetch. If an act is
repealed, find the successor act, update the quote and the ISAP link on the
page, and note it in whatsnew. When an act is merely amended, still verify the
cited article number exists in the current consolidated text (via lexlege.pl).

| Act (ELI id) | Cited as | Pages |
|---|---|---|
| Ustawa o zasadach ewidencji i identyfikacji podatników (DU/1995/702) | art. 3 ust. 1 pkt 1 — primary PESEL tax basis | `pesel.md` |
| Ustawa o ewidencji ludności (DU/2010/1427) | art. 7 ust. 2 — PESEL tax basis | `pesel.md` |
| Rozporządzenie MC z 29.06.2020 o profilu zaufanym (DU/2020/1194) | załącznik nr 1 pkt 1 — PESEL fallback basis | `pesel.md` |
| Ustawa o opiece nad dziećmi do lat 3 (DU/2011/235) | art. 3a — PESEL for children under 3 | `pesel.md` |
| Ustawa o systemie oświaty (DU/1991/425) | art. 92k ust. 2 pkt 2 lit. f — PESEL for children 3–18 | `pesel.md` |
| Ustawa zasiłkowa (DU/1999/636) | art. 48a, art. 49 — benefit base for <12 months of coverage | `zus_chorobowe.md` |
| Ustawa emerytalna (DU/1998/1118) | art. 5, art. 26, art. 87 | `emerytura.md` |
| Umowa PL–Ukraina o zabezpieczeniu społecznym (DU/2013/1373) | period summation, benefit transfer | `emerytura.md` |
| Umowa PL–Białoruś o zabezpieczeniu społecznym (DU/2022/575) | period summation, benefit transfer (in force since 01.04.2022) | `emerytura.md` |

Also re-check the KAS recommendation page linked from `pesel.md` — if KAS
changes the recommended wording of the tax basis, update the quote.
