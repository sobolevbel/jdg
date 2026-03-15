# Декларации

Для регистрации и актуализации информации:

- CEIDG-1 ([Регистрация JDG](https://sobolevbel.github.io/jdg/registration_jdg/))
- VAT-R ([польский VAT](https://sobolevbel.github.io/jdg/registration_vat/), [VAT UE](https://sobolevbel.github.io/jdg/registration_vat_ue/))

Ежемесячные декларации:

- ZUS DRA
- ZUS RCA (за наёмных работников)
- JPK_V7M
- VAT UE
- VAT-9M

Ежеквартальные декларации:

- JPK_V7K

Ежегодные декларации:

- PIT (PIT-28, PIT-36, PIT-36L)
- Годовой расчёт ZUS (это доп. блок XII в декларации ZUS DRA 04)
- JPK_EWP или JPK_PKPiR
- ZUS RWS ([каникулы](https://sobolevbel.github.io/jdg/zus_vacation/#kak-podat-zaiavku-na-zus-kanikuly))

## ZUS DRA

С 2022 года в связи с переходом на Polski Ład предприниматели обязаны отправлять декларацию ZUS DRA за себя каждый месяц.

1. Перейти на вкладку ePłatnik. (если вкладка отсутствует - нужно активировать согласно [руководству](https://www.zus.pl/portal/pomoc/index.html?aktywacja_p3atnika.html))

    ![Choose ePłatnik tab][1]

2. В меню **Dokumenty** выбрать пункт **Dodaj dokument**

    ![Dodaj dokument][2]

3. В открывшемся окне из большого списка деклараций выбрать ZUS DRA и нажать Wybierz -> Przejdz do kreatora.

    ![Choose ZUS DRA][3]

4. Любуемся своими данными и жмем Dalej.
5. Nowy komplet rozliczeniowy -> Dalej.
6. На следующем шаге нужно выбрать 2022 год и нужный месяц, поставить галочку, что оплачиваем зус за себя и в выпадающем списке выбрать тип декларации 6 - до 20 числа. Если у вас действует **Ulga na start** - то поле "Stopa procentowa składek na ubezpieczenie wypadkowe" оставьте пустым. Иначе, вписываем туда значение **1,67**. Нажимаем Dalej. Если используете **Ulga na start** - то соглашайтесь с сообщением о том, что не указали процентную ставку на ubezpieczenie wypadkowe. Вам это не нужно.

    ![basic declaration options][6]

7. С 2022 года ЗУС на рычалте зависит от доходов. Поэтому на этом шаге нужно указать ваши доходы за текущий или прошлый год. Если у вас Ulga na start - то Kod tytułu ubezpieczenia: 054000, если preferencyjny zus (после полугода ульги на старт) - то 057000.

    ![Podstawy składek][7]

    Чуть ниже на странице находим форму
    **"Forma opodatkowania obowiązująca w danym miesiącu oraz przychód i dochód z działalności gospodarczej dla celów wyliczenia składki miesięcznej na ubezpieczenie zdrowotne"**
    и выбираем свою форму налогообложения. Я сделаю пример на основе рычалта.

    Есть два варианта расчета здровотной складки зуса: на основе доходов за текущий или за прошлый год. Если вы в прошлом году не вели деятельность - то вы можете рассчитать только на основе текущего года. Я сделаю пример на основе текущего года.

    Обратите внимание, нужно заполнять либо поле за текущий год, либо за прошлый. Если заполнить оба поля - будет ошибка. Укажите сумму вашего дохода с начала года до конца месяца, за который подается декларация (до уплаты налогов, без VAT). То есть, если подаете декларацию в августе за июль, то указывается сумму дохода с начала года до 31.07.

    ![Podstawy składek][71]

    Теперь в самом низу жмем кнопку **Oblicz** и сайт подсчитывает нам основание для складки здровотной.

    ![Podstawy składek][72]

    Осталось пролистать вверх и в первой форме поставить галочку "Podstawy minimalne" чтобы рассчитать все складки.

    ![Podstawy składek][73]

    Нажимаем Dalej. Сайт спрашивает хотим ли платить в Fundusz pracy. Можем отказаться.

8. На следующем экране менять ничего не нужно, даже если в ваш ZUS вписаны члены вашей семьи. Dalej.

    ![Nothing to change][8]

9. Теперь можно посмотреть что получилось с помощью кнопки Podgląd. Сумма к оплате указана на второй странице в разделе IX поле **02. Kwota do zapłaty**. Убедитесь что она верная.

10. Подписать декларацию профилем зауфаным и отправить с помощью кнопочек Weryfikuj и Wyślij i zakończ.

    ![Weryfikuj и Wyślij i zakończ][10]

Найти отправленные декларации можно на странице Dokumenty -> Dokumenty wysłane.

[Поддержите наш гайд чашкой кофе ♥][44]

### Коректа

Коректа ZUS DRA - это такой же ZUS DRA, только версия 2 (тип корректа) вместо 1 (первичная подача).

1. [общая официальная инструкция](https://www.zus.pl/-/korekta-dokumentow-rozliczeniowych) на польском от ZUS
2. [инструкция](https://pomoc.infakt.pl/hc/pl/articles/115000763504-Jak-skorygowa%C4%87-deklaracj%C4%99-rozliczeniow%C4%85-ZUS-DRA) на польском для пользователей inFakt

## VAT (польский)

Плательщики польского VAT (czynny płatnik VAT) имеют обязательство ежемесячной (JPK_V7M) или ежеквартальной (JPK_V7K)
отправки декларации JPK_VAT, в которой отражены ваши продажи и покупки с VAT.

Статья на [biznes.gov.pl][11] про декларации VAT.

### Когда отправлять декларацию

Декларация JPK_V7M должна быть отправлена до 25 числа каждого месяца за предыдущий месяц. То есть, за июль нужно отправить
декларацию до 25 августа. Если 25 число выпадает на выходной - то срок отправки переносится на следующий рабочий день.

!!! info "Нулевой JPK"
    Даже если в отчетном месяце не было транзакций, все-равно необходимо отправить нулевую декларацию VAT.
    В полях PodatekNalezny и PodatekNaliczony нужно вписать "0.00".

### Какую программу использовать

Вы можете использовать любую программу, поддерживающую генерацию/отправку VAT деклараций, например:

* [e-mikrofirma][12] от министерства финансов.

### Как отправить декларацию

Coming soon...

### VAT от аренды

Как учитывать VAT в inFakt при сдаче жилья в аренду?

- [Ответ](https://t.me/JDG_PBH/547209) в Telegram
- [Уточнение от бухгалтера](https://t.me/JDG_PBH/547215) в Telegram

Coming soon...

## VAT-UE

Плательщики европейского VAT (VAT UE, регистрация в реестре VIES) имеют обязательство отправки декларации VAT UE за те месяцы, в которых получили доход за услуги контрагентам в ЕС.
В декларации VAT-EU указывается номер VAT-EU контрагента и сумма оказанных услуг.

### Когда отправлять декларацию

Декларация подаётся в электронном виде в налоговую инспекцию до 25-го числа месяца, следующего за месяцем, в котором возникло налоговое обязательство по совершённой сделке или в котором было произведено перемещение товаров либо изменение в рамках процедуры склада call-off stock.

!!! info "Нулевая VAT UE"
    «Нулевая» - это значит вообще ничего не заполнено, пусто. Такую можно не отправлять. Если всё же отправили, то ничего страшного.

⚖️ В [art. 100 ust. 1](https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/podatek-od-towarow-i-uslug-17086198/art-100) ustawy o VAT перечислены случаи, когда VAT-UE надо подавать.

### Как отправить декларацию

См. [Электронные формуляры VAT](https://www.podatki.gov.pl/podatki-firmowe/vat/formularze/#VAT-UE) на оф. сайте налоговой.

### Коректа

VAT-UEK используется для исправления ранее отправленной декларации VAT-UE.

Coming soon...

## PIT (годовая декларация)

Подробнее читайте в статье о [декларации PIT][88].

## Декларации для ИП на паузе

Во время приостановки предпринимательской деятельности или после ликвидации НЕ НУЖНО отправлять:
- декларации VAT
- отчёты ZUS DRA

Нужно отправить даже во время паузы:
- декларации VAT и отчёт ZUS DRA за последний месяц (когда ещё велась деятельность).
- годовую налоговую декларацию PIT.
- годовую декларацию ZUS, если в предыдущем году велась деятельность. Если в апреле текущего года (2026) уже не велась деятельность, то это будет пустой ZUS DRA 04/2026 с заполненным кодом страхования в блоке X и заполненным блоком XII (как описано в [инструкции](https://t.me/JDG_PBH/542098) в Telegram).

[Поддержите наш гайд чашкой кофе ♥][44]{ .md-button .md-button--primary }

[1]: images/zus_dra/zus-dra-1.png
[2]: images/zus_dra/zus-dra-2.png
[3]: images/zus_dra/zus-dra-3.png
[6]: images/zus_dra/zus-dra-6.png
[7]: images/zus_dra/zus-dra-7-new.png
[71]: images/zus_dra/zus-dra-7-1-new.png
[72]: images/zus_dra/zus-dra-7-2-new.png
[73]: images/zus_dra/zus-dra-7-3-new.png
[8]: images/zus_dra/zus-dra-8.png
[10]: images/zus_dra/zus-dra-10.png
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
[23]: declarations.md#4-tip-dokhodov
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
[44]: https://buymeacoffee.com/devsobolev
[46]: https://t.me/JDG_PBH/372301
[47]: https://dzieciom.pl/podopieczni/42671
[48]: https://dzieciom.pl/podopieczni/43917
[49]: https://www.siepomaga.pl/vasilisa-loban
[50]: https://dzieciom.pl/podopieczni/40923
[51]: https://fanimani.pl/standwithukraine/
[52]: https://www.facebook.com/bmhuborg
[53]: https://news.zerkalo.io/economics/91472.html
[54]: https://devby.io/news/support-devby24
[55]: https://t.me/partyzanka_rb_pl/650
[56]: https://www.siepomaga.pl/artem-padzialowski
[57]: https://dzieciom.pl/podopieczni/44133
[58]: https://www.siepomaga.pl/margarita
[59]: https://www.siepomaga.pl/nastka-liaszczewicz
[60]: https://www.siepomaga.pl/yeudakim-zacharewicz
[61]: images/pit_eurzad_skarbowy/01.png
[62]: images/pit_eurzad_skarbowy/02.png
[63]: images/pit_eurzad_skarbowy/zus01.png
[64]: images/pit_eurzad_skarbowy/zus02.png
[65]: images/pit_eurzad_skarbowy/03.png
[66]: images/pit_eurzad_skarbowy/04.png
[67]: images/pit_eurzad_skarbowy/05.png
[68]: images/pit_eurzad_skarbowy/06.png
[69]: images/pit_eurzad_skarbowy/07.png
[70]: images/pit_eurzad_skarbowy/08.png
[77]: images/pit_eurzad_skarbowy/09.png
[78]: https://www.siepomaga.pl/paulina-danilchanka

[88]: declarations_pit.md
