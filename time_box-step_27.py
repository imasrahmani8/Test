# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TimeBox
import random

def _reset_demo_data():
    """Возвращает исходные демо-данные для тестирования."""
    tasks = [
        {"id": 1, "title": "Написать отчёт", "duration_min": 45},
        {"id": 2, "title": "Прочитать статью", "duration_min": 20},
        {"id": 3, "title": "Сделать зарисовки", "duration_min": 15},
    ]
    timeboxes = [
        {"id": 1, "name": "Утренний блок", "duration_min": 90, "breaks": 2},
        {"id": 2, "name": "Вечерний блок", "duration_min": 60, "breaks": 1},
    ]
    returns = {
        "tasks": tasks,
        "timeboxes": timeboxes,
        "session_count": 0,
        "completed_tasks": [],
        "stats": {"total_worked": 0, "total_broke": 0, "sessions_run": 0},
    }
    return returns

def reset_demo_data():
    """Сбрасывает все демо-данные в начало."""
    state = _reset_demo_data()
    global tasks, timeboxes, session_count, completed_tasks, stats
    tasks = state["tasks"]
    timeboxes = state["timeboxes"]
    session_count = 0
    completed_tasks = []
    stats = {
        "total_worked": 0,
        "total_broke": 0,
        "sessions_run": 0,
    }

def clear_state():
    """Полностью очищает все данные и статистику."""
    global tasks, timeboxes, session_count, completed_tasks, stats
    tasks = []
    timeboxes = []
    session_count = 0
    completed_tasks = []
    stats = {"total_worked": 0, "total_broke": 0, "sessions_run": 0}

def load_demo_data():
    """Загружает демо-данные и показывает их."""
    state = _reset_demo_data()
    print("=== Демо-задачи ===")
    for t in state["tasks"]:
        print(f"  {t['id']}: {t['title']} ({t['duration_min']} мин)")
    print("=== Тайм-боксы ===")
    for tb in state["timeboxes"]:
        print(f"  {tb['id']}: {tb['name']} — {tb['duration_min']} мин, перерывов: {tb['breaks']}")
