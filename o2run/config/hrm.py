'''
	Developer NavdeepGhai
	Email: navdeep@ameotech.com
'''

from frappe import _

def get_data():
	
	return [
			{
				"Label": _("O2RUN HRM Reports"),
				"items":[
					"type": "report",
                                        "is_query_report": True,
                                        "name": "Employee Account Statement",
                             	        "doctype": "Employee",

				]
			},
	]
