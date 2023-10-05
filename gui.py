import tkinter as tk
import csv_reader

window = tk.Tk()


stores_names = []
stores_raw = csv_reader.get_stores_list()
#for store in stores_raw:
#	stores_names.append(store[1].title())
#stores_var = tk.StringVar(value=stores_names)

lb = tk.Listbox(window, selectmod="SINGLE")
i = 1

for store in stores_raw:
	lb.insert(i, store[1])
	i += 1

lb.pack()


window.mainloop()