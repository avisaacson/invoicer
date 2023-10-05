import csv

with open("stores.csv") as stores_csv:
	csv_reader = csv.reader(stores_csv, delimiter=',')
	next(csv_reader)

	stores_list = []
	for row in csv_reader:
		with open(f"order_nums/{row[1]}.txt", 'w') as f:
			f.write('1')