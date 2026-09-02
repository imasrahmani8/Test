# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TimeBox
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "underline": "\033[4m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
}

_color_enabled = True

def color(text, color):
    if not _color_enabled:
        return text
    return ANSI.get(color, "") + str(text) + ANSI["reset"]

def colored(text, color):
    return color(text, color)

def success(text):
    return colored(text, "green")

def error(text):
    return colored(text, "red")

def warn(text):
    return colored(text, "yellow")

def info(text):
    return colored(text, "blue")

def title(text):
    return colored(text, "cyan") + ANSI["bold"]

def status_done():
    return ANSI["green"] + "✓" + ANSI["reset"]

def status_pending():
    return ANSI["yellow"] + "○" + ANSI["reset"]

def status_active():
    return ANSI["red"] + "●" + ANSI["reset"]

def status_break():
    return ANSI["bright_blue"] + "☕" + ANSI["reset"]

def clear_line():
    return "\033[2K\r"
