---
title: JPK_V7M via e-mikrofirma — Free VAT Filing in Poland
description: How to submit the JPK_V7M declaration for free via the official e-mikrofirma app from the Ministry of Finance — logging in, invoices, zero declaration, signing, UPO, korekta
tags:
  - Declarations
  - VAT
  - JPK
---

# Submitting JPK_V7M via e-mikrofirma

**e-mikrofirma** is a free official application from the Ministry of Finance for keeping
a simple invoice register and submitting JPK_V7M/JPK_V7K declarations. It suits those who
don't want to pay for inFakt/wFirma and are fine with entering invoices manually.

Official documentation: [Podręcznik użytkownika aplikacji e-mikrofirma][1] (PDF, Polish).

## Who it's for

- VAT payers with a small number of invoices per month.
- Those who need to submit a **zero** JPK_V7M declaration for free.
- Those who generate the JPK XML file in another program and just want to send it —
  for that, [Klient JPK_WEB][2] is enough (see [below](#sending-a-ready-xml-klient-jpk-web)).

## Logging in

1. Go to [e-Urząd Skarbowy][3].
2. Choose to log in via **login.gov.pl** (profil zaufany, aplikacja mObywatel,
   bankowość elektroniczna, or e-dowód).

    !!! warning "Logging in with «dane podatkowe» won't work"
        If you log in to e-Urząd Skarbowy with taxpayer data (NIP/PESEL + amounts
        from declarations), the e-mikrofirma application is **unavailable**. You need
        a full login via login.gov.pl.

3. Inside e-Urząd Skarbowy, open the **e-mikrofirma** tile.

## Initial profile setup

On first login, the application will ask you to register a company profile — the **Rejestracja** screen:

- **Dane identyfikacyjne**: NIP (⚠ cannot be changed after registration — double-check
  before submitting), REGON and BDO (optional), first name, last name, date of birth,
  company name and logo (optional — they will appear on invoices).
- **Dane adresowe**: company address, phone, e-mail.
- **Dane do rozliczeń**: settlement method — **miesięczne (JPK_V7M)** or kwartalne (JPK_V7K),
  bank account number, your Urząd Skarbowy.
- A checkbox confirming you've read the klauzule informacyjne and the **Zarejestruj** button.

After registration you land on the start page with a menu on the left: **Nowy dokument**
(invoices), **e-Faktury zakupu w KSeF**, **Lista dokumentów**, **Ewidencje**,
**Deklaracje**, **Rozliczenia**, **Lista JPK**, **Baza kontrahentów**. If a banner
«Konto nie jest powiązane z KSeF» appears at the top — the «instrukcji» link inside it
explains how to grant the application permissions in KSeF (needed for issuing e-Faktury).

## Entering invoices

### Sales invoice

Menu → **Nowy dokument** → **Nowa faktura sprzedaży**. The form has five sections.
Fields marked with an asterisk in the application are required — they are also marked
with `*` below.

!!! info "From April 1, 2026 — e-Faktura via KSeF"
    Right in the Kontrahent section, the application warns: issue an invoice for
    a counterparty **with a NIP** via **Nowa e-Faktura sprzedaży (KSeF)** — a separate
    menu item with almost the same set of fields. A regular invoice is allowed until
    the end of 2026, but only as long as the total of such invoices doesn't exceed
    10 000 zł brutto per month.

**1. Dane faktury** — the invoice details:

| Field | What to enter |
|---|---|
| Oznaczenia (opt.) | checkboxes MPP (mechanizm podzielonej płatności), MK (metoda kasowa), faktura do paragonu — a typical freelancer doesn't need them |
| Numer faktury `*` | number in your own series, e.g. `1/07/2026`. The application doesn't track numbering — continue your own |
| Data wystawienia `*` | issue date in RRRR-MM-DD format (there's a calendar) |
| Miejsce wystawienia (opt.) | city of issue |
| Data księgowania `*` | **the key field**: the date binding the invoice to a reporting period — it determines which month's ewidencja and JPK the document lands in |
| Data dostawy / usługi `*` | date the service was provided (for monthly services — the last day of the month) |

**2. Kontrahent** — the buyer:

| Field | What to enter |
|---|---|
| Nazwa kontrahenta `*` | the client's company name (on repeat entry it's pulled from the Baza kontrahentów) |
| NIP kontrahenta (opt.) | the client's NIP — 10 digits without a prefix; for an individual without a NIP, leave empty |
| Miejscowość `*`, Kod pocztowy `*`, Numer budynku `*` | the client's address |
| Poczta, Ulica, Numer lokalu (opt.) | the rest of the address |

**3. Pozycje** — the invoice line items:

- The **Faktura wystawiona w cenach: Netto / Brutto** `*` switch — which prices to
  calculate from (usually Netto).
- The line items table: **Nazwa** (name of the service/goods), **Cena jedn. netto**, **Ilość**,
  **Jednostka miary** (e.g. `szt.` or `usł.`), **Stawka VAT** — a dropdown:
  `23%`, `8%`, `5%`, `0%`, `ZW` (zwolnione — a «Powód zwolnienia» field will appear),
  `OO` (odwrotne obciążenie). The **Netto / VAT / Brutto [PLN]** columns recalculate
  automatically, with a **Suma** row at the bottom.
- The **Dodaj kolejną pozycję** button — if there are several line items.
- **Kody towarów i usług** (opt.) — GTU_01–GTU_13; not required for programming.
- **Oznaczenia dotyczące procedur** (opt.) — SW, EE, TP, etc.; a typical sole trader doesn't need them.

**4. Płatność** — payment:

| Field | What to enter |
|---|---|
| Typ płatności `*` | `przelew`, `gotówka`, `za pobraniem`, `karta płatnicza`, or `inny` |
| Numer rachunku bankowego (opt.) | your account (26 digits) — will appear on the invoice |
| Faktura opłacona (checkbox) | check it if the payment has already been received |
| Umowa określa termin płatności (checkbox) | if the payment deadline is fixed by a contract |
| Dni na płatność `*` | payment term in days — Termin płatności `*` is calculated automatically (or can be set manually) |

**5. Uwagi** (opt.) — notes up to 256 characters (e.g. `Reverse charge — VAT is
charged to the buyer` for a counterparty outside the EU).

At the bottom there are three buttons: **Zapisz** (save), **Zapisz i pokaż PDF** (save and
open the invoice PDF), **Anuluj**. Saved invoices live in **Lista dokumentów → Faktury
sprzedaży**, where you can also edit them, download the PDF, or issue a faktura
korygująca.

### Purchase invoice

Menu → Nowy dokument → **Nowa faktura zakupu**. Similar, but the counterparty's NIP is
required, and you need to choose the **Rodzaj wpisu** (fixed assets or other goods
and services). From 01.02.2026, an oznaczenie faktury is mandatory: NrKSeF (the number
from KSeF), BFK (paper/electronic outside KSeF), or OFF.

## Generating JPK_V7M for a period

1. Enter all documents for the reporting month.
2. **Deklaracje** section → select the period → **Uzupełnij deklarację**. Most of the
   fields will be filled in automatically from the entered invoices.

    !!! warning "Carrying over the VAT nadwyżka (field P_39)"
        The VAT surplus from the previous period is **not carried over automatically** —
        check it and enter it manually.

3. **Zapisz** (or Zapisz i pokaż PDF — to check it with your own eyes).
4. **Rozliczenia** section → select the period → **Generuj i wyślij JPK_VAT** — the period
   will be closed, and the application will redirect you to Klient JPK_WEB for signing
   and sending. (The **Generuj JPK_VAT** button without sending lets you download the XML
   or undo closing the period with the Cofnij rozliczenie button.)

## Zero declaration

If there were no sales or purchases in the reporting month, you still need to submit
a zero declaration:

1. **Rozliczenia** section → the **Nowe zerowe rozliczenie** button (top right corner).
2. Choose the period → **Dodaj rozliczenie**.
3. Then as usual: **Uzupełnij deklarację** → **Zapisz** → **Generuj i wyślij JPK_VAT**.

## Signing and sending

Sending goes through **Klient JPK_WEB**. Signing methods:

1. **Profil Zaufany** — a pz.gov.pl login window opens, you sign and wait for the
   automatic redirect back (don't close the window).
2. **Kwota przychodu** (dane autoryzujące) — for individuals only: NIP, first name,
   last name, date of birth, and **the income amount from the PIT declaration for the
   year two years before the year of sending** (e.g. when sending in 2026 — the income
   from the PIT for 2024).
3. **Podpis kwalifikowany** — for holders of a qualified signature.

After signing — **Wyślij**. The Podsumowanie screen will show a **Numer referencyjny**
(save it) and you'll get an e-mail notification.

!!! warning "Sent ≠ accepted"
    A successful send doesn't yet mean successful processing. The confirmation is status
    **200 «Przetwarzanie dokumentu zakończone poprawnie. Wygenerowano UPO»**.

## Downloading the UPO

UPO (Urzędowe Poświadczenie Odbioru) is the official confirmation that the declaration
was accepted:

- in e-mikrofirma: **Lista JPK → JPK_VAT** → next to the sent document, the
  **Pobierz UPO** button → Pokaż PDF / Pobierz XML;
- in Klient JPK_WEB: [Sprawdź status][4] → enter the Numer referencyjny → **Sprawdź** →
  Pobierz PDF / XML.

## Korekta

If you found an error after sending:

1. **Rozliczenia** → **Cofnij rozliczenie** (the status changes to Cofnięte).
2. Make the corrections in the invoices/declaration.
3. **Generuj i wyślij JPK_VAT** again — the file will be sent with cel złożenia **2**
   (correction), and the original document gets the **Skorygowane** status.

## Sending a ready XML (Klient JPK_WEB)

If you generate JPK_V7M in another program (or your accountant sent you an XML),
you can send it without e-mikrofirma — directly via [Klient JPK_WEB][2]:

1. On the **Wyślij dokumenty** screen, drag and drop the .xml file (or **+ Dodaj pliki**).
2. **Dalej** → **Podpisz dokumenty** (the signing methods are the same — see above).
3. **Wyślij** → save the Numer referencyjny → download the UPO after processing.

## Common errors

| Code | What it means | What to do |
|---|---|---|
| 401 | Weryfikacja negatywna — the file doesn't match the XSD schema | Check the file structure (current JPK_V7M schema) |
| 407 / 411 | This document was already sent (duplicate) | Nothing — the declaration is already accepted; to fix something, send a korekta |
| 412 / 413 | Encryption / checksum error | Send the file again |
| 419 | Błąd w danych autoryzujących | Check the first name, last name, date of birth, NIP, and kwota przychodu (PIT for the year before last) |
| 420 | No valid UPL-1 power of attorney | Sign with your own profile, not someone else's, or file a UPL-1 |

[1]: https://www.podatki.gov.pl/podatki-firmowe/jednolity-plik-kontrolny/jpk_vat-z-deklaracja/pliki-do-pobrania
[2]: https://e-mikrofirma.mf.gov.pl/jpk-client/
[3]: https://urzadskarbowy.gov.pl/
[4]: https://e-mikrofirma.mf.gov.pl/jpk-client/status
