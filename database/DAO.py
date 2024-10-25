from database.DTO import TaskDTO

class TaskDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_table(self):
        with self.db_connection as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    priority TEXT NOT NULL
                )
            ''')

    def add_task(self, task_dto):
        with self.db_connection as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tasks (task, priority) VALUES (?, ?)", (task_dto.task_description, task_dto.priority))
            conn.commit()
            task_dto.task_id = cur.lastrowid

    def get_all_tasks(self):
        with self.db_connection as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tasks")
            rows = cur.fetchall()

            tasks = [TaskDTO(task_id=row[0], task_description=row[1], priority=row[2]) for row in rows]
            return tasks

    def remove_task(self, task_id):
        with self.db_connection as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
