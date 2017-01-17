// Copyright (c) 2016, Ahmad18189 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Driver Event Slip', {
	refresh: function(frm) {

	},
	customer_event_request:function(frm){
		frappe.call({
		doc: frm.doc,
		method: "fill_data",
		callback: function(r) {
			console.log(r.message);
			 cur_frm.refresh_fields(["menu_food_item","menu_item"]);
		}
		});
	}
});
