---
title: PIT Declaration — Annual Tax Return for JDG
description: How to file an annual PIT-28, PIT-36, or PIT-36L declaration for a sole proprietor in Poland — step-by-step guide via e-Deklaracje and e-Urząd Skarbowy
tags:
  - Declarations
  - Taxes
  - JDG
---

# PIT Declaration

PIT is the personal income tax on individuals (podatek dochodowy od osób fizycznych).

Every entrepreneur who ran a business in the previous year is required to submit an annual tax declaration.

## Types of PIT Declarations

| Form | Who must file | Notes |
|-------------------|----------------------|-------------|
| PIT-28 | Entrepreneurs who used the **ryczałt** taxation system during the reporting year. Individuals who received rental income. | |
| PIT-36 | Entrepreneurs who used the general taxation system (**skala podatkowa** 12%/32%) during the reporting year. Employees with income from abroad or other sources | Option for joint filing with a spouse or child |
| PIT-36L | Entrepreneurs who used the flat-rate taxation system (**podatek liniowy**, 19%) during the reporting year | |
| PIT-37 | Employees who received income from employment (skala podatkowa 12%/32%) | Filled based on PIT-40A/PIT-11A or PIT-11 from the employer. Auto-generated and submitted on 30.04 at 23:59 if you don't send your own version to the tax office |
| PIT-38 | Individuals who received capital gains (crypto transactions, investments, dividends, interest on deposits in foreign banks, etc.) | Auto-generated and submitted on 30.04 at 23:59 if you don't send your own version to the tax office |
| PIT-39 | Individuals who received income from real estate sales | |

## Income from Multiple Sources

Situation: In the previous year I had income from my JDG taxed under the ryczałt system, and now I'll have income from other sources (say, a side gig) taxed under the general system (skala podatkowa). How do I calculate my income to determine the 12/32% tax rate? Can I use the tax-free allowance for employment income up to 30,000 zł if my total individual income exceeds 30,000 zł including ryczałt?

Answer: At year-end, Ryczałt is declared separately in PIT-28. Skala podatkowa 12/32% is declared separately in PIT-36 or PIT-37. Income under skala podatkowa and ryczałt is NOT combined!

> Jeżeli prowadzisz działalność gospodarczą opodatkowaną ryczałtem od przychodów ewidencjonowanych i jednocześnie osiągasz przychody z innych źródeł, na przykład z umowy o pracę, umowy zlecenia, umowy o dzieło, emerytury, najmu prywatnego opodatkowanego na zasadach ogólnych, albo z tytułu sprzedaży innych rzeczy, musisz odrębnie opodatkować i rozliczyć dochody z działalności gospodarczej oraz dochody osiągnięte z pozostałych tytułów.
> W tym przypadku dochody z działalności gospodarczej nie łączą się z dochodami uzyskanymi w ramach innych źródeł przychodów.

📚 Source: [Jak rozliczać przychody z różnych źródeł][78]

## Joint PIT

### Who Is Eligible to File a Joint PIT

A joint PIT can be filed by spouses if both of them use the general taxation system (Skala podatkowa w podatku dochodowym na zasadach ogólnych), do not use ryczałt, and have not signed a separate property agreement. Another condition is that the spouses were married for the entire year, or got married during the reporting year and were still married on the last calendar day of the year.

!!! danger "Important!"
    If at least one spouse files a non-zero PIT-28 (with JDG income under ryczałt), they cannot file PIT-37 or PIT-36 jointly.

PIT-28 with rental income is an exception that does not prohibit joint filing by spouses.

A joint PIT with a child can be filed by a parent or guardian raising a child alone (Osoba samotnie wychowująca dziecko).

!!! example "Example 1"
    Spouse-JDG on skala podatkowa + Spouse with no income = can file a joint PIT-36.

!!! example "Example 2"
    Spouse-JDG on skala podatkowa + Spouse-employee = can file a joint declaration (PIT-36 instead of PIT-37 in this case).

!!! example "Example 3"
    Spouse-JDG on ryczałt + Spouse with no income = CANNOT file a joint declaration. The JDG spouse declares income separately in PIT-28.

