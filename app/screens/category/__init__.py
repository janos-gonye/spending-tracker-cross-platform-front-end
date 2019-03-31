from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.category import CategoryService
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup


Builder.load_file('screens/category/category.kv')


class CategoryScreen(Screen):
	"""
	The user can manage his or her categories and subcategories.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.service = CategoryService()

	def on_pre_enter(self):
		try:
			self.categories = self.service.get_all()
			print(self.categories)
		except ConnectionError_ as err:
			InfoPopup(title='Connection Error', message=str(err)).open()
