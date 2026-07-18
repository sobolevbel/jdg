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

При первом входе приложение попросит зарегистрировать профиль фирмы — экран **Rejestracja**:

- **Dane identyfikacyjne**: NIP (⚠ после регистрации изменить нельзя — проверьте перед
  отправкой), REGON и BDO (опционально), имя, фамилия, дата рождения, название фирмы
  и логотип (опционально — появятся на фактурах).
- **Dane adresowe**: адрес фирмы, телефон, e-mail.
- **Dane do rozliczeń**: способ расчёта — **miesięczne (JPK_V7M)** или kwartalne (JPK_V7K),
  номер банковского счёта, ваш Urząd Skarbowy.
- Галочка о ознакомлении с klauzulami informacyjnymi и кнопка **Zarejestruj**.

После регистрации попадаёте на стартовую страницу с меню слева: **Nowy dokument**
(фактуры), **e-Faktury zakupu w KSeF**, **Lista dokumentów**, **Ewidencje**,
**Deklaracje**, **Rozliczenia**, **Lista JPK**, **Baza kontrahentów**. Если сверху
висит плашка «Konto nie jest powiązane z KSeF» — по ссылке «instrukcji» в ней описано,
как выдать приложению права в KSeF (нужно для выставления e-Faktur).

## Внесение фактур

### Фактура продажи

Menu → **Nowy dokument** → **Nowa faktura sprzedaży**. Форма состоит из пяти секций.
Поля, отмеченные звёздочкой в приложении, обязательны — ниже они тоже помечены `*`.

!!! info "С 1 апреля 2026 — e-Faktura через KSeF"
    Прямо в секции Kontrahent приложение предупреждает: фактуру для контрагента
    **с NIP** выставляйте через **Nowa e-Faktura sprzedaży (KSeF)** — отдельный пункт
    меню с почти таким же набором полей. Обычная фактура допустима до конца 2026 года,
    только пока сумма таких фактур не превышает 10 000 zł brutto в месяц.

**1. Dane faktury** — данные самой фактуры:

| Поле | Что вносить |
|---|---|
| Oznaczenia (опц.) | галочки MPP (mechanizm podzielonej płatności), MK (metoda kasowa), faktura do paragonu — типичному фрилансеру не нужны |
| Numer faktury `*` | номер по вашей серии, например `1/07/2026`. Приложение нумерацию не ведёт — продолжайте свою |
| Data wystawienia `*` | дата выставления в формате RRRR-MM-DD (есть календарь) |
| Miejsce wystawienia (опц.) | город выставления |
| Data księgowania `*` | **ключевое поле**: дата привязки фактуры к отчётному периоду — именно по ней документ попадёт в ewidencję и JPK за конкретный месяц |
| Data dostawy / usługi `*` | дата оказания услуги (для помесячных услуг — последний день месяца) |

**2. Kontrahent** — покупатель:

| Поле | Что вносить |
|---|---|
| Nazwa kontrahenta `*` | название фирмы клиента (при повторном вводе подтягивается из Bazy kontrahentów) |
| NIP kontrahenta (опц.) | NIP клиента — 10 цифр без префикса; для физлица без NIP оставить пустым |
| Miejscowość `*`, Kod pocztowy `*`, Numer budynku `*` | адрес клиента |
| Poczta, Ulica, Numer lokalu (опц.) | остальной адрес |

**3. Pozycje** — позиции фактуры:

- Переключатель **Faktura wystawiona w cenach: Netto / Brutto** `*` — от чего считать
  (обычно Netto).
- Таблица позиций: **Nazwa** (название услуги/товара), **Cena jedn. netto**, **Ilość**,
  **Jednostka miary** (например `szt.` или `usł.`), **Stawka VAT** — выпадающий список:
  `23%`, `8%`, `5%`, `0%`, `ZW` (zwolnione — появится поле «Powód zwolnienia»),
  `OO` (odwrotne obciążenie). Kolumny **Netto / VAT / Brutto [PLN]** пересчитываются
  автоматически, внизу строка **Suma**.
- Кнопка **Dodaj kolejną pozycję** — если позиций несколько.
- **Kody towarów i usług** (опц.) — GTU_01–GTU_13; для программирования не требуется.
- **Oznaczenia dotyczące procedur** (опц.) — SW, EE, TP и т.д.; типовому ИП не нужны.

**4. Płatność** — оплата:

| Поле | Что вносить |
|---|---|
| Typ płatności `*` | `przelew`, `gotówka`, `za pobraniem`, `karta płatnicza` или `inny` |
| Numer rachunku bankowego (опц.) | ваш счёт (26 цифр) — появится на фактуре |
| Faktura opłacona (галочка) | отметьте, если оплата уже получена |
| Umowa określa termin płatności (галочка) | если срок оплаты зафиксирован договором |
| Dni na płatność `*` | срок оплаты в днях — Termin płatności `*` посчитается сам (можно и вручную) |

**5. Uwagi** (опц.) — примечания до 256 знаков (например `Reverse charge — VAT is
charged to the buyer` для контрагента вне ЕС).

Внизу три кнопки: **Zapisz** (сохранить), **Zapisz i pokaż PDF** (сохранить и открыть
PDF фактуры), **Anuluj**. Сохранённые фактуры лежат в **Lista dokumentów → Faktury
sprzedaży**, оттуда же их можно редактировать, скачать PDF или выставить фактуру
korygującą.

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
