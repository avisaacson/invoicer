def invoice_num():
	f = open("invoice_num.txt")
	num = int(f.read())
	num += 1
	f.close()

	f = open("invoice_num.txt", 'w')
	num = str(num)
	f.write(num)
	f.close()
	return num


def order_num(store):
	f = open(f"order_nums/{store.name}.txt")
	num = int(f.read())
	num += 1
	f.close()

	f = open(f"order_nums/{store.name}.txt", 'w')
	num = str(num)
	f.write(num)
	f.close()
	return num


def invoice_num_undo():
	f = open("invoice_num.txt")
	num = int(f.read())
	num -= 1
	f.close()

	f = open("invoice_num.txt", 'w')
	num = str(num)
	f.write(num)
	f.close()
	return num


def order_num_undo(store):
	f = open(f"order_nums/{store.name}.txt")
	num = int(f.read())
	num -= 1
	f.close()

	f = open(f"order_nums/{store.name}.txt", 'w')
	num = str(num)
	f.write(num)
	f.close()
	return num