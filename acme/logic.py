# logic.py

import model  # Импортируем модель данных

class EventLogic:
    def __init__(self):
        self.events = []  # Список для хранения событий
        self.current_id = 1  # Идентификатор для нового события

    def create(self, event: model.Event) -> int:
        event.id = self.current_id  # Устанавливаем ID события
        self.events.append(event)  # Добавляем событие в список
        self.current_id += 1  # Увеличиваем ID для следующего события
        return event.id  # Возвращаем ID созданного события

    def list(self) -> list:
        return self.events  # Возвращаем список всех событий

    def read(self, event_id: str) -> model.Event:
        for event in self.events:
            if event.id == int(event_id):
                return event  # Возвращаем событие по ID
        raise ValueError(f"Event with id {event_id} not found!")  # Ошибка, если событие не найдено

    def update(self, event_id: str, updated_event: model.Event):
        for index, event in enumerate(self.events):
            if event.id == int(event_id):
                self.events[index] = updated_event  # Обновляем событие
                return
        raise ValueError(f"Event with id {event_id} not found!")  # Ошибка, если событие не найдено

    def delete(self, event_id: str):
        for index, event in enumerate(self.events):
            if event.id == int(event_id):
                del self.events[index]  # Удаляем событие по ID
                return
        raise ValueError(f"Event with id {event_id} not found!")  # Ошибка, если событие не найдено
