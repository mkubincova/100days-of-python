from flask import Flask, render_template, redirect, jsonify, url_for, request, flash
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
import uuid
import json

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
Bootstrap5(app)

JSON_FILE_PATH = 'data.json'


def read_todos_from_file():
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def write_todos_to_file(todo_data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(todo_data, file, indent=2)


todo_list = read_todos_from_file()


@app.route("/")
def home():
    reversed_todo_list = todo_list[::-1]
    return render_template("index.html", todos=reversed_todo_list)


@app.route("/add", methods=["POST"])
def add_todo():
    global todo_list
    text = request.form['task']

    if text:
        new_todo = {'id': str(uuid.uuid4()), 'task': text, 'completed': False}
        todo_list.append(new_todo)
        write_todos_to_file(todo_list)

    flash('TODO added successfully!', 'success')
    return redirect(url_for('home'))


@app.route('/update_todo/<todo_id>', methods=['POST'])
def update_todo(todo_id):
    global todo_list
    todo = next((item for item in todo_list if item['id'] == todo_id), None)
    if todo:
        todo['completed'] = not todo['completed']
        write_todos_to_file(todo_list)
        return jsonify({'message': 'Todo item updated successfully'})
    else:
        return jsonify({'error': 'Todo item not found'}), 404


@app.route('/delete_todo/<todo_id>', methods=['POST'])
def delete_todo(todo_id):
    global todo_list
    todo_list = [todo for todo in todo_list if todo['id'] != todo_id]
    write_todos_to_file(todo_list)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4999)
