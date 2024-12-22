from flask import Flask, request

app = Flask(__name__)

import model  # Импорт модели данных
import logic  # Импорт логики работы с событиями

_event_logic = logic.EventLogic()  # Инициализация логики событий

class ApiException(Exception):
    pass

def _from_raw(raw_event: str) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) == 3:
        event = model.Event()
        event.id = None  # ID будет создан автоматически
        event.date = parts[0]
        event.title = parts[1]
        event.text = parts[2]
        return event
    else:
        raise ApiException(f"invalid RAW event data {raw_event}")

def _to_raw(event: model.Event) -> str:
    return f"{event.id}|{event.date}|{event.title}|{event.text}"

API_ROOT = "/api/v1"
CALENDAR_API_ROOT = API_ROOT + "/calendar"

@app.route(CALENDAR_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _id = _event_logic.create(event)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404

@app.route(CALENDAR_API_ROOT + "/", methods=["GET"])
def list():
    try:
        events = _event_logic.list()
        raw_events = "\\n".join([_to_raw(event) for event in events])
        return raw_events, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404

@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        event = _event_logic.read(_id)
        return _to_raw(event), 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404

@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _event_logic.update(_id, event)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404

@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _event_logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404

if __name__ == "__main__":
    app.run(debug=True)
