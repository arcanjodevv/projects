from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {'id': 1, 'title': 'Estudar Python', 'done': False},
    {'id': 2, 'title': 'Fazer exercício físico', 'done': True}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    return jsonify(task)

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Título é obrigatório'}), 400
    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    data = request.json
    task['title'] = data.get('title', task['title'])
    task['done'] = data.get('done', task['done'])
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': 'Tarefa deletada'})

if __name__ == '__main__':
    app.run(debug=True)
