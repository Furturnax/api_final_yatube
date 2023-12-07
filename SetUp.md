## Развёртывание проекта:
+ Клонировать репозиторий и перейти в него в командной строке:
```shell script
git clone git@github.com:Furturnax/api_final_yatube.git
```

```shell script
cd api_final_yatube/
```

+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```shell script
python -m venv venv
```

```shell script
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```shell script
python -m pip install --upgrade pip
```

```shell script
pip install -r requirements.txt
```

+ Перейти в директорию с manage.py:
```shell script
cd yatube_api/
```

+ Выполнить миграции:
```shell script
python manage.py migrate
```

+ Запустить проект:
```shell script
python manage.py runserver
```

<br>

## Схема базы данных:
<img src="./assets/db_schema.png" alt="Schema of db">

<br>

## Порядок запросов к API:
Для работы понадобится программа **Postman**. Она существует в `desktop` и `web` версии. Она удобна функционалом. Либо использовать стандартный интерфейс `DRF` без установки дополнительного ПО. 

Запустить проект. По адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API **Yatube**. В документации описано, как работает API. Документация представлена в формате **Redoc**.

Зарегистрировать пользователя через Admin-панель.
+ Перейти в директорию с manage.py:
```shell script
cd yatube_api/
```

+ Создать пользователя-администратора:
```shell script
python manage.py createsuperuser
```

Получить JWT-токен через **Postman**.  
+ По адресу http://127.0.0.1:8000/api/v1/jwt/create/, через POST запрос передать данные в формате `JSON`:
```
{
	"username": "username",
	"password": "password"
}
```
+ и получить `"access"-токен`:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQyOTM4LCJpYXQiOjE3MDEzNTY1MzgsImp0aSI6ImZiN2Y5ZTYwYTNiMzQxMzU5NGJlYjc2YTBkNWE0YzlmIiwidXNlcl9pZCI6M30._h5--Xdayja6eMHENZnbRA50XMR7H8b-UQYTqYyaSdc
```

Авторизировать токен во вкладке **Authorization**.
- В разделе **Type** выбрать `Bearer token`;
- В разделе **Token** вставить полученный `"access"-токен`;
- Выполнять запросы к `API`, описанных в документации. 

Начать делать запросы согласно документации.
