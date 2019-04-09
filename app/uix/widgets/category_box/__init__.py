from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('uix/widgets/category_box/category_box.kv')


class CategoryBox(BoxLayout):

	def __init__(self, category, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.category = category
		self.title.text = f"[b]{category.title}[/b]"
		self.description.text = f"[b]{category.description}[/b]"
