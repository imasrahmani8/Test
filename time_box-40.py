# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TimeBox
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="TimeBox: Focus Session Planner")
    parser.add_argument("--task", "-t", help="Add a task")
    parser.add_argument("--box", "-b", type=float, help="Start a focus box (minutes)")
    parser.add_argument("--break", "-r", type=float, help="Start a break (minutes)")
    parser.add_argument("--done", "-d", type=str, help="Mark task as done")
    parser.add_argument("--stats", "-s", action="store_true", help="Show session statistics")
    parser.add_argument("--list-tasks", action="store_true", help="List all tasks")
    args = parser.parse_args()

    if args.box:
        print(f"Starting focus session: {args.box:.0f} minutes")
    elif args.break_:
        print(f"Starting break: {args.break_:.0f} minutes")
    elif args.done:
        print(f"Task done: {args.done}")
    elif args.list_tasks:
        print("Listing tasks...")
    elif args.stats:
        print("Session statistics...")
    elif args.task:
        print(f"Task added: {args.task}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
