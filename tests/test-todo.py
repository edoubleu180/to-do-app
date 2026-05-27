from todo import TodoManager
from storage import Storage

def test_add_task(tmp_path):
    storage = Storage(tmp_path / "tasks.json")
    manager = TodoManager(storage)

    manager.add_task("Test task")
    assert len(manager.list_tasks()) == 1
