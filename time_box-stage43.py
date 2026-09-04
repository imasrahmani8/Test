# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TimeBox
class Pagination:
    def __init__(self, items, per_page=10):
        self.items = items
        self.per_page = per_page
        self.total = len(items)
        self.pages = self._paginate()

    def _paginate(self):
        return [self.items[i:i+self.per_page] for i in range(0, self.total, self.per_page)]

    def get_page(self, page_num):
        return self.pages[page_num - 1]

    def get_page_count(self):
        return (self.total + self.per_page - 1) // self.per_page
