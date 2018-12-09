class SessionService:
	email = None
	token = None

	@staticmethod
	def create(email, token):
		SessionService.email = email
		SessionService.token = token

	@staticmethod
	def destroy():
		SessionService.email = None
		SessionService.token = None
