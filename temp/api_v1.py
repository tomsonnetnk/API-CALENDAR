#Этот код создает простой CRUD API для работы с календарем, реализуя указанные требования.

from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Локальное хранилище для событий
events = {}

def validate_event(event):
    if len(event['title']) > 30 or len(event['text']) > 200:
        return False
    if event['date'] in events:
        return False
    return True

@app.route('/api/v1/calendar/', methods=['POST'])
def create_event():
    event = request.json
    if validate_event(event):
        events[event['date']] = event
        return jsonify(event), 201
    return jsonify({"error": "Invalid event"}), 400

@app.route('/api/v1/calendar/', methods=['GET'])
def get_events():
    return jsonify(list(events.values())), 200

@app.route('/api/v1/calendar/<date>', methods=['GET'])
def read_event(date):
    event = events.get(date)
    if event:
        return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404

@app.route('/api/v1/calendar/<date>', methods=['PUT'])
def update_event(date):
    event = request.json
    if date in events:
        events[date].update(event)
        return jsonify(events[date]), 200
    return jsonify({"error": "Event not found"}), 404

@app.route('/api/v1/calendar/<date>', methods=['DELETE'])
def delete_event(date):
    if date in events:
        del events[date]
        return jsonify({"message": "Event deleted"}), 204
    return jsonify({"error": "Event not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

