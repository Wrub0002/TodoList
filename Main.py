# main.py

from input_handling.Validate_input import yes_no_check
from task_manager.add_task import add_task
from task_manager.remove import remove_task

tasks = []

while True:
    task = input("Enter a task: ")
    add_task(tasks, task)

    add_more = yes_no_check("Would you like to add more tasks? (Yes/No): ")

    if add_more == "no":
        print(f"Current tasks: {tasks}")

        delete = yes_no_check("Would you like to delete any task from the list? (Yes/No): ")

        if delete == "yes":
            task_to_remove = input("Enter the task to remove: ")
            remove_task(tasks, task_to_remove)

        print(f"Current tasks: {tasks}")
        break
