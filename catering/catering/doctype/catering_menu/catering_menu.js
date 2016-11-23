// Copyright (c) 2016, Ahmad18189 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Catering Menu', {
	refresh: function(frm) {

	},
	onload: function(frm) {
	
	},

});

cur_frm.set_query("food_item", "menu_food_item", function(doc, cdt, cdn) {
var d = locals[cdt][cdn];
	return{
		filters: [
				['Food Item', 'food_type', '=', d.food_type]

		]
	};
});
cur_frm.cscript.custom_food_type =
  function(doc, cdt, cdn) {
	var d = locals[cdt][cdn];
	d.food_item ="";
	d.unit_price ="";
	d.total_price ="";
	alert(d.food_item);
    cur_frm.refresh_fields(["menu_food_item"]);
    calc_all(doc);
	cur_frm.set_query("food_item", "menu_food_item", function(doc, cdt, cdn) {
			return{
			filters: [
				['Food Item', 'food_type', '=', d.food_type]
			]
		};
	});
  };
cur_frm.cscript.custom_food_item =
cur_frm.cscript.custom_size =
  function(doc, cdt, cdn) {
	  
	  var d = locals[cdt][cdn];
	  frappe.call({
      doc: doc,
      args:{'cdn':cdn,'cdt':cdt ,"size" :d.size},
      method: "get_food_item",
      callback: function(r) {
		 console.log(r.message)
		cur_frm.refresh_fields(["menu_food_item","menu_total_cost"]);
		calc_all(doc);
      }
    });

  }
  cur_frm.cscript.custom_quantity =
  cur_frm.cscript.custom_unit_price =
  function(doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		d.total_price = parseFloat(d.unit_price)* parseFloat(d.quantity);		
	   	cur_frm.refresh_fields(["menu_food_item","menu_total_cost"]);
	   	calc_all(doc);
  }

cur_frm.set_query("item", "menu_item", function(doc, cdt, cdn) {
var d = locals[cdt][cdn];
	return{
		filters: [
				['Item', 'item_category', '=', d.item_category]

		]
	};
});
cur_frm.cscript.custom_item_category =
  function(doc, cdt, cdn) {
	var d = locals[cdt][cdn];
	d.item ="";
    cur_frm.refresh_fields(["menu_food_item","menu_total_cost"]);
    calc_all(doc);
	cur_frm.set_query("item", "menu_item", function(doc, cdt, cdn) {
			return{
			filters: [
				['Item', 'item_category', '=', d.item_category]
			]
		};
	});
  };
 
 cur_frm.cscript.custom_item =
  function(doc, cdt, cdn) {
	  
	  var d = locals[cdt][cdn];
	  frappe.call({
      doc: doc,
      args:{'cdn':cdn,'cdt':cdt },
      method: "get_item",
      callback: function(r) {
		 console.log(r.message)
		 cur_frm.refresh_fields(["menu_item","menu_total_cost"]);
		 calc_all(doc);
      }
    });

  }
  cur_frm.cscript.custom_mi_quantity =
  cur_frm.cscript.custom_mi_unit_price =
  function(doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		d.mi_total_price = parseFloat(d.mi_unit_price)* parseFloat(d.mi_quantity);	
		calc_all(doc);
	   	cur_frm.refresh_fields(["menu_item","menu_total_cost"]);
  }
  cur_frm.cscript.discount =
  function(doc, cdt, cdn) {
		calc_all(doc);
  }
 
 
 calc_all = function(doc)
 {
	 frappe.call({
      doc: doc,
      method: "get_totals",
      callback: function(r) {
		 console.log(r.message)
		cur_frm.refresh_fields(["menu_total_cost"]);
      }
 })
}
