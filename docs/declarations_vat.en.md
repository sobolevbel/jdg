---
title: VAT Declarations and JPK for JDG
description: How to file JPK_V7M, VAT-UE and VAT-9M for a sole proprietorship in Poland — deadlines, zero declarations, submitting via infakt and wfirma
tags:
  - Declarations
  - VAT
  - Taxes
---

# VAT Declarations

VAT = Value Added Tax.

!!! warning "KSeF becomes mandatory in 2026"
    Starting in 2026, Poland is phasing in the mandatory **KSeF** (Krajowy System e-Faktur) —
    the national electronic invoicing system:

    - from **February 1, 2026** — companies with sales above 200 mln zł (in 2024) must issue
      e-faktury. From the same date, **all** entrepreneurs must **receive** invoices via
      KSeF — regardless of size or VAT status;
    - from **April 1, 2026** — everyone else must issue e-faktury too, **including those
      exempt from VAT** (zwolnieni podmiotowo and przedmiotowo);
    - from **January 1, 2027** — the smallest businesses (invoiced sales up to 10 000 zł
      brutto per month) — until that date they can keep issuing invoices the old way.

    Until December 31, 2026 a transition period applies: no penalties for violations,
    invoices from cash registers outside KSeF and the offline24 mode are allowed. inFakt
    and wFirma are integrated with KSeF — invoices are sent to the system automatically.
    Details at [ksef.podatki.gov.pl][1].

## VAT (Polish)

Active VAT payers (czynny płatnik VAT) are required to submit a monthly (JPK_V7M) or quarterly (JPK_V7K)
JPK_VAT declaration that reflects your sales and purchases with VAT.

Article on [biznes.gov.pl][2] about VAT declarations.

### When to submit the declaration

The JPK_V7M declaration must be submitted by the 25th of each month for the previous month. For example, the July declaration must be submitted by August 25th. If the 25th falls on a weekend, the deadline moves to the next business day.

!!! info "Zero JPK"
    Even if there were no transactions in the reporting month, you still need to submit a zero VAT declaration.
    In the PodatekNalezny and PodatekNaliczony fields, enter "0.00".

### Which software to use

You can use any software that supports generating/submitting VAT declarations, for example:

* [e-mikrofirma][3] from the Ministry of Finance — free, see [our guide][4].
* inFakt
* wFirma

### How to submit the declaration

??? info "Free: e-mikrofirma"
    The official free application from the Ministry of Finance. Works both for zero
    declarations and for sending a ready XML generated in another program.
    See [Submitting JPK_V7M via e-mikrofirma][4].

??? info "inFakt users"
    In inFakt you can submit the declaration directly from the app.
    See [Submitting the VAT JPK_V7M declaration][5].

??? info "wFirma users"
    In wFirma you can submit the declaration directly from the app.
    Path: Podatki - JEDNOLITY PLIK KONTROLNY - dodaj
    It automatically calculates everything and generates the declaration. Then you need to submit it by confirming with the income amount from the PIT declaration filed the previous year.
    [wFirma instructions for JPK VAT][6] in Polish.

### VAT on rent

How to account for VAT in inFakt when renting out property?

- [Answer][7] on Telegram
- [Clarification from an accountant][8] on Telegram

Coming soon...

### VAT deduction on purchases

