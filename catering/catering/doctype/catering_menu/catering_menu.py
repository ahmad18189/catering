# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ahmad18189 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CateringMenu(Document):
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
		if self.get("menu_item"):
			for value in self.get("menu_item"):
				total_item += value.mi_total_price
		if self.get("menu_food_item"):
			for value in self.get("menu_food_item"):
				total_food += value.total_price
		
		self.menu_total_cost = total_food+total_item-self.discount
			

