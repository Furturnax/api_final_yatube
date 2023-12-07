# Проект "API для YaTube v. 2.0 Release Version"
Реализация API для социальной сети **"YaTube"**. Публикуйте свои записи с фотографиями, комментируйте чужие, присоединяйтесь к сообществам. 

Основные возможности:
- любой пользователь, даже анонимный, может запросить список всех публикаций, сообществ; 
- авторизованные пользователи могут смотреть подробности публикации, получать информацию о сообществах;
- автор может создавать публикации, а другие пользователи комметрировать их.

Проект является учебным. Основная польза в приобретении понимания реализации `API` через `Django REST Framework`, с использованием:
- [API для YaTube v. 1.0](https://github.com/Furturnax/api_yatube);
- созданной системы `JWT-токенов`;
- `ViewSet`, `mixins` и `GenericViewSet`;
- валидации данных, реализованных в `serializers` и `models`;
- настроек пагинации для публикаций; 
- механизма подписки пользователей друг на друга;
- локализации `API Response` ошибок.

<br>

## Технологический стек:
- [Python 3.11.5](https://docs.python.org/release/3.11.5/)
- [Django 3.2](https://docs.djangoproject.com/en/3.2/)
- [Django REST Framework 3.12.4](https://www.django-rest-framework.org/topics/documenting-your-api/)
- [Pytest 6.2.4](https://docs.pytest.org/en/6.2.x/)
- [SQLite](https://www.sqlite.org/docs.html)
- [JSON Web Token](https://jwt.io/introduction)
- [Djoser](https://djoser.readthedocs.io/en/latest/)

<br>

## Развёртывание проекта :shipit: :
[Руководство по развёртыванию проекта](./SetUp.md)

<br>

## Dreamteam:

[GitHub](https://github.com/yandex-praktikum) | Автор проекта - Yandex Practicum  

[GitHub](https://github.com/Furturnax) | Разработчик - Andrew Fedorchenko 

[GitHub](https://github.com/nik-miniakink) | Наставник - Nikolay Minyakin

[GitHub](https://github.com/EugeneSal) | Ревьюер - Evgeniy Salahutdinov
