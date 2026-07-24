# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TimeBox
def print_metrics():
    total = {
        "sessions": 0, "completed": 0, "in_progress": 0, "skipped": 0,
        "tasks": 0, "completed_tasks": 0, "breaks": 0,
        "total_minutes_worked": 0, "total_minutes_broken": 0,
    }
    for s in sessions:
        total["sessions"] += 1
        if s.status == "done":
            total["completed"] += 1
            for t in s.tasks:
                if t.done:
                    total["completed_tasks"] += 1
                else:
                    total["tasks"] += 1
        elif s.status == "active":
            total["in_progress"] += 1
            for t in s.tasks:
                if t.done:
                    total["completed_tasks"] += 1
                else:
                    total["tasks"] += 1
        elif s.status == "skipped":
            total["skipped"] += 1
            for t in s.tasks:
                if not t.done:
                    total["tasks"] += 1
        for b in s.breaks:
            total["breaks"] += 1
    for s in sessions:
        if s.status == "done" or s.status == "active":
            total["total_minutes_worked"] += sum(t.duration for t in s.tasks)
            total["total_minutes_broken"] += sum(b.duration for b in s.breaks)
    print(f"Sessions: {total['sessions']}, Completed: {total['completed']}")
    print(f"In Progress: {total['in_progress']}, Skipped: {total['skipped']}")
    print(f"Tasks: {total['tasks']}, Completed Tasks: {total['completed_tasks']}")
    print(f"Breaks: {total['breaks']}")
    print(f"Worked: {total['total_minutes_worked']} min, Breaked: {total['total_minutes_broken']} min")
