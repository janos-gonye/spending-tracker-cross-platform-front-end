from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('screens/category/category.kv')


class CategoryScreen(Screen):
	"""
	The user can manage his categories and subcategories.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
