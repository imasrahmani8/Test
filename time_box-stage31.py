# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TimeBox
import json, os

PROFILE_FILE = "timebox_profiles.json"
def load_profiles():
    if not os.path.exists(PROFILE_FILE):
        return [{"name": "default", "active": True}]
    with open(PROFILE_FILE) as f:
        data = json.load(f)
    for p in data:
        if "active" not in p:
            p["active"] = False
    return data

def save_profiles(profiles):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

def switch_profile(name):
    profiles = load_profiles()
    for p in profiles:
        if p["name"] == name:
            active = not p["active"]
            p["active"] = active
            return active
    print(f"Профиль '{name}' не найден")
    return False

def list_profiles():
    profiles = load_profiles()
    for p in profiles:
        status = "✓ активен" if p["active"] else ""
        print(f"- {p['name']}: {status}")
