'''
	Developer Navdeep Ghai
'''
import frappe
from frappe import _
import urlparse

no_cache = 1
no_sitemap = 1

def get_context(context):
	
	name = frappe.request.args.get("name")
	if name:
		item_detail  = get_item_detail(name)
		title = item_detail.get("item_name") if  item_detail else "Item not found"

	context.update({"title":title, "item": item_detail})






def get_item_detail(name):
	
	name = urlparse.unquote(name)
	cond = " WHERE item.name= '%s' "%(name)
	result = frappe.db.sql(""" SELECT item.name, item.item_name, item.item_code, item.description,item.image, ip.price_list_rate \
			FROM `tabItem` item LEFT JOIN `tabItem Price` ip ON   ip.item_code = item.name %s """%(cond),  as_dict=True)
		
	
	return result[0] if len(result)> 0 else None
	
