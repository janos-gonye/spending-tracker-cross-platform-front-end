import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label


class SpendingTrackerApp(App):

	def build(self):
		return Label(text='Hello Github! :)')


if __name__ == '__main__':
	SpendingTrackerApp().run()
