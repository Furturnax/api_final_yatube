# Проект "API для YaTube"
## Описание

Реализация API для социальной сети **"YaTube"**.

<br>

## Как запустить проект :shipit::

>Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Furturnax/api_final_yatube.git
```

```bash
cd api_final_yatube
```

>Cоздать и активировать виртуальное окружение (Windows/Bash):
```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

>Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

>Выполнить миграции:
```bash
python manage.py migrate
```

>Запустить проект:
```bash
python manage.py runserver
```

<br>

## Примеры запросов

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API **Yatube**. В документации описано, как работает API. Документация представлена в формате **Redoc**.