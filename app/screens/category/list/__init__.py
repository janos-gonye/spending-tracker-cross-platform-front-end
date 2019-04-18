from functools import partial

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
		self.init_scroll_list()

	def on_enter(self):
		super().on_enter()
		if not self.conn_error:
			self.list_categories()

	def on_leave(self):
		self.list.clear_widgets()

	def delete_category(self, category):
		print(category)

	def update_category(self, category):
		print(category)

	def list_categories(self):
		for category in self.categories:
			cat_box = CategoryBox(category=category)
			cat_box.remove_btn.on_release = partial(self.delete_category,
													category=category)
			cat_box.update_btn.on_release = partial(self.update_category,
													category=category)
			self.list.add_widget(cat_box)

	def init_scroll_list(self):
		# Necessary to scroll
		self.list.bind(minimum_height=self.list.setter('height'))
