# Рутинные операции ИП (ежемесячно) с использованием wfirma.pl

Данный документ описывает типичные операции ИП-шника на ryczałt в программе wfirma.pl.
Минимальная настройка wfirma описана [здесь][1].

## Выставление фактур

В последний день месяца (если у вас с заказчиком договоренность на помесячную оплату), или по факту выполнения (отгрузки) работ необходимо сгенерировать и выставить фактуру заказчику.

1. Идем на стартовую страницу.
2. Нажимаем Wystaw fakturę (Выставить фактуру).

![2]

Также это можно сделать на странице **Przychody => Sprzedaż**. Откроется окошко Wystawianie faktury.

### Podstawowe informacje
(Основная информация)

1. Выбираем контрагента, которому выставляем фактуру (из выпадающего списка Nabywca). Адрес и номер NIP или VAT UE подтянутся автоматически из каталога.
2. Дата выставления фактуры. "Сегодня" либо будущую дату, чтобы запланировать наперед.
3. Дата оказания услуги (последний день месяца либо фактическую дату оказания услуги, если они нерегулярны).
4. Выбираем срок оплаты, если необходимо. Считается от дня выставления фактуры.
5. Выбираем метод оплаты. Заполняется автоматически при выборе контрагента из формы контрагента.
6. Выбираем продукт. В нашем случае - услугу. Остальные данные заполнятся автоматически из формы продукта (либо введите вручную).
7. Цена.
8. Налоговая ставка, соответствующая коду PKWiU оказанной услуги.
9. Если экспортируете услугу в ЕС (не в Польшу) или за пределы ЕС, то в Opis напишите:

    > Do rozliczenia podatku VAT zobowiązany jest nabywca usługi (odwrotne obciążenie). Reverse charge - VAT is charged to the buyer.

    или просто:

    > "Odwrotne obciążenie / Reverse charge".

    Более подробно - [на странице, посвященной VAT][4].

![3]

### Księgowe
(Бухгалтерия)

1. Schemat księgowy - Выберите схему бухгалтерского учёта, которая зависит от того, кому и в какую страну вы предоставляете услугу.

![5]

Например, нужно выбрать "Świadczenie usług w UE", если экспортируете услугу в ЕС. В таком случае wfirma сама добавит "Odwrotne obciążenie / Reverse charge" в печатную версию фактуры (перепроверяйте):

![6]

### Zaawansowane

1. Выберите валюту оплаты (Waluta).

    Внимание: если изменили валюту, убедитесь, что цена на вкладке Podstawowe informacje не конвертировалась, иначе исправьте.

2. Укажите счет, на который должна быть оплата.
3. Можете выбрать язык фактуры, например, польский-английский.

![7]

Нажимаем Zapisz, чтобы сохранить данные. Фактура сохранена!

## Печать фактуры

Теперь нам необходимо распечатать фактуру, чтобы она была учтена в wfirma. Также это можно сделать при выставлении фактуры, нажав Zapisz i drukuj.

1. Идем в Przychody.
2. Выбираем фактуру.
3. Нажимаем Drukuj.
4. Нажимаем Dalej.

![8]

Файл фактуры загрузится — теперь его можно отправить клиенту. Файл [желательно сохранить][9] где-нибудь у себя.

## Получение оплаты и учет курсовых разниц

Когда деньги пришли на счет, необходимо добавить приход платежа.

1. Идем в Przychody.
2. Выбираем фактуру.
3. Переходим на вкладку Płatności.
4. Нажимаем Dodaj.
5. Указываем дату поступления денег.
6. Тип оплаты - przelew.
7. Указываем сумму.
8. Нажимаем Zapisz.

![10]

При получении оплаты в иностранной валюте могут возникать курсовые разницы. Закон предписывает учитывать курсовые разницы - как положительные, так и отрицательные.

Убедитесь, что у вас включена [функция расчета курсовой разницы][12] до того, как добавляете приход платежа.

После добавления прихода делаем следующее:

1. Идём в Przychody - Różnice kursowe.
2. Выбираем фактуру.
3. Нажимаем Wystaw DW.

![11]

Все, курсовая разница добавлена и будет учитываться при расчете налоговой базы.

## Вычисление и оплата налогов

