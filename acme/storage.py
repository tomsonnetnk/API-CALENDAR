# storage.py

import json

class Storage:
    def __init__(self, filename='events.json'):
        self.filename = filename
        self.load()

    def load(self):
        """Загрузка данных из файла в память."""
        try:
            with open(self.filename, 'r') as file:
                self.events = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.events = []

    def save(self):
        """Сохранение данных из памяти в файл."""
        with open(self.filename, 'w') as file:
            json.dump(self.events, file)

    def create(self, event):
        """Добавление события в память и сохранение."""
        event.id = len(self.events) + 1  # Простой автоинкремент
        self.events.append(event.__dict__)
        self.save()
        return event.id

    def list(self):
        """Получение списка событий."""
        return [model.Event(**event) for event in self.events]

    def read(self, _id):
        """Получение события по ID."""
        for event in self.events:
            if event['id'] == _id:
                return model.Event(**event)
        raise Exception("Event not found")

    def update(self, _id, updated_event):
        """Обновление события."""
        for index, event in enumerate(self.events):
            if event['id'] == _id:
                self.events[index] = updated_event.__dict__
                self.save()
                return
        raise Exception("Event not found")

    def delete(self, _id):
        """Удаление события."""
        self.events = [event for event in self.events if event['id'] != _id]
        self.save()
