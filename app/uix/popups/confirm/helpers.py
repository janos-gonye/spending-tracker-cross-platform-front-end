from kivy.uix.popup import Popup

from uix.popups.confirm import ConfirmPopup


def confirm(title, question, confirmed=None, not_confirmed=None):
	"""
	title: title
	question: question asked from the user
	confirmed: callback, if user clicks 'yes'
	not_confirmed: callback, if user clicks 'no'
	"""
	def _on_answer(instance, answer):
		if confirmed and answer:
			confirmed()
		elif not_confirmed and not answer:
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
