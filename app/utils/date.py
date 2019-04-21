from datetime import datetime
from datetime import timezone


def datetime2timestamp(date):
	return date.replace(tzinfo=timezone.utc).timestamp()


def timestamp2datetime(timestamp):
	return datetime.utcfromtimestamp(float(timestamp))
