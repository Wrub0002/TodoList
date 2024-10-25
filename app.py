from flask import Flask, url_for,render_template, request,redirect
from database.DAO import TaskDAO
from database.DBConnection import DBConnection
from database.DTO import TaskDTO
from input_handling.ValidationHandler import ValidationHandler

app = Flask(__name__)

db_conn = DBConnection('tasks.db').get_connection()
task_dao = TaskDAO(db_conn)

# Home route to display all tasks
@app.route('/')
def index():
    tasks = task_dao.get_all_tasks()
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form.get('task_description')
    priority = request.form.get('priority', 'normal')

    # Validate the task description using ValidationHandler
    if ValidationHandler.validate_task_description(task_description):
        task_dto = TaskDTO(task_description=task_description, priority=priority)
        task_dao.add_task(task_dto)
    return redirect(url_for('index'))

# Route to delete a task by its task_id
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
        tasks = task_dao.get_all_tasks()

        if ValidationHandler.validate_task_id(task_id, tasks):
            task_dao.remove_task(task_id)
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)




