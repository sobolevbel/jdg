---
title: Changing data and closing a JDG
description: How to change PKD codes and other sole proprietorship data in CEIDG, and how to suspend or close a JDG — step-by-step instructions and FAQ
tags:
  - CEIDG
  - Reference
---

# Changing data and closing a JDG

A company's life doesn't end with registration: sometimes you need to add a new type
of activity, change your address, or close the business altogether. Almost all changes
are made in the same place where you registered your JDG — on [biznes.gov.pl][1] via
the **Zmień dane w CEIDG** application.

!!! warning "Deadlines"
    You must report data changes (PKD codes, addresses, etc.) to CEIDG
    within **7 days** of the change.

## Changing PKD codes

How to add, remove, or change a JDG activity code:

1. Go to the site where you registered the JDG: [biznes.gov.pl][1]
2. Select **Zmień dane w CEIDG**
3. Log in with your profil zaufany
4. Check the **Kody PKD** box
5. Choose what you need: removing a PKD code, adding a PKD code, or changing the main PKD code
6. Enter the PKD code
7. Sign and submit the application

You must have one main code. You can list an unlimited number of additional codes,
but don't add codes "just in case" — the list of codes in CEIDG can be updated
when you actually need it. If your type of activity has changed, you must add the new
PKD codes or remove the outdated ones within 7 days of the change.

## Changing your address

