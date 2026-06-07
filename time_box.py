# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TimeBox
import time
from datetime import datetime, timedelta

# --- TimeBox: Базовая структура и демо-данные ---

class Task:
    def __init__(self, name, duration_minutes):
        self.name = name
        self.duration = timedelta(minutes=duration_minutes)

class Session:
    def __init__(self, task: Task, break_duration_minutes: int = 5):
        self.task = task
        self.break_duration = timedelta(minutes=break_duration_minutes)
        self.start_time = None
        self.end_time = None
        self.status = "pending"

class TimeBoxApp:
    def __init__(self):
        self.sessions = []
        self.current_session = None
        self.stats = {"completed": 0, "total_focus_minutes": 0}

    def add_demo_tasks(self):
        self.sessions.append(Session(Task("Кодирование", 25), break_duration_minutes=5))
        self.sessions.append(Session(Task("Аналитика", 15), break_duration_minutes=5))
        self.sessions.append(Session(Task("Тесты", 10), break_duration_minutes=5))

    def start_session(self, index: int):
        if 0 <= index < len(self.sessions):
            session = self.sessions[index]
            session.start_time = datetime.now()
            session.status = "running"
            self.current_session = session
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Старт сессии: {session.task.name}")
            return True
        return False

    def end_session(self):
        if self.current_session and self.current_session.status == "running":
            self.current_session.end_time = datetime.now()
            duration = self.current_session.end_time - self.current_session.start_time
            self.stats["completed"] += 1
            self.stats["total_focus_minutes"] += int(duration.total_seconds() / 60)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Сессия завершена: {self.current_session.task.name} ({duration})")
            self.current_session = None
            return True
        return False

    def get_status(self):
        if self.current_session:
            elapsed = datetime.now() - self.current_session.start_time
            remaining = self.current_session.task.duration - elapsed
            return f"Текущая задача: {self.current_session.task.name}\nОсталось: {remaining}"
        return "Нет активной сессии"

# Инициализация приложения и добавление демо-задач
app = TimeBoxApp()
app.add_demo_tasks()

# Демонстрация работы (комментарий для отладки, можно убрать в продакшен)
# app.start_session(0)
# print(app.get_status())
