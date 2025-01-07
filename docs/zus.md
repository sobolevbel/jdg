# Zakład Ubezpieczeń Społecznych

Все предприниматели, ведущие JDG в Польше обязаны застраховаться в государственной
[службе социального страхования][1] и оплачивать страховые взносы.

## Размер взносов

ZUS состоит из 2 основных частей:

1. Медицинское страхование (Składka zdrowotna)
2. Социальное страхование, включает в себя
    1. Пенсионное страхование (Ubezpieczenie emerytalne)
    2. Страхование от потери трудоспособности (Ubezpieczenie rentowe)
    3. Страхование от несчастных случаев (Ubezpieczenie wypadkowe)
    4. Фонд труда и Фонд солидарности (Fundusz pracy i Fundusz Solidarnościowy)
    5. Страхование на случай болезни (Ubezpieczenie chorobowe)

Размер взносов по медицинскому страхованию в месяц рассчитывается по формуле `базовая ставка * 9%`.
Размер базовой ставки рассчитывается от дохода:

1. Доход до 60 000 злотых: Базовая ставка вычисляется как 60% от средней заработной платы
2. Доход от 60 000 злотых до 300 000 злотых: Базовая ставка вычисляется как 100% от средней заработной платы
3. Доходы выше 300 000 злотых: Базовая ставка вычисляется как 180% процентов от средней зарплаты

В буквальных цифрах **на 2024 год** это:

1. Доход до 60 000 злотых: 4.660,71 zł
2. Доход от 60 000 злотых до 300 000 злотых: 7.767,85 zł
3. Доходы выше 300 000 злотых: 13.982,13 zł

Далее, подставим в формулу числа и получим размеры взносов по медицинскому страхованию:

1. 4.660,71  * 9% = 419,46 zł
2. 7.767,85 * 9% = 699,11 zł
3. 13.982,13 * 9% = 1258,39 zł

Важно отметить, что при превышении порога, пересчет идет и за прошлые месяцы.

**Пример:**

Максим облагается Ryczałt-налогом на зарегистрированный доход.
В марте 2024 года доход Макса превысил 60 000 злотых, а в октябре - более 300 000 злотых.
Как будет выглядеть ежегодный расчет взноса на здравоохранение?

В течение года Максим должен выплачивать взносы на медицинское обслуживание по следующей схеме:

- Январь - 419,46 zł,
- Февраль  - 419,46 zł,
- Март - 699,11 zł (превышение порога в 60 000 zł),
- Апрель - 699,11 zł,
- Май - 699,11 zł,
- Июнь - 699,11 zł,
- Июль - 699,11 zł,
- Август- 699,11 zł,
- Сентябрь - 699,11 zł,
- Октябрь  - 1258,39 zł (превышение порога в 300 000 zł),
- Ноябрь - 1258,39 zł,
- Декабрь - 1258,39 zł

В течение года Макс выплатил взносы на здравоохранение на общую сумму 9507,86 злотых: `419,46 * 2 + 699,11 * 7 + 1258,39 * 3`.

Поскольку за календарный год Макс превысил порог в 300 000 злотых, он должен ежемесячно делать взносы за медицинское страхование
в размере 1258,39 злотых. Таким образом, годовой взнос составляет: `1258,39 * 12 = 15100,68`, но сумма
взносов Максима из примера выше составила всего 9507,86 злотых. Это означает, что после завершения годового расчета у Максима
осталась недоплата взноса на медицинское обслуживание. Он обязан выплатить еще 5592,82 злотых: `15100,68 - 9507,86`.

## Таблица расчета взносов ZUS