### PIT

1. На главной странице, если вы правильно настроили дашборд, у вас будет такая табличка. Нажимаем Wylicz. Также это можно сделать, перейдя на Start - Podatki и нажать Wylicz podatek.

     ![13]

2. В мае платим за апрель. Нажимаем Dalej.

     ![14]

3. Здесь оставляем все так, оно возьмет процент указанный в фактуре и в настройках. Нажимаем Zapisz.

     ![15]

4. Нажимаем Zapłać.

     ![18]

### ZUS

1. На главной странице, если вы правильно настроили дашборд, у вас будет такая табличка. Нажимаем Wylicz. Также это можно сделать, перейдя на Start - ZUS и нажать Wylicz podatek.

     ![16]

2. Нажимаем Zapisz.

     ![17]

3. Нажимаем Zapłać.

     ![19]

## Отправка деклараций

### VAT UE

Если оказываете услугу лицу на территории ЕС, то обязаны иметь регистрацию VAT UE и отправлять ежемесячные декларации.
А те, у кого не было клиентов из ЕС в прошлом месяце, могут смело пропустить этот раздел.

1. Нажимаем Generuj.

     ![20]

2. Нажимаем Dalej.

     ![21]

3. Нажимаем Wyślij.

     ![22]

4. Нажимаем Wyślij do urzędu.

     ![23]

После отправки проверяйте статус. Перейдите в Start - Podatki - Podatek VAT. Если зеленый, то все ок, Ужонд получил вашу декларацию.

![24]

### ZUS DRA

Чтобы отправить декларацию ZUS DRA из wfirma, сначала необходимо верифицировать профиль. Далее:

1. Нажимаем Wyślij.

     ![25]

2. В окошке Wysyłanie deklaracji do ZUS на вкладке "Podpis - wfirma.pl" нажимаем кнопку Zleć do podpisu i wysyłki, чтобы передать ZUS DRA на подпись и отправку.

     ![26]

После отправки проверяйте статус. Перейдите в Start - ZUS - Deklaracje rozliczeniowe. Если зеленый, то все ок.

![27]

### VAT

...

## Курсовая разница od środków własnych

Если получаете оплату в валюте и продаете ее позже для расходов, связанных с предпринимательской деятельностью, например, для уплаты налогов, то также необходимо учесть [курсовую разницу][28] (КР) от собственных средств (środków własnych). Для рассчёта воспользуемся [калькулятором][30] и методом LIFO (метод FIFO или LIFO выбирайте себе сами).

1. Нажимаем Przychody.
2. Нажимаем Inne przychody.
3. Нажимаем Dodaj inny przychód и выбираем Pozostałe przychody (DW).
4. В окошке Dodawanie nowego dowodu wewnętrznego на вкладке Podstawowe informacje заполняем Nazwa przychodu. Примерный текст для положительной КР:

     > Dodatnia różnica kursowa. Rozliczenie różnic kursowych od środków własnych, 100 USD, Data wpływu środków: 2025-05-06, Kurs wpływu środków: 3.775200 (085/A/NBP/2025), Data wypływu środków: 2025-05-12, Kurs wypływu środków: 3.812400 (faktyczny)

5. Указываем сумму.
6. Нажимаем Zapisz i drukuj для сохранения и печати.

![29]

Все, курсовая разница добавлена и будет учитываться при расчете налоговой базы.

[1]: wfirma_settings.md
[2]: images/wfirma_routine/wystaw_fakture.png
[3]: images/wfirma_routine/wystaw_fakture_main.png
[4]: faq.md#vat
[5]: images/wfirma_routine/wystaw_fakture_ksiegowe.png
[6]: images/wfirma_routine/wystaw_fakture_vat_comment.png
[7]: images/wfirma_routine/wystaw_fakture_zaawansowane.png
[8]: images/wfirma_routine/fakture_drukuj.png
[9]: workflow.md#kakie-dokumenty-khranit
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
[28]: workflow.md/#uchet-kursovykh-raznits
[29]: images/wfirma_routine/kr_od_wlasnych_srodkow.png
[30]: https://kalkulatory.gofin.pl/kalkulatory/kalkulator-roznic-kursowych-od-wlasnych-srodkow-walutowych
