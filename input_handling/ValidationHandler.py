
class ValidationHandler:

    @staticmethod
    def validate_task_id(task_id, tasks):
        task_exists = any(task.task_id == task_id for task in tasks)
        if task_exists:
            return True
        else:
            print(f"Task with ID {task_id} not found. Please enter a valid ID.")
            return False
    @staticmethod
    def validate_task_description(task_description):
        if not task_description.strip():
            print("Task description cannot be empty.")
            return False
        return True

    @staticmethod
    def get_valid_task_id(tasks):
        while True:
            try:
                task_id = int(input("enter the task ID to remove: "))
                if ValidationHandler.validate_task_id(task_id, tasks):
                    return task_id
            except ValueError:
                print("invalid input, please enter a valid number. ")