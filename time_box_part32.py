# === Stage 32: Добавь журнал действий пользователя ===
# Project: TimeBox
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action_type, task_name=None, duration_minutes=0, details=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": action_type,
            "task_name": task_name,
            "duration_minutes": duration_minutes,
            "details": details,
        }
        self.entries.append(entry)

    def get_summary(self):
        return {
            "total_sessions": sum(1 for e in self.entries if e["action_type"] == "session_complete"),
            "total_focus_time": sum(e["duration_minutes"] for e in self.entries if e["action_type"] == "session_complete"),
            "total_breaks": sum(1 for e in self.entries if e["action_type"] == "break_taken"),
        }

    def get_recent(self, count=5):
        return self.entries[-count:]
