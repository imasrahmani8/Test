# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TimeBox
def next_action_recommendations(sessions, active_task=None):
    """Recommend the next action based on current session state."""
    if not sessions:
        return {"action": "start_session", "message": "Начните новую фокус-сессию."}

    last = max(sessions, key=lambda s: s["end_time"])
    now = datetime.now()
    
    if now < last["end_time"]:
        remaining = (last["end_time"] - now).total_seconds() / 60
        return {"action": "continue_session", "message": f"Сессия завершится через {remaining:.0f} мин."}

    days_since = (now - last["end_time"]).days
    if days_since < 7:
        return {"action": "review_stats", "message": f"За последнюю неделю вы потратили {sum(s['duration'] for s in sessions)} часов. Продолжайте!"}

    return {"action": "start_session", "message": "Давно не работали? Начните новую фокус-сессию."}
