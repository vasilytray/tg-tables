### Запуск RabbitMQ через Docker
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