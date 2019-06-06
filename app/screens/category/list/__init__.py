from functools import partial

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.category.base import CategoryScreen
from services.exceptions import ConnectionError_
from uix.popups.confirm.helpers import confirm
from uix.popups.info import InfoPopup
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

	def delete_category(self, widget, category):
		def delete():
			try:
				self.service.delete(category=category)
			except ConnectionError_ as err:
				InfoPopup(title='Error',
						  message=str(err)).open()
			else:
				self.fetch_categories()
				self.show_if_error()
				self.list_categories()
		confirm(title="Delete Category",
				question=f"Are you sure?\n({category.history})",
				confirmed=delete)

	def update_category(self, category):
		self.manager.get_screen('category_update').category = category
		self.manager.current = 'category_update'

	def list_categories(self):
		self.list.clear_widgets()
		self.categories.sort(key=lambda c: c.history)
		for category in self.categories:
			cat_box = CategoryBox(category=category)
			cat_box.remove_btn.on_release = partial(self.delete_category,
													widget=cat_box,
													category=category)
			cat_box.update_btn.on_release = partial(self.update_category,
													category=category)
			self.list.add_widget(cat_box)

	def init_scroll_list(self):
		# Necessary to scroll
		self.list.bind(minimum_height=self.list.setter('height'))
