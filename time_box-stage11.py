# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TimeBox
import json, os

DATA_FILE = "timebox_data.json"

def save_state(tasks: list, sessions: list) -> None:
    data = {"tasks": tasks, "sessions": sessions}
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Ошибка сохранения данных: {e}")

def load_state() -> dict:
    if not os.path.exists(DATA_FILE):
        return {"tasks": [], "sessions": []}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Ошибка загрузки данных: {e}")
        return {"tasks": [], "sessions": []}
