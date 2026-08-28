# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: TimeBox
import unittest
from datetime import datetime, timedelta

# Пример блок-теста для пограничных случаев тайм-бокса
class TestTimeBoxEdgeCases(unittest.TestCase):
    def test_empty_task_list(self):
        self.assertEqual(len(tasks), 0)

    def test_add_duplicate_task(self):
        add_task("Тест", 30)
        add_task("Тест", 30)
        self.assertEqual(len(tasks), 2)

    def test_invalid_duration(self):
        with self.assertRaises(ValueError):
            add_task("Тест", 0)

    def test_invalid_time_format(self):
        with self.assertRaises(ValueError):
            parse_time("abc")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            parse_time("")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            parse_date("2023-13-01")

    def test_invalid_date_month(self):
        with self.assertRaises(ValueError):
            parse_date("2023-00-01")

    def test_invalid_date_day(self):
        with self.assertRaises(ValueError):
            parse_date("2023-13-01")

if __name__ == "__main__":
    unittest.main()
