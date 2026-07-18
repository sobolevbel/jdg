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

![2]

Впишите свой номер NIP и подтянутся сведения о вашем ИП из картотеки

![3]

Заполните недостающие поля, так же заполните адрес для корреспонденции (Adres korespondencyjny) и свои данные "продавца" (Dane Sprzedawcy)

## Активация бухгалтерского модуля (бесплатно)

Для активации бухгалтерии откройте закладку [Księgowość][4] на главном экране. Проверьте свои данные и подтвердите номер телефона. Затем выберите из списка советника/консультанта? Из своего региона (не знаю зачем???).

После активации infakt запросит недостающие данные для ведения учета и бухгалтерии. Проверьте регистрационные данные сверху страницы, заполните поля адреса и номера PESEL, затем снизу выберите свою систему учета налогов и VAT (введите свои данные).

![5]

Чаще всего ИТ-шники используют *Ryczałt ewidencjonowany* в качестве системы учета и ежемесячные зачисления PIT (Płacę podatek PIT miesięcznie).
Укажите с какого месяца собираетесь вести учет в infakt - почти всегда совпадает с месяцем начала ведения деятельности.

На следующей странице введите сумму прихода с начала года, освобожденное от уплаты VAT (TODO: плательщики, объясните этот пункт)

![6]

Дальше настраиваем ставку налога и сумму фактур с начала года, если ранее вели бухгалтерию где-то еще помимо infakt.

![7]

На этом этапе настройка почти завершена. При заходе на страницу [Księgowość][4] infakt будет еще спрашивать некоторые вещи по настройке VAT, номер налогового счета, т.д. Эту информацию просто сохраняйте.

## Настройка данных ZUS

Следующим шагом идет настройка параметров для ZUS. Перейдите на страницу [Księgowość -> Składki ZUS][8], или в настройках [Ustawienia -> Księgowość -> ZUS][9] (до окончания настроек будет светиться кнопка *Uzupełnij brakujące dane*).

![10]

Выбираете свои настройки. Типичные настройки для начинающих:

* Czy korzystasz z ulgi na start? **Tak**
* Preferencyjna stawka ZUS przez 24 miesiące działalności **Tak**
* Sposób wyliczania składki zdrowotnej **Na podstawie bieżącego przychodu**

Если планируете оплачивать складки через infakt, имеет смысл добавить так же номер счета ZUS. Для этого введите номер своего счета в поле *Indywidualny rachunek składkowy*. Номер счета можно узнать из письма ZUS, которое приходит после регистрации, либо на самом портале [ZUS -> Panel Płatnika -> Moje dane -> Numery rachunków składkowych][11]

![12]

## Настройки фактур

Пройдите в [Ustawienia -> Faktury -> Ogólne][13], чтобы настроить некоторые значения для фактур.

Основные настройки, влияющие на содержимое фактур, это *Domyślna waluta* (выбираем ту, что чаще используется), *Domyślny sposób płatności* (чаще всего это Przelew - банковский перевод).

> TODO: добавить настройки специфичные для VAT

## Настройка услуг

Добавляем продукт (в нашем случае - услугу) на странице [Przychody -> Produkty -> Nowy Produkt][14]

![15]

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

Выберите свою ставку Ryczałt для данной услуги. Ставка должна соответствовать коду PKWiU. Для программистов это 12%.

## Настройка контрагентов

Добавляем вашего/ваших заказчиков на странице [Przychody -> Produkty -> Nowy Klient][16]

![17]

Ищем по номеру NIP либо вводим руками, если заказчик за пределами Польши, и сохраняем.
Если клиент за пределами EU, то имеет смысл для него в поле *Domyślne uwagi do faktur dla tego klienta* сохранить комментарий:

> Reverse charge - VAT is charged to the buyer.
> Do rozliczenia podatku VAT zobowiązany jest nabywca usługi (odwrotne obciążenie).

Так же можно настроить способ и сроки оплаты для этого клиента (если вам это важно). Как минимум, имеет смысл указать *Sposób płatności* (потому что он может сбиваться между разными фактурами с разным типом оплаты).

Добавляем сколько нужно контрагентов.

## Настройка счетов

Добавляем свой счет на станице [Ustawienia -> Faktury -> Konta bankowe][18].

![19]

Этот счет будет показываться на фактуре для заказчика.

Если счетов больше чем один, в фактуре светится тот что установлен по-умолчанию (*Konto domyślne*). Можно будет сменить при создании фактуры.

## Подпись на фактуре

Переходим в настройку шаблонов фактур на странице [Ustawienia -> Faktury -> Szablony][20]

![21]

Тут можно добавить изображение своей подписи и логотип фирмы, а так же поиграться с шаблонами самой фактуры (infakt предлагает какой-то выбор).

Изображение подписи должно иметь соотношение сторон примерно 3 к 1 (я использовал картинку примерно 960x360).

## Разное

Если будете пользоваться сервисом infakt для высылки фактур заказчику, можно настроить тексты писем на английском и польском языках. Для этого откройте [Ustawienia -> Faktury -> Teksty][22] и отредактируйте шаблоны писем.

[1]: https://app.infakt.pl/app/ustawienia/konto/dane_firmy
[2]: images/infakt_settings/ustawienia.png
[3]: images/infakt_settings/nip.png
[4]: https://app.infakt.pl/app/ksiegowosc
[5]: images/infakt_settings/ksiegovosc_dane_podstavove.png
[6]: images/infakt_settings/ksiegovosc_kwota.png
[7]: images/infakt_settings/ksiegovosc_przychody.png
[8]: https://app.infakt.pl/app/program_do_ksiegowosci/deklaracja_zus
[9]: https://app.infakt.pl/app/ustawienia/ksiegowosc/zus
[10]: images/infakt_settings/ksiegovosc_zus.png
[11]: https://www.zus.pl/portal/obszar-platnika.npi#KPL0001
[12]: images/infakt_settings/ustawienia_zus.png
[13]: https://app.infakt.pl/app/ustawienia/faktury/ogolne
[14]: https://app.infakt.pl/app/produkty
[15]: images/infakt_settings/nowy_produkt.png
[16]: https://app.infakt.pl/app/klienci
[17]: images/infakt_settings/nowy_klient.png
[18]: https://app.infakt.pl/app/ustawienia/faktury/konta_bankowe
[19]: images/infakt_settings/konto_bankowe.png
[20]: https://app.infakt.pl/app/ustawienia/faktury/szablony
[21]: images/infakt_settings/szablony.png
[22]: https://app.infakt.pl/app/ustawienia/faktury/teksty
