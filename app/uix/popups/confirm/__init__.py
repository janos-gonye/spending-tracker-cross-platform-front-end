from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup


Builder.load_file('uix/popups/confirm/confirm.kv')


class ConfirmPopup(GridLayout):
	text = StringProperty()

	def __init__(self,**kwargs):
		self.register_event_type('on_answer')
		super().__init__(**kwargs)

	def on_answer(self, *args):
		pass


if __name__ == '__main__':
	class PopupTest(App):
		def build(self):
			content = ConfirmPopup(text='Do You Love Kivy?')
			content.bind(on_answer=self._on_answer)
			self.popup = Popup(title="Answer Question",
							   content=content,
							   size_hint=(.4, .3),
							   auto_dismiss= False)
			self.popup.open()

		def _on_answer(self, instance, answer):
			print ("User answer: " , repr(answer))
			self.popup.dismiss()

	PopupTest().run()
