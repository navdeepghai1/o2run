# -*- coding: utf-8 -*-
'''
Developer Navdeep Ghai
email navdeepghai1@gmail.com
'''
from __future__ import unicode_literals

__version__ = '0.0.1'

import frappe

@frappe.whitelist()
def update_language(lang):

        try:
                setting  = frappe.get_doc("System Settings", "System Settings")
                if not frappe.db.get_value("Language", filters={"name": lang}):
                        frappe.msgprint("Your Selected Langauge doesn't support")
                        return

                setting.language = lang
                setting.save()
                frappe.db.commit()
		return {"status": "Changed"}
        except  Exception as e:
                frappe.throw("Error while setting langauge")
                return {"status": "Error"}


