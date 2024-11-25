import flet as ft
from Models.BillingModel import Billing
from datetime import datetime

class BillRow(ft.DataRow):
    def __init__(self, billing:Billing,cells: list = None, **kwargs):
        super().__init__(**kwargs)
        self.cells = [
            ft.DataCell(ft.TextButton(billing.getName())),
            ft.DataCell(ft.Text(billing.date))
        ]


class ItemRow(ft.DataRow):
    def __init__(self, name="plumbus",price=30_000,stock=911):
        super().__init__()
        self.cells = [
            ft.DataCell(ft.TextField(value=name,border=ft.InputBorder.NONE)),
            ft.DataCell(ft.TextField(value=str(price),border=ft.InputBorder.NONE)),
            ft.DataCell(ft.TextField(value=str(stock),border=ft.InputBorder.NONE)),
            ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, icon_color="red"))
        ]
#NavigationColumn es un container con dos columns
class NavigationColumn(ft.Container):
    def __init__(self, name=""):
        super().__init__()
        self.name = name
        self.spacing = 0
        self.scroll = ft.ScrollMode.ALWAYS
        self.width = 200
        self.height = 550
        self.bgcolor = ft.colors.GREY_900
        self.selected_index = 0
        self.padding = 10
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self._setup_Navigation()
    
    def _setup_Navigation(self):
        title = ft.Text(self.name,height=35)
        veryUsefullInfo = ft.Container(content=ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
            ft.Text("Manager", text_align=ft.TextAlign.CENTER, size=23),
            ft.Text(datetime.now().strftime("%H:%M:%S"), text_align=ft.TextAlign.CENTER),
            ft.Text(datetime.today().date(), text_align=ft.TextAlign.CENTER),
        ]),
        height=120,
        width= 200
        )
        navigationButtons = ft.Container(content=ft.Column(
            spacing=4,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextButton(text="Regristro de recibos diarios", width=180, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))),
                ft.TextButton(text="Inventario", width=180,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
            ]
        ),
        height=150
        )
        closingButtons = ft.Container(content=ft.Column(
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
            ft.TextButton(text="Salir", on_click= lambda _: print("nos salimos"), height=25),
            ft.TextButton(text="Cerrar sesión", on_click= lambda _: self.page.go(""), height=25)
        ]),
        height=60
        )

        self.content=ft.Column(
            expand=True,
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[title,veryUsefullInfo,navigationButtons,closingButtons])
       



 
class ManagerView(ft.View):
    def __init__(self, title: str = "Default Title", controls: list = None, **kwargs):
        super().__init__(route="/login", **kwargs)  # You must provide a `route` for the view
        self.title = title
        self.cont = ft.Row(controls=[], expand=True)
        self.controls = [self.cont]
        self.BillingsPage = ft.Column(expand=True, visible=False, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.BillingRows = []
        self.Inventory = ft.Column(expand=True, visible=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.InventoryRows = []
        self._setupInventoryRows(range(5))
        self._setupBillingRows([Billing(date="jujujuju"),Billing(date="tomorrow")])
        self._setup_view()

    def _setupInventoryRows(self, items=[]):
        for a in items:
            self.InventoryRows.append(ItemRow())

    def _setupBillingRows(self,billings:list):
        self.BillingRows = []
        for a in billings:
            self.BillingRows.append(BillRow(a))

    def _setup_view(self):
        content = self.cont

        content.controls.append(NavigationColumn("<Nombre Empresa>"))
        content.controls.append(ft.VerticalDivider(width=1))
        content.controls.append(self.BillingsPage)
        content.controls.append(self.Inventory)
        # Add a divider for visual separationç
        self.BillingsPage.controls = [
            ft.Text("Registro de Recibos diarios"),
            ft.Column(
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=[ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Nombre del archivo")),
                        ft.DataColumn(ft.Text("Fecha de creación"))
                    ],
                    rows=self.BillingRows
                    )]
                )
            ]

        self.Inventory.controls = [
            ft.Text("Inventario"),
            ft.Column(
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=[ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Nombre item")),
                        ft.DataColumn(ft.Text("    Precio    ")),
                        ft.DataColumn(ft.Text("Cantidad")),
                        ft.DataColumn(ft.Text("  ")),
                    ],
                    rows=self.InventoryRows
                    )]
                )
            ]
    
    def changePage(p):
        pass