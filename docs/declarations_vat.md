# Декларации VAT

VAT = НДС - налог на добавленную стоимость.

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
* inFakt

### Как отправить декларацию

??? info "Пользователи inFakt"
    В inFakt можно выслать декларацию напрямую из программы.
    См. [Отправка декларации VAT JPK_V7M](https://sobolevbel.github.io/jdg/infakt_routine/#otpravka-deklaratsii-vat-jpk-v7m).

??? info "Пользователи wFirma"
    В wFirma можно выслать декларацию напрямую из программы.
    Путь: Podatki - JEDNOLITY PLIK KONTROLNY - dodaj
    оно автоматически всё считает и генерирует декларацию. Далее надо выслать, подтвердив суммой дохода из декларации PIT, отправленной в предыдущем году.
    [Инструкция](https://pomoc.wfirma.pl/-jpk-vat-jednolity-plik-kontrolny-dla-rejestrow-vat) на польском.

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
