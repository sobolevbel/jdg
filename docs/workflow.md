# Типичный рабочий процесс для рутинных операций ИПшника

Ваша обязанность как JDG выставлять фактуру каждый месяц, если оказывали услуги заказчику, и оплата налогов. Налоги платятся каждый месяц:

- `ZUS DRA` - до 20 числа каждого месяца
- `Podatek dochodowy` - подоходный налог, процент зависит от вида деятельности - до 20 числа каждого месяца
- `VAT` - если оказываете услугу лицу на территории Польши - до 25 числа каждого месяца
- `VAT-UE` - если оказываете услугу лицу на территории ЕС - до 25 числа каждого месяца

## План

1. Оказываете услугу.
2. Выставляете фактуру заказчику

   В общем случае заказчик ничего не должен писать в назначении платежа. Однако, говорят что указание номера фактуры в переводе облегчает жизнь при налоговой проверке.

   В фактуре можно описать следующее: инвойс за "месяц" и пару пунктов типа: фикс багов, реализация микросервисов и тд, буквально 3-4 пункта.

   В поле `Nazwa towaru lub usługi` можно указывать `Software development / Tworzenie oprogramowania (PKWiU 62.01)`.

3. Получаете деньги на бизнес-счёт
4. Оплачиваете все необходимые налоги и сохраняете чеки
    - podatek dochodowy
    - ZUS
    - VAT: при необходимости и возможности вычитаем VAT с покупок из общего VAT. [Детальнее][1]

Более детальное описание конкретных операций на примере сервиса `infakt.pl` можно найти [тут][2].

## Учет курсовых разниц

1. [Статья от inFakt][3]
2. [Статья от Poradnik Przedsiębiorcy][4]
3. [Гайд как учесть КР в inFakt][5]

Для JDG курсовые разницы появляются в двух случаях:

1. [Transakcyjne różnice kursowe][6]
2. [Różnice kursowe od środków własnych][7]

Во втором случае используются три метода — FIFO, LIFO и по средним, где в очередь попадают поступления на счёт.
Метод расчёта нельзя менять в течение налогового года.

Курс считается по [Narodowy Bank Polski][8]

## Подача декларации VAT-UE

Подача e-декларации VAT-UE происходит на сайте налоговой с помощью [интерактивной PDF-формы][9]

- Сперва нужно установить Adobe Reader и расширение к нему [отсюда][10].
- На этой же странице внизу есть инструкция. Вкратце: скачать pdf-ку с формой, открыть в Adobe Reader с установленным
    расширением, заполнить форму, и через визард расширения подписать личными данными и отправить.
- В конце визарда будет ссылка на скачивание UPO.

[1]: faq.md#vat
[2]: infakt_routine.md
[3]: https://www.infakt.pl/blog/jak-zaksiegowac-roznice-kursowe
[4]: https://poradnikprzedsiebiorcy.pl/-ryczalt-a-roznice-kursowe
[5]: infakt_routine.md#poluchenie-oplaty-i-uchet-kursovykh-raznits
[6]: https://pomoc.ifirma.pl/pomoc-artykul/transakcyjne-roznice-kursowe-u-ryczaltowca
[7]: https://www.ifirma.pl/blog/roznice-kursowe-od-srodkow-wlasnych-a-ryczalt.html
[8]: https://www.nbp.pl/home.aspx?c=/ascx/archa.ascx
[9]: https://www.podatki.gov.pl/vat/e-deklaracje-vat/formularze-vat/#VAT-UE
[10]: https://www.podatki.gov.pl/e-deklaracje/wtyczka-do-podpisywania-i-przesylania-danych-xml-z-interaktywnych-formularzy-pdf/
