# Переход на Duży ZUS

Когда все льготы заканчиваются (обычно после 24 месяцев składek preferencyjnych), то необходимо перейти на **Duży ZUS**.

!!! success "Официальный сайт"
    [Jakie składki na ubezpieczenia społeczne płaci przedsiębiorca do ZUS][19]

!!! question "Когда переходить на duży ZUS"
    См. [Сроки перехода между режимами][20]

## Что нужно сделать

Есть бухгалтер? Просто напомните ему о том, что у вас скоро заканчиваются все льготы.
Нет бухгалтера? Читайте инструкцию ⬇️

1. Сняться с учёта в ZUS с помощью бланка **ZUS ZWUA**.
2. Зарегистрироваться для страхования:

    a. Если работаете параллельно на Umowa o Pracę, то с помощью бланка **ZUS ZZA**;

    b. Иначе с помощью бланка **ZUS ZUA** с новым кодом 0570 xx. Если вы переходите со składek preferencyjnych на duży ZUS, то ваш старый код: **0570**, а новый: **0510**.

3. Переключить в настройках inFakt/wFirma/iFirma на duży ZUS.

Подробно и наглядно каждый из этих шагов описан ниже.

### Шаг 1

Логинимся в [eZUS][1] одним из доступных для иностранцев способов:

- логин и пароль
- профиль зауфаны
- через банк

Если какой-то способ временно не работает, то попробуйте другой.

Никак не получается войти в eZUS? См. [возможные причины и решения][22].

### Шаг 2

Вверху справа выбираем вкладку **ePłatnik**, в меню слева выбираем **Rejestr ubezpieczonych -> Aktualni ubezpieczeni**.

Нажимаем кнопку **Podgląd**.

![zus_actualni_ubezpieczeni][2]

Открывается картотека  Kartoteka ubezpieczonego

![zus_kartoteka_ubezpieczonego][3]

### Шаг 3

Внутри картотеки можем выбрать закладку **Ubezpieczenia**.

Отображается текущий код и дата, начиная с которой он действует.
На картинке ниже виден пример, когда уже действуют складки преференцийне (Składki preferencyjne) и надо перейти на дужий ZUS (Duży ZUS).

Информацию обо всех кодах для предпринимателей ищите в [таблице](http://127.0.0.1:8000/jdg/zus_next_level/#tablitsa-kodov-strakhovaniia-zus).

Нажимаем **Zmień dane**.

![zus_kartoteka_ubezpieczonego_zmien_dane][4]

На вкладке Obsługa ubezpieczonego появляется пошаговая форма для внесения изменений.

На шаге "Wybierz dane do zmiany" выбираем галочку в пункте **Dane ubezpieczeń** и нажимаем кнопку **Dalej**.

![zus_obsluga_ubezpieczonego][5]

### Шаг 4

На шаге "Dane ubezpieczeń" нажимаем кнопку **Edytuj**.

![zus_obsluga_ubezpieczonego_edytuj][6]

Появляется попап с названием "Zgłoszenie ubezpieczonego → Tytuły ubezpieczeń" с текущими данными.

![zus_kod_tytulu_ubezpieczenia][7]

**Актуализируем данные:**

- Слева меняем Kod tytułu ubezpieczenia (код типа страховки; напоминаем, что для перехода на duży ZUS ваш новый код: **05 10**).
- Меняем даты в левой части на первое число того месяца, с которого начинается Duży ZUS (обычно это текущий месяц). В результате в **ZUS ZUA** в поле *Data powstania obowiązku ubezpieczenia* (или *Data zgłoszenia do ubezpieczenia*) будет указан тот же день, что и в **ZUS ZWUA**. Тогда у иностранца нет перерыва в страховании.

* Справа выбираем *Kod wykonywanego zawodu*. Нужно для статистики. Подробнее см. в [таблице кодов профессий][13].

* Под кодом типа страховки располагаются четыре секции:

    - **Obowiazkowe ubezpieczenia społeczne** (Обязательные взносы на соцстрахование). Если была ульга на старт, чекбоксы будут пустые. В этом случае надо отметить 3 из 4 как на картинке:
        * [x] Emerytalnemu 
        * [ ] Chorobowemu
        * [x] Rentowym
        * [x] Wypadkowemu

    - **Dobrowolne ubezpieczenia społeczne** (Добровольные взносы на соцстрахование).
        * [ ] Chorobowym - тут можно при желании отметить складку хоробову, чтобы иметь возможность получать больничные. Решение остаётся за вами, но по результатам опроса большинство предпринимателей отказывается от неё. Если отметили галочкой, то соответственно поставьте дату — первое число текущего месяца.
    - **Obowiązkowe ubezpieczenie zdrowotne** (Обязательный взнос на медстрахование)
    - **Dobrowolne ubezpieczenie zdrowotne** (Добровольный взнос на медстрахование)

- нажимаем **Zapisz**

Попап закрывается и шаг 4 показывает обновленные данные.
На картинке ниже пример, когда совершен переход со Składki preferencyjne на Duży ZUS.

![składki_preferencyjne_to_duzy_zus][9]

Нажимаем **Dalej**

### Шаг 5

На последнем шаге показаны два автоматически созданных документа:

- ZUS ZUA – для регистрации с новым кодом
- ZUS ZWUA – для формальной отмены предыдущей регистрации

Нажимаем **Weryfikuj** чтобы кнопка **Wyślij i zakończ** стала активной.

![documenty_zua_zwua][10]

После проверки ZUA получает статус Błąd (ошибка), связанный с тем, что сначала должна быть обработана заявка ZWUA и лишь
потом ZUA, но это формальность, так и должно быть. На самом деле заявки посылаются в ZUS одновременно и обрабатываются
работником вместе, в правильном порядке.

![document_zua_error][11]

Нажимаем **Wyślij i zakończ**, подписываем через ePUAP обе заявки одной подписью.

### Итог

Заявки сразу переносятся в **Dokumenty -> Dokumenty wysłane**.

После обработки данные в картотеке должны обновиться (см. скриншот 3).

TODO: помогите сделать гайд лучше! добавьте сюда скриншот, на котором виден код 05 10.

Можно ещё проверить, что в картотеке в закладке **Członkowie rodziny** остались все ранее приписанные родственники.

Через какое-то время заявки появятся в **Dokumenty w ZUS**.

## UPP - подтверждение отправки

См. [UPP][21].

## Типичные ошибки

См. [сборник ошибок][22].

[Поблагодарить автора :coffee:][12]

[1]: https://www.zus.pl/ezus/logowanie
[2]: images/zus_duzy/duzy_zus_1.png
[3]: images/zus_duzy/duzy_zus_2.png
[4]: images/zus_duzy/duzy_zus_3.png
[5]: images/zus_duzy/duzy_zus_4.png
[6]: images/zus_duzy/duzy_zus_5.png
[7]: images/zus_duzy/duzy_zus_6.png
[9]: images/zus_duzy/duzy_zus_7.png
[10]: images/zus_duzy/duzy_zus_8.png
[11]: images/zus_duzy/duzy_zus_9.png
[12]: https://justandrei.github.io/coffee
[13]: zus_next_level.md/#tablitsa-kodov-professii
[19]: https://www.biznes.gov.pl/pl/portal/00274
[20]: zus_next_level.md/#sroki-perekhoda-mezhdu-rezhimami
[21]: zus_next_level.md/#upp-podtverzhdenie-otpravki
[22]: zus_errors.md
