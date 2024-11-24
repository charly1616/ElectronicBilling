import flet as ft 

class EmployeeView(ft.View):
    def __init__(self, title = "", controls: list = None, **kwargs):
        super().__init__()  # You must provide a `route` for the view
        self.title = ""
        self.controls = []
        self.padding = 20
        self.scroll = "adaptive"
    
        # Datos iniciales
        datos = [
            {"Item": "Banana", "Cantidad": 2, "Subtotal": 2000},
        ]

        # Función para generar filas dinámicamente
        def generar_filas():
            return [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(fila["Item"])),
                        ft.DataCell(ft.Text(str(fila["Cantidad"]))),
                        ft.DataCell(ft.Text(fila["Subtotal"])),
                    ]
                )
                for fila in datos
            ]

        # Crear la tabla dinámica
        tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Item")),
                ft.DataColumn(ft.Text("Cantidad")),
                ft.DataColumn(ft.Text("Subtotal")),
            ],
            rows=generar_filas(),
        )

        # Función para añadir "Erick, 20, Barranquilla" al hacer clic
        def agregar_fila_fija(e):
            datos.append({"Item": "Pera", "Cantidad": 1, "Subtotal": "1000"})
            tabla.rows = generar_filas()
            self.update()

        # Botón para agregar la fila fija
        boton_agregar_fijo = ft.ElevatedButton("Agregar pera", on_click=agregar_fila_fija)
        
        # Añadir componentes a la página
        self.controls = [boton_agregar_fijo,
            tabla]
        self._setup_view()

    def _setup_view(self):
        # Add a title at the top
        self.controls.insert(0, ft.Text(self.title, size=24, weight="bold"))
        # Add a divider for visual separation
        self.controls.insert(1, ft.Divider())