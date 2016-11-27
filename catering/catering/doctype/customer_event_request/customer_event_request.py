# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ahmad18189 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class CustomerEventRequest(Document):
	def get_catering_menu_data(self):
		if self.catering_menu:
			cm = frappe.get_doc("Catering Menu",self.catering_menu)
			self.menu_food_item = cm. menu_food_item
			self.menu_item = cm. menu_item
			self.menu_class = cm. menu_class
		self.get_totals()
		return "done"
			
	def get_food_item(self, cdn,cdt,size):
		if self.get("menu_food_item"):
			for value in self.get("menu_food_item"):
				if value.name == cdn : 
					fi = frappe.get_doc("Food Item",value.food_item)
					if size == "Normal" : 
						value.unit_price = fi.normal_price
						value.total_price = value.quantity * value.unit_price 
						self.get_totals()
						return "done Normal"
					if size == "Small" : 
						value.unit_price = fi.small_price
						value.total_price = value.quantity * value.unit_price 
						self.get_totals()
						return "done Small"
					if size == "Medium" : 
						value.unit_price = fi.medium_price
						value.total_price = value.quantity * value.unit_price 
						self.get_totals()
						return "done Medium"
					if size == "Large" : 
						value.unit_price = fi.large_price
						value.total_price = value.quantity * value.unit_price 
						self.get_totals()
						return "done Large"
		self.get_totals()
		return "done"
	def get_item(self, cdn,cdt):
		price = 0
		if self.get("menu_item"):
			for value in self.get("menu_item"):
				if value.name == cdn : 
					fi = frappe.get_doc("Item",value.item)
					value.mi_unit_price = fi.standard_rate
					value.mi_total_price = value.mi_quantity * value.mi_unit_price 
		self.get_totals()
				
		return "done"
			
	def get_totals(self):
		total_item = 0 
		total_food =0
		total_worker =0
		discount = self.discount if self.discount else 0
		if self.get("menu_item"):
			for value in self.get("menu_item"):
				total_item += value.mi_total_price
		if self.get("menu_food_item"):
			for value in self.get("menu_food_item"):
				total_food += value.total_price
		if self.get("service_personnel"):
			for value in self.get("service_personnel"):
				total_worker += value.total_price
		
		self.total_cost = total_food+total_worker+total_item-discount
		
		
@frappe.whitelist()
def make_quotation(source_name, target_doc=None):
	def set_missing_values(source, target):
		target.customer = source.customer
		for value in source.get("menu_item"):
			child = target.append('items', {})
			child.item_code = value.item
			child.item_name= frappe.db.get_value("Item", value.item, "item_name")
			child.description = frappe.db.get_value("Item", value.item, "description")
			child.qty = value.mi_quantity
			child.rate = value.mi_unit_price
		
		food_items_price = 0
		for value in source.get("menu_food_item"):
			food_items_price += value.total_price
		for value in source.get("service_personnel"):
			food_items_price += value.total_price
		
		child = target.append('items', {})
		child.item_code = "مناسبة"
		child.item_name= frappe.db.get_value("Item",child.item_code, "item_name")
		child.description = frappe.db.get_value("Item",child.item_code, "description")
		child.qty = 1
		child.rate = food_items_price
		
		target.discount_amount = source.discount
		 
	
	doc = get_mapped_doc("Customer Event Request", source_name, {
			"Customer Event Request": {
				"doctype": "Quotation",
				"field_map": {
					"customer": "customer",
				}}
		}, target_doc, set_missing_values)
	return doc


			


