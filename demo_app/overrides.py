# from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
# from erpnext.controllers.stock_controller import StockController

# class gabishistockentry(StockController):
#     def validate_finished_goods(self):
#         print("\n\n\n This is the place we put our logic... \n\n\n")
#         return



from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
from erpnext.controllers.stock_controller import StockController

class gabishistockentry(StockController):
    
    def validate(self):
        print("\n\n\n This is the place we put our logic... \n\n\n")
        return
