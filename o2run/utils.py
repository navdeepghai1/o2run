'''
	Developer Navdeep Ghai
'''


import frappe
from frappe import _, msgprint, throw

TEMPLATE_PATH = "templates/includes/jitem.html"

@frappe.whitelist(allow_guest=True)
def get_items(group):
	condition = " WHERE item.item_group='%s'"%(group)
	items = frappe.db.sql(""" SELECT item.name, item.item_group, item.description, item.image, item.item_code, \
			item.item_name, ip.price_list_rate from `tabItem` item LEFT JOIN `tabItem Price` ip ON  item.name= \
			ip.item_code %s """%(condition) , as_dict=True)
	results = []
	template =  frappe.get_template(TEMPLATE_PATH)
	for item in items:
		text = template.render({"item":item})
		results.append(text)
		
	return results
