frappe.ui.form.on('Stock Entry Detail', {
	qty: function(frm, cdt, cdn){
	    var d = frappe.model.get_doc(cdt, cdn);
	    if (d.qty){
            if (d.t_warehouse == "Finished Goods - DE"){
                frm.set_value("fg_completed_qty", d.qty)
            }
	    }
	}
})