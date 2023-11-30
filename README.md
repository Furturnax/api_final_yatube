# Проект "API для YaTube"

Реализация API для социальной сети **"YaTube"**. Публикуйте свои записи с фотографиями, комментируйте чужие, присоединяйтесь к сообществам. 

Основные возможности:
- любой пользователь, даже анонимный, может запросить список всех публикаций, сообществ; 
- авторизованные пользователи могут смотреть подробности публикации, получать информацию о сообществах;
- для автора реализован `CRUD` для публикаций;
- для автора реализован `CRUD` для комментариев;
- авторизованные пользователи могут подписываться на других пользователей;
- реализована система `JWT-токенов`.

Проект является учебным. Основная польза в приобретении понимания реализации полного цикла `CRUD` через `ViewSet` и отдельных его компонентов через `mixins` и `GenericViewSet`, валидацию данных реализованных в `serializers`, определения роутера к разным `endpoints` и многое другое.

<br>

## Технологический стек:

- Python 3.11.5
- Django 3.2.16
- Django REST Framework 3.12.4
- SQLite3
- Аутентификация по токену JWT + Djoser

<br>

## Как запустить проект :shipit: :

>Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Furturnax/api_final_yatube.git
```

```bash
cd api_final_yatube/
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


>Перейти в директорию с manage.py:
```bash
cd yatube_api/
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

## Порядок запросов к API:

>Для работы понадобится программа **Postman**. Она существует в `desktop` и `web` версии. 


Запустить проект. По адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API **Yatube**. В документации описано, как работает API. Документация представлена в формате **Redoc**.


Зарегистрировать пользователя через **Postman**. По адресу http://127.0.0.1:8000/api/v1/users/ в формате `JSON` передать данные:
```
{
	"username": "username",
	"password": "password"
}
```


Получить JWT-токен через **Postman**. По адресу http://127.0.0.1:8000/api/v1/jwt/create/ получить `"access"-токен` в формате:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQyOTM4LCJpYXQiOjE3MDEzNTY1MzgsImp0aSI6ImZiN2Y5ZTYwYTNiMzQxMzU5NGJlYjc2YTBkNWE0YzlmIiwidXNlcl9pZCI6M30._h5--Xdayja6eMHENZnbRA50XMR7H8b-UQYTqYyaSdc
```


Авторизировать токен во вкладке **Authorization**:
1. В разделе **Type** выбрать `Bearer token`;
2. В разделе **Token** вставить полученный `"access"-токен`;
3. Выполнять запросы к `API`, описанных в документации. 