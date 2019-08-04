class ListScreenMixin:

    def init_scroll_list(self):
        # Necessary to scroll
        self.list.bind(minimum_height=self.list.setter('height'))
