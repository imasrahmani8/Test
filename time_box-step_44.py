# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TimeBox
import shutil
import os
from datetime import datetime

def backup_data_file(data_file_path):
    """Создаёт резервную копию файла данных с автоматическим управлением версионными папками."""
    if not os.path.exists(data_file_path):
        print(f"[TimeBox] Файл данных не найден: {data_file_path}")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(os.path.dirname(data_file_path), f"backups_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, os.path.basename(data_file_path))
    shutil.copy2(data_file_path, backup_path)
    print(f"[TimeBox] Резервная копия создана: {backup_path}")
    return backup_path
