from flask import Flask, jsonify, request
import os

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    # Aqui você usa a variável PORT para configurar a porta
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

