# JDG — ИП в Польше

[![Деплой](https://github.com/sobolevbel/jdg/actions/workflows/ci.yml/badge.svg)](https://github.com/sobolevbel/jdg/actions/workflows/ci.yml)
[![Лицензия: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/sobolevbel/jdg)](https://github.com/sobolevbel/jdg/stargazers)

Комьюнити-гайд по открытию и ведению **JDG** (jednoosobowa działalność gospodarcza — ИП)
в Польше для иностранцев: PESEL, регистрация фирмы, ZUS, налоги, декларации,
бухгалтерия, легализация (карта побыту).

**📖 Читать гайд: <https://sobolevbel.github.io/jdg/>**

Вопросы и обсуждение — в Telegram-чате [«ИП в Польше»](https://t.me/JDG_PBH).
Для участников проекта есть [чат контрибьюторов](https://t.me/+WK5ppqgHxXA3MjAy).

## In English

A community-driven guide to registering and running a sole proprietorship (JDG)
in Poland as a foreigner — PESEL, company registration, ZUS, taxes, VAT,
accounting, residence permit. Read it at
**<https://sobolevbel.github.io/jdg/en/>** (or use the language switcher in the
site header).

## Как помочь проекту

Нашли опечатку или устаревшую информацию? **Git не нужен:**

1. Нажмите значок карандаша ✏️ в шапке любой страницы гайда.
2. GitHub откроет веб-редактор — поправьте текст и нажмите **Commit changes**.
   GitHub сам создаст форк и Pull Request.

Для правок побольше (новые страницы, скриншоты, перевод) читайте
[руководство контрибьютора](CONTRIBUTING.md) — там соглашения по оформлению,
стайлгайд скриншотов, правило синхронизации английской версии и инструкции по
локальной сборке.

Не хочется править самому — [создайте issue](https://github.com/sobolevbel/jdg/issues/new/choose).

## Локальная сборка

Сайт собирается генератором [MkDocs](https://www.mkdocs.org/) с темой Material.

Обычный способ (нужен Python 3):

```shell
pip install -r requirements.txt
python -m mkdocs serve
```

Docker-way 🙃:

```shell
docker compose up --build
```

Сайт поднимется на <http://localhost:8000>. Подробности и линтеры — в
[CONTRIBUTING.md](CONTRIBUTING.md).

## Лицензия

[CC0 1.0](LICENSE) — материалы гайда переданы в общественное достояние.

```text
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