<!-- Section based on community experience (issue #116). VAT payers, please verify
and extend it based on your own experience. -->

If you are a czynny VAT payer, VAT on purchases for your business (laptop, phone,
software, etc.) can be deducted:

1. You buy the goods/service for the business — the seller issues a VAT invoice with your NIP.
2. You enter the invoice into the expenses of your accounting software (in inFakt — the
   Koszty section), specifying netto/brutto and the VAT rate from the invoice.
3. When preparing the monthly JPK_V7M declaration, the software automatically reduces
   the VAT payable (podatek należny) by the VAT amount from your purchases (podatek naliczony).
4. If the VAT on purchases exceeded the VAT on sales, the excess (nadwyżka) can be carried
   over to the next period or refunded to your account — you specify the method in the
   JPK_V7M declaration itself (a refund usually takes up to 60 days).

!!! note "For those on ryczałt without VAT"
    If you are not a VAT payer, you cannot deduct VAT. On ryczałt, expenses don't affect
    the tax base at all — tracking koszty only makes sense on skala podatkowa and
    podatek liniowy.

### WNT: buying goods from the EU (reverse charge)

<!-- Based on community experience (issue #116); screenshots of WNT bookkeeping in wFirma:
https://t.me/JDG_PBH/490707 -->

WNT (wewnątrzwspólnotowe nabycie towarów) is a purchase of goods from a counterparty in
another EU country (for example, an iPhone from the German Apple Store) under the reverse
charge mechanism:

1. **Before the purchase** you must be registered in VIES (the VAT-UE registry) — otherwise
   the seller won't be able to issue an invoice without VAT. Registration is done via VAT-R
   (see [VAT-UE registration][9]).
2. The seller issues an invoice **without VAT** (netto price) to your EU-NIP
   (with the PL prefix).
3. In your accounting software, the purchase is entered into expenses with a 23% VAT rate.
   The seller's NIP must be entered as EU (not PL). In inFakt, a counterparty can't be
   looked up automatically by an EU number — enter the details manually.
4. For the month of the purchase, **two** declarations are submitted:
    - **VAT-UE** — it will contain the netto amount of the purchase;
    - the regular **JPK_V7M** — the goods will appear both in the sales register and in the
      purchase register: it's as if 23% VAT was charged to you (like on a sale) and
      immediately deducted (like on a purchase). The total is 0 zł — nothing extra to pay.

Bottom line: the goods are bought at netto, without VAT. wFirma instructions in Polish:
[invoice recognition][10], [accounting for goods purchased from the EU][11].

## VAT-UE

EU VAT payers (VAT UE, registered in the VIES registry) are required to submit a VAT UE declaration for the months in which they earned income for services provided to EU counterparties.
The VAT-EU declaration includes the counterparty's VAT-EU number and the amount of services rendered.

### When to submit the declaration

The declaration is submitted electronically to the tax office by the 25th of the month following the month in which the tax obligation arose for the transaction or in which goods were moved or changes were made under the call-off stock procedure.

!!! info "Zero VAT UE"
    "Zero" means nothing is filled in at all — it's empty. You don't have to submit one. If you did submit it anyway, no big deal.

In [art. 100 ust. 1][12] ustawy o VAT, the cases requiring VAT-UE submission are listed.

### How to submit the declaration

See [Electronic VAT forms][13] on the official tax office website.

### Correction

VAT-UEK is used to correct a previously submitted VAT-UE declaration.

Coming soon...

[1]: https://ksef.podatki.gov.pl/etapy-wdrozenia-ksef/
[2]: https://www.biznes.gov.pl/pl/portal/00237
[3]: https://e-mikrofirma.mf.gov.pl/jpk-form/
[4]: declarations_jpk_emikrofirma.md
[5]: infakt_routine.md#submitting-the-vat-jpk-v7m-declaration
[6]: https://pomoc.wfirma.pl/-jpk-vat-jednolity-plik-kontrolny-dla-rejestrow-vat
[7]: https://t.me/JDG_PBH/547209
[8]: https://t.me/JDG_PBH/547215
[9]: registration_vat_ue.md
[10]: https://pomoc.wfirma.pl/-odczytywanie-faktur-z-telefonu
[11]: https://pomoc.wfirma.pl/-jak-zaksiegowac-zakup-towarow-od-kontrahenta-z-ue
[12]: https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/podatek-od-towarow-i-uslug-17086198/art-100
[13]: https://www.podatki.gov.pl/podatki-firmowe/vat/formularze/#VAT-UE
