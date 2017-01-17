# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Catering",
			"color": "grey",
			"icon": "octicon octicon-book",
			"type": "module",
			"label": _("Catering")
		},
		{
			"module_name": "Kitchen",
			"color": "grey",
			"icon": "octicon octicon-flame",
			"type": "module",
			"label": _("Kitchen")
		}
	]
