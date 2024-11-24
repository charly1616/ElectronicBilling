import flet as ft

class LoginView(ft.View):
    def __init__(self, title: str = "Default Title", controls: list = None, **kwargs):
        super().__init__(route="/login", **kwargs)  # You must provide a `route` for the view
        self.title = title
        self.route = "/Register"
        self.cont = ft.Row(controls=[])
        self.controls = [self.cont]
        self._setup_view()

    def _setup_view(self):
        image = ft.Container(height=380,width=380,bgcolor=ft.colors.WHITE)
        LoginPart = ft.Column()
        LoginPart.controls.append(ft.Text("E-FacturaNet", size=24))
        LoginPart.controls.append(ft.TextField(label="Email"))
        LoginPart.controls.append(ft.TextField(label="Contraseña", password=True))
        LoginPart.controls.append(ft.ElevatedButton("Iniciar Sesión", on_click=lambda _: print("Login clicked!")))
        LoginPart.controls.append(ft.ElevatedButton("Crear cuenta", on_click=lambda _: self.page.go("/Register")))

        self.cont.controls = [image, LoginPart]