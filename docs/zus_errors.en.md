---
title: Common ZUS errors
description: Errors when working with eZUS and submitting declarations — error codes 68015101, 69012001, 69004101, how to fix them and support contacts
tags:
  - ZUS
  - Declarations
---

# Common ZUS errors

## Login-related

!!! bug "Login"
    The zus.pl website won't log you into your account! It hangs on Logowanie... or kicks you back to the login page:
    ![auto-logout][6]

Try the following solutions:

1. Clear your cookies ([How to delete cookies for the zus site?](https://t.me/JDG_PBH/520344)).
2. Log into ZUS using a different browser.
3. Log into ZUS via an incognito tab ([How to use incognito mode in Google Chrome?](https://support.google.com/chrome/answer/95464?hl=ru)).
4. Sometimes ZUS hangs on the loading screen, but if you go back to the previous page [https://www.zus.pl/ezus/](https://www.zus.pl/ezus/) and try logging in again, it works.
5. Wait it out. eZUS sometimes has technical issues and there's nothing you can do about it.

## Related to switching between contribution modes

| ⚠️ **What to do if you missed the deadline for switching to składki preferencyjne?** |
|--------------------------------------------------------------------------------------------------------------|
| If an entrepreneur misses the 7-day deadline, there is nothing preventing them from doing it later. Do it now, as soon as possible. Keep in mind that failing to meet the legally established reporting deadline is a violation of the provisions of the Act on the Social Insurance System (ustawy o systemie ubezpieczeń społecznych) and is punishable by a fine. ([Source](https://oficynafk.pl/skladki/preferencyjne-skladki-zus-po-uldze-na-start-obnizone-skladki-zus-krok-po-kroku-19514.html)) |

| ⚠️ **Important note for wFirma users** |
|--------------------------------------------------------------------------------------------------------------|
| To avoid problems with switching modes in wFirma, you should first submit the ZUS DRA for the sixth month of ulga na start and only then proceed with the switch. This matches the [algorithm in the guide][5]. |

When verifying a form, look for the result on the uwagi i błędy tab. Here's a screenshot for reference:
![uwagi i blędy][9]
Let's collect the most common errors and their solutions on this page together!

### 68015101

If you submitted ZUS ZUA before ZUS ZWUA was processed, you may see an error like this:
![68015101][1]

Error text:
> Nie możesz wysłać zgłoszenia z kodem z grupy 05xx, jeżeli jest jeszcze niewyrejstrowany okres podlegania z kodem 05XX. Jeśli wysłałeś dokument ZWUA, poczekaj z wysłaniem nowego zgłoszenia na przetworzenie dokumentu ZWUA w ZUS. (blok V pole 1) Błąd zwykły

This message says you need to wait until ZUS ZWUA is processed. But actually, you don't have to wait — you can submit it with the error. The declaration will still be processed correctly.

### 69012001

![69012001][2]

When verifying the ZUS DRA declaration for the last month of Ulga na Start, you will likely see a status of «Informacja» and a message «Zbliża się koniec okresu ulgi (blok X pole 1)» on the uwagi i błędy tab. This is normal — ZUS is simply informing you that the relief period is ending and you need to prepare for switching to the next contribution mode.
!!! info
    This is not a blocking error: there is nothing to fix, you can safely submit and pay the declaration.

### 69004101

When verifying the ZUS DRA declaration for the last month of Ulga na Start, you see a message «dla ubezpieczonego brak zgłoszenia z podanym kodem tytułu».
![dla ubezpieczonego brak zgłoszenia z podanym kodem tytułu»][4]

On the uwagi i błędy tab there is an error with code 69004101 and text «brak raportu za ubezpieczonego zgłoszonego przez płatnika».
![69004101][3]

The error indicates a mismatch between the insurance code you reported to ZUS and the insurance code specified on the ZUS DRA declaration.

!!! example "possible cause"
    This can happen, for example, if an entrepreneur already switched to skladki preferencyjne at the beginning of October (including changing wFirma settings), but the previous month should still be covered by the relief.

!!! success "solution"
    Try this solution:

    1. Delete the incorrect ZUS DRA in wFirma;
    2. Switch wFirma settings back to Ulga na Start;
    3. Regenerate the ZUS DRA;
    4. After successfully submitting the DRA to ZUS, switch the settings back to preferencyjne contributions.

    Unfortunately, wFirma does not keep a history of setting changes.

    :telegram: Source: [message](https://t.me/JDG_PBH/468097?thread=468020) from [Oksana Sviderska](https://t.me/oksanasviderska)

## Other errors

If you encounter an error that is not yet documented, or the suggested solutions don't work, reach out directly to [ZUS][7] or ask in the [:telegram: JDG in Poland][8] chat.
!!! tip "How to ask your question properly?"
    Include all important information in your question — everything that is relevant and that you think matters. The chat admins have prepared a checklist for you. If you're not sure how to answer some of these, just say so — other chat members will help you out.

    * What are you trying to do?
    * Which form are you filling out?
    * At which step does the question / problem / error occur?
    * The error text in Polish.
    * The error code. When verifying a ZUS form, look for the result on the uwagi i błędy tab.
    * A screenshot of the error and a screenshot of the step(s) preceding the error.
    * Have you already tried any possible solutions on your own?
    * Tax regime? Possible answers:
        1. ryczałt — flat-rate tax
        2. podatek liniowy — linear tax 19%
        3. skala podatkowa or opodatkowanie na zasadach ogólnych — general tax scale 0 / 12% / 32%
    * When was the first day of your business activity? DATE.
    * Do you combine self-employment with a regular job? (note: part of the contributions is paid by the employer; this is about umowa o pracę or umowa zlecenie)
    * Are you a retiree or a person with a disability?
    * Do you calculate monthly contributions based on the current year's income or the previous year's?
    * Which reliefs are you using? Possible answers:
        1. Ulga na Start (first 6 months);
        2. Składki Preferencyjne (next 24 months);
        3. Mały ZUS+ (income up to 120 000 zł);
        4. Wakacje składkowe (1-month holiday from ZUS contributions);
        5. Duży ZUS — full contributions, no reliefs.
        !!! tip "You can check this as follows"
            Go to ZUS - Ubezpieczony - and look up your insurance code.
    * Did you consent to paying sickness insurance contributions (składka chorobowa)?

        !!! tip "You can check this as follows"
            Go to ZUS - ePłatnik - Dokumenty w ZUS and find your most recent ZUS ZUA. If the ZUS ZUA had the składki chorobowe checkbox ticked (block VIII field 05), it means you signed up for these voluntary additional contributions.

    * (for ryczałt) your annual income falls in the range: up to 60000 zł, from 60000 zł to 300000 zł, above 300000 zł. Specify which year you are answering about, or provide income for both the previous and current year.
    * Share a screenshot of the ZUS settings from the accounting service you use (inFakt, wFirma, iFirma) in the chat.
    * If you did not register as a sole trader and are running działalność nierejestrowa, make sure to mention that in your question as well.
    * Did you receive a letter from ZUS? What does it say?
    * Did you receive a reply from ZUS? And how was your original question worded?

[1]: images/zus_errors/zus_error_68015101.jpg
[2]: images/zus_errors/zus_error_69012001.jpg
[3]: images/zus_errors/zus_error_69004101.jpg
[4]: images/zus_errors/zus_error_brak_zgłoszenia_z_podanym_kodem.jpg
[5]: zus_obnizone_skladki.md#wfirma
[6]: images/zus_errors/zus_logout.jpg
[7]: zus_contact.md
[8]: https://t.me/JDG_PBH/529911
[9]: images/zus_errors/uwagi_i_bledy.jpg
