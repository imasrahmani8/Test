# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TimeBox
class TimeBoxState:
    def __init__(self):
        self.tasks = []
        self.sessions = []
        self.stats = {"completed_sessions": 0, "total_focus_time": 0}

    def add_task(self, title: str, duration_minutes: int) -> None:
        task_id = len(self.tasks) + 1
        self.tasks.append({
            "id": task_id,
            "title": title,
            "duration_minutes": duration_minutes,
            "status": "pending"
        })

    def start_session(self, task_id: int) -> dict:
        if not self.tasks or self.tasks[-1]["id"] != task_id:
            raise ValueError("Задача не найдена или не является последней")
        session = {
            "task_id": task_id,
            "start_time": time.time(),
            "status": "running",
            "elapsed_seconds": 0
        }
        self.sessions.append(session)
        return session

    def end_session(self, session: dict) -> None:
        if session["status"] != "running":
            raise ValueError("Сессия не активна")
        elapsed = int(time.time() - session["start_time"])
        session["end_time"] = time.time()
        session["elapsed_seconds"] = elapsed
        session["status"] = "completed"
        
        self.stats["completed_sessions"] += 1
        self.stats["total_focus_time"] += elapsed

def get_state():
    if not hasattr(TimeBoxState, '_instance'):
        TimeBoxState._instance = TimeBoxState()
    return TimeBoxState._instance

state = get_state()
