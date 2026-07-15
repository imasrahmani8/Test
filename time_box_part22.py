# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TimeBox
def check_overdue_reminders(tasks):
    overdue = [t for t in tasks if t["timebox"] is not None and datetime.now() > t["timebox"]]
    return overdue
