# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: TimeBox
APP_CONFIG = {
    "app_name": "TimeBox",
    "version": "0.29",
    "max_focus_minutes": 50,
    "default_break_minutes": 10,
    "break_interval": 4,
    "timezone": "UTC",
    "stats_enabled": True,
}

def load_config():
    return APP_CONFIG.copy()
