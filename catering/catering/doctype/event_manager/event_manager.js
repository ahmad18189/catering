// Copyright (c) 2016, Ahmad18189 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Event Manager', {
	refresh: function(frm) {

	}
});
var numbers_only_fields = [ 'phone_number'];
$.each(numbers_only_fields, function(index, value) {
  $('[data-fieldname=' + value + ']').on('keypress', numbersonly);
});
function numbersonly(e) {
  var unicode = e.charCode ? e.charCode : e.keyCode;
  if (unicode != 8) { //if the key isn't the backspace key (which we should allow)
    if (unicode < 48 || unicode > 57) //if not a number
      return false; //disable key press
  }
}
