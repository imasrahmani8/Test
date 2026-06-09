# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TimeBox
class Task:
    def __init__(self, name: str, duration_minutes: int):
        self.name = name
        self.duration_minutes = duration_minutes

    @property
    def is_valid(self) -> bool:
        return len(self.name.strip()) > 0 and self.duration_minutes > 0

class TimeBoxSession:
    def __init__(self, task: Task, focus_minutes: int, break_minutes: int):
        self.task = task
        self.focus_minutes = focus_minutes
        self.break_minutes = break_minutes
        self.is_valid = self._validate()

    @property
    def is_valid(self) -> bool:
        return (self.task.is_valid and 
                self.focus_minutes > 0 and 
                self.break_minutes >= 0)

    def _validate(self) -> bool:
        if not self.task.is_valid:
            return False
        if self.focus_minutes <= 0:
            return False
        if self.break_minutes < 0:
            return False
        return True

def parse_input(prompt: str) -> Task | None:
    user_input = input(prompt).strip()
    if not user_input:
        return None
    
    try:
        name, duration_str = user_input.split(maxsplit=1)
        duration_minutes = int(duration_str.strip())
        task = Task(name=name, duration_minutes=duration_minutes)
        return task if task.is_valid else None
    except ValueError:
        print("Ошибка: формат ввода неверен. Используйте 'Название задачи длительность(мин)'")
        return None
