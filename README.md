# API-CALENDAR
Домашнее задание
Техническое задание: Сервис для работы с Календарем.

Требования:

— API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление
— модель данных "Событие": ID, Дата, Заголовок, Текст
— локальное хранилище данных
— максимальная длина заголовка — 30 символов
— максимальная длина поля Текст — 200 символов
— нельзя добавить больше одного события в день
— API интерфейс: /api/v1/calendar/… (по аналогии с заметкой)
— формат данных: "ГГГГ-ММ-ДД|заголовок|текст" (по аналогии с заметкой)

Написать и протестировать приложение, по аналогии с сервисом заметок из Воркшопа.

КОМАНДЫ ДЛЯ ЗАПУСКА И ТЕСТИРОВАНИЯ

## запуск приложения

```
./venv/bin/flask --app ./acme/server.py run
```


## cURL тестирование

### добавление новой заметки
```
curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "title|text"
```

### получение всего списка заметок
```
curl http://127.0.0.1:5000/api/v1/note/
```

### получение заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/note/1/
```

### обновление текста заметки по идентификатору / ID == 1 /  новый текст == "new text"
```
curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|new text"
```

### удаление заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/note/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/note/1/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/note/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 120

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 60

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/note/
-- пусто --
```
