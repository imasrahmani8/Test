# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TimeBox
def get_weekly_stats(tasks, breaks):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1) - timedelta(days=1)
    
    weekly_data = {d: {'tasks': 0, 'breaks': 0} for d in range(week_start, week_end + 1)}
    
    for task in tasks:
        if task['date'] and week_start <= task['date'] <= week_end:
            weekly_data[task['date']]['tasks'] += 1
    
    for break_item in breaks:
        if break_item['date'] and week_start <= break_item['date'] <= week_end:
            weekly_data[break_item['date']]['breaks'] += 1
            
    return list(weekly_data.items())
