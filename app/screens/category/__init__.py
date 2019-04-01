from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.category import CategoryService
from services.exceptions import ConnectionError_
from uix.widgets.category_box import CategoryBox
from uix.popups.info import InfoPopup


Builder.load_file('screens/category/category.kv')


class CategoryScreen(Screen):
	"""
	The user can manage his or her categories and subcategories.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.service = CategoryService()
		self.conn_error = None
		self._init_scroll_list()

	def on_pre_enter(self):
		try:
			self.categories = self.service.get_all()
		except ConnectionError_ as err:
			self.conn_error = err

	def on_enter(self):
		if self.conn_error:
			InfoPopup(title='Connection Error', message=str(self.conn_error)).open()
		else:
			self._list_categories()

	def _list_categories(self):
		for category in self.categories:
			self.list.add_widget(CategoryBox(category=category))

	def _init_scroll_list(self):
		# Necessary to scroll
		self.list.bind(minimum_height=self.list.setter('height'))
