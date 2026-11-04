---
title: Настройка infakt.pl для JDG
description: Первоначальная настройка infakt.pl для ведения бухгалтерии JDG — данные фирмы, банковский счёт, настройки ZUS и налогов
tags:
  - Бухгалтерия
  - infakt
---

# Первоначальная настройка

Перед началом работы с infakt, необходимо выполнить минимальную настройку аккаунта.
Для этого идем в [Ustawienia][1]

![inFakt: данные фирмы и кнопка Edytuj][2]

Для загрузки данных из реестра нажмите *Edytuj* у *Dane Twojej firmy*, затем *Wyszukaj dane firmowe po numerze NIP*. Введите свой NIP и нажмите *Wyszukaj*.

![inFakt: поле NIP, кнопки Wyszukaj и Uzupełnij dane ręcznie][3]

Заполните недостающие поля, так же заполните адрес для корреспонденции (Adres korespondencyjny) и свои данные "продавца" (Dane Sprzedawcy)

<span id="aktivatsiia-bukhgalterskogo-modulia-besplatno"></span>

## Активация бухгалтерского модуля

Для подключения бухгалтерии откройте закладку [Księgowość][4] на главном экране и заполните запрашиваемые данные. Самостоятельная бухгалтерия — платный сервис с бесплатным пробным периодом; актуальные условия указаны на [странице программы inFakt][5].

После подключения проверьте [Ustawienia -> Księgowość -> Dane podstawowe][6]: регистрационные данные, дату начала деятельности и дату начала ведения учёта в inFakt. Если начинаете учёт с открытия ИП, даты совпадают. PESEL и другие данные владельца находятся в отдельном разделе [Dane właściciela][7]. Для изменения параметров нажимайте *Edytuj* рядом с нужным блоком.

![inFakt: Dane podstawowe — даты начала учёта, реквизиты и кнопки Edytuj][8]

В разделе [Ustawienia -> Księgowość -> VAT][9] проверьте *Rodzaj prowadzonej sprzedaży VAT*, *Metoda rozliczania VAT*, *Okres rozliczenia VAT* и регистрацию VAT-UE. В поле *Kwota do przeniesienia na kolejny okres rozliczeniowy z ostatniej deklaracji VAT* указывается VAT к переносу из предыдущей декларации.

![inFakt: параметры VAT и VAT-UE, кнопки Edytuj для изменения настроек][10]

Систему налогообложения и период расчёта PIT проверьте в разделе [Ustawienia -> Księgowość -> Podatek dochodowy][11]. Чаще всего ИТ-шники используют *Ryczałt od przychodów ewidencjonowanych* в качестве системы учёта и ежемесячный расчёт PIT (*Okres rozliczenia podatku dochodowego*).

Если ранее вели бухгалтерию где-то ещё, укажите выручку с начала года до начала учёта в inFakt в блоке *Wartość przychodu od początku roku*. Ниже находится отдельный блок *Wartość przychodu* — выручка из годовой декларации для авторизации электронной отправки налоговых деклараций.

![inFakt: Podatek dochodowy — система налогообложения, период и начальная выручка][12]

## Настройка данных ZUS

Следующим шагом идет настройка параметров для ZUS. Перейдите на страницу [Księgowość -> Składki ZUS][13], или в настройках [Ustawienia -> Księgowość -> ZUS][14]. Если появится кнопка *Uzupełnij brakujące dane*, заполните недостающие данные. Для изменения отдельного параметра нажмите *Edytuj* рядом с ним.

![inFakt: льготы ZUS и метод расчёта składka zdrowotna, кнопки Edytuj][15]

Выбираете свои настройки. Типичные настройки для начинающих при наличии права на льготные взносы:

* Czy korzystasz z ulgi na start? **Tak**
* Preferencyjna stawka ZUS przez 24 miesiące działalności **Tak**
* Jaką metodą chcesz wyliczać wartość składki zdrowotnej? **Na podstawie bieżącego przychodu**

Если планируете оплачивать складки через infakt, имеет смысл добавить так же номер счета ZUS. Для этого нажмите *Edytuj* у *Indywidualny rachunek składkowy*, введите номер своего счёта и нажмите *Zapisz*. Номер счета можно узнать из письма ZUS, которое приходит после регистрации, либо на самом портале [ZUS -> Panel Płatnika -> Moje dane -> Numery rachunków składkowych][16]

![inFakt: поле Indywidualny rachunek składkowy и кнопка Zapisz][17]

## Настройки фактур

Пройдите в [Ustawienia -> Faktury -> Ogólne][18] и нажмите *Edytuj*, чтобы настроить некоторые значения для фактур.

Основные настройки, влияющие на содержимое фактур, это *Domyślna waluta* (выбираем ту, что чаще используется), *Domyślny sposób płatności* (чаще всего это Przelew - банковский перевод).

Здесь же задаются *Domyślna stawka VAT na fakturze* и *Domyślna stawka ryczałtu na fakturze* — ставки по умолчанию, которые можно менять для отдельной услуги или фактуры.

![inFakt: общие настройки фактур и кнопка Edytuj для изменения значений по умолчанию][19]

## Настройка услуг

Добавляем продукт (в нашем случае - услугу) на странице [Przychody -> Produkty -> Nowy produkt][20]

![inFakt: Nowy produkt — название, цена, ставки VAT и Ryczałt, кнопка Zapisz produkt][21]

Обычно для программистов это могут быть:

* usługi komputerowe
* Tworzenie oprogramowania
* usługi oprogramowania

Важно выбрать то, что соответствует вашему роду деятельности и коду PKWiU
В зависимости от контракта у вас может быть фиксированная сумма в месяц, либо почасовая ставка. Вписываем Cena netto = ваша ставка (за месяц или за час).

