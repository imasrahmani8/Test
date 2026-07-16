# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TimeBox
def print_table(headers, rows):
    """Print a formatted table to console."""
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(str(cell)) > widths[i]:
                widths[i] = len(str(cell))

    format_str = "  ".join("{:<" + str(w) + ")" for w in widths)
    print(format_str.format(*headers))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print(format_str.format(*row))
