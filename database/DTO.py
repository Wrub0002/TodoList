# DTO.py

class TaskDTO:
    def __init__(self, task_id=None, task_description=None):
        self.task_id = task_id
        self.task_description = task_description

    def __repr__(self):
        return f"TaskDTO(id={self.task_id}, description={self.task_description})"

    def __str__(self):
        return self.task_description
