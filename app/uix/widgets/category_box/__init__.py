from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('uix/widgets/category_box/category_box.kv')


class CategoryBox(BoxLayout):

	def __init__(self, category, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title.text = f"[b]{category.history}[/b]"
		self.description.text = f"[b]{category.description}[/b]"
