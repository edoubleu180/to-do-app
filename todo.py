class TodoManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, description):
        task = {"id": len(self.tasks) + 1, "description": description, "done": False}
        self.tasks.append(task)
        self.storage.save(self.tasks)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.storage.save(self.tasks)
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.storage.save(self.tasks)
