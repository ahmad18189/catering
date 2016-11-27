// Copyright (c) 2016, Ahmad18189 and contributors
// For license information, please see license.txt
cur_frm.add_fetch("customer_event_request", "event_date_and_time", "event_date_and_time");
cur_frm.add_fetch("customer_event_request", "customer", "customer");
cur_frm.add_fetch("customer_event_request", "event_manager", "event_manager");

frappe.ui.form.on('Kitchen Event Food Details', {
	refresh: function(frm) {

	}
});
cur_frm.cscript.custom_show_all_food_type = 
cur_frm.cscript.custom_food_type = 
cur_frm.cscript.custom_customer_event_request = 
function(doc, cdt, cdn) {
  var d = locals[cdt][cdn];
	frappe.call({
		doc: doc,
		method: "get_cer",
		callback: function(r) {
			console.log(r.message);
			 cur_frm.refresh_fields(["kitchen_food_item","total_food_items","food_item_remaining","food_item_done"]);
		}
	});

};
cur_frm.cscript.custom_done = function(doc, cdt, cdn) {
  var d = locals[cdt][cdn];
	frappe.call({
		doc: doc,
		method: "calc_food_item",
		callback: function(r) {
			console.log(r.message);
			 cur_frm.refresh_fields(["kitchen_food_item","total_food_items","food_item_remaining","food_item_done"]);
		}
	});

};