<table>
    <thead>
        <tr>
            <th class="border-r text-center">
                Składki ZUS 2024<br>
                Ryczałt<br>
                <span class="text-bl">A</span> +
                <span class="text-rd">B</span> +
                <span class="text-green">C</span> +
                <span class="text-gr">D</span>
            </th>
            <th class="border-r">Годовой доход</th>
            <th class="border-r ulga">Ulga na start</th>
            <th class="border-r preferencyjne-01-06">Składki preferencyjne (c 01.01 до 31.06)</th>
            <th class="border-r preferencyjne-07-12">Składki preferencyjne (c 01.07 до 31.12)</th>
            <th class="duzy">Duży zus</th>
        </tr>
    </thead>
    <tbody>
        <tr class="ulga-bg">
            <th rowspan="3" class="border-r border-t text-bl text-bold valign-center">
                A: Składka zdrowotna
            </th>
            <td class="border-r">0 - 60 000</td>
            <td colspan="4" class="text-bl text-center text-bold">419,46</td>
        </tr>
        <tr class="ulga-bg">
            <td class="border-r">60 000.01 - 300 000</td>
            <td colspan="4" class="text-bl text-center text-bold">699,11</td>
        </tr>
        <tr class="ulga-bg">
            <td class="border-r">&gt; 300 000</td>
            <td colspan="4" class="text-bl text-center text-bold">1258,39</td>
        </tr>
        <tr>
            <th rowspan="4" class="border-r border-t text-rd text-bold valign-center">
                B: ubezpieczenie społeczne
            </th>
            <td class="border-r">Emerytalna</td>
            <td class="border-r ulga text-center">0</td>
            <td class="border-r preferencyjne-01-06 text-center">248,41</td>
            <td class="border-r preferencyjne-07-12 text-center">251,81</td>
            <td class="duzy text-center">916,35</td>
        </tr>
        <tr>
            <td class="border-r">Rentowa</td>
            <td class="border-r ulga text-center">0</td>
            <td class="border-r preferencyjne-01-06 text-center">101,81</td>
            <td class="border-r preferencyjne-07-12 text-center">103,20</td>
            <td class="duzy text-center">375,55</td>
        </tr>
        <tr>
            <td class="border-r">Wypadkowa</td>
            <td class="border-r ulga text-center">0</td>
            <td class="border-r preferencyjne-01-06 text-center">21,25</td>
            <td class="border-r preferencyjne-07-12 text-center">21,54</td>
            <td class="duzy text-center">78,40</td>
        </tr>
        <tr class="text-rd">
            <td class="border-r text-bold">
                <b>Вместе</b>
            </td>
            <td class="border-r ulga text-bold text-center"><b>0</b></td>
            <td class="border-r preferencyjne-01-06 text-bold text-center"><b>371,47</b></td>
            <td class="border-r preferencyjne-07-12 text-bold text-center"><b>376,55</b></td>
            <td class="duzy text-bold text-center"><b>1370,30</b></td>
        </tr>
        <tr class="text-green">
            <td colspan="2" class="border-r border-t text-green text-bold valign-center">
                <b>C: Fundusz Pracy</b>
            </td>
            <td class="border-r ulga text-center">0</td>
            <td class="border-r preferencyjne-01-06 text-center">0</td>
            <td class="border-r preferencyjne-07-12 text-center">0</td>
            <td class="duzy text-bold text-center">115,01</td>
        </tr>
        <tr class="text-bold">
            <th rowspan="3" class="border-r text-bold">
                <b>Вместе (<span class="text-bl">A</span> +
                <span class="text-rd">B</span> +
                <span class="text-green">C</span>):</b>
                <td class="border-r">0 - 60 000</td>
                <td class="border-r ulga text-center text-bold">419,46</td>
                <td class="border-r preferencyjne-01-06 text-center text-bold">790,93</td>
                <td class="border-r preferencyjne-07-12 text-center text-bold">796,01</td>
                <td class="duzy text-bold text-center text-bold">1904,77</td>
            </th>
        </tr>
        <tr class="text-bold">
            <td class="border-r">60 000.01 - 300 000</td>
            <td class="border-r ulga text-center text-bold">699,11</td>
            <td class="border-r preferencyjne-01-06 text-center text-bold">1070,58</td>
            <td class="border-r preferencyjne-07-12 text-center text-bold">1075,66</td>
            <td class="duzy text-bold text-center text-bold">2184,42</td>
        </tr>
        <tr class="text-bold">
            <td class="border-r">&gt; 300 000</td>
            <td class="border-r ulga text-center text-bold">1258,39</td>
            <td class="border-r preferencyjne-01-06 text-center text-bold">1629,86</td>
            <td class="border-r preferencyjne-07-12 text-center text-bold">1634,94</td>
            <td class="duzy text-bold text-center">2743,7</td>
        </tr>
        <tr class="text-gr">
            <td colspan="2" class="border-r border-t text-gr text-bold valign-center">
                <b>D: Chorobowa</b><br>
                (не обязательная)
            </td>
            <td class="border-r ulga text-bold text-center">0</td>
            <td class="border-r preferencyjne-01-06 text-bold text-center">31,18</td>
            <td class="border-r preferencyjne-07-12 text-bold text-center">31,61</td>
            <td class="duzy text-bold text-center">115,01</td>
        </tr>
    </tbody>
</table>

Медицинскую часть (zdrowotna) нужно платить всегда, даже если параллельно есть
еще страховка по трудовому договору. Медицинская складка даёт доступ
к медицинскому обслуживанию для предпринимателя и членов его семьи.

От уплат социальной складки зависят социальные выплаты. В том числе —
декретные, больничные, будущая пенсия, но эти выплаты пропорциональны сумме с которой вы оплачиваете взносы.

Первые 6 месяцев можно пользоваться льготой "Ulga na start" и не платить
социальные складки. Соответственно, социальными выплатами тоже воспользоваться не получится. После истечения льготы на старт, можно
[перейти][23] на следующую льготу — **ZUS preferencyjne** и пользоваться ею в
течение 24 месяцев. После 30 месяцев деятельности начинается оплата полного ZUS (duży zus) — минимум 60% от средней заплаты.

Больше деталей на [biznes.gov.pl][25] и [e-pity][24]

## Ulga na start

Для новых предпринимателей есть возможность получить льготу
для оплаты ZUS на первые полгода и уменьшенный ZUS на следующие два года.

Для получения льготы нужно во время регистрации в ZUS указать в декларации ZUS ZZA код **05 40**.

[Официальный сайт][2]

## Регистрация

Предприниматель обязан в течение 7 дней после регистрации JDG зарегистрироваться
в ZUS. Сделать это можно как во время регистрации деятельности, так и позже.

