from collections import OrderedDict

class LRUPageReplacement:
    capacity, page_queue = 3, OrderedDict()

    def page_fault(self, page):
        if page in self.page_queue:
            self.page_queue.move_to_end(page)
            return False
        elif len(self.page_queue) == self.capacity:
            self.page_queue.popitem(last=False)
        self.page_queue[page] = None
        return True

lru_algorithm = LRUPageReplacement()

page_requests = [1, 2, 3, 4, 1, 2, 5, 1, 2]

for page in page_requests:
    if lru_algorithm.page_fault(page):
        print(f"Page {page} caused a page fault. Page order: {list(lru_algorithm.page_queue.keys())}")
    else:
        print(f"Page {page} is already in the memory HIT . Page order: {list(lru_algorithm.page_queue.keys())}")