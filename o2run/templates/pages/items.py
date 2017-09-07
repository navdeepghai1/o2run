'''

	Developer Navdeep Ghai
'''

import frappe
from frappe import _, msgprint, throw

no_cache = 1
no_sitemap = 1

def get_context(context):
	item_groups = get_item_groups()
	items = get_items()
	context.update({"item_groups": item_groups, "items":items})




def get_item_groups():
	
	return frappe.db.sql("""SELECT  name FROM `tabItem Group` ORDER BY name ASC""", as_dict=True)



def get_items():

	items = frappe.db.sql("""SELECT item.name, item.item_name, item.item_code, item.description, item.image, pl.price_list_rate, \
				pl.currency  FROM `tabItem` item LEFT JOIN `tabItem Price` pl  ON item.item_code = \
				pl.item_code WHERE selling=1 LIMIT 20""", as_dict=True)
	return items
