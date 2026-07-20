# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TimeBox
def parse_date(date_str, fmt=None):
    """Parse a date string with automatic format detection and error handling."""
    if not date_str or not isinstance(date_str, str):
        return None
    
    formats = [fmt] if fmt else ['%Y-%m-%d', '%d.%m.%Y', '%Y/%m/%d']
    
    for f in formats:
        try:
            return datetime.strptime(date_str.strip(), f)
        except ValueError:
            continue
    
    from datetime import date as date_obj
    if len(date_str) == 8 and all(c.isdigit() for c in date_str):
        y, m, d = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:])
        return date(y, m, d)
    
    raise ValueError(f"Не удалось распарсить дату: '{date_str}'. Используйте формат YYYY-MM-DD")
