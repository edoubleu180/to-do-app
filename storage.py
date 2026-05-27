import json
from pathlib import Path

class Storage:
    def __init__(self, filename="tasks.json"):
        self.file = Path(filename)
        if not self.file.exists():
            self.file.write_text("[]")

    def load(self):
        return json.loads(self.file.read_text())

    def save(self, tasks):
        self.file.write_text(json.dumps(tasks, indent=4))
