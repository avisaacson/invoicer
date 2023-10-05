from fpdf import *
from date_utils import *
import increment_utils


INCH = 72

W1 = INCH * 2.5
W2 = INCH * 1.5

H1 = 14
H2 = 24


def write_invoice(store, wine_order_items, ship_date):
	pdf = FPDF(orientation='L', unit="pt", format="letter")
	pdf.add_page()
	pdf.set_font(family="courier", style='b', size=9)

	pdf.set_left_margin(INCH)

	pdf.image("logo.png", w=INCH * 2.5)

	pdf.ln(INCH / 4)

	pdf.cell(W1, H1, txt="SHIP TO:")
	pdf.cell(W1, H1, txt="BILL TO:")
	pdf.cell(W1, H1, txt="REMIT TO:")
	pdf.set_font_size(8)
	pdf.set_text_color(75, 75, 75)
	pdf.cell(0, H1, txt="AMITYVILLE CELLARS", ln=1)

	pdf.set_font_size(10)
	pdf.set_font(family='', style='')
	pdf.set_text_color(0, 0, 0)
	pdf.cell(W1, H1, txt=store.name)
	pdf.cell(W1, H1, txt=store.name)
	pdf.cell(W1, H1, txt="AMITYVILLE CELLARS")
	pdf.set_font_size(8)
	pdf.set_text_color(75, 75, 75)
	pdf.cell(0, H1, txt="35 COX NECK RD", ln=1)

	pdf.set_font_size(10)
	pdf.set_text_color(0, 0, 0)
	pdf.cell(W1, H1, txt=store.corporate)
	pdf.cell(W1, H1, txt=store.corporate)
	pdf.cell(W1, H1, txt="AMITYVILLE ENOLOGY, INC.")
	pdf.set_font_size(8)
	pdf.set_text_color(75, 75, 75)
	pdf.cell(0, H1, txt="MATTITUCK NY, 11952", ln=1)

	pdf.set_font_size(10)
	pdf.set_text_color(0, 0, 0)
	pdf.cell(W1, H1, txt=store.address)
	pdf.cell(W1, H1, txt=store.address)
	pdf.cell(W1, H1, txt="33 FORREST PL")
	pdf.set_font_size(8)
	pdf.set_text_color(75, 75, 75)
	pdf.cell(0, H1, txt="NYS LIC NUMBER: 1333479", ln=1)

	pdf.set_font_size(10)
	pdf.set_text_color(0, 0, 0)
	pdf.cell(W1, H1, txt=f"{store.city} {store.state}, {store.zip_code}")
	pdf.cell(W1, H1, txt=f"{store.city} {store.state}, {store.zip_code}")
	pdf.cell(W1, H1, txt="AMITYVILLE NY, 11701")
	pdf.set_font_size(8)
	pdf.set_text_color(75, 75, 75)
	pdf.cell(0, H1, txt="NYS TAX ID: 84-2243592", ln=1)

	pdf.set_font_size(10)
	pdf.set_text_color(0, 0, 0)
	pdf.cell(W1, H1, txt=store.phone, ln=1)

	pdf.cell(W1, H1, txt=f"CONTACT: {store.contact}", ln=1)

	pdf.ln(INCH / 4)

	pdf.cell(W2, H2, txt="CUSTOMER LIC NUM", border=1)
	pdf.cell(W2, H2, txt="INVOICE NUMBER", border=1)
	pdf.cell(W2, H2, txt="ORDER NUMBER", border=1)
	pdf.cell(W2, H2, txt="DUE DATE", border=1)
	pdf.cell(W2, H2, txt="SHIP DATE", border=1)
	pdf.cell(W2, H2, txt="TERMS", border=1, ln=1)

	invoice_num = increment_utils.invoice_num()
	pdf.cell(W2, H2, txt=f"{store.county} - {store.liquor_num}", border=1)
	pdf.cell(W2, H2, txt=invoice_num, border=1)
	pdf.cell(W2, H2, txt=increment_utils.order_num(store), border=1)
	pdf.cell(W2, H2, txt=due_date(ship_date), border=1)
	pdf.cell(W2, H2, txt=ship_date, border=1)
	pdf.cell(W2, H2, txt="NET 30", border=1, ln=1)

	pdf.ln(INCH / 4)

	pdf.cell(42, H2, txt="ITEM #", border=1, align='C')
	pdf.cell(60, H2, txt="VINTAGE", border=1, align='C')
	pdf.cell(34, H2, txt="SIZE", border=1, align='C')
	pdf.cell(400, H2, txt="DESCRIPTION", border=1)
	pdf.cell(72, H2, txt="UNIT PRICE", border=1, align='C')
	pdf.cell(40, H2, txt="UNITS", border=1, ln=1, align='C')

	total_price = 0
	num_units = 0
	for sku in wine_order_items:
		pdf.cell(42, H2, txt=sku.item_num, border=1)
		pdf.cell(60, H2, txt=sku.vintage, border=1)
		pdf.cell(34, H2, txt=sku.size, border=1)
		pdf.cell(400, H2, txt=sku.description, border=1)
		if int(sku.cases_on_order) >= int(sku.discount_num_cases):
			pdf.cell(72, H2, txt=f"${sku.discount_price}", border=1)
			total_price += float(sku.discount_price) * float(sku.cases_on_order)
		else:
			pdf.cell(72, H2, txt=f"${sku.price}", border=1)
			total_price += float(sku.price) * float(sku.cases_on_order)
		pdf.cell(40, H2, txt=str(sku.cases_on_order), border=1, ln=1, align='C')
		num_units += sku.cases_on_order

	pdf.cell(536, H2, txt="AMOUNT DUE ", border=1, align='R')
	pdf.cell(72, H2, txt=f"${str(format(total_price, '.2f'))}", border=1)
	pdf.cell(40, H2, txt=str(num_units), border=1, ln=1, align='C')

	pdf.ln(INCH / 4)

	pdf.multi_cell(INCH * 9, 12, txt="THE UNDERSIGNED LICENSEE HEREBY ACKNOWLEDGES THAT ALL OF THE ALCOHOLIC BEVERAGES ITEMIZED ABOVE HAVE BEEN ORDERED, AND WERE RECEIVED ON:")

	pdf.ln(INCH / 2.5)

	pdf.cell(0, txt="SIGNATURE:_______________________________________________________________________ DATE:____________________")

	pdf.ln(INCH / 2.5)

	pdf.cell(0, txt="PRINT NAME:________________________________________________________________________________________________")

	pdf.ln(INCH / 2.5)

	pdf.set_font_size(8)
	pdf.set_text_color(75, 75, 75)
	pdf.multi_cell(INCH * 9, 12, txt="WHOLESALE WINES SOLD TO NYS LICENSED RETAILERS ARE NOT SUBJECT TO NYS SALES TAX; AMITYVILLE ENOLOGY, INC. ASSUMES NYS AND FEDERAL EXCISE TAX LIABILITY FOR ALL WINE SOLD.")


	pdf.output(f"invoices/{invoice_num}_{store.name.lower()}.pdf")


#write_invoice(store, wine_order_items, ship_date)