import tkinter as tk
from Models.BillingModel import Item, Billing, IVA 

def show_invoice(billing):
    billing.calculateTotals()

    # Crear ventana
    window = tk.Tk()
    window.title("Factura Electrónica")

    # Mostrar detalles
    details = f"""
    Empresa: {billing.company}
    NIT: {billing.NIT}
    Fecha: {billing.date}
    --------------------------
    Items:
    """
    for item in billing.items:
        details += f"- {item.name} (Cantidad: {item.quantity}, Precio Unitario: {item.unitPrice:.2f})\n"
    details += f"""
    --------------------------
    Subtotal: {billing.subtotal:.2f}
    Total (IVA {IVA*100:.0f}%): {billing.total:.2f}
    Monto Pagado: {billing.paidAmount:.2f}
    """

    # Etiqueta para mostrar detalles
    label = tk.Label(window, text=details, justify="left", padx=10, pady=10)
    label.pack()

    # Botón para cerrar la ventana
    close_button = tk.Button(window, text="Cerrar", command=window.destroy)
    close_button.pack()

    window.mainloop()