Ставка VAT зависит от того, кому вы оказываете услугу (если вы не плательщик VAT):

* услуга внутри Польши — `zw.` После выбора появится селектор для выбора основания освобождения, обычно это zwolnienie podmiotowe.
* контрагент в другой стране ЕС — `np.` с пометкой art. 28b (место оказания услуги — страна контрагента).
* контрагент за пределами ЕС (например, США или Канада) — `np.`

Если вы являетесь плательщиком VAT, для услуг внутри Польши вместо `zw.` указываете свою ставку VAT (обычно 23%).

Выберите свою ставку Ryczałt для данной услуги. Ставка должна соответствовать коду PKWiU. Для программистов это 12%. После заполнения нажмите *Zapisz produkt*.

## Настройка контрагентов

Добавляем вашего/ваших заказчиков на странице [Przychody -> Klienci -> Nowy klient][22]

![inFakt: NIP клиента, кнопка Dalej и переход к ручному заполнению][23]

Введите NIP и нажмите *Dalej*, либо выберите *Uzupełnij dane klienta ręcznie*, если заказчик за пределами Польши. В форме выберите тип контрагента в *Rodzaj działalności gospodarczej* и страну в *Państwo*.
Если клиент за пределами EU, то имеет смысл для него в поле *Domyślne uwagi do faktur dla tego klienta* сохранить комментарий:

> Reverse charge - VAT is charged to the buyer.
> Do rozliczenia podatku VAT zobowiązany jest nabywca usługi (odwrotne obciążenie).

Так же можно настроить способ и сроки оплаты для этого клиента (если вам это важно). Как минимум, имеет смысл указать *Sposób płatności* (потому что он может сбиваться между разными фактурами с разным типом оплаты).

Срок оплаты задаётся в поле *Domyślny termin płatności*. После заполнения нажмите *Zapisz klienta*.

![inFakt: данные клиента, страна, условия оплаты, примечания и кнопка Zapisz klienta][24]

Добавляем сколько нужно контрагентов.

## Настройка счетов

На странице [Ustawienia -> Faktury -> Konta bankowe][25] нажмите *Dodaj nowe konto*, заполните реквизиты и нажмите *Zapisz*. Для подтверждения добавления потребуется *Hasło inFakt* — пароль аккаунта.

![inFakt: Dodaj nowe konto — реквизиты, счёт по умолчанию и кнопка Zapisz][26]

Этот счет будет показываться на фактуре для заказчика.

Если счетов больше чем один, в фактуре светится тот что установлен по-умолчанию (флажок *Ustaw jako konto domyślne*). Можно будет сменить при создании фактуры.

## Подпись на фактуре

Переходим в настройку шаблонов фактур на странице [Ustawienia -> Faktury -> Szablony][27]

![inFakt: Elementy graficzne — кнопки Wybierz plik для логотипа и подписи][28]

В блоке *Elementy graficzne* нажмите *Edytuj*. Кнопки *Wybierz plik* позволяют загрузить логотип фирмы (*Logotyp firmowy*) и изображение подписи (*Podpis*).

Изображение подписи должно иметь соотношение сторон примерно 3 к 1 (я использовал картинку примерно 960x360).

## Разное

Если будете пользоваться сервисом infakt для высылки фактур заказчику, можно настроить тексты писем на английском и польском языках. Для этого откройте [Ustawienia -> Faktury -> Teksty][29] и отредактируйте шаблоны писем.

[1]: https://app.infakt.pl/app/ustawienia/konto/dane_firmy
[2]: images/infakt_settings/01_dane_firmy.jpg
[3]: images/infakt_settings/02_wyszukaj_nip.jpg
[4]: https://app.infakt.pl/app/ksiegowosc
[5]: https://www.infakt.pl/program-do-ksiegowosci/
[6]: https://app.infakt.pl/app/ustawienia/ksiegowosc/dane_podstawowe
[7]: https://app.infakt.pl/app/ustawienia/ksiegowosc/dane_wlasciciela
[8]: images/infakt_settings/03_dane_ksiegowe.jpg
[9]: https://app.infakt.pl/app/ustawienia/ksiegowosc/vat
[10]: images/infakt_settings/04_vat.jpg
[11]: https://app.infakt.pl/app/ustawienia/ksiegowosc/pit
[12]: images/infakt_settings/05_pit.jpg
[13]: https://app.infakt.pl/app/ksiegowosc/skladki_zus
[14]: https://app.infakt.pl/app/ustawienia/ksiegowosc/zus
[15]: images/infakt_settings/06_zus.jpg
[16]: https://www.zus.pl/portal/obszar-platnika.npi#KPL0001
[17]: images/infakt_settings/07_rachunek_zus.jpg
[18]: https://app.infakt.pl/app/ustawienia/faktury/ogolne
[19]: images/infakt_settings/08_ustawienia_faktur.jpg
[20]: https://front.infakt.pl/produkty
[21]: images/infakt_settings/09_nowy_produkt.jpg
[22]: https://app.infakt.pl/klienci
[23]: images/infakt_settings/10_nip_klienta.jpg
[24]: images/infakt_settings/11_dane_klienta.jpg
[25]: https://app.infakt.pl/app/ustawienia/faktury/konta_bankowe
[26]: images/infakt_settings/12_konto_bankowe.jpg
[27]: https://app.infakt.pl/app/ustawienia/faktury/szablony
[28]: images/infakt_settings/13_podpis_logo.jpg
[29]: https://app.infakt.pl/app/ustawienia/faktury/teksty
