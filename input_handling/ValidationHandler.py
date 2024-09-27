

def validate_task_id(task_id, tasks):
    task_exists = any(task.task_id == task_id for task in tasks)
    if task_exists:
        return True
    else:
        print(f"Task with ID {task_id} not found. Please enter a valid ID.")
        return False
