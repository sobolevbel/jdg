---
title: Отправка JPK_V7M через e-mikrofirma
description: Как бесплатно отправить декларацию JPK_V7M через официальное приложение e-mikrofirma от Министерства финансов — вход, фактуры, нулевая декларация, подпись, UPO, korekta
tags:
  - Декларации
  - VAT
  - JPK
---

# Отправка JPK_V7M через e-mikrofirma

**e-mikrofirma** — бесплатное официальное приложение Министерства финансов для ведения
простого реестра фактур и отправки деклараций JPK_V7M/JPK_V7K. Подходит тем, кто не
хочет платить за inFakt/wFirma и готов вносить фактуры вручную.

Официальная документация: [Podręcznik użytkownika aplikacji e-mikrofirma][1] (PDF, польский).

<!-- TODO: скриншоты интерфейса e-mikrofirma для каждого шага -->

## Кому подходит

- Плательщикам VAT с небольшим количеством фактур в месяц.
- Тем, кому нужно отправить **нулевую** декларацию JPK_V7M бесплатно.
- Тем, кто генерирует XML-файл JPK в другой программе и хочет просто его отправить —
  для этого достаточно [Klient JPK_WEB][2] (см. [ниже](#otpravka-gotovogo-xml-klient-jpk-web)).

## Вход

1. Перейдите в [e-Urząd Skarbowy][3].
2. Выберите вход через **login.gov.pl** (profil zaufany, aplikacja mObywatel,
   bankowość elektroniczna или e-dowód).

    !!! warning "Вход «danymi podatkowymi» не подходит"
        При входе в e-Urząd Skarbowy по данным налогоплательщика (NIP/PESEL + суммы
        из деклараций) приложение e-mikrofirma **недоступно**. Нужен полноценный
        вход через login.gov.pl.

3. Внутри e-Urząd Skarbowy откройте плитку **e-mikrofirma**.

## Первичная настройка профиля

При первом входе приложение попросит зарегистрировать профиль фирмы (кнопка **Zarejestruj**):

- **Dane identyfikacyjne**: NIP (после регистрации не редактируется), имя, фамилия,
  дата рождения, название фирмы.
- **Dane adresowe**: адрес фирмы, телефон, e-mail.
- **Dane do rozliczeń**: способ расчёта — **miesięczne (JPK_V7M)** или kwartalne (JPK_V7K),
  номер банковского счёта, ваш Urząd Skarbowy.

После регистрации приложение автоматически связывается с KSeF — статус связи виден
на стартовом экране.

## Внесение фактур

### Фактура продажи

Menu → Nowy dokument → **Nowa faktura sprzedaży**. Заполняете номер и даты фактуры
(**Data księgowania** определяет, в какой период попадёт документ), данные контрагента,
позиции с ценой и ставкой VAT (при ставке `ZW` обязательно указать powód zwolnienia),
данные об оплате — и **Zapisz**.

!!! info "С 1 апреля 2026 — e-Faktura через KSeF"
    Фактуры контрагентам с NIP с 01.04.2026 выставляются через **Nowa e-Faktura
    sprzedaży (KSeF)**. Обычная фактура (обозначение BFK) допустима до конца 2026 года
    только пока сумма таких фактур не превышает 10 000 zł brutto в месяц.

### Фактура покупки

Menu → Nowy dokument → **Nowa faktura zakupu**. Аналогично, но NIP контрагента
обязателен, и нужно выбрать **Rodzaj wpisu** (основные средства или прочие товары
и услуги). С 01.02.2026 обязательно oznaczenie faktury: NrKSeF (номер из KSeF),
BFK (бумажная/электронная вне KSeF) или OFF.

## Генерация JPK_V7M за период

1. Внесите все документы за отчётный месяц.
2. Раздел **Deklaracje** → выделите период → **Uzupełnij deklarację**. Большая часть
   полей заполнится автоматически из внесённых фактур.

    !!! warning "Перенос nadwyżki VAT (поле P_39)"
        Сумма излишка VAT с предыдущего периода **не переносится автоматически** —
        проверьте и внесите её вручную.

3. **Zapisz** (или Zapisz i pokaż PDF — проверить глазами).
4. Раздел **Rozliczenia** → выделите период → **Generuj i wyślij JPK_VAT** — период
   закроется, и приложение перекинет вас в Klient JPK_WEB для подписи и отправки.
   (Кнопка **Generuj JPK_VAT** без отправки даёт возможность скачать XML или отменить
   закрытие периода кнопкой Cofnij rozliczenie.)

## Нулевая декларация

Если в отчётном месяце не было ни продаж, ни покупок, нулевую декларацию всё равно
нужно отправить:

1. Раздел **Rozliczenia** → кнопка **Nowe zerowe rozliczenie** (правый верхний угол).
2. Выберите период → **Dodaj rozliczenie**.
3. Дальше стандартно: **Uzupełnij deklarację** → **Zapisz** → **Generuj i wyślij JPK_VAT**.

## Подпись и отправка

Отправка идёт через **Klient JPK_WEB**. Способы подписи:

1. **Profil Zaufany** — откроется окно логина pz.gov.pl, подписываете и ждёте
   автоматического возврата (не закрывайте окно).
2. **Kwota przychodu** (dane autoryzujące) — только для физлиц: NIP, имя, фамилия,
   дата рождения и **сумма дохода из декларации PIT за год на два года раньше года
   отправки** (например, при отправке в 2026 — доход из PIT за 2024).
3. **Podpis kwalifikowany** — для владельцев квалифицированной подписи.

После подписи — **Wyślij**. На экране Podsumowanie появится **Numer referencyjny**
(сохраните его) и придёт e-mail-уведомление.

!!! warning "Отправлено ≠ принято"
    Успешная отправка ещё не означает успешную обработку. Подтверждение — статус
    **200 «Przetwarzanie dokumentu zakończone poprawnie. Wygenerowano UPO»**.

## Скачивание UPO

UPO (Urzędowe Poświadczenie Odbioru) — официальное подтверждение приёма декларации:

- в e-mikrofirma: **Lista JPK → JPK_VAT** → у отправленного документа кнопка
  **Pobierz UPO** → Pokaż PDF / Pobierz XML;
- в Klient JPK_WEB: [Sprawdź status][4] → ввести Numer referencyjny → **Sprawdź** →
  Pobierz PDF / XML.

## Korekta

Если после отправки нашли ошибку:

1. **Rozliczenia** → **Cofnij rozliczenie** (статус сменится на Cofnięte).
2. Внесите исправления в фактуры/декларацию.
3. Снова **Generuj i wyślij JPK_VAT** — файл уйдёт с целью złożenia **2** (корректа),
   первичный документ получит статус **Skorygowane**.

## Отправка готового XML (Klient JPK_WEB)

Если вы генерируете JPK_V7M в другой программе (или бухгалтер прислал вам XML),
отправить его можно без e-mikrofirmy — напрямую через [Klient JPK_WEB][2]:

1. На экране **Wyślij dokumenty** перетащите файл .xml (или **+ Dodaj pliki**).
2. **Dalej** → **Podpisz dokumenty** (способы подписи те же — см. выше).
3. **Wyślij** → сохраните Numer referencyjny → скачайте UPO после обработки.

## Типичные ошибки

| Код | Что означает | Что делать |
|---|---|---|
| 401 | Weryfikacja negatywna — файл не соответствует схеме XSD | Проверить структуру файла (актуальная схема JPK_V7M) |
| 407 / 411 | Такой документ уже был отправлен (дубликат) | Ничего — декларация уже принята; для исправления отправьте корректу |
| 412 / 413 | Ошибка шифрования / контрольной суммы | Отправить файл заново |
| 419 | Błąd w danych autoryzujących | Проверить имя, фамилию, дату рождения, NIP и kwotę przychodu (PIT за позапрошлый год) |
| 420 | Нет действующей доверенности UPL-1 | Подписывать своим профилем, а не чужим, либо подать UPL-1 |

[Поддержите наш гайд чашкой кофе ♥][5]{ .md-button .md-button--primary }

[1]: https://www.podatki.gov.pl/podatki-firmowe/jednolity-plik-kontrolny/jpk_vat-z-deklaracja/pliki-do-pobrania
[2]: https://e-mikrofirma.mf.gov.pl/jpk-client/
[3]: https://urzadskarbowy.gov.pl/
[4]: https://e-mikrofirma.mf.gov.pl/jpk-client/status
[5]: support.md
