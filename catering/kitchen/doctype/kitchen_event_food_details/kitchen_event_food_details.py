# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ahmad18189 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class KitchenEventFoodDetails(Document):
	def get_cer(self):
		cer = frappe.get_doc("Customer Event Request",self.customer_event_request)
		food_items = cer.get("menu_food_item")
		self.kitchen_food_item=[]
			
		for value in food_items:
			if self.show_all_food_type !=1 :
				if value.food_type == self.food_type:
					child = self.append('kitchen_food_item', {})
					child.food_type=value.food_type
					child.food_item=value.food_item
					child.size=value.size
					child.quantity=value.quantity
			else :
				child = self.append('kitchen_food_item', {})
				child.food_type=value.food_type
				child.food_item=value.food_item
				child.size=value.size
				child.quantity=value.quantity
		
		self.calc_food_item()
		return "done"
	
	def calc_food_item(self):
		fi = self.get("kitchen_food_item")
		temp =0
		temp1 =0
		self.total_food_items = len(fi)
		for value in fi : 
			if value.done != 1:
				temp +=1
			else:
				temp1 +=1
		self.food_item_remaining = temp 
		self.food_item_done = temp1 
		return "done"
