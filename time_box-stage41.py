# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: TimeBox
def dry_run(self, action, **kwargs):
        """Simulate an operation without modifying state. Returns a dict describing the hypothetical change."""
        result = {"mode": "dry-run", "action": action, "details": {}}
        if action == "create_task":
            self.details["task"] = kwargs.get("task", {})
        elif action == "create_timbox":
            self.details["timbox"] = kwargs.get("timbox", {})
        elif action == "create_break":
            self.details["break"] = kwargs.get("break", {})
        elif action == "update_task":
            self.details["updated_task"] = kwargs.get("task", {})
        elif action == "delete_task":
            self.details["deleted_task_id"] = kwargs.get("task_id")
        elif action == "update_timbox":
            self.details["updated_timbox"] = kwargs.get("timbox", {})
        elif action == "delete_timbox":
            self.details["deleted_timbox_id"] = kwargs.get("timbox_id")
        elif action == "update_break":
            self.details["updated_break"] = kwargs.get("break", {})
        elif action == "delete_break":
            self.details["deleted_break_id"] = kwargs.get("break_id")
        elif action == "add_timbox_to_task":
            self.details["task_id"] = kwargs.get("task_id")
            self.details["timbox_id"] = kwargs.get("timbox_id")
        elif action == "remove_timbox_from_task":
            self.details["task_id"] = kwargs.get("task_id")
            self.details["timbox_id"] = kwargs.get("timbox_id")
        else:
            result["error"] = f"Unknown action: {action}"
        return result
