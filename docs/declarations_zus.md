# Отчёты ZUS

JDG выступает в нескольких ролях: как плательщик взносов (płatnik) и как застрахованное лицо (ubezpieczony).

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

1. [общая официальная инструкция][11] на польском от ZUS
2. [инструкция][12] на польском для пользователей inFakt

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
[11]: https://www.zus.pl/-/korekta-dokumentow-rozliczeniowych
[12]: https://pomoc.infakt.pl/hc/pl/articles/115000763504-Jak-skorygowa%C4%87-deklaracj%C4%99-rozliczeniow%C4%85-ZUS-DRA

[44]: https://buymeacoffee.com/devsobolev
