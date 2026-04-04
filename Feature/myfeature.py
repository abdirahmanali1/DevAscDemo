from dataclasses import dataclass, field
from typing import List

"""
Basic Python feature: a tiny in-memory task manager.
"""



@dataclass
class TaskManager:
    tasks: List[str] = field(default_factory=list)

    def add_task(self, task: str) -> None:
        task = task.strip()
        if not task:
            raise ValueError("Task cannot be empty.")
        self.tasks.append(task)

    def list_tasks(self) -> List[str]:
        return self.tasks.copy()

    def remove_task(self, index: int) -> str:
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        return self.tasks.pop(index)


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Set up project")
    manager.add_task("Implement feature")
    manager.add_task("Write tests")

    print("Tasks:")
    for i, task in enumerate(manager.list_tasks(), start=1):
        print(f"{i}. {task}")