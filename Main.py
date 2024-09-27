# main.py

from input_handling.Validate_input import yes_no_check
from database.DAO import TaskDAO
from database.DTO import TaskDTO
from database.DBConnection import DBConnection



def main():
    # Create database connection
    db_conn = DBConnection('tasks.db').get_connection()

    # Create DAO
    task_dao = TaskDAO(db_conn)
    task_dao.create_table()  # Ensure the table exists

    print("Hello, welcome to your to-do list")
    while True:
        # Show menu
        answer = input("What would you like to do?\n"
                       "[1] See current tasks\n"
                       "[2] Add a task\n"
                       "[3] Remove a task\n"
                       "[4] Exit\n"
                       "Enter your choice: ")

        if answer == "1":
            tasks = task_dao.get_all_tasks()
            if tasks:
                print("Current tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.task_description} (ID: {task.task_id})")
            else:
                print("Your task list is empty.")

        elif answer == "2":
            # Add a task
            task_description = input("Enter the task: ")
            task_dto = TaskDTO(task_description=task_description)
            task_dao.add_task(task_dto)
            print(f"Task '{task_dto.task_description}' added with ID {task_dto.task_id}.")

            # Ask if user wants to add more tasks
            add_more = yes_no_check("Would you like to add more tasks? (Yes/No): ")
            if add_more.lower() == "no":
                print(f"Current tasks: {task_dao.get_all_tasks()}")

        elif answer == "3":
            # Remove a task
            task_id = int(input("Enter the task ID to remove: "))
            task_dao.remove_task(task_id)
            print(f"Task {task_id} has been removed.")


        elif answer == "4":
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

    # Close the database connection when done
    DBConnection('tasks.db').close_connection()


if __name__ == "__main__":
    main()