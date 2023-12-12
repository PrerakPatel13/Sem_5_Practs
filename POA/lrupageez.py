from collections import OrderedDict

class LRUPageReplacement:
    capacity, page_order = 3, OrderedDict()

    def check_page_fault(self, page):
        if page in self.page_order:
            self.page_order.move_to_end(page)
            return False
        elif len(self.page_order) == self.capacity:
            self.page_order.popitem(last=False)
        self.page_order[page] = None
        return True

lru_algorithm = LRUPageReplacement()

page_requests = [1, 2, 3, 4, 1, 2, 5, 1, 2]

for page in page_requests:
    if lru_algorithm.check_page_fault(page):
        print(f"Page {page} caused a page fault. Page order: {list(lru_algorithm.page_order.keys())}")
    else:
        print(f"Page {page} is already in the memory HIT . Page order: {list(lru_algorithm.page_order.keys())}")