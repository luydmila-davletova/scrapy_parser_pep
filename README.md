# Асинхронный парсер документов PEP на Scrapy.

## Технологии проекта

- Python 3.8
- Scrapy

## Описание проекта:

Парсер, собирающий информацию с сайта https://www.python.org/
- версии языка и авторов версий;
- статусы всех стандартов PEP.

Вся собранная информация сохраняется в файлы с расширением **csv**:
- Информация о стандарте: номер, статус, автор-(ы);
- Колличество каждого статуса на сайте + общая сумма.

## Инструкция по развёртыванию:
1. Клонируйте проект на локальную машину:
```bash
git clone https://github.com/luydmila-davletova/scrapy_parser_pep
```
2. Установите и активируйте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Запускаем парсер pep.
```
scrapy crawl pep
```

### Автор проекта:
[Людмила Давлетова](https://github.com/luydmila-davletova)