# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TimeBox
def calculate_monthly_stats(tasks, breaks):
    from datetime import date, timedelta
    if not tasks: return {}
    today = date.today()
    months = {m: {'focus': 0, 'breaks': 0} for m in range(12)}
    for t in tasks:
        d = date.fromisoformat(t['date'])
        month_idx = (d.month - 1) % 12
        if today.year == d.year or (today.year > d.year and d.month >= today.month):
            months[month_idx]['focus'] += t.get('duration', 0)
    for b in breaks:
        d = date.fromisoformat(b['date'])
        month_idx = (d.month - 1) % 12
        if today.year == d.year or (today.year > d.year and d.month >= today.month):
            months[month_idx]['breaks'] += b.get('duration', 0)
    return {f"Месяц_{m+1}": dict(months[m]) for m in range(12)}
