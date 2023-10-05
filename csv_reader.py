import csv


def get_stores_list(skip_header=True):
	with open("stores.csv") as stores_csv:
		csv_reader = csv.reader(stores_csv, delimiter=',')
		if skip_header:
			next(csv_reader)

		stores_list = []
		for row in csv_reader:
			stores_list.append(row)

		return stores_list