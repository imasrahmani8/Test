# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TimeBox
def archive_record(record):
    """Archive a completed or old record by moving it to an archive list."""
    if isinstance(record, dict) and "active" in record:
        record["active"] = False
        return "archived"
    elif isinstance(record, tuple) and len(record) == 2:
        task_id, status = record
        if status == "done":
            return "archived"
    return None

def get_archived_records(boxes):
    """Retrieve all archived records from the boxes."""
    archived = []
    for box in boxes:
        if isinstance(box, dict) and "archive" in box:
            archived.extend(box["archive"])
    return archived

def clear_archive(boxes):
    """Remove old archive entries to free memory."""
    for i, box in enumerate(boxes):
        if isinstance(box, dict) and "archive" in box:
            box["archive"] = []
