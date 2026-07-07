# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TimeBox
class Tag:
    def __init__(self, name):
        self.name = name.lower().strip()

    @property
    def is_valid(self):
        return len(self.name) > 0 and not self.name.startswith('_')

    def to_dict(self):
        return {"name": self.name}

class Task:
    def __init__(self, title, tags=None):
        if tags is None:
            tags = []
        self.title = title
        self.tags = [Tag(t) for t in tags]
        # keep only valid tags
        self.tags = [t for t in self.tags if t.is_valid]

    def add_tag(self, tag_name):
        new = Tag(tag_name)
        if not new.is_valid:
            return False
        if tag_name not in {t.name for t in self.tags}:
            self.tags.append(new)
            return True
        return False

    def remove_tag(self, tag_name):
        initial = len(self.tags)
        self.tags = [t for t in self.tags if t.name.lower() != tag_name.lower()]
        return len(self.tags) < initial

    @property
    def tag_names(self):
        return [t.name for t in self.tags]

class TimedSession:
    def __init__(self, task=None, duration_minutes=0, break_duration_minutes=5, tags=None):
        if task is None:
            task = Task(title="")
        if tags is None:
            tags = []
        self.task = task
        self.duration_minutes = duration_minutes
        self.break_duration_minutes = break_duration_minutes
        self.tags = [Tag(t) for t in tags]
        self.tags = [t for t in self.tags if t.is_valid]

    def add_tag(self, tag_name):
        return self.task.add_tag(tag_name)

    def remove_tag(self, tag_name):
        return self.task.remove_tag(tag_name)

    @property
    def tag_names(self):
        combined = set(self.task.tag_names + [t.name for t in self.tags])
        return sorted(combined)
