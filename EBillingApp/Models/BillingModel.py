import random
import xml.etree.ElementTree as ET
IVA = 0.19

class Item:
    def __init__(self, name, quantity, unitPrice):
        self.name = name
        self.quantity = quantity
        self.unitPrice = unitPrice
        pass

class Billing:
    def __init__(self, company = "",NIT = "8=====D", paidAmount=0, date=""):
        self.items = []
        self.date = date
        self.paidAmount = paidAmount
        self.subtotal = 0
        self.total = 0
        
    def getName(self):
        return ("GeneralBilling."+str(random.randint(1000, 9999)))
    
    def _addItem(self, it:Item):
        self.items.append(it)
    

    def ToXML(self):
        pass