## Как узнать свой счет для оплаты ZUS

После регистрации ИП через +-2 недели должно прийти письмо (физическое, конверт) из ZUS со всеми счетами и т.д. и функционал появится в кабинете, на сайте [eskladka.pl][3].

А так же можно проверить счета на вышеупомянутом сайте, для этого необходимо ввести два идентификатора NIP и REGON (или NIP и PESEL).

## Как платить ZUS

Оплачивать ZUS нужно до 20 числа следующего месяца за отчетным.
Например, за июль зус оплачивается до 20 августа.

Оплату следует производить обычным переводом на индивидуальный счет ZUS.
В назначении платежа можно писать что угодно, это ни на что не влияет.

## Справка о незадолженности в ZUS

- Можно пойти физически в отделение ZUS (любое, не обязательно вашего района) и получить все справки с мокрыми печатями
- Можно на [портале ZUS](https://www.zus.pl/portal/)

1. Переходим на сайт [Katalog usług elektronicznych](https://www.zus.pl/portal/obszar-platnika.npi#KUS0001), в окно фильтра вписываем `RWN`.

    ![images/zus_zaswiadczenie_5.1.jpeg](images/zus_zaswiadczenie/zus_zaswiadczenie_5.1.jpeg)

2. Нас перекидывает в **ZUS** на форму заполнения `wniosek RWN`. Проверяем данные в форме.

   ![zus_zaswiadczenie_2.png][7]

3. Выбираем кол-во экземпляров справки и нажимаем **Zapisz**.

   ![zus_zaswiadczenie_2.1.png][8]

4. Закрываем документ.

   ![zus_zaswiadczenie_2.2.png][9]

5. Соглашаемся.

    ![zus_zaswiadczenie_2.3.png][10]

6. Проверяем документ и нажимаем **Wyślij**.

   ![zus_zaswiadczenie_2.4.png][11]

7. Подписываем через Profil Zaufany

   ![zus_zaswiadczenie_2.5.png][12]

8. Нажимаем **Ok**

   ![zus_zaswiadczenie_2.6.png][13]

9. Нажимаем **Ok**

   ![zus_zaswiadczenie_2.7.png][14]

10. После того как дождались письмо (1-7 дней), заходим в [ZUS][1]. В меню выбираем Płatnik. Слева в меню **Dokumenty i wiadomości** **Korespondencja z ZUS**. Выбираем документ и подтверждаем получение через Profil Zaufany.

    ![zus_zaswiadczenie_4.png][15]

11. После подтверждения появится пункт **Szczegóły**

    ![zus_zaswiadczenie_4.1.png][16]

12. Открываем документ **Przeglądaj dokument**.

    ![zus_zaswiadczenie_4.2.png][17]

13. Печатаем **Drukuj**.

    ![zus_zaswiadczenie_4.3.png][18]

## Добавление ePUAP к профилю ZUS

1. Если у вас есть profil zaufany, перейдите к Panel ogólny -> Ustawienia -> Dane profilu и нажмите Dodaj powiązanie z ePUAP.

    ![zus_epuap_1.png][19]

2. Вы будете перенаправлены на страницу входа в доверенный профиль, залогиньтесь и подпишите profilem zaufany.

    ![zus_epuap_2.png][20]
    ![zus_epuap_3.png][21]

3. в итоге профиль ZUS будет связан с profilem zaufanym.

    ![zus_epuap_4.png][22]

[1]: https://www.zus.pl
[2]: https://www.biznes.gov.pl/pl/firma/zus/chce-rozliczac-zus/ulga-na-start-6-miesiecy-bez-skladek-na-ubezpieczenie-spoleczne
[3]: https://eskladka.pl/Home
[4]: https://www.biznes.gov.pl/pl/firma/zus/chce-rozliczac-zus/proc_750-zaswiadczenie-o-niezaleganiu-zus
[5]: images/zus_zaswiadczenie/zus_zaswiadczenie_1.png
[6]: images/zus_zaswiadczenie/zus_zaswiadczenie_1.1.png
[7]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.png
[8]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.1.png
[9]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.2.png
[10]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.3.png
[11]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.4.png
[12]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.5.png
[13]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.6.png
[14]: images/zus_zaswiadczenie/zus_zaswiadczenie_2.7.png
[15]: images/zus_zaswiadczenie/zus_zaswiadczenie_4.png
[16]: images/zus_zaswiadczenie/zus_zaswiadczenie_4.1.png
[17]: images/zus_zaswiadczenie/zus_zaswiadczenie_4.2.png
[18]: images/zus_zaswiadczenie/zus_zaswiadczenie_4.3.png
[19]: images/zus_epuap/zus_epuap_1.png
[20]: images/zus_epuap/zus_epuap_2.png
[21]: images/zus_epuap/zus_epuap_3.png
[22]: images/zus_epuap/zus_epuap_4.png
[23]: zus_obnizone_skladki.md
[24]: https://www.e-pity.pl/kalkulatory-podatkowe/skladki-zus-przedsiebiorcy/
[25]: https://www.biznes.gov.pl/pl/portal/00286#2
