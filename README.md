# JDG (Jednoosobowa działalność gospodarcza)  — ИП в Польше

[Перейти на сайт](https://sobolevbel.github.io/jdg/)

Для сборки сайта из `markdown` файлов используется генератор статических сайтов [MkDocs](https://www.mkdocs.org/).
С синтаксисом markdown можно ознакомиться [здесь](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

## Как поучаствовать в проекте

1. Форкните проект, создайте новую ветку и начинайте работу.
2. Когда работа будет готова — проверьте локально что сайт собирается и запушьте ветку в репозиторий.
3. Создайте Pull Request в master.

Пошаговые инструкции:
1. От GitHub, на английском: [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
2. На русском [GitHub - Внесение собственного вклада в проекты](https://git-scm.com/book/ru/v2/GitHub-%D0%92%D0%BD%D0%B5%D1%81%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%B2%D0%BA%D0%BB%D0%B0%D0%B4%D0%B0-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B)

## Процесс работы

### Нормальный способ
Для локальной сборки сайта необходимо установить:

- python 3+
- зависимости проекта

Для установки зависимостей проекта используйте команду `pip install -r requirements.txt`

Запустить проект:

`python -m mkdocs serve`

### Docker-way 🙃

Нужны:
- docker
- docker-compose

А дальше запускаете:

`docker-compose up --build`

### Obsidian
Или можете просто установить Obsidian и в нём редактировать и сразу видеть отрендеренный Markdown.

```
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |            | /
  )  |  \  `.___________|/
  `--'   `--'
```
