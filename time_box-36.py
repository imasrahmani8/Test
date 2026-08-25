# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TimeBox
def validate_and_repair(box):
    """Проверка целостности данных тайм-бокса и простой ремонт."""
    errors = []
    if not box.get("task"):
        errors.append("task is required")
        box["task"] = "Unknown"
    if not box.get("duration"):
        errors.append("duration is required")
        box["duration"] = 25
    if not isinstance(box.get("duration"), (int, float)):
        errors.append("duration must be a number")
        box["duration"] = 25
    if not box.get("break_duration"):
        errors.append("break_duration is required")
        box["break_duration"] = 5
    if not isinstance(box.get("break_duration"), (int, float)):
        errors.append("break_duration must be a number")
        box["break_duration"] = 5
    if box.get("status") not in ["planned", "active", "completed", "paused"]:
        errors.append("invalid status")
        box["status"] = "planned"
    if box.get("start_time") and not isinstance(box["start_time"], (int, float)):
        errors.append("start_time must be a number")
        box["start_time"] = 0
    if box.get("end_time") and not isinstance(box["end_time"], (int, float)):
        errors.append("end_time must be a number")
        box["end_time"] = 0
    if box["status"] == "active" and box["end_time"] <= box["start_time"]:
        box["end_time"] = box["start_time"] + box["duration"]
    if box["status"] == "completed" and box["end_time"] <= box["start_time"]:
        box["end_time"] = box["start_time"] + box["duration"]
    if box["status"] == "paused" and box["end_time"] <= box["start_time"]:
        box["end_time"] = box["start_time"] + box["duration"]
    if errors:
        box["repair_log"] = errors
    return box
