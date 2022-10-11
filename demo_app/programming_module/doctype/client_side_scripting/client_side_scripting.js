// Copyright (c) 2022, Gabishi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	// refresh: function(frm) {
		// frappe.msgprint("Hello De-codE")
		// frappe.throw("This is an Error")

		family_members_on_form_rendered: function(frm) {
			frappe.throw("Hello D-codE from 'family_members' child table rendered event" )

	}
});