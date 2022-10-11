import frappe

def validate(doc, event):
    print(f"\n\n\n\n\n{doc}, {event}")
    frappe.throw("This is the proof that error occured")