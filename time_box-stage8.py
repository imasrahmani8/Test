# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TimeBox
def show_menu():
    print("\n=== TimeBox Меню ===")
    print("1. Добавить задачу")
    print("2. Запустить фокус-сессию")
    print("3. Показать статистику")
    print("4. Выход")
    choice = input("Выберите действие: ")
    if choice == "1":
        task_name = input("Название задачи: ")
        duration = int(input("Длительность (мин): "))
        tasks.append({"name": task_name, "duration": duration})
        print(f"Задача '{task_name}' добавлена.")
    elif choice == "2":
        if not tasks:
            print("Нет задач для выполнения.")
            return
        idx = int(input("Выберите задачу (индекс): ")) - 1
        task = tasks[idx]
        print(f"Запуск сессии по задаче '{task['name']}' на {task['duration']} минут...")
        import time
        end_time = time.time() + task["duration"] * 60
        while time.time() < end_time:
            remaining = int((end_time - time.time()) / 60)
            print(f"\rОсталось: {remaining} мин", end="", flush=True)
            time.sleep(1)
        print("\nСессия завершена!")
    elif choice == "3":
        if not tasks:
            print("Нет данных для статистики.")
            return
        total = sum(t["duration"] for t in tasks)
        completed = len([t for t in tasks if t.get("completed", False)])
        print(f"Всего задач: {len(tasks)}, Завершено: {completed}, Всего минут: {total}")
    elif choice == "4":
        print("Выход из программы.")
        exit()
    else:
        print("Некорректный выбор.")

if __name__ == "__main__":
    tasks = []
    while True:
        show_menu()
