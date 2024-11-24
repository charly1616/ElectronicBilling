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
        LoginPart.controls.append(ft.Text("Welcome to the login page.", size=20))
        LoginPart.controls.append(ft.TextField(label="Username"))
        LoginPart.controls.append(ft.TextField(label="Password", password=True))
        LoginPart.controls.append(ft.ElevatedButton("Login", on_click=lambda _: print("Login clicked!")))
        LoginPart.controls.append(ft.ElevatedButton("Register", on_click=lambda _: print("Register clicked!")))

        self.cont.controls = [image, LoginPart]