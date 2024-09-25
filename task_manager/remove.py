# remove.py

def remove_task(task_list, task):
    """Removes a task from the task list."""
    if task in task_list:
        task_list.remove(task)
        print(f"'{task}' was removed from your list of tasks.")
    else:
        print(f"'{task}' not found in the list of tasks.")
