![main workflow](https://github.com/zamaev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# api_yamdb
API к платформе для оставления отзывов к произведениям, составления рейтингов и комментирования отзывов

## Настройки перед запуском
Создать файл `.env` по шаблону `.env.example` в директории `infra/` и заполнить данными:
```yaml
DB_ENGINE=django.db.backends.postgresql # работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к БД
POSTGRES_PASSWORD=postgres # пароль для подключения к БД
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

## Запуск проекта
Запуск приложения в контейнерах:
```bash
cd infra
sudo docker-compose up -d
```
Применение миграций:
```bash
sudo docker-compose exec web python manage.py migrate
```
Сбор статических файлов
```bash
sudo docker-compose exec web python manage.py collectstatic
```
Заполнение БД демо-данными:
```bash
sudo docker-compose exec web python manage.py loaddata fixtures.json
```
Авторизация в админке с демо данными
```
http://localhost/admin/
admin:admin
```

## Примеры запросов
### Регистрация 
Отправляет на почту код подтверждения для получения токена.
```
POST /api/v1/auth/signup/
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "user"
}
```

### Получение токена
```
POST /api/v1/auth/token/
Content-Type: application/json

{
  "username": "user",
  "confirmation_code": "blwe40-caa91ba6bc59d8a5bc3bded3b4c56972"
}
```

## Документация
Полный список эндпоинтов можно посмотреть запустив сайт и перейдя по ссылке `/redoc/`

## Авторы
- [Айдрус](https://github.com/zamaev)
