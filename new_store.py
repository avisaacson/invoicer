from store import Store

import csv


store_atts = ["store name", "corporate name", "county", "contact", "liquor license num", "sales tax id", "address", "city", "state", "zip", "phone"]


def ask_store_info():
	store_name = ask_store_att(store_atts[0])
	corp_name = ask_store_att(store_atts[1])
	county = ask_store_att(store_atts[2])
	contact = ask_store_att(store_atts[3])
	liquor_lic_num = ask_store_att(store_atts[4])
	sales_tax_id = ask_store_att(store_atts[5])
	address = ask_store_att(store_atts[6])
	city = ask_store_att(store_atts[7])
	state = ask_store_att(store_atts[8])
	zipcode = ask_store_att(store_atts[9])
	phone = ask_store_att(store_atts[10])
	new_store = Store(store_name, corp_name, county, contact, liquor_lic_num, address, city, state, zipcode, phone, sales_tax_id)
	return new_store


def ask_store_att(store_att):
	while True:
		ans = 0
		attr = input(f"\nPlease enter {store_att}: ")
		ans = input(f"""If "{attr.upper()}" is good press enter: """)
		if ans == "":
			return attr.upper()


def append_store(store):
	num_lines = _count_lines()
	with open('stores.csv', 'a') as f:
	    writer_obj = csv.writer(f)
	    writer_obj.writerow(num_lines, store.name, store.corp_name, store.county, store.contact, store.liquor_lic_num, store.sales_tax_id, store.address, store.city, store.state, store.zip, store.phone)
	    f.close()


def _count_lines():
	reader = csv.reader(open("stores.csv"))
	num_lines = len(list(reader))
	return num_lines


def create_order_num_doc(name):
	with open(f"{name}.txt") as f:
		f.write(0)


	

def main():
	new_store = ask_store_info()
	append_store(new_store)
	create_order_num_doc(new_store.name)





if __name__=="__main__":
	main()