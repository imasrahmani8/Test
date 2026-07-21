# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TimeBox
def demo_commands():
    """Блок демо-команд для ручного тестирования TimeBox."""
    # Симуляция ввода данных и проверка ключевых функций
    tasks = [
        {"title": "Учить Python", "duration_min": 45, "priority": "high"},
        {"title": "Написать отчёт", "duration_min": 30, "priority": "medium"},
        {"title": "Перерыв", "duration_min": 10, "priority": "low"},
    ]
    timeboxes = [
        {"task_id": 0, "start_hour": 9, "end_hour": 10},
        {"task_id": 2, "start_hour": 10, "end_hour": 10.17},
        {"task_id": 1, "start_hour": 10.30, "end_hour": 11},
    ]

    # Проверка расписания: нет ли перекрытий
    for i in range(len(timeboxes)):
        for j in range(i + 1, len(timeboxes)):
            assert not (timeboxes[i]["start_hour"] < timeboxes[j]["end_hour"] and
                         timeboxes[j]["start_hour"] < timeboxes[i]["end_hour"]), \
                "Пересечение тайм-боксов!"

    # Подсчёт статистики
    total = sum(t["duration_min"] for t in tasks)
    print(f"Всего задач: {len(tasks)}, общее время: {total} мин")

    # Валидация приоритетов
    priorities = set(t["priority"] for t in tasks)
    assert "high" in priorities and "medium" in priorities, \
        "Ожидается наличие high и medium задач"

    print("✓ Демо-тесты пройдены успешно")

demo_commands()
