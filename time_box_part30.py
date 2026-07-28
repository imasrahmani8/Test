# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TimeBox
# Этап 30: Многопрофильная поддержка (20–60 строк)

class Profile:
    def __init__(self, name, default_focus_min=25, default_break_min=5):
        self.name = name
        self.default_focus_min = default_focus_min
        self.default_break_min = default_break_min
        self.stats = {"sessions": 0, "total_focus_min": 0}

    def log_session(self, focus_minutes):
        self.stats["sessions"] += 1
        self.stats["total_focus_min"] += focus_minutes


class MultiProfileManager:
    _profiles = {}

    @classmethod
    def add_profile(cls, name, **kwargs):
        p = Profile(name, default_focus_min=kwargs.get("default_focus_min", 25),
                    default_break_min=kwargs.get("default_break_min", 5))
        cls._profiles[name] = p
        return p

    @classmethod
    def get_profile(cls, name):
        return cls._profiles.get(name)

    @classmethod
    def list_profiles(cls):
        return dict(sorted(cls._profiles.items()))
