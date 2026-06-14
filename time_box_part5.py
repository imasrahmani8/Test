# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TimeBox
def delete_task(task_id: int) -> bool:
    tasks = load_tasks()
    if task_id not in tasks:
        print(f"Задача с ID {task_id} не найдена.")
        return False
    del tasks[task_id]
    save_tasks(tasks)
    print(f"Задача с ID {task_id} успешно удалена.")
    return True

def delete_session(session_id: int) -> bool:
    sessions = load_sessions()
    if session_id not in sessions:
        print(f"Сессия с ID {session_id} не найдена.")
        return False
    del sessions[session_id]
    save_sessions(sessions)
    print(f"Сессия с ID {session_id} успешно удалена.")
    return True

def delete_stat(stat_key: str) -> bool:
    stats = load_stats()
    if stat_key not in stats:
        print(f"Статистика по ключу '{stat_key}' не найдена.")
        return False
    del stats[stat_key]
    save_stats(stats)
    print(f"Статистика по ключу '{stat_key}' успешно удалена.")
    return True
