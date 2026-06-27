# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: TimeBox
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            tasks = [Task(**item) for item in data]
        elif isinstance(data, dict):
            tasks = [Task(**data)]
        else:
            raise ValueError("Неверный формат данных JSON")
        return tasks
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {filepath}: {type(e).__name__}")
        return []