When moving, you need to update your address in a whole range of places. The checklist
below is based on community experience (the #ChangeAddress note from the "JDG in Poland" chat).

### Government registries

- **CEIDG and the tax office** — the address is updated on [biznes.gov.pl][1] with the
  same CEIDG-1 form used when registering the JDG (**Zmień dane w CEIDG**). Deadline — **7 days**.

    !!! warning "Your tax office may change"
        For a sole proprietor, the tax office branch is determined by the address of
        **residence** (zamieszkania) — the business address (siedziba firmy) only matters
        for companies. If you're moving — check whether your urząd skarbowy has changed
        ([more details at poradnikprzedsiebiorcy][7]).

- **ZUS (the płatnik section)** — the address is also changed via biznes.gov.pl: when
  filling out the CEIDG-1 form, select the corresponding items (ZUS ZUA or ZUS ZZA).
- **VAT-R** — if you're a VAT payer (Polish VAT or VAT-UE) and the move changes your
  urząd skarbowy, update the address with the VAT-R form. Attach your lease agreement,
  the owner's permission to use the address for the JDG, and an oświadczenie
  ([example documents in the chat][8]).

### Business environment

- **Bookkeeping**: inFakt / wFirma / iFirma — or notify your accountant.
- **Bank and payment systems**: PayPal, Revolut, etc.
- **Services that issue invoices to you**: Upwork (tax information),
  AWS / GCP / OCI / Azure, GitHub (billing information), OpenAI, and other subscriptions.
- **Contractors**: use the new address on new invoices, inform your clients,
  and update the address in your contract.

### Karta pobytu and legalization

- If **the karta pobytu shows an address** — you need to notify the voivode about the
  change of residence address and replace the card (the plastic). This is a noticeably
  simpler procedure than obtaining the card in the first place — it takes about 1 month.
- Moving **to another voivodeship**, no address on the card — you can keep the old card
  (or replace it if you wish).
- Moving **within the same voivodeship**, no legalization case pending, no address on
  the card — no need to notify the voivode.
- If you're **awaiting a decision** on the card — notify the urząd about the change of
  correspondence address ([letter template][9]).
- If you're awaiting a decision **and moved to another voivodeship** — the case will
  have to be transferred between voivodeships (search for "przeniesienie sprawy do
  innego województwa").

    !!! warning
        Transferring the case will significantly increase the wait for the decyzja.

### Moving to another voivodeship and ZUS

When you change voivodeship, your territorial assignment to an NFZ branch changes, so
in ZUS you need to deregister at the old address (**ZUS ZWUA**) and register at the new
one (**ZUS ZUA/ZZA**). Your accountant can do this.

Even after that, one place with the old address remains: Ubezpieczony -> Moje dane ->
Dane adresowe -> **Zameldowania** (looks like a bug). It's updated with the **US-13**
application: [US-13 online (template in the chat)][10] / [US-13 offline form][11].

### Tips

- Leave a request at the post office to forward correspondence from your old address
  to the new one — [Poczta Polska: Dosyłanie przesyłek][12] (it used to work only for
  letters, but the service has since been extended to parcels).
- Pay special attention to the addresses at the tax office, ZUS, and your virtual
  office, if you used one.

    !!! danger "A forgotten address can cost you the company"
        There is a known [case][13]: a letter from the tax office arrived at a virtual
        office for a sole proprietor whose contract with the office had expired. The
        office replied that no such business was registered at the address — and the
        tax office **forcibly closed the JDG**, without notice.

- There's a [chat note about all the various JDG addresses][14].

Not business-related, but also worth doing when you move:

- update your address in the PESEL registry: wymeldować yourself from the old address
  and zameldować at the new one;
- register at a new przychodnia (POZ): fill out the deklarację wyboru lekarza
  rodzinnego i pielęgniarki — in person or online.

📚 Sources: [inFakt blog][15], personal experience of "JDG in Poland" chat members.

## Suspension (zawieszenie) or closure

If there's a chance you'll resume business activity within the next two and a half
years (counting from when the JDG was opened), it's better to suspend the company
(zawieszenie) so you don't lose the Ulga na Start and Składki Preferencyjne benefits —
if you reopen a JDG sooner than 60 months after closing, you no longer have the right
to these benefits.

## Closing a JDG

The closure is done on [biznes.gov.pl][2] with an application for wykreślenie działalności from CEIDG.

!!! info "Insurance after closing"
    If you stay in Poland after closing the JDG, remember: foreigners are required to
    have insurance. You'll have to arrange private insurance or voluntary ZUS so there
    are no uninsured days. There's no fine for a gap in mandatory insurance, but a gap
    may negatively affect obtaining a residence permit later.

### Closure FAQ

**Can I close a JDG retroactively?**

Yes. But you'll have to contact ZUS so they recalculate the automatically accrued
contributions due ([more details in the zawartka.pl article][3]).

**Can I close a JDG with a future date?**

No ([answer from poradnikprzedsiebiorcy][4]).

**Do tax obligations to Poland end immediately after closing a JDG?**

There are nuances. You'll still have to file the annual PIT and ZUS declarations — they
may result in an additional payment or a refund. It may happen that after closing you
receive a delayed payment from a client for services provided before the closure; if the
payment is in a foreign currency, you'll have to calculate exchange rate differences on
it. And if the closure isn't from the 1st of the month — pay ZUS for the partial month.

**Do I need to change anything in ZUS when closing?**

You need to deregister (wyrejestrować) the family members who were attached to your ZUS
insurance — with the **ZCNA** form. You have 7 days to make the changes.

**Am I obliged to notify the urząd about ceasing business activity?**

Yes, within **15 business days** — if you have a karta pobytu (KCP) issued for
continuing to run a JDG ([art. 113 ustawy o cudzoziemcach][5]). In other situations — no.

[Support our guide with a cup of coffee ♥][6]{ .md-button .md-button--primary }

[1]: https://www.biznes.gov.pl/pl
[2]: https://www.biznes.gov.pl/pl/portal/0077
[3]: https://zawartka.pl/2023/11/09/zamkniecie-dzialalnosci-z-data-wsteczna-a-zus/
[4]: https://poradnikprzedsiebiorcy.pl/-data-likwidacji-dzialalnosci-gospodarczej
[5]: https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/cudzoziemcy-18053962/art-113
[6]: support.md
[7]: https://poradnikprzedsiebiorcy.pl/-zmiana-adresu-wykonywania-dzialalnosci-i-adresu-zamieszkania-a-wlasciwosc-urzedu-skarbowego
[8]: https://t.me/JDG_PBH/516086
[9]: https://t.me/JDG_PBH/474043
[10]: https://t.me/JDG_PBH/499132
[11]: https://www.zus.pl/wzory-formularzy/pracujacy/konto-w-zus/-/asset_publisher/mhHJQUQYSi0w/content/wniosek-us-13
[12]: https://www.poczta-polska.pl/zlec-usluge-online/dosylanie/
[13]: https://t.me/JDG_PBH/381440
[14]: https://t.me/JDG_PBH/105158
[15]: https://www.infakt.pl/blog/zmiana-adresu-firmy-formalnosci/
