import flet as ft 


class ItemButton(ft.Column):
    def __init__(self, **kwargs):
        super().__init__()
        self.controls=[ft.Text("SUKMI",width=50, bgcolor=ft.colors.AMBER_600)]
        self.visible = True
        self.expand = False
        self.on_click = lambda _: print("clicked ujuju")
        


class EmployeeView(ft.View):
    def __init__(self, title = "", controls: list = None, **kwargs):
        super().__init__()  # You must provide a `route` for the view
        self.title = ""
        self.controls = []
        self.padding = 20
        self.scroll = "adaptive"
        
        # Datos iniciales
        self.datos = []

        # Función para generar filas dinámicamente
        def generarFilas():
            return [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(fila["Item"])),
                        ft.DataCell(ft.Text(str(fila["Cantidad"]))),
                        ft.DataCell(ft.Text(fila["Subtotal"])),
                    ]
                )
                for fila in self.datos
            ]

        # Crear la tabla dinámica
        self.variableQueContieneLaTabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Item")),
                ft.DataColumn(ft.Text("Cantidad")),
                ft.DataColumn(ft.Text("Subtotal")),
            ],
            rows=generarFilas(),
        )

        def agregarCosas(e):
            self.datos.append({"Item": "Pera", "Cantidad": 1, "Subtotal": "1000"})
            self.variableQueContieneLaTabla.rows = generarFilas()
            self.update()

        self.botonParaAgregarCosas = ft.ElevatedButton("Agregar cosa", on_click=agregarCosas)
        
        def borrarCosasDeLaVariableQueContieneLaTabla(e):
            self.variableQueContieneLaTabla.rows = []
            self.datos = []
            self.View.update()
            
        self.botonParaBorrarCosasDeLaVariableQueContieneLaTabla = ft.ElevatedButton("Reiniciar tabla", on_click=borrarCosasDeLaVariableQueContieneLaTabla)
        
        self._setup_view()

    def _setup_view(self):
        
        self.Columna = ft.Column(controls=[self.variableQueContieneLaTabla], height=450, scroll= ft.ScrollMode.ADAPTIVE)
        self.Texto = ft.Text("Texto", height=60)
        self.Table = ft.Column(controls= [self.Columna, self.Texto])
        
        self.MenuCosa = ft.Container(content=ft.GridView(controls=[ItemButton() for a in range(6)] , height=300,width=300, expand=False))
        self.Botones = ft.Row(controls=[self.botonParaAgregarCosas, self.botonParaBorrarCosasDeLaVariableQueContieneLaTabla], height=60)
        self.Menu = ft.Column(controls= [self.MenuCosa, self.Botones],height= 450, width=450)
        
        self.View = ft.Container(content=ft.Row(controls = [self.Table, self.Menu]))
        
        self.controls = [self.View]

        
