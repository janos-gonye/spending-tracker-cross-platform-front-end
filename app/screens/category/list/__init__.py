from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.category.base import CategoryScreen
from uix.widgets.category_box import CategoryBox


Builder.load_file('screens/category/list/category_list.kv')


class CategoryListScreen(CategoryScreen):
	"""
	The user can manage his or her categories and subcategories.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._init_scroll_list()

	def on_enter(self):
		super().on_enter()
		if not self.conn_error:
			self._list_categories()

	def on_leave(self):
		self.list.clear_widgets()

	def _list_categories(self):
		for category in self.categories:
			self.list.add_widget(CategoryBox(category=category))

	def _init_scroll_list(self):
		# Necessary to scroll
		self.list.bind(minimum_height=self.list.setter('height'))
