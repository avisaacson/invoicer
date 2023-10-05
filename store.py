class Store():
	def __init__(self, name, corporate, county, contact, liquor_num, address, city, state, zip_code, phone, sales_tax_id=None):
		self.name = name
		self.corporate = corporate
		self.county = county
		self.contact = contact
		self.liquor_num = liquor_num
		self.address = address
		self.city = city
		self.state = state
		self.zip_code = zip_code
		self.phone = phone
		self.sales_tax_id = sales_tax_id



#,STORE,CORPORATE NAME,COUNTY,CONTACT,LIQUOR LICENSE #,SALES TAX ID,ADDRESS,CITY,STATE,ZIP,PHONE