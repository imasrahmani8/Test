# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TimeBox
def export_state():
    import json
    from datetime import datetime
    state = {
        "tasks": tasks,
        "timers": timers,
        "breaks": breaks,
        "stats": stats,
        "exported_at": datetime.now().isoformat()
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
