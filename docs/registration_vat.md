---
title: Регистрация плательщиком VAT в Польше
description: Как зарегистрироваться плательщиком внутрипольского VAT (НДС) для JDG — заполнение VAT-R, лимит 240 000 злотых, возврат VAT с покупок
tags:
  - Регистрация
  - VAT
  - Налоги
---

# Регистрация плательщиком внутрипольского VAT

!!! question "Зачем регистрировать польский VAT"
    Польский VAT вам понадобится если вы оказываете услуги польским заказчикам
    и превысили годовой лимит в 240_000 злотых (на 2026 год). Либо вы хотите возвращать VAT c покупок на фирму.

!!! note
    К этому моменту у вас уже должны быть номера NIP и REGON.

[Ссылка на портал](https://www.biznes.gov.pl/pl) где происходит регистрация.
Нам нужен пункт `Zmień dane w CEIDG`.

## 1. Нас встречает важная информация

В блоке **Usługi CEIDG** выберите **Zmień dane w CEIDG**, затем **Rozpocznij**. Если появляется **Podpowiadanie danych**, выберите свой профиль.

Ознакомьтесь с **Ważne informacje** и нажмите **Dalej**.

![Важная информация перед изменением данных CEIDG][1]

## 2. Цель подачи формы

Выберите **Chcę edytować wpis, wysłać dokumenty do ZUS lub urzędu skarbowego** и укажите дату изменения CEIDG. Это отдельное поле, не дата начала обязанностей по польскому VAT.

![Цель изменения записи CEIDG и дата изменения][2]

## 2.1. Указываем страхование

Позже в мастере раздел **Ubezpieczenia społeczne** запросит текущий вид страхования. Выбирайте **ZUS**, если застрахованы в нём.

![Раздел Ubezpieczenia społeczne с выбранным ZUS][3]

Дополнительные заявления о регистрации в ZUS только ради VAT добавлять не нужно.

## 3. Выбираем данные, которые нужно изменить

В разделе **Załączniki** отметьте **Podatek VAT: VAT-R**. Мастер также включает обязательные шаги страхования, налоговой и e-Doręczenia, может отметить связанные поля контактов и адреса.

![Раздел Załączniki: приложение Podatek VAT: VAT-R][4]

Проверьте подставленные данные и сохраняйте прежние значения там, где ничего не меняется. Гражданам стран вне ЕС мастер предлагает выбрать **Dane osobowe, obywatelstwo** и указать актуальные данные документа о пребывании.

Общие экраны адреса, контактов и e-Doręczenia описаны в [гайде VAT-UE][5].

## 4. Выбираем пункт о регистрации плательщиком VAT

Если ещё не регистрировались как активный или освобождённый плательщик VAT, выбирайте **Rejestracja podatnika VAT**. Если польский VAT или VAT-UE уже регистрировали, выбирайте **Aktualizacja danych podatnika VAT**.

![Цель VAT-R: регистрация или актуализация данных плательщика][6]

## 5. Отказываемся от освобождения

Для регистрации активного польского VAT выберите **Nie** в вопросе **Chcę zarejestrować się jako zwolniony podatnik VAT**.

![Регистрация активного польского VAT: выбран вариант Nie][7]

На **Dane identyfikacyjne** укажите имена отца и матери.

![Идентификационные данные VAT-R: обязательные имена родителей][8]

При актуализации VAT-R мастер также спросит, меняется ли налоговая. Ответьте по своей ситуации.

## 6. Причина регистрации VAT-овцем

Нажмите **Wybierz tytuł podatkowy**, отметьте подходящее основание или основания и нажмите **Zapisz**. Ориентируйтесь на текст, а не только на номер пункта.

Ниже приведено описание наиболее часто обсуждаемых пунктов в телеграм чате "ИП в Польше" (тег заметки для бота Rose: #WhenVATIsRequired).

**Podmiotowe (по доходу)**

| Nazwa i Podstawa prawna                                                                                                  | Opis                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  podatnik rozpoczynający działalność gospodarczą nie ma prawa do zwolnienia, o którym mowa w art. 113 ust. 1 lub 9 ustawy | ИП начинает деятельность, но не имеет права на освобождение по доходу. (если не имеете права работать без VAT, т.е. деятельность связана с консультациями либо ваш код деятельности подразумевает обязательную регистрацию на VAT) |
|  podatnik rezygnuje (zrezygnował) ze zwolnienia, o którym mowa w art. 113 ust. 1 lub 9 ustawy                             | ИП добровольно отказывается от освобождения по доходу. (добровольная регистрация до утраты права на освобождение)                                                                                      |
|  podatnik traci (utracił) zwolnienie, o którym mowa w art. 113 ust. 1 lub 9 ustawy                                        | ИП утратил право на освобождение по доходу. (например, превысил лимит 240 000 zł).                                                                                                                                             |
|  podatnik wykonuje czynności, o których mowa w art. 113 ust. 13 ustawy                                                    | ИП выполняет действия, исключающие освобождение по доходу. (например, торговля подакцизными товарами).                                                                                                                         |

**Przedmiotowe (по виду деятельности)**

|  Nazwa i Podstawa prawna                                                                                                                                       | Opis                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
|  podatnik będzie dokonywał (dokonuje) sprzedaży wyłącznie zwolnionej od podatku od towarów i usług na podstawie art. 43 ust. 1, z wył. pkt 3, i art. 82 ustawy | ИП осуществляет только операции, освобождённые от НДС по характеру деятельности.                         |
|  podatnik będzie korzystał (korzysta) ze zwolnienia, o którym mowa w art. 43 ust. 1 pkt 3 ustawy                                                               | Освобождение для rolnik ryczałtowy (фермера на специальном режиме), а не общее освобождение для образования или финансовых услуг. |
|  podatnik rezygnuje (zrezygnował) ze zwolnienia, o którym mowa w art. 43 ust. 1 pkt 3 ustawy                                                                   | Rolnik ryczałtowy отказывается от освобождения по art. 43 ust. 1 pkt 3.                                   |

!!! note
    мы не приводим порядковые номера, т.к. они меняются, читайте описание внимательно и выбирайте подходящий вам.

![Список оснований регистрации VAT: выбор подходящего пункта и Zapisz][9]

Пункты **art. 43 ust. 1 pkt 3** относятся к rolnik ryczałtowy. Проверяйте основание именно своего освобождения по [закону о VAT][10].

## 7. Дата начала VAT обязательств

В **Data rozpoczęcia tytułu obowiązku podatkowego** укажите дату, соответствующую выбранному основанию регистрации. Это не автоматически следующий день после подачи. При первичной регистрации подайте VAT-R до операций, для которых регистрация обязательна.

С соответствующей даты нужно рассчитывать VAT и подавать необходимые декларации. Актуализация только ради добавления VAT-UE не начинает регистрацию польского VAT заново.

![Основание и дата начала обязанности по польскому VAT][11]

### 7.1 Пункт Zwolnienie usług finansowych

В блоке **Zwolnienie usług finansowych** ничего не выбираем.

![Zwolnienie usług finansowych: оба варианта оставлены пустыми][12]

## 8. Metoda kasowa

При обычной первичной регистрации без [кассового метода][13] выбирайте **Nie** в вопросе **Wybieram metodę kasową rozliczania podatku VAT**.

![Первичная регистрация VAT: Nie для метода kasowa][14]

При актуализации, если не меняем метод, выбираем **Bez zmian**.

## 9. Золото и такси

Если не регистрируете деятельность такси или торговлю инвестиционным золотом, выберите **Nie dotyczy** в **Szczególne rodzaje działalności gospodarczej**.

![Первичная регистрация VAT: Nie dotyczy для специальных процедур][15]

При актуализации без изменения этих процедур выбирайте **Bez zmian**.

## 10. VAT-UE

Одновременно можно зарегистрировать VAT-UE. Если он нужен, продолжайте по [инструкции VAT-UE][5]. Если нет, выберите **Nie chcę rejestrować się do VAT-UE**.

![Польский VAT без VAT-UE: выбран отказ от регистрации VAT-UE][16]

## 11. Выбрать тип деклараций

Для обычной первичной регистрации активного VAT с ежемесячными декларациями отметьте **miesięczna deklaracja VAT**. Укажите месяц и год первой польской декларации, соответствующие началу VAT-обязательства.

![Ежемесячная декларация VAT и первый отчётный месяц и год][17]

Для квартальной подачи действуют отдельные условия. При простой актуализации существующей регистрации сохраните свой действующий порядок: **Bez zmian** в вопросе о квартальных периодах не означает переход на квартальные декларации.

## 12. Выберите свою налоговую

Проверьте налоговую на **Informacje o zgłoszeniu rejestracyjnym podatnika VAT**. E-mail и телефон — необязательные поля для связи.

![Налоговая и необязательные контактные данные для VAT-R][18]

## 13. Подтверждение регистрации VAT

Можете отказаться от платного получения подтверждения регистрации VAT.
Вряд ли оно когда-нибудь вам пригодится.

![Отказ от платного бумажного подтверждения регистрации VAT][19]

## 14. Освядчение

Дальше нужно утвердить что вы имеете право пользования адресом, под
которым живете (договор аренды, например) и что на вас не
распространяются запреты, о которых написано в приведенном законе.

![Oświadczenie перед подписанием заявления CEIDG][20]

## 15. Подпись

Дальше, как обычно, подписываем внёсек профилем зауфаным, отправляем и ждем
регистрации или письма от налоговой с уточнениями. Если процесс
регистрации затягивается - напишите в налоговую или сходите ногами и
узнайте чего им не хватает.

Отследить, что вы были зарегистрированы можно на [сайте][21].
Это - так называемый белый список, `biała lista`, список всех плательщиков VAT.
До момента наступления даты указанной в пункте `Дата начала VAT обязательств` нет особого смысла проверять,
появилась ли регистрация в белом списке - она не будет в нем фигурировать до этой даты даже если процесс
со стороны налоговой был завершен.

## 16. Ускорение регистрации VAT

!!! tip
    Этот пункт не обязателен, но может помочь закончить регистрацию немного быстрее.

Если нужно зарегистрироваться плательщиком VAT как можно скорее - будет не лишним сразу после подачи заявления на
регистрацию VAT отправить в ужонд электронное письмо.

!!! example
    Dzień dobry.

    Uzupełniam zgłoszenie rejestracyjne VAT-R/VAT-UE o dokumenty dotyczące miejsca prowadzenia działalności:

    - Załączam oświadczenie o braku stałego miejsca wykonywania działalności gospodarczej.
    - Załączam skan umowy najmu jako osoba fizyczna.

!!! warning "Обратите внимание"
    **oświadczenie o braku stałego miejsca wykonywania działalności gospodarczej** пишется только в том случае, если фактического адреса "miejsca wykonywania działalności" не указано при регистрации JDG!

К письму следует прикрепить скан договора аренды и собственно освядченне, в котором нужно в нескольких предложениях
описать род своей деятельности, основу можно взять из описания кодов PKD которые были выбраны при регистрации JDG плюс
немного подробностей что конкретно вы делаете в повседневной работе. Особых требований к оформлению нет, но прикреплять
лучше в виде .pdf, .docx или в виде скана).

!!! example
    Imię Nazwisko  
    ul. Ulica 123/125  
    00-123 Miasto  
    NIP: 1234567890  
    PESEL: 2345678901  

    **Oświadczenie**

    Ja, niżej podpisany, oświadczam, że od dnia **DD.MM.YYYY** prowadzę działalność gospodarczą i wykonuję usługi związane z:

    **Тут кратко описываем род своей деятельности, 1-3 предложения в свободной форме.**

    Do wykonywania działalności dysponuję laptopem z zainstalowanymi pakietami niezbędnych programów komputerowych (*MS Office, Skype, Zoom, Jira, Figma, Outlook, Chrome* itp.).
    Samodzielnie wykonuję wszystkie czynności i nie zatrudniam żadnych pracowników. Nie mam stałego adresu prowadzenia działalności gospodarczej, mogę pracować wszędzie, gdzie jest dostęp do Internetu.

    Dołączam do oświadczenia:

    - skan umowy z klientem,  **не обязательно, можно не отправлять если US не запросил этого документа**
    - skan umowy najmu mieszkania.

    Wynajmuję mieszkanie jako osoba fizyczna.

    место подписания, дата, подпись

**Предпочитаемый способ - pismo ogólne через сайт `e-Urząd Skarbowy`** (специалист из Urząd Skarbowy просили так
высылать документы, проверено несколькими пользователями)

Как это оформить, читай в [инструкции по pismo ogólne][22]

**Альтернативный способ - отправить письмо на e-mail.**

Найти e-mail своего Urzędu Skarbowego можно на странице контактов
подразделений [министерства финансов][23], скачав
таблицу `Baza teleadresowa jednostek KAS.xls` (у искомого уженда кроме нужного адреса должен быть тип "US" в столбце "
TYP") или найдя свой уженд вручную на сайте.

[1]: images/registration_vat_ue/ceidg_01_wazne.jpg
[2]: images/registration_vat_ue/ceidg_02_cel.jpg
[3]: images/registration_vat_ue/ceidg_10_zus.jpg
[4]: images/registration_vat_ue/ceidg_04_vat_r.jpg
[5]: registration_vat_ue.md
[6]: images/registration_vat/01_rejestracja.jpg
[7]: images/registration_vat/02_bez_zwolnienia.jpg
[8]: images/registration_vat/03_dane_identyfikacyjne.jpg
[9]: images/registration_vat/04_tytul_lista.jpg
[10]: https://eli.gov.pl/api/acts/DU/2026/1263/text.html
[11]: images/registration_vat/05_tytul_data.jpg
[12]: images/registration_vat/06_uslugi_finansowe.jpg
[13]: https://poradnikprzedsiebiorcy.pl/-czy-wiesz-jak-rozliczac-faktury-metoda-kasowa
[14]: images/registration_vat/07_metoda_kasowa.jpg
[15]: images/registration_vat/08_procedury.jpg
[16]: images/registration_vat/09_vat_ue.jpg
[17]: images/registration_vat/10_deklaracje.jpg
[18]: images/registration_vat/11_urzad.jpg
[19]: images/registration_vat/12_potwierdzenie.jpg
[20]: images/registration_vat/13_oswiadczenie.jpg
[21]: https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka
[22]: pismo_ogolne.md
[23]: https://www.gov.pl/web/kas/dane-teleadresowe-jednostek-kas
