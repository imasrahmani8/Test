# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TimeBox
def generate_summary(tasks, sessions):
    if not tasks:
        return "Нет данных для сводки."
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t['status'] == 'completed')
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks else 0
    
    active_sessions = [s for s in sessions if not s.get('ended')]
    
    summary_lines = [f"Сводка TimeBox:", f"- Задач всего: {total_tasks}", f"- Выполнено: {completed_tasks} ({completion_rate:.1f}%)", f"- Активные сессии: {len(active_sessions)}"]
    
    if active_sessions:
        total_focus_time = sum(s.get('duration', 0) for s in active_sessions)
        summary_lines.append(f"- Время в фокусе сейчас: {total_focus_time} мин")
        
    return "\n".join(summary_lines)