!!! example "Example 4"
    Spouse-JDG on ryczałt who also worked as an employee that same year + Spouse-employee = CANNOT file a joint declaration (even for the portion of income taxed under the general system). The employee spouse declares income in PIT-37. The JDG spouse files two declarations: PIT-28 for ryczałt and PIT-37 for employment (or PIT-36, if needed).

!!! example "Example 5"
    Spouse-JDG on ryczałt, business paused, zero income for the previous year + Spouse-employee = can file a joint PIT-37 (or PIT-36, if needed). The JDG spouse submits a zero PIT-28.

!!! info "Useful links"

    📜 Law: [Art. 6 - Podatek dochodowy od osób fizycznych][79].  
    📚 [Wspólne rozliczenie małżonków][80] - tax office website  
    📚 [Wspólne rozliczenie małżonków PIT][81] - e-pity  
    📚 [Osoba samotnie wychowująca dziecko][82] - tax office website  

## Ways to File PIT

* In person at the tax office
* Send a completed paper declaration by mail (list polecony or courier)
* Online via the Internet

In this guide we'll focus on online filing as the most efficient method.

## Software for Filing PIT

Choose a service based on your preferences and where you kept your books last year (full year). Here's a list of popular services:

| Service | Advantages | Disadvantages | Instructions |
|--------|--------------|------------|------------|
| [Twój e-PIT][83] | Government, official. Great for simple cases, e.g. PIT-37 with income from umowa o pracę. This guide has instructions for JDG. | Can get confused with foreign income, hard to automatically add it to the tax base. | [PIT-28 via Twój e-PIT](#pit-28-via-twoj-e-pit) |
| [e-pity][84] | A tried-and-true service, handles non-standard cases well. This guide has instructions for JDG. | - | [PIT-28 via e-pity for Android](#e-pity-for-android) |
| [fill-up][85] | Ideal for those who kept books in inFakt — allows automatic data import. Others can fill in manually. | - | [PIT in inFakt][88] |
| [pitroczny.pl][86] | A service for those who kept books in iFirma. | Opens late: approximately after March 9 | [Instructions for pitroczny.pl][89] in Telegram |
| [wFirma][87] | Can generate and submit PIT on its own, no intermediaries needed. | Only free during the first year for new clients | [Official PIT-28 instructions][90] |

## e-pity for Android

Here I'll explain how to submit a PIT-28 declaration using a JDG with the ryczałt taxation system as an example.
For other taxation systems the process may differ slightly, but overall it will be similar.

To create and submit the declaration we'll use the free app [**e-pity**][15],
specifically its Android version.

[:google-play: Google Play][13]

[:app-store: App Store][14]

### 0. Settings and the 1.5% Tax

This step is optional but still important.

You have the right to direct 1.5% of the tax you've already paid to any charitable organization.
If you don't do this, that percentage simply goes to the tax office, so it makes sense to fund
something you care about.

To be able to choose the organization you want, you need to check the boxes in the settings
as shown in the screenshot, and later provide the KRS number of the organization you want to send
your 1.5% to. If you don't check the boxes, the app will pick some default fund.

![e-pity settings: checkboxes for choosing the organization to receive 1.5% of your tax][16]

### 1. When to Submit

Officially, the annual declaration must be submitted **between February 15 and April 30** inclusive. In 2028
the deadline shifts to May 2, since April 30 falls on a Sunday and is followed by the public holiday on May 1.

In practice, you can submit as early as January, but declarations won't start being processed until February 15.
And of course, the earlier you submit, the sooner you'll get your tax refund.

Now press the big button to create your declaration.

![e-pity home screen with the button to create a new declaration][17]

### 2. Declaration Calculation Method

Here you can choose the calculation method. Options are:

- Individual calculation.
- Together with a spouse. Only available under the general taxation system. If your spouse
    doesn't work or earns little, this method lets you double your first tax bracket
    at the 12% rate. As a result, you should pay less tax or get a refund.
- Together with a spouse who died during the year. Same as above, with one exception.
- Single parent raising children.

Also, at this step you can choose whether to create a new declaration or correct an existing one.

![e-pity: choosing the settlement type (rodzaj rozliczenia) — individually, with a spouse, or as a single parent][18]

Below is an example of a declaration with individual tax calculation.

### 3. Personal Information

Here you need to fill in your details. Note that since you're filing as
an entrepreneur, you must provide your NIP, not PESEL. You also need to enter your
name, address, and select your tax office. If you have a karta dużej rodziny, enter it
here — your tax refund will come faster.

![e-pity: personal data form (dane podstawowe) — NIP, name, address, tax office selection][19]

### 4. Income Type

On the next screen you need to add your income. Press Pozostałe and choose your taxation system.

- General system: PIT-36
- Flat-rate system: PIT-36L
- Ryczałt: PIT-28

We'll choose ryczałt and PIT-28 as an example.

![e-pity: Przychody podatnika screen, Pozostałe button for adding income][20]

![e-pity: Dodaj przychody podatnika — choosing the tax system, Ryczałt (PIT-28) option][21]

### 5. Gross Income Amount

At this step you need to enter the full name of your business (which usually matches your
name), and the gross income amount excluding VAT in PLN for the entire year at the appropriate rate.
If you worked at different rates, enter the corresponding amounts in the appropriate fields.

![e-pity: Przychody form — company name and gross income amounts per ryczałt rate][22]

Press "Zapisz" to return to the [previous screen][23], where your income info
should now appear. Press Dalej.

### 6. ZUS Contributions

Next, fill in the ZUS contributions for 12 months in separate fields: social contributions (first field)
and health insurance (second field).
If you have **ulga na start** active, your social contribution will be 0. The app will automatically
calculate the deductible amount — half the health insurance contribution.

You can find your payments in the ZUS portal (Płatnik->Podział wpłat). To get data older than a year, use the "Zamów dane archiwalne" button (within 48 hours the requested data will appear on the same tab).

Note that you need to enter contributions actually paid during the reporting year.
Contributions paid in the new year (following the reporting year) should not be included, even if they're
December contributions — you'll include those in next year's PIT.

![e-pity: fields for yearly ZUS contributions — społeczne and zdrowotne][24]

### 7. Taxes Paid

On the next step, in the 12 fields "Kwoty ryczałtu należnego obliczone i wykazane w ewidencji (zaokrąglone do pełnych złotych)" you need to enter month-by-month the amounts of income tax due, calculated and recorded in the ewidencja (rounded to full złoty).
If you pay taxes quarterly, check the appropriate box.

There's a difference from ZUS payments here: you must enter the calculated tax amount in the field for the reporting month, regardless of the fact that you actually paid it the following month.

!!! example "Example 1"
    For July you owe 2,000 PLN in taxes. You actually paid it by August 20,
    but in the PIT you need to enter this tax in the July (lipiec) field.

!!! example "Example 2"
    For December you have 1,500 PLN in taxes, and you paid it by January 20 of the following year. But in the PIT
    you need to enter it in the December (grudzień) field.

It's possible that the amounts in your ewidencja don't match the amounts of tax actually paid (monthly advances). Accidentally overpaid? Made a mistake in the payment description? Or recalculated taxes at the end of the year and found an underpayment for previous months? Things happen.

At the very bottom of the form there's a field "Kwota wpłaconego ryczałtu za cały rok". By default, the "sum" checkbox (sumowanie kwoty za cały rok) is checked and the total paid tax is calculated automatically. Uncheck it if the amounts from your ewidencja don't match the payments made.
It's important to understand the difference:
- in the first 12 fields, the taxpayer enters how much they should have paid,
- and in the second-to-last field, how much they actually paid.

![e-pity: monthly ryczałt amounts and the Kwota wpłaconego ryczałtu za cały rok field][40]

Press Dalej.

### 8. Tax Reliefs and Deductions

On the next step you can use tax reliefs and deductions if you're eligible. Read about
each one and decide whether it applies to you.

![e-pity: list of available reliefs and deductions (ulgi)][25]

### 9. Internet Deduction

Among the reliefs there's an interesting one available to anyone in Poland — the internet
deduction. It lets you recover internet costs for the year up to 760 zł. You can
use it for any two consecutive years, once in your lifetime. You can't skip a year between those two —
if you used it last year, you must use it this year too.
Also, you cannot deduct internet costs if you already wrote them off as business expenses (on the general or
flat-rate taxation systems).

This deduction covers home and mobile internet as well as payments for
any other public internet, for example, in an internet cafe. You need to keep receipts or invoices for
all internet payments — they may sometimes be requested.

You can read more, for example, in the [PITax article on ulga internetowa][26], or just google "ulga na internet".

![e-pity: Ulga na internet form — choosing the relief year and entering the expenses amount][27]

Select the third checkbox if you haven't used the deduction before, or the first one if you used it
last year. In the field, enter the total of all your internet costs for the year.

### 10. Additional Information

The next step covers specific edge cases that people might encounter.
Nothing applies to me, so I just press Dalej.

![e-pity: Dodatkowe informacje screen with special-case options][28]

### 11. Debtors and Creditors

Next you can enter information about your debtors and creditors. I don't have any, so
I just move on.

![e-pity: Dłużnicy i wierzyciele screen — information about debtors and creditors][29]

### 12. Enter Your Bank Account for the Refund

![e-pity: bank account (rachunek) and owner name fields for the tax refund][41]

Enter your account number and name. You can use any account — it doesn't have to be your business one.
If the account is shared with your spouse, you need to enter the names of all account holders.

### 13. Donate 1.5% of Your Paid Tax to Charity

On the next step you can specify a fund to receive 1.5% of the tax you've already
paid. You don't need to pay anything extra. You can opt out and the 1.5%
will simply go to the tax office, but it's better to help someone — it's a great opportunity.

To direct 1.5% of your tax to a fund, you need to enter its KRS number. You can find funds
helping children, animals. There are funds supporting Ukraine and Belarus. Look for something that interests
you.

![e-pity: step for donating 1.5% of tax to an OPP organization, ZMIEŃ OPP button][31]

Press the **ZMIEŃ OPP** button and on the next step choose a fund you're interested in or manually
enter the KRS number of the fund you want.

![e-pity: choosing an OPP foundation from the list or entering a KRS number manually][32]

### 14. List of Funds

Below is a list of funds that might interest you.

Cel szczególowy is not always required. Enter it without quotation marks, exactly as shown.

- 0000507234 - Belarusian initiative [Partyzanka][54] (cel szczegółowy: **85537**). Helping refugees from Belarus and Ukraine.
- 0000030279 - Polish fund [Ocalenie][42], actively helping refugees from Belarus, Ukraine, and other countries.
- 0000190607 - [Towarzystwo][34] przyjaciół Ukrainy.
- 0000507234 - Fundacja [Stand with Ukraine][50] (cel szczegółowy: **83905**). Helping war victims.
- 0000017257 - Animal shelter [fund][35] Fundacja św. Franciszka.
- 0000348880 - School for children with disabilities [Bona Fide][45].
- 0000883672 - [Center][36] for Belarusian Solidarity.
- 0000270261 - [Belarusian Youth Hub][51] (cel szczegółowy: **HUB Warszawa 11876**).
- 0000507234 - [Zerkalo][52] (cel szczegółowy: **84784**).
- 0000507234 - [Dzik pic, devby.io][53] (cel szczegółowy: **85644**).

Children's medical treatment:

- 0000396361 - [Paulina][77] Danilchanka - cel szczegółowy: **0890517 Paulina**
- 0000396361 - [Yeudakim][59] Zakharevich - cel szczegółowy: **0451161 Yeudakim**
- 0000396361 - [Anastasiya][58] Liaszczewicz - cel szczegółowy: **0491365 Anastasiya**
- 0000396361 - [Margarita][57] Datskiewicz - cel szczegółowy: **0104216 Margarita**
- 0000037904 - [Artur][56] Nikanau - cel szczegółowy: **44133 NIKANAU ARTUR**
- 0000396361 - [Artem][55] Padzialowski - cel szczegółowy: **0568766 Artyom**
- 0000037904 - [Zlatoslava][49] Mytnik - cel szczegółowy: **40923 Mytnik Zlatoslava**
- 0000396361 - [Vasilisa][48] Loban - cel szczegółowy: **0165621 Vasilisa**
- 0000037904 - [Dzmitry][47] Kharutski - cel szczegółowy: **43917 Kharutski Dzmitry**
- 0000037904 - [Petr][46] Vakhrameyev - cel szczegółowy: **42671 Vakhrameyev Petr**

[List of funds][30] from e-pity.pl.

If you check the box to share your data with the fund, they'll send you a report next year on how they spent your money.

### 15. Summary

On the final screen you can see how many złoty you've been calculated for a refund or additional payment.
Here you can also download a PDF of the declaration and view the refund or underpayment amounts.

To see how the refund or underpayment was calculated, press the "Jak jest obliczany
podatek?" button.

![e-pity: summary screen (podsumowanie) with the amount to be refunded or paid][37]

### 16. Submitting the Declaration to the Tax Office

On the next step you can submit the declaration to the tax office.
The submission was successful if you received a UPO with status 200 in response.

If this isn't your first declaration, the app will ask you to enter the exact income amount
from the previous year for verification.

Worth mentioning: you are required to keep a copy of the PIT declaration along
with its UPO for 5 years from the date of submission.

Also, people living in Warsaw can now get a Karta Warszawiaka if they filed taxes in Warsaw.
To do this, go to a ZTM customer service point with your city card, a printed
first page of the PIT declaration, and the UPO for it. In other cities the procedure is similar.

### 17. Declaration List

Now on the main screen you can see your declaration. You can download it and visually check that everything is in order.

![e-pity: home screen with the list of created declarations][38]

You can manage the declaration using the button on the right.

![e-pity: declaration actions menu — send, edit, download PDF, correction][39]

Using the corresponding buttons you can submit the declaration to the tax office, edit it, download the PDF,
rename it, delete it, or submit a correction if you want to change
something after it's been sent to the tax office.

For applying for a residence permit, download the declaration together with the UPO.

## PIT-28 via Twój e-PIT

This is an alternative way to file a PIT declaration — the official government service Twój e-PIT (in e-Urząd Skarbowy). It's not very different from the e-pity service, but some people might find it more convenient. The government Twój e-PIT is great, especially if you have a simple ryczałt for one person.
Here's a picture guide.

### 1. Login

Go to [https://urzadskarbowy.gov.pl/services][83]: log in via your bank, profil zaufany, or using last year's data, and select Twój e-PIT.

### 2. Choosing a Declaration

A page will open where you choose which PIT to submit. PIT-28 will be at the very bottom.

### 3. Choose the Type of Activity

![Twój e-PIT: Kreator PIT-28, choosing the business activity form][60]

### 4. Enter Your Income

I take it from ewidencja przychodów for the last month of the reporting year — it has the annual total.

![Twój e-PIT: yearly income (przychody) field in Kreator PIT-28][61]

### 5. Next Is the Reliefs Step

Since I only use the ZUS contribution deduction, I'll write about that — it applies to everyone. For other reliefs, read below in the guide: [Reliefs](#reliefs).

- 5.1 - log into ZUS
- 5.2 - choose informacje roczne
- 5.3 - view the document for the needed year and find the zdrowotna (FUZ) contribution there
- 5.4 - enter half of that contribution in the form field
- 5.5 - find składki społeczne (FUS)
- 5.6 - enter 100% of that contribution in the form field

![ZUS account: navigating to the Informacje roczne section][62]
![ZUS account: yearly document with zdrowotne (FUZ) and społeczne (FUS) contributions][63]
![Kreator PIT-28, Ulgi i odliczenia step: Składki zdrowotne field — 50% of the paid contribution][64]

### 6. Verify Required Amounts Against Actual Payments

If you paid everything on time, they'll all show up automatically. You just need to click 2 checkboxes and verify.

![Kreator PIT-28, Ryczałt należny i wpłacony step: verifying tax amounts, two checkboxes][65]

### 7. Podsumowanie

You'll see the entered form results for verification.

![Kreator PIT-28: Podsumowanie page with the entered data for review][66]

### 8. Final Check Before Submission

As in the guide above, if you've entered data before, everything will be pre-filled. If not:
- you need to enter a bank account number for the overpayment refund
- you can choose who gets the 1.5% of your tax — [Charity](#13-donate-1-5-of-your-paid-tax-to-charity)
- see the overpayment amount

![Twój e-PIT: declaration summary — przychód, ryczałt, 1.5% dla OPP, rachunek bankowy][67]
![Twój e-PIT: kwota nadpłaty and the Akceptuj i wyślij button][68]

### 9. PIT-28 Is Ready

You'll be automatically redirected to a page where you can download the PIT-28 for the year and the UPO. You'll also see the refund status there a bit later.

![Twój e-PIT: Gratulacje message confirming the e-PIT-28 form was sent][69]
![Twój e-PIT: Złożone dokumenty tab — PIT-28, Podgląd UPO and Status zwrotu][76]

P.S. This is my favorite way to file. In practice, you only need to enter the ZUS contribution and your income. Everything else is already filled in and calculated.

## Reliefs

### PIT Zerowy

Also known as "Ulga dla młodych do 26 roku życia".
Zero PIT for those under 26 at the time of receiving income DOES NOT APPLY TO JDG INCOME!

### Ulga na Internet

[Internet deduction](#9-internet-deduction).

## Getting Help

When the annual filing season starts, search in your city for accountants on duty ([dyżur podatkowy PIT warszawa][91]). Such events are organized periodically: free help filling out your PIT in exchange for 1.5% going to their OPP. For example, here's the schedule for [Ursynów, Warsaw][92].

## Checking Status

On the [Status e-Deklaracji][93] page you can check the status of your submitted declaration and download the UPO.

## Correction

After submitting your PIT you have 5 full years to make corrections. That is, declarations for 2025 can be corrected until the end of 2031.

Source: [Korekta zeznania][94].

In the field "6. Cel złożenia formularza (zaznaczyć właściwy kwadrat)":

* [ ] 1. złożenie zeznania
* [x] 2. korekta zeznania

In the field "6a. Rodzaj korekty (zaznaczyć właściwy kwadrat)":

* [x] 1. korekta zeznania, o której mowa w art. 81 Ordynacji podatkowej²
* [ ] 2. korekta zeznania, o której mowa w art. 81b § 1a Ordynacji podatkowej³

My understanding of 6a:

* [x] if you found the error yourself, check the first box.
* [x] if the auditing authorities found the error, check the second box.

## How Long to Wait for an Overpayment Refund

The earlier you file, the faster you'll get it back. Official deadlines:

| Filing method | Maximum refund waiting time |
|---------------|-------------------------------------|
| Paper form | ⏱ 3 months |
| Online (electronic form) | ⏱ 45 days |

Notes:

- the countdown starts from February 15, since the tax office doesn't begin reviewing PITs until then.
- if there are errors in the declaration, they may delay the refund. And if you had a debt to the tax office or an unpaid fine, you might not get a refund at all, since the overpayment goes first toward paying off debts.

## How to Pay Additional Tax

It's quite expected that due to rounding of monthly advances, the annual calculation may result in an additional payment of 1 to 6 złoty.

Pay to the same mikrorachunek as your tax advances, but choose a different symbol formularza: it should match the name of the PIT declaration (as a reminder, for ryczałt it's PIT-28).

Instructions: [How to find your tax payment account?][95].

You must pay the tax by 30.04 regardless of when you filed the PIT declaration. After that date, late payment interest is charged.

## Useful Links

!!! question "Where does it say you can deduct 100% of the social contribution?"
    ⚖ [Art. 11. - Odliczenia od przychodów - Zryczałtowany podatek dochodowy od niektórych przychodów][96], ust. 1

!!! question "Where does it say you can deduct 50% of the health contribution?"
    ⚖ [Art. 11. - Odliczenia od przychodów - Zryczałtowany podatek dochodowy od niektórych przychodów][96], ust. 1a

[11]: https://www.biznes.gov.pl/pl/portal/00237
[12]: https://e-mikrofirma.mf.gov.pl/jpk-form/
[13]: https://play.google.com/store/apps/details?id=com.efile.epitymobile
[14]: https://apps.apple.com/us/app/e-pity/id1213410455
[15]: https://www.e-pity.pl
[16]: images/pit/pit1.jpg
[17]: images/pit/pit2.jpg
[18]: images/pit/pit3.jpg
[19]: images/pit/pit4.jpg
[20]: images/pit/pit5.jpg
[21]: images/pit/pit6.jpg
[22]: images/pit/pit7.jpg
[23]: #4-income-type
[24]: images/pit/pit8.jpg
[25]: images/pit/pit9.jpg
[26]: https://www.pitax.pl/wiedza/mniejsze-podatki/ulga-internetowa
[27]: images/pit/pit10.jpg
[28]: images/pit/pit11.jpg
[29]: images/pit/pit12.jpg
[30]: https://www.e-pity.pl/wykaz-opp/
[31]: images/pit/pit13.jpg
[32]: images/pit/pit14.jpg
[34]: https://tpu.org.pl/
[35]: https://www.facebook.com/fundacja.sw.franciszka/
[36]: https://belaruscenter.eu/by/
[37]: images/pit/pit15.jpg
[38]: images/pit/pit16.jpg
[39]: images/pit/pit17.jpg
[40]: images/pit/pit8-1.jpg
[41]: images/pit/pit18.jpg
[42]: https://en.ocalenie.org.pl
[45]: https://t.me/JDG_PBH/372301
[46]: https://dzieciom.pl/podopieczni/42671
[47]: https://dzieciom.pl/podopieczni/43917
[48]: https://www.siepomaga.pl/vasilisa-loban
[49]: https://dzieciom.pl/podopieczni/40923
[50]: https://fanimani.pl/standwithukraine/
[51]: https://www.facebook.com/bmhuborg
[52]: https://news.zerkalo.io/economics/91472.html
[53]: https://devby.io/news/support-devby24
[54]: https://t.me/partyzanka_rb_pl/650
[55]: https://www.siepomaga.pl/artem-padzialowski
[56]: https://dzieciom.pl/podopieczni/44133
[57]: https://www.siepomaga.pl/margarita
[58]: https://www.siepomaga.pl/nastka-liaszczewicz
[59]: https://www.siepomaga.pl/yeudakim-zacharewicz
[60]: images/pit_eurzad_skarbowy/01.png
[61]: images/pit_eurzad_skarbowy/02.png
[62]: images/pit_eurzad_skarbowy/zus01.png
[63]: images/pit_eurzad_skarbowy/zus02.png
[64]: images/pit_eurzad_skarbowy/03.png
[65]: images/pit_eurzad_skarbowy/04.png
[66]: images/pit_eurzad_skarbowy/05.png
[67]: images/pit_eurzad_skarbowy/06.png
[68]: images/pit_eurzad_skarbowy/07.png
[69]: images/pit_eurzad_skarbowy/08.png
[76]: images/pit_eurzad_skarbowy/09.png
[77]: https://www.siepomaga.pl/paulina-danilchanka
[78]: https://www.biznes.gov.pl/pl/portal/00235#5
[79]: https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/podatek-dochodowy-od-osob-fizycznych-16794311/art-6
[80]: https://www.podatki.gov.pl/poradniki-i-informatory/wspolne-rozliczenie-malzonkow/
[81]: https://www.e-pity.pl/wspolne-rozliczenie-malzonkow-pit/
[82]: https://www.podatki.gov.pl/poradniki-i-informatory/osoba-samotnie-wychowujaca-dziecko/
[83]: https://urzadskarbowy.gov.pl/services
[84]: https://www.e-pity.pl
[85]: https://fill-up.pl
[86]: https://www.pitroczny.pl
[87]: https://wfirma.pl
[88]: https://pomoc.infakt.pl/hc/pl/articles/115000185250-Gdzie-znale%C5%BA%C4%87-PIT-roczny-w-aplikacji
[89]: https://t.me/JDG_PBH/515049
[90]: https://pomoc.wfirma.pl/-zeznanie-roczne-pit-28-jak-wygenerowac-i-uzupelnic-w-systemie
[91]: https://www.google.com/search?q=dy%C5%BCur+podatkowy+PIT+warszawa
[92]: https://ursynow.um.warszawa.pl/-/dyzur-pracownikow-urzedu-skarbowego-na-ursynowie
[93]: https://klient-eformularz.mf.gov.pl/declaration-client/status
[94]: https://www.pit.pl/korekta-zeznania/
[95]: taxes.md#how-to-find-your-tax-payment-account
[96]: https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/zryczaltowany-podatek-dochodowy-od-niektorych-przychodow-16832090/art-11
