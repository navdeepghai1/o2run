# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "O2run",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("O2run")
		},
		{
			"module_name": "HRM",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("O2RUN HRM")
		}
	]
