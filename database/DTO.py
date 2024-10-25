
class TaskDTO:
    def __init__(self, task_id=None, task_description=None, priority=None):
        self.task_id = task_id
        self.task_description = task_description
        self.priority = priority

    def __repr__(self):
        return f"TaskDTO(id={self.task_id}, description={self.task_description}), priority={self.priority})"

    def __str__(self):
        return f"{self.task_description} ({self.priority})"
