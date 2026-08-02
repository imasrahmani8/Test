# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TimeBox
TEMPLATES = {
    "pomodoro": {"name": "Помодоро", "work_min": 25, "break_min": 5},
    "deep_work": {"name": "Глубокая работа", "work_min": 60, "break_min": 15},
    "quick_task": {"name": "Быстрая задача", "work_min": 15, "break_min": 3},
}

def apply_template(template_name):
    if template_name not in TEMPLATES:
        print(f"Неизвестный шаблон: {template_name}")
        return None
    t = TEMPLATES[template_name]
    work_sec = t["work_min"] * 60
    break_sec = t["break_min"] * 60
    return ("focus", work_sec, break_sec), ("rest", break_sec)

def new_session_from_template(template_name):
    result = apply_template(template_name)
    if not result:
        return None
    focus_type, break_type = result[0], result[1]
    session = {"type": "focus", "end_time": 0}
    task = {"type": "rest"}
    for rec in (session, task):
        rec["time_left"] = 0
        if rec["type"] == focus_type:
            rec.update({"work_min": TEMPLATES[template_name]["work_min"], "break_min": TEMPLATES[template_name]["break_min"]})
    return session, task

def show_templates():
    print("Доступные шаблоны:")
    for name, info in TEMPLATES.items():
        print(f"  {name}: работа {info['work_min']} мин, перерыв {info['break_min']} мин")
