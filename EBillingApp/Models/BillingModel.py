import random
import xml.etree.ElementTree as ET

IVA = 0.19

class Item:
    def __init__(self, id, name, quantity, unitPrice):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unitPrice = unitPrice

class Billing:
    def __init__(self, company="", NIT="10101010", paidAmount=0, date="", items=[]):
        self.company = company
        self.NIT = NIT
        self.items = items
        self.date = date
        self.paidAmount = paidAmount
        self.subtotal = 0
        self.total = 0

    def getName(self):
        return "GeneralBilling." + str(random.randint(1000, 9999))

    def _addItem(self, it: Item):
        self.items.append(it)

    def calculateTotals(self):
        self.subtotal = sum(item.unitPrice * item.quantity for item in self.items)
        self.total = self.subtotal * (1 + IVA)

    def ToXML(self):
        root = ET.Element("Factura")
        ET.SubElement(root, "Empresa").text = self.company
        ET.SubElement(root, "NIT").text = self.NIT
        ET.SubElement(root, "Fecha").text = self.date
        ET.SubElement(root, "MontoPagado").text = str(self.paidAmount)

        items_element = ET.SubElement(root, "Items")
        for item in self.items:
            item_element = ET.SubElement(items_element, "Item")
            ET.SubElement(item_element, "Nombre").text = item.name
            ET.SubElement(item_element, "Cantidad").text = str(item.quantity)
            ET.SubElement(item_element, "PrecioUnitario").text = str(item.unitPrice)

        ET.SubElement(root, "Subtotal").text = str(self.subtotal)
        ET.SubElement(root, "Total").text = str(self.total)

        return ET.tostring(root, encoding='unicode')
    