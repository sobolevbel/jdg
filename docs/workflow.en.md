---
title: JDG workflow — monthly obligations
description: What to do each month as a JDG — issuing invoices, paying taxes, ZUS DRA, JPK. Deadlines and step-by-step procedure
tags:
  - Accounting
  - JDG
  - Declarations
---

# Typical workflow for routine sole proprietorship operations

As a JDG, you are obligated to issue an invoice (faktura) every month if you provided services to a client, and to pay your taxes.

!!! abstract "Taxes are paid every month"

    !!! abstract "ZUS"
        Pay ZUS and submit [ZUS DRA][14] by the 20th of each month

    !!! abstract "Podatek dochodowy"
        Income tax — due by the 20th of each month

    !!! abstract "VAT"
        If you provide services to a person or entity within Poland — due by the 25th of each month

    !!! abstract "VAT-UE"
        If you provide services to a person or entity within the EU — due by the 25th of each month

## Plan

1. You provide the service.
2. You issue an invoice (faktura) to the client.

In general, the client does not need to include anything specific in the payment reference. However, it is said that including the invoice number in the bank transfer makes life easier in case of a tax audit.

In the invoice you can describe something like: invoice for "month" and a few line items such as bug fixes, microservice implementation, etc. — roughly 3–4 items.

In the `Nazwa towaru lub usługi` (name of goods or service) field, you can specify, for example, `Software development / Tworzenie oprogramowania (PKWiU 62.01)`.

3. You receive payment into your business bank account.
4. You pay all required taxes and keep the receipts:
    - podatek dochodowy (income tax)
    - ZUS (social security contributions)
    - VAT: if applicable, you can deduct input VAT from purchases against the total VAT owed. [Details][1]

A more detailed description of specific operations using the `infakt.pl` service as an example can be found [here][2].

## Accounting for exchange rate differences

1. [Article by inFakt][3]
2. [Article by Poradnik Przedsiębiorcy][4]
3. [Guide on recording exchange rate differences in inFakt][5]

For a JDG, exchange rate differences (różnice kursowe) arise in two cases:

1. [Transakcyjne różnice kursowe][6] (transactional exchange rate differences)
2. [Różnice kursowe od środków własnych][7] (exchange rate differences on own funds)

In the second case, three methods are used — FIFO, LIFO, and weighted average — where incoming payments to the account form the queue.
The calculation method cannot be changed during the tax year.

Exchange rates are taken from the [Narodowy Bank Polski][8] (National Bank of Poland).

## Filing the VAT-UE declaration

Filing the VAT-UE e-declaration is done on the tax office website using an [interactive PDF form][9].

- First, you need to install Adobe Reader and its extension from [here][10].
- On the same page at the bottom there are instructions. In short: download the PDF form, open it in Adobe Reader with the
    installed extension, fill out the form, and use the extension's wizard to sign with your personal data and submit.
- At the end of the wizard there will be a link to download the UPO (confirmation of submission).

## What documents to keep

You need to retain accounting documentation and documents related to social insurance (ZUS).

Printing and storing paper copies is NOT required.
In Poland, a sole proprietor may keep documentation in electronic form, provided it can be easily printed in chronological order if needed.
Therefore, archive this documentation in the cloud for yourself, in case of an audit.

**Retention period: until the end of the current calendar year + 5 full calendar years. Even if you close the JDG.**
Documents related to employee activity require a longer retention period — 10 years, and in some situations this can reach 50 years.

List of documents:

- The main document for ryczałt is the `ewidencja przychodów` (revenue ledger). Your accountant fills it out.

- Additionally, you need to keep documents confirming sales (faktury that you issue) and purchases (faktury issued to you when purchasing goods and services for the business; if there is no faktura, a receipt or ticket can serve as a substitute).

- For czynny podatnik VAT (active VAT taxpayer): JPK_V7M (monthly) or JPK_V7K (quarterly). These also need to be retained. You cannot download them from the tax office website.

- VAT declarations, if applicable: VAT UE, VAT-9M, VAT-8, etc.

- Dowody wewnętrzne (internal evidence documents) — this type of document is used, for example, to record exchange rate differences that arise when you receive payment in a foreign currency.

- Some sole proprietors may also have an [ewidencja środków][11] trwałych (register of fixed assets) — buildings, cars, devices, and other items such as an expensive laptop purchased for the business. [More details][12].

- Some may have an ewidencja przebiegu pojazdów (vehicle mileage log) — for a car registered to the business.

- In addition, another large group of documents that need to be retained are declarations and reports submitted to ZUS. You will most likely have ZUS ZZA, ZUS ZUA, ZUS ZCNA, the monthly ZUS DRA, and during the "holiday" month also [ZUS RCA][13]. Do not rely on the ZUS website — people have reported in the chat that they were unable to download documents older than two years from it.

- The annual PIT declaration (though it can be easily downloaded from the Polish tax office website).

- Documents that confirm the tax deductions (ulgi) you claimed in your annual PIT declaration. These could be invoices for internet service or confirmation of charitable donations, for example.

- For electronic documents submitted to the tax office or ZUS via the internet, you need to keep proof of submission: UPO for PIT, UPP for ZUS DRA.

[1]: faq.md#vat
[2]: infakt_routine.md
[3]: https://www.infakt.pl/blog/jak-zaksiegowac-roznice-kursowe
[4]: https://poradnikprzedsiebiorcy.pl/-ryczalt-a-roznice-kursowe
[5]: infakt_routine.md#receiving-payment-and-accounting-for-exchange-rate-differences
[6]: https://pomoc.ifirma.pl/pomoc-artykul/transakcyjne-roznice-kursowe-u-ryczaltowca
[7]: https://www.ifirma.pl/blog/roznice-kursowe-od-srodkow-wlasnych-a-ryczalt.html
[8]: https://www.nbp.pl/home.aspx?c=/ascx/archa.ascx
[9]: https://www.podatki.gov.pl/vat/e-deklaracje-vat/formularze-vat/#VAT-UE
[10]: https://www.podatki.gov.pl/e-deklaracje/wtyczka-do-podpisywania-i-przesylania-danych-xml-z-interaktywnych-formularzy-pdf/
[11]: https://stat.gov.pl/metainformacje/slownik-pojec/pojecia-stosowane-w-statystyce-publicznej/938,pojecie.html
[12]: https://poradnikprzedsiebiorcy.pl/-ewidencja-srodkow-trwalych
[13]: https://sobolevbel.github.io/jdg/zus_vacation/#ezhemesiachnye-otchioty-vo-vremia-zus-kanikul
[14]: declarations.md#zus-dra
