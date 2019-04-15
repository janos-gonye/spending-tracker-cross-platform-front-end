from kivy.uix.popup import Popup

from uix.popups.confirm import ConfirmPopup


def confirm(title, question, confirmed, not_confirmed):
	"""
	title: title
	question: question asked from the user
	confirmed: callback, if user clicks 'yes'
	not_confirmed: callback, if user clicks 'no'
	"""
	def _on_answer(instance, answer):
		if (answer):
			confirmed()
		else:
			not_confirmed()
		# Close the window anyway
		popup.dismiss()


	content = ConfirmPopup(text=question)
	content.bind(on_answer=_on_answer)
	popup = Popup(title=title,
				  content=content,
				  size_hint=(.65, .3),
				  auto_dismiss= False)
	popup.open()
