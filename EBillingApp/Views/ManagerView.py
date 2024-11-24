import flet as ft
<<<<<<< Updated upstream



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
            ft.Text("Manager", text_align=ft.TextAlign.CENTER),
            ft.Text("<hh.mm.ss>", text_align=ft.TextAlign.CENTER),
            ft.Text("<dd.mm.yyyy>", text_align=ft.TextAlign.CENTER),
        ]),
        height=150,
        width= 200
        )
        navigationButtons = ft.Container(content=ft.Column(
            spacing=4,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextButton(text="Boton1", width=180),
                ft.TextButton(text="Boton2", width=180)
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
       



=======
 
>>>>>>> Stashed changes
class ManagerView(ft.View):
    def __init__(self, title: str = "Default Title", controls: list = None, **kwargs):
        super().__init__(route="/login", **kwargs)  # You must provide a `route` for the view
        self.title = title
        self.cont = ft.Row(controls=[], expand=True)
        self.controls = [self.cont]
        self._setup_view()

    def _setup_view(self):
        content = self.cont

        content.controls.append(NavigationColumn("<Nombre Empresa>"))
        content.controls.append(ft.VerticalDivider(width=1))
        # Add a divider for visual separation
    
    def changePage(p):
        pass