# Телеграм-бот на вебхуках: FastAPI, Aiogram Dialog, FastStream и RabbitMQ в единой экосистеме
Автор: [Yakovenko Oleksii](https://github.com/Yakvenalex)

Исходный код: [TableHabnter](https://github.com/Yakvenalex/TableHabnter)

## 🚀 Быстрый старт

### 1. Получаем токен Telegram-бота

1. Перейдите к [BotFather](https://t.me/BotFather) в Telegram.
2. Используйте команду `/newbot`, чтобы создать нового бота.
3. Укажите имя бота на кириллице (например, "МойТестБот").
4. Придумайте уникальный логин на латинице, который будет заканчиваться на `bot` (например, `my_test_bot`).
5. Скопируйте токен бота, который выдаст BotFather. Он понадобится для настройки приложения.

---

### 2. Запуск RabbitMQ через Docker

Чтобы поднять RabbitMQ, выполните следующую команду:
```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 \
-e RABBITMQ_DEFAULT_USER=admin \
-e RABBITMQ_DEFAULT_PASS=password \
-e RABBITMQ_DEFAULT_VHOST=my_vhost \
rabbitmq:3-management
```
#### Доступ к веб-интерфейсу RabbitMQ
После успешного запуска контейнера веб-интерфейс RabbitMQ будет доступен по адресу:
http://localhost:15672/

Эта команда создаст контейнер с RabbitMQ, настроит учетные данные администратора и развернет веб-интерфейс для управления очередями сообщений.

---

### 3. Установка зависимостей

Убедитесь, что у вас установлен Python 3.1 или выше. Затем установите зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

---


---

## 🛠 Технологии

- **Aiogram 3** — лучший фреймворк для разработки телеграм-ботов на Python

- **Aiogram dialog 2.3** - фреймворк, который очень сильно упрощает работу с FSM в Aiogram 3

- **SQLAlchemy 2** - фреймворк для работы с табличными базами данных (демонстрацию покажу на примере SQLite, но можно будет легко переключить на любую другую табличную базу данных)

- **FastStream 0.5.3** - python-фреймворк для работы с брокерами сообщений (многие нарекают его «убийцей Celery»)

- **APScheduler 3.1** - фреймворк, который позволит удобно работать с отложенными задачами и задачами по расписанию

- **FastAPI** -  фреймворк, который позволит всех этих ребят: телеграм-бота, APScheduler, FastStream и так далее объединить в рамках одного приложения (одной экосистемы)

- **Alembic** - для миграций базы данных

- **Uvicorn** - для запуска веб-сервера

- **HTTPX** — отправка POST-запросов.

---

## 📄 Лицензия

Этот проект распространяется под лицензией MIT.

---