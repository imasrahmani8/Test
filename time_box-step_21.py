# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TimeBox
class Reminder:
    def __init__(self, task_id, date):
        self.task_id = task_id
        self.date = date

    @staticmethod
    def from_input():
        print("Введите ID задачи для напоминания:")
        tid = input()
        print(f"Введите дату (YYYY-MM-DD) для напоминания о задаче {tid}:")
        d = input()
        return Reminder(tid, d)

    def show(self):
        print(f"Напоминание: задача {self.task_id} — дата {self.date}")

    @staticmethod
    def list_all(reminders):
        if not reminders:
            print("Нет активных напоминаний.")
            return
        for r in reminders:
            print(r.show())

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add(self, reminder):
        self.reminders.append(reminder)

    @staticmethod
    def from_input():
        mgr = ReminderManager()
        r = Reminder.from_input()
        mgr.add(r)
        return mgr

    def list_all(reminders):
        Reminder.list_all(reminders)
