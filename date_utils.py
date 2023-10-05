from datetime import datetime, timedelta, date


def date_tomorrow():
	return str(date.today() + timedelta(days=1))


def due_date(ship_date):
	format_str = "%Y-%m-%d"
	datetime_obj = datetime.strptime(ship_date, format_str)
	return str(datetime_obj.date() + timedelta(days=30))