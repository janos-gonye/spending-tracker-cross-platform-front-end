import constants


def create_url(protocol, host, port, path, params={}):
	if path[0] == '/':
		path = path[1:]
	url = "{protocol}://{host}:{port}/{path}".format(
		protocol=protocol,
		host=host,
		port=port,
		path=path)
	if len(params) > 0:
		url += '?'
		for key, value in params.items():
			url += '{param}={value}&'.format(param=key, value=value)
		url = url[:-1] # chopp of last unnecessary '?' or last '&'
	return url


def succ_status(code):
	"""is successful http status code?"""
	return 200 <= code < 300
