# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ahmad18189 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DriverEventSlip(Document):
	
	def fill_data(self):
		if self.customer_event_request :
			cr = frappe.get_doc("Customer Event Request",self.customer_event_request)
			if cr.get("menu_food_item"):
				self.menu_food_item=[]
				for value in cr.get("menu_food_item"):
					child = self.append('menu_food_item', {})
					child.food_type = value.food_type
					child.food_item = value.food_item
					child.size = value.size
					child.quantity = value.quantity
					child.received = 1
			if cr.get("menu_item"):
				self.menu_item=[]
				for value in cr.get("menu_item"):
					child = self.append('menu_item', {})
					child.item_category = value.item_category
					child.item = value.item
					child.mi_quantity = value.mi_quantity
					child.received = 1
		return "done"
				
