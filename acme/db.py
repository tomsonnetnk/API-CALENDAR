# db.py

import sqlite3

class Database:
    def __init__(self, db_name='calendar.db'):
        """ Инициализация базы данных и создание таблицы событий, если она не существует. """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """ Создание таблицы для событий. """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                title TEXT NOT NULL,
                text TEXT
            )
        ''')
        self.connection.commit()

    def insert_event(self, event):
        """ Вставка нового события в базу данных. """
        self.cursor.execute('''
            INSERT INTO events (date, title, text) VALUES (?, ?, ?)
        ''', (event.date, event.title, event.text))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_all_events(self):
        """ Получение всех событий из базы данных. """
        self.cursor.execute('SELECT * FROM events')
        return self.cursor.fetchall()

    def get_event(self, event_id):
        """ Получение события по ID. """
        self.cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
        return self.cursor.fetchone()

    def update_event(self, event_id, event):
        """ Обновление события по ID. """
        self.cursor.execute('''
            UPDATE events SET date = ?, title = ?, text = ? WHERE id = ?
        ''', (event.date, event.title, event.text, event_id))
        self.connection.commit()

    def delete_event(self, event_id):
        """ Удаление события по ID. """
        self.cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
        self.connection.commit()

    def close(self):
        """ Закрытие соединения с базой данных. """
        self.connection.close()
