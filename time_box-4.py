# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: TimeBox
def edit_task(task_id: int, **updates) -> dict | None:
    if not updates:
        return None
    for task in tasks:
        if task['id'] == task_id:
            task.update(updates)
            return task.copy()
    raise ValueError(f"Task {task_id} not found")
