"""
file: for utitlity funtions
"""

from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def get_next_renewal_date(subscribed_date: str, duration=0):
	"""
	subsribed_date: start date of the subscription
	duration: duration to extend the subscription
	"""
	try:
		date_object = datetime.strptime(subscribed_date, '%d-%m-%Y').date()
		renewal_date = date_object + relativedelta(months=duration) + relativedelta(days=-10)
		renewal_date_str = renewal_date.strftime("%d-%m-%Y")
		return renewal_date_str
	except Exception as err:
		return "INVALID_DATE"