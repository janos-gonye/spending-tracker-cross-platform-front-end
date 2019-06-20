from kivy.uix.screenmanager import ScreenManager


class AdaptiveScreenManager(ScreenManager):
	previously_active = None

	def switch_to(self, screen, **options):
		self.previously_active = self.current
		super().switch_to(screen, **options)

	def switch_back(self):
		"""
		Switch back to previously active screen.
		Useful if you want adaptive back/cancel buttons.
		"""
		self.current = self.previously_active
