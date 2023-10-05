from csv_reader import *
from wine_skus_list import wine_skus
from invoice_writer import write_invoice
from store import Store
from date_utils import date_tomorrow
from invoice_void import void
import time



def display_stores():
	stores_list = get_stores_list()
	for store in stores_list:
		print(store[0], store[1])
	print("'q' to quit")


def select_store():
	return input("Ship to which store?: ")


def do_quit(answer):
	if answer == 'q'.lower():
		return True
	else:
		return False

def store_is_valid(store_selected):
	stores_list = get_stores_list(skip_header=False)
	for store in stores_list:
		if store_selected == store[0]:
			return True
	return False


def init_store(store_num):
	stores_list = get_stores_list()
	for store in stores_list:
		if store_num == store[0]:
			return Store(store[1], store[2], store[3], store[4], store[5], store[7], store[8], store[9], store[10], store[11])


def display_skus():
	for sku in wine_skus:
		print(int(sku.item_num), sku.description, sku.vintage, '$'+str(sku.price))
	print('"void" an invoice')


def select_sku_item_num():
	return input("Enter sku item number: ")


def void_selected(selection):
	if selection == "void".lower():
		return True
	else:
		return False


def sku_num_is_valid(sku_num_selected):
	for sku in wine_skus:
		if int(sku_num_selected) == int(sku.item_num):
			return True
	else:
		return False 

	
def get_wine_sku(sku_num_selected):
	for sku in wine_skus:
		if int(sku_num_selected) == int(sku.item_num):
			return sku



def ask_num_cases():
	while True:
		ans = input("Ship how many cases?: ")
		if ans.isnumeric():
			return int(ans)
		else:
			print("Invalid input. Please enter a numeric value, such as 2.")
			continue


def add_another_sku():
	while True:
		ans = input("Add another wine sku to the order? Press 'y' or <enter>, press 'n' to continue': ")
		if ans.lower() == 'y' or ans == '':
			return True
		elif ans.lower() == 'n':
			return False
		else:
			print("Invalid input.")


def commit_order(order):
	while True:
		for sku in order:
			print(sku.item_num, sku.cases_on_order)
		ans = input("Press 'y' or <enter> to commit. Otherwise, press 'n' to reset whole order: ")
		if ans.lower() == 'y' or ans == '':
			return True
		elif ans.lower() == 'n':
			return False
		else:
			print("Invalid input")
			continue

def ship_tomorrow():
	while True:
		ans = input("Ship tomorrow? Press 'y' or <enter>. To select a different date press 'n': ")
		if ans.lower() == 'y' or ans == '':
			return True
		elif ans.lower() == 'n':
			return False
		else:
			print("Invalid input.")


def set_ship_date():
	return input("Enter date to ship. (yyyy-mm-dd): ")


def main():
	while True:
		display_stores()
		store_num = select_store()

		if do_quit(store_num):
			break
		if store_is_valid(store_num):
			store = init_store(store_num)
			wine_order_items = []

			while True:
				display_skus()
				sku_item_num = select_sku_item_num()

				if void_selected(sku_item_num):
					void(store)
					break
				if sku_num_is_valid(sku_item_num):
					wine_sku = get_wine_sku(sku_item_num)
					wine_sku.cases_on_order = ask_num_cases()
					wine_order_items.append(wine_sku)
					if add_another_sku():
						continue
					if not commit_order(wine_order_items):
						wine_order_items = []
						continue

					if not ship_tomorrow():
						ship_date = set_ship_date()
					else:
						ship_date = date_tomorrow()

					write_invoice(store, wine_order_items, ship_date)
					print("\ndone")
					break



if __name__=="__main__":
	main()