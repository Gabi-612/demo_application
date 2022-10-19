from erpnext.education.doctype.student.student import Student
from frappe.model.document import Document

class gabishistudent(Document):
    def validate(self):
        print("\n\n\n This is the place we put our logic... \n\n\n")
        return