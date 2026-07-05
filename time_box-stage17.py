# === Stage 17: Добавь группировку записей по категориям ===
# Project: TimeBox
from collections import defaultdict, Counter
def group_by_category(tasks):
    groups = defaultdict(list)
    for task in tasks:
        cat = task.get('category', 'General')
        groups[cat].append(task)
    return dict(sorted(groups.items()))
