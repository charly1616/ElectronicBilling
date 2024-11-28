import flet as ft
import random
import InformationCatcher as info

class ItemButton(ft.Container):
    def __init__(self,father, pname="Fart in Glass", price = 1000, num = "0",productArray=[],**kwargs):
        super().__init__()
        self.pname = pname
        self.price = price
        self.num = num
        self.father = father
        self.content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
            spacing=0,
            controls=
            [ft.Text(f"[{self.num}]", text_align=ft.TextAlign.CENTER),
            ft.Text(self.pname, text_align=ft.TextAlign.CENTER),
            ft.Text(self.price, text_align=ft.TextAlign.CENTER)])
        self.bgcolor=ft.colors.AMBER_600
        self.border_radius = 5
        self.width,self.height = 140,140
        self.visible = True
        self.expand = False

        def addProduct(e):
            value = [x for x in productArray if x["Item"] == pname]
            if len(value) == 0:
                productArray.append({"Item":pname,"Cantidad":1,"Subtotal":price})
            else:
                for a in value:
                    a["Cantidad"]+=1
                    a["Subtotal"]=price*a["Cantidad"]
            father.variableQueContieneLaTabla.rows = father.generarFilas()
            father.update()

        self.on_click = addProduct if productArray != None else lambda _:print("Producto añadido")
        


class EmployeeView(ft.View):
    def __init__(self, title = "", controls: list = None, **kwargs):
        super().__init__()  # You must provide a `route` for the view
        self.title = ""
        self.controls = []
        self.padding = 20
        self.scroll = "adaptive"
        self.Texto = ft.Text("Texto", height=60)
        # Datos iniciales
        self.datos = []

        # Función para generar filas dinámicamente
        def generarFilas():
            self.Texto.value = "Total: " + str(sum(x["Subtotal"] for x in self.datos))
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
        self.generarFilas = generarFilas
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
        
        self.Columna = ft.Column(controls=[self.variableQueContieneLaTabla], height=450, width=400, scroll= ft.ScrollMode.ADAPTIVE)
        self.Texto = ft.Text("Texto", height=60)
        self.Table = ft.Column(controls= [self.Columna, self.Texto])
        
        self.MenuCosa = ft.Container(content=ft.GridView(
            controls=[ItemButton(
                num=i, pname=a["name"],price=a["price"],
                productArray=self.datos,
                father = self
                ) for i,a in enumerate(info.getProducts())] , height=340,width=540,
            max_extent=135,
            expand=1,
            runs_count=6,
            ))
        self.Botones = ft.Row(controls=[self.botonParaAgregarCosas, self.botonParaBorrarCosasDeLaVariableQueContieneLaTabla], height=60)
        self.Menu = ft.Column(controls= [self.MenuCosa, self.Botones],height= 450, width=450)
        
        self.View = ft.Container(content=ft.Row(controls = [self.Table, self.Menu]))
        
        self.controls = [self.View]

        
