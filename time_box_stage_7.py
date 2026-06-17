# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TimeBox
def sort_tasks(tasks, key='date'):
    if not tasks: return []
    reverse = False
    if key == 'priority': reverse = True
    elif key == 'name': reverse = False
    else: key = 'date'
    def get_sort_val(t):
        try: return t['start_date'] or ''
        except: return ''
    if key == 'priority':
        def sort_key(t): return (-t.get('priority', 0), -get_sort_val(t))
    elif key == 'name':
        def sort_key(t): return (t.get('name', ''), get_sort_val(t))
    else:
        def sort_key(t): return (get_sort_val(t), t.get('priority', 0), t.get('name', ''))
    return sorted(tasks, key=sort_key)
