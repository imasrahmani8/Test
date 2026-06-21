# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TimeBox
import json, sys, os
from datetime import datetime, timedelta
from typing import Dict, List, Optional

def load_initial_data(json_string: str) -> Dict[str, any]:
    """Загружает начальные данные из JSON-строки и валидирует структуру."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_fields = ['tasks', 'timeboxes', 'breaks']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")
            
            if isinstance(data[field], list):
                # Преобразование списков в объекты, если они хранятся как простые структуры
                if field == 'tasks':
                    for task in data['tasks']:
                        if not isinstance(task.get('id'), int) or not isinstance(task.get('title'), str):
                            raise ValueError("Некорректная структура задачи")
                elif field == 'timeboxes':
                    for tb in data['timeboxes']:
                        if not isinstance(tb.get('duration_minutes'), (int, float)):
                            raise ValueError("Длительность тайм-бокса должна быть числом")
                
        # Установка текущей даты и времени для сессии
        now = datetime.now()
        
        return {
            'tasks': data['tasks'],
            'timeboxes': data['timeboxes'],
            'breaks': data['breaks'],
            'current_session_start': now,
            'completed_tasks': [],
            'active_timebox_id': None
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для тестирования с реальным JSON):
# if __name__ == "__main__":
#     sample_json = '[{"id": 1, "title": "Написать код"}, {"duration_minutes": 25}]'
#     initial_data = load_initial_data(sample_json)
#     print(f"Загружено задач: {len(initial_data['tasks'])}")
