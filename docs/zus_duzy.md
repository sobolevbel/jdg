# Переход на Składki Preferencyjne и Duży ZUS

## Шаг 1

Логинимся в [zus.pl][1].

## Шаг 2

Вверху справа выбираем вкладку **ePłatnik**, в меню слева выбираем **Rejestr ubezpieczonych -> Aktualni ubezpieczeni**

Нажимаем кнопку **Podgląd**

![zus_actualni_ubezpieczeni][2]

Открывается картотека

![zus_kartoteka_ubezpieczonego][3]

## Шаг 3

Внутри картотеки можем выбрать закладку **Ubezpieczenia**

Отображается текущий код и дата, начиная с которой он действует.
На картинке ниже виден пример, когда уже действуют складки преференцийне (Składki preferencyjne) и надо перейти на дужий ZUS (Duży ZUS).

Информация о всех кодах приведена ниже.

Нажимаем **Zmień dane**

![zus_kartoteka_ubezpieczonego_zmien_dane][4]

Появляется пошаговая форма для внесения изменений

Ставим галочку в пункте **Dane ubezpieczeń** и нажимаем кнопку **Dalej**

![zus_obsluga_ubezpieczonego][5]

## Шаг 4

Нажимаем кнопку **Edytuj**

![zus_obsluga_ubezpieczonego_edytuj][6]

Появляется попап с текущими данными

![zus_kod_tytulu_ubezpieczenia][7]

Под кодом типа страховки располагаются четыре секции:

- **Obowiazkowe ubezpieczenia społeczne** (Обязательные складки сполечные). Если была ульга на старт, чекбоксы будут
  пустые, в этом случае надо отметить 3 из 4, как на картинке (все, кроме “Chorobowemu”)
- **Dobrowolne ubezpieczenia społeczne** (Добровольные складки сполечные). Тут можно при желании отметить складку
  хоробову, чтобы иметь возможность получать больничные
- **Obowiązkowe ubezpieczenie zdrowotne** (Обязательная складка здровотная)
- **Dobrowolne ubezpieczenie zdrowotne** (Добровольная складка здровотная)

Актуализируем данные

- меняем Kod tytułu ubezpieczenia
- меняем даты в левой части на первое число текущего месяца
- при переходе с ulga na start также отмечаем галочками складки сполечные, кроме хоробовой
- при желании платить складку хоробову (для возможности получения больничных) отмечаем ее справа, в добровольной части,
  и соответственно ставим дату — первое число текущего месяца
- нажимаем **Zapisz**

Попап закрывается и шаг 4 показывает обновленные данные.
На картинке ниже пример, когда совершен переход со Składki preferencyjne на Duży ZUS.

![składki_preferencyjne_to_duzy_zus][9]

Нажимаем **Dalej**

## Шаг 5

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

## Итог

Заявки сразу переносятся в **Dokumenty -> Dokumenty wysłane**.

После обработки данные в картотеке должны обновиться (см. скриншот 3).

Можно еще проверить, что в картотеке в закладке **Członkowie rodziny** остались все ранее приписанные родственники.

Через какое-то время заявки появятся в **Dokumenty w ZUS**.

[Поблагодарить автора :coffee:][12]

[1]: https://www.zus.pl/
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
