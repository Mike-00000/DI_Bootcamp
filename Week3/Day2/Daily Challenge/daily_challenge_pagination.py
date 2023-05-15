class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.content = items or []
        self.items_per_page = pageSize
        self.total_items = len(self.content)
        self.total_pages = (self.total_items + pageSize - 1) // pageSize
        self.current_page = 1

    def get_current_page(self):
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        return self.content[start_index:end_index]

    def get_visible_items(self):
        return self.get_current_page()

    def go_to_page(self, page):
        if page < 1 or page > self.total_pages:
            print("Invalid page number. Please enter a valid page.")
        else:
            self.current_page = page

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

p.get_visible_items() 

p.next_page()

p.get_visible_items()

p.last_page()

p.get_visible_items()
