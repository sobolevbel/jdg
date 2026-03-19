---
title: Monthly Operations in wfirma.pl
description: Monthly routine for a sole proprietor on ryczałt in wfirma.pl — issuing invoices, paying ZUS, submitting ZUS DRA, JPK_V7M, VAT-UE
tags:
  - Accounting
  - wfirma
  - Declarations
---

# Routine Operations for a Sole Proprietor (Monthly) Using wfirma.pl

This document covers the typical monthly operations for a sole proprietor on ryczałt in wfirma.pl.
The minimum wFirma setup is described [here][1].

## Issuing Invoices

On the last day of the month (if you have a monthly billing agreement with your client), or upon completion (delivery) of work, you need to generate and issue an invoice to your client.

1. Go to the main page.
2. Click Wystaw fakturę (Issue an invoice).

![2]

You can also do this on the **Przychody - Sprzedaż** page. The Wystawianie faktury window will open.

### Podstawowe informacje

(Basic information)

1. Select the counterparty you're invoicing (from the Nabywca dropdown). The address and NIP or VAT UE number will be pulled automatically from the directory.
2. Data wystawienia — the invoice issue date. "Today" or a date in the past.
3. Data sprzedaży — the sale date, i.e. the date the service was provided (last day of the month, or the actual date of service if it's irregular).

    > Nieprzerwane usługi mogą być rozliczane w ustalonych z góry okresach rozliczeniowych, takich jak miesiąc lub kwartał – w takim przypadku za datę powstania przychodu uznaje się ostatni dzień okresu rozliczeniowego określonego w umowie lub na wystawionej fakturze, ale nie rzadziej niż raz w roku.

    Source: [point 1e from Art. 14.](https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/podatek-dochodowy-od-osob-fizycznych-16794311/art-14#:~:text=za%20dat%C4%99%20powstania%20przychodu%20uznaje%20si%C4%99%20ostatni%20dzie%C5%84%20okresu%20rozliczeniowego%20okre%C5%9Blonego%20w%20umowie)

4. Termin płatności — choose the payment deadline if needed. It's counted from the invoice issue date.
5. Metoda płatności — choose the payment method. This is auto-filled when you select a counterparty from the form.
6. Select the product (Produkt). In our case — a service. The rest of the data will be filled automatically from the product catalog (or enter it manually).
7. Net price (Cena netto on a VAT invoice) or just price (Cena on a non-VAT invoice).
8. (for ryczałt) The tax rate corresponding to the PKWiU code of the service provided.
9. If you're exporting a service to a legal entity (company) with an office in the EU or outside the EU (i.e. not to Poland and not to an individual), the invoice must include the following note:

    > Do rozliczenia podatku VAT zobowiązany jest nabywca usługi (odwrotne obciążenie). Reverse charge - VAT is charged to the buyer.

    or simply:

    > "Odwrotne obciążenie / Reverse charge".

    For a more detailed explanation, see [the page dedicated to VAT][4].
    In the screenshot we added the note manually, but in fact wFirma adds this note automatically if you select the correct Schemat księgowy (more on this below).

10. Rabat — in theory, you can specify a discount in this field.
11. Want to list multiple services on one invoice? Click "Nowy wiersz" — a new row will appear. Repeat steps 6-10.

![3]

### Księgowe

(Accounting)

1. Schemat księgowy — Select the accounting scheme, which depends on whom and to which country you provide the service.

    ![5]

    !!! example "Export within the EU"
        For example, you need to select "Świadczenie usług w UE" if you're exporting a service under art. 28b ustawy o VAT (e.g. IT or marketing services) to a legal entity (company) with an office in another EU country (not Poland).

    !!! example "Export outside the EU"
        And if you're exporting a service to a legal entity (company) with an office outside the EU (e.g. the US or the UK), you need to select "Świadczenie usług poza UE".

    In each case, wFirma will automatically add "Odwrotne obciążenie / Reverse charge" to the printed version of the invoice (double-check after saving):

    ![6]

### Zaawansowane

(Advanced settings)

1. Select the payment currency (Waluta).

    !!! danger "Warning"
        If you changed the currency, make sure the price on the Podstawowe informacje tab hasn't been converted — otherwise fix it.

2. Specify the bank account to receive payment (Rachunek).
3. You can choose the invoice language (Język), e.g. Polish-English as in the screenshot.

![7]

Click Zapisz to save. The invoice is saved!

## Printing the Invoice

Depending on your account settings and what you did in the previous step, the new invoice may exist in **draft** status.
Now we need to print the invoice so it moves to "confirmed" status and is definitely recorded in wFirma's accounting. You can also do this when issuing the invoice by clicking Zapisz i drukuj.

1. Go to Przychody - Sprzedaż.
2. Select the invoice from the table.
3. Click Drukuj.
4. Click Dalej.

![8]

The invoice file will download — now you can send it to the client. It's [a good idea to save][9] it somewhere for yourself.

## Receiving Payment and Accounting for Exchange Rate Differences

When the money arrives in your account, you need to record the incoming payment.

1. Go to Przychody - Sprzedaż.
2. Select the invoice from the table.

    ??? info "About filters"
        If you don't see the invoice in the table, switch to the year and month when the invoice was issued using the controls below the table.
        ![35]

3. Go to the Płatności tab.
4. Click Dodaj.
5. Enter the date the money was received (Data płatności).
6. In the Metoda płatności field, select the payment type — przelew.
7. Enter the amount (Kwota). If the invoice is for $1000 but $10 less arrived due to intermediary bank fees, still enter the full amount ($1000) so the invoice shows as "fully paid".
8. Click Zapisz.

![10]

When receiving payment in a foreign currency, exchange rate differences may arise. The law requires you to account for exchange rate differences — both positive and negative.

Make sure you've enabled the [exchange rate difference calculation feature][12] before adding the incoming payment.

After recording the payment, do the following:

1. Go to Przychody - Różnice kursowe.
2. Select the invoice from the table.

    ??? info "About filters"
        If you don't see the invoice in the table, switch to the year and month when the invoice was issued using the controls below the table.
        ![35]

3. Click Wystaw DW (exchange rate differences are recorded in accounting with a special document called "Dowód Wewnętrzny").

![11]

Done, the exchange rate difference has been added and will be taken into account when calculating the tax base.

??? question "How do I find all my exchange rate DWs in my accounting?"

    On the same page, to see the full list of your DWs, you can clear all filters below the table: Rok, Miesiąc and Status.

    ![36]

## Calculating and Paying Taxes

### PIT

1. On the main page, if you've set up the dashboard correctly, you'll see a panel like this. Click Wylicz. You can also do this by going to Start - Podatki and clicking Wylicz podatek.

    ![13]

2. In May we pay for April. That's why on the screenshot the Miesięczna zaliczka na podatek dochodowy window shows Okres as Miesiąc: Kwiecień and Rok: 2025. Select the previous month and click Dalej.

    ![14]

3. Leave everything as is:
    * Stawka ryczałtu — for ryczałt, the system will use the tax rate specified on the invoices.
    * Składki społeczne do odliczenia od przychodu — The system will deduct 100% of the social insurance contributions actually paid to ZUS in the previous month. While you're on Ulga na Start, you're exempt from social insurance contributions, so "Razem 0,00" as in Example 1's screenshot is normal.
    * Składki zdrowotne do odliczenia od przychodu — The system will deduct 50% of the health insurance contributions actually paid to ZUS in the previous month. The first time you'll see "Razem 0,00" — this is normal. If this month you pay 461.66 zł for health insurance, then next month expect to see 230.83 zł in this field.

    ???+ example "Example 1: Report for the first month of business activity"
        Everything is zero and that's expected.
        ![15]

    ??? example "Example 2: A regular month of bookkeeping in wFirma (Duży ZUS)"
        As expected, the system automatically pulls 100% of the social insurance contributions actually paid to ZUS in the previous month and 50% of the health insurance contributions actually paid to ZUS in the previous month.
        You didn't forget to mark ZUS DRA as paid, right?
        ![37]

    ??? example "Special case: starting bookkeeping in wFirma not from the very beginning of JDG registration"
        You need to fill in manually. Take the amount of contributions actually paid to ZUS in the reporting month:

        * Enter 100% społeczne (Emerytalna + Rentowa + Wypadkowa + Chorobowa, WITHOUT składki Na Fundusz Pracy!) in the "Składki społeczne do odliczenia od przychodu" field. In the screenshot, 1518.98 zł corresponds to the ZUS for entrepreneurs on ryczałt without benefits for December 2025.
        * Enter 50% zdrowotnej in the "Składki zdrowotne do odliczenia od przychodu" field. In the screenshot, 384.72 zł corresponds to half the ZUS for entrepreneurs on ryczałt with annual income from 60,000 to 300,000 zł in 2025.

        ![33]

    * Click Zapisz to save.

4. If the amount matches your expectations, click Zapłać to pay. Payment deadline: by the 20th of the month following the reporting month.

    ![18]

5. If the amount doesn't match your expectations, double-check the calculations (wFirma shows them step by step) and click Modyfikuj to make changes.

5. If the amount doesn't match your expectations, double-check the calculations (wFirma shows them step by step) and click Modyfikuj to make changes.

### ZUS

1. On the main page, if you've set up the dashboard correctly, you'll see a panel like this. Click Wylicz. You can also do this by going to Start - ZUS and clicking Wylicz podatek.

    ![16]

2. In the Dodawanie deklaracji ZUS DRA window, check everything:

    ![17]

    ??? info "Comments on the screenshot"
        The Podstawowe tab contains the basic settings.
        Typically, the ZUS DRA report is prepared for the previous month. For example, in May we report for April. That's why the corresponding dates are selected in the screenshot.
        In our example, we don't check the "Roczne rozliczenie składki zdrowotnej" checkbox because the JDG is on ryczałt and didn't conduct business activity in the previous year.

    * Miesiąc, Rok — the reporting month and year.
    * Data wypełnienia — the date of completion.
    * Roczne rozliczenie składki zdrowotnej — Annual health insurance contribution settlement (for the previous year).
        This is a special checkbox that only appears in the form for **April**.

        ??? note "When do you NOT need to check this box?"

            * If you're on ryczałt and started business in January, February, March, or April of the current year.
            * If you're on podatek liniowy or skala podatkowa and started business in February, March, or April of the current year.
            * (rare exception) If you calculate składka zdrowotna under some special rules that don't require you to prepare an annual settlement.

            It's important to understand that ZUS counts the insurance year in its own way, and it doesn't coincide with the calendar year for all tax systems. That's why these conditions are non-obvious.

        ??? note "When do you need to check this box?"

            In all other cases. I.e. if you conducted business activity in the previous year.
            It's quite possible that a ZUS surcharge awaits you based on the calculation results.
            Read more in the wFirma article: [Roczne rozliczenie składki zdrowotnej][38].
            ![39]

    ??? note "Advanced settings"

        On the Zaawansowane tab, you can indicate that you have a ZUS holiday in the reporting month (Wakacje składkowe checkbox).

        It's also worth checking that the selected method for calculating health insurance contributions (Sposób wyliczenia składki zdrowotnej) matches what you chose at the beginning of the year. If it's the beginning of the year, you're preparing ZUS DRA 01/20YY, and last year you conducted business activity the full year from start to finish, now is the time to make this choice. Pick whichever you prefer, but remember that the chosen method is locked in until the end of the current year.

        ![34]

        The expected settings for beginning entrepreneurs as shown in the screenshot: "Sposób: Standardowy - na podstawie bieżącego przychodu", and "Wakacje składkowe" is unchecked.

    When ready, click Zapisz to save.

    ??? note "Advanced settings"
        On the Zaawansowane tab, you can indicate that you have a ZUS holiday in the reporting month (Wakacje składkowe checkbox).
        It's also worth checking that the selected method for calculating health insurance contributions (Sposób wyliczenia składki zdrowotnej) matches what you chose at the beginning of the year. If it's the beginning of the year, you're preparing ZUS DRA 01/20YY, and last year you conducted business activity the full year from start to finish, now is the time to make this choice. Pick whichever you prefer, but remember that the chosen method is locked in until the end of the current year.

        ![34]

        The expected settings for beginning entrepreneurs as shown in the screenshot: "Sposób: Standardowy - na podstawie bieżącego przychodu", and "Wakacje składkowe" is unchecked.

3. Click Zapisz to save.

4. If the amount matches your expectations, click Zapłać to pay. Payment deadline: by the 20th of the month following the reporting month. The screenshot shows **ZUS = 461.66 zł**. That's exactly how much the first ZUS payment comes to for entrepreneurs on ryczałt who use the Ulga na Start benefit in 2025.

    ![19]

    !!! note "ZUS increase"
        In 2026, the first ZUS payment on ryczałt went up to **498.35 zł**. Składka zdrowotna is tied to the average salary in Poland.

4. If the amount doesn't match your expectations, you need to investigate...

    * Double-check the parameters selected in the previous step: click Modyfikuj → Zaawansowane tab
    * Double-check the health insurance contribution calculations (wFirma shows them step by step): click Modyfikuj to make changes → Zaawansowane tab → uncheck "Automatyczne wyliczenie miesięcznej składki zdrowotnej"
    * Cross-reference with the [Składki ZUS][41] website (ryczałt, 2026)
    * Double-check the [ZUS settings][40] in your account.

!!! note "ZUS increase"
    In 2026, the first ZUS payment on ryczałt went up to **498.35 zł**. Składka zdrowotna is tied to the average salary in Poland.

## Submitting Declarations

### VAT UE (VAT-UE, VAT EU, VAT-EU)

If you provide services to a person within the EU territory, you're required to have a VAT UE registration and submit monthly declarations.
Those who had no EU clients last month can safely skip this section.

1. Click Generuj.

    ![20]

2. In May we report for April. That's why on the screenshot the Dodawanie informacji VAT-UE window shows Rok: 2025 and Miesiąc: Kwiecień. Verify that the previous month is selected and click Dalej.

    ![21]

3. Click Wyślij.

    ![22]

4. In the Wysyłanie deklaracji do urzędu skarbowego window, on the "Bez podpisu" tab, enter your personal details and the income amount from last year's PIT declaration. `0` if you didn't file one back then. Click Wyślij do urzędu to submit VAT UE to the tax office.

    ![23]

Note on the screenshot: to sign VAT UE in 2025, we need to find the PIT that was filed in 2024, i.e. the income declared in it was for 2023.

After submission, check the status. Go to Start - Podatki - Podatek VAT. If it's green, everything is fine — the tax office received your declaration.

![24]

### ZUS DRA

To submit the ZUS DRA declaration from wfirma, you first need to [verify your profile][31].

!!! info
    It's worth noting that verification is not mandatory. wFirma provides one year of free use upon registration. If you don't verify your profile, after a year you can register again and get another free year (assuming the promotion is still available). Whether it's worth the effort — that's up to you. However, in that case you'll need to download the ZUS DRA file yourself and upload it to the ZUS portal. To do this, in the "Deklaracje, zeznania i JPK" block, click "ZUS DRA", and in the window that appears, click "Eksportuj deklarację ZUS". Then import the downloaded XML file (zus_kedu.xml) to the ZUS portal as described in the example with [infact, step 2][32].

After verifying your profile, follow these steps:

1. Click Wyślij.

    ![25]

2. In the Wysyłanie deklaracji do ZUS window, on the "Podpis - wfirma.pl" tab, click Zleć do podpisu i wysyłki to submit the ZUS DRA for signing and sending.

    ![26]

After submission, check the status. Go to Start - ZUS - Deklaracje rozliczeniowe. If there's a green icon and the status is "Przesyłka przyjęta do ZUS", everything is fine — ZUS has accepted the declaration.

![27]

You can also verify this on the ZUS portal under ePlatnik - Dokumenty - Dokumenty w ZUS, but the record may not appear there immediately — it can take at least a few days.

### VAT

...

## Exchange Rate Differences from Own Funds (od środków własnych)

If you receive payment in a foreign currency and sell it later for expenses related to your business activity, for example to pay taxes, you also need to account for [exchange rate differences][28] from own funds (środków własnych). For the calculation, we'll use a [calculator][30] and the LIFO method (choose FIFO or LIFO for yourself).

1. Click Przychody.
2. Click Inne przychody.
3. Click Dodaj inny przychód and select Pozostałe przychody (DW).
4. In the Dodawanie nowego dowodu wewnętrznego window, on the Podstawowe informacje tab, fill in Nazwa przychodu. Sample text for a positive exchange rate difference:

     > Dodatnia różnica kursowa. Rozliczenie różnic kursowych od środków własnych, 100 USD, Data wpływu środków: 2025-05-06, Kurs wpływu środków: 3.775200 (085/A/NBP/2025), Data wypływu środków: 2025-05-12, Kurs wypływu środków: 3.812400 (faktyczny)

5. Enter the amount.
6. Click Zapisz i drukuj to save and print.

![29]

Done, the exchange rate difference has been added and will be taken into account when calculating the tax base.

[1]: wfirma_settings.md
[2]: images/wfirma_routine/wystaw_fakture.png
[3]: images/wfirma_routine/wystaw_fakture_main.png
[4]: faq.md#vat
[5]: images/wfirma_routine/wystaw_fakture_ksiegowe.png
[6]: images/wfirma_routine/wystaw_fakture_vat_comment.png
[7]: images/wfirma_routine/wystaw_fakture_zaawansowane.png
[8]: images/wfirma_routine/fakture_drukuj.png
[9]: workflow.md#what-documents-to-keep
[10]: images/wfirma_routine/fakture_oplata.png
[11]: images/wfirma_routine/fakture_kr.png
[12]: wfirma_settings.md#podatki-funkcje-ksiegowe
[13]: images/wfirma_routine/pit_wylicz.png
[14]: images/wfirma_routine/pit_dalej.png
[15]: images/wfirma_routine/pit_zapisz.png
[16]: images/wfirma_routine/zus_wylicz.png
[17]: images/wfirma_routine/zus_zapisz.png
[18]: images/wfirma_routine/pit_oplata.png
[19]: images/wfirma_routine/zus_oplata.png
[20]: images/wfirma_routine/vat_eu_generuj.png
[21]: images/wfirma_routine/vat_eu_dalej.png
[22]: images/wfirma_routine/vat_eu_wyslij.png
[23]: images/wfirma_routine/vat_eu_wyslij_do_urzedu.png
[24]: images/wfirma_routine/vat_eu_status.png
[25]: images/wfirma_routine/zus_dra_wyslij.png
[26]: images/wfirma_routine/zus_dra_wyslij_confirm.png
[27]: images/wfirma_routine/zus_dra_status.png
[28]: workflow.md#accounting-for-exchange-rate-differences
[29]: images/wfirma_routine/kr_od_wlasnych_srodkow.png
[30]: https://kalkulatory.gofin.pl/kalkulatory/kalkulator-roznic-kursowych-od-wlasnych-srodkow-walutowych
[31]: wfirma_settings.md#company-verification
[32]: infakt_routine.md#preparing-the-zus-dra-declaration-and-paying-contributions
[33]: images/wfirma_routine/pit_miesięczna_zaliczka_na_podatek_dochodowy.png
[34]: images/wfirma_routine/zus_dra_zaawansowane.png
[35]: images/wfirma_routine/faktury_filtr_rm.png
[36]: images/wfirma_routine/kr_filtr_rms.png
[37]: images/wfirma_routine/pit_zapisz_2.png
[38]: https://pomoc.wfirma.pl/-roczne-rozliczenie-skladki-zdrowotnej
[39]: https://pomoc.wfirma.pl/images/fx/max/679774
[40]: wfirma_settings.md#podatki-zus
[41]: https://justandrei.github.io/jdg-tools/zus/
