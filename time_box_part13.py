# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TimeBox
def search_tasks(query: str) -> list[dict]:
    if not query.strip():
        return []
    lower_q = query.lower()
    results = [t for t in tasks.values()]
    filtered = [
        t for t in results
        if (lower_q in t.get('title', '').lower() or
            lower_q in t.get('description', '').lower() or
            lower_q in str(t.get('category', '')).lower())
    ]
    return filtered
