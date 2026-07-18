# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TimeBox
def print_task_card(task):
    """Компактный вывод одной задачи с деталями тайм-бокса."""
    status = task.status if hasattr(task, 'status') else getattr(task, '_state', 'new')
    box_info = ''
    if hasattr(task, 'box'):
        box = task.box
        if box:
            box_info = f" | Тайм-бокс: {box.start} → {box.end}"
            if box.breaks:
                breaks_str = ', '.join(b.duration for b in box.breaks)
                box_info += f", Перерывы: [{breaks_str}]"
    print(f"[{status}] {task.title}{box_info}")
