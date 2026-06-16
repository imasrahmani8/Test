# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TimeBox
def filter_tasks(status=None, category=None, tags=None):
    filtered = []
    for task in tasks:
        if status and task.get('status') != status:
            continue
        if category and task.get('category') != category:
            continue
        if tags is not None:
            task_tags = set(task.get('tags', []))
            if not any(tag in task_tags for tag in tags):
                continue
        filtered.append(task)
    return filtered
