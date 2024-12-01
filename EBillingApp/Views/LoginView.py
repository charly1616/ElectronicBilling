import flet as ft
import DBManager as db

class LoginView(ft.View):
    def __init__(self, title: str = "Default Title", controls: list = None, **kwargs):
        super().__init__(route="/login", **kwargs)  # You must provide a `route` for the view
        self.title = title
        self.route = "/Register"
        self.cont = ft.Row(controls=[])
        self.controls = [self.cont]
        self._setup_view()

    def iniciarSesion(self):
        userid = db.findUser(self.email.value,self.password.value)
        if userid != -1:
            db.empresa_id = db.findUserCompany(userid)
            db.userLogged = userid
            if db.isUserManager(userid):
                self.page.go("/Manager")
            else:
                self.page.go("/Employee")

    def _setup_view(self):
        self.email = ft.TextField(label="Email")
        self.password = ft.TextField(label="Contraseña", password=True)

        image = ft.Container(height=380,width=380,bgcolor=ft.colors.WHITE)
        LoginPart = ft.Column()
        LoginPart.controls.append(ft.Text("E-FacturaNet", size=24))
        LoginPart.controls.append(self.email)
        LoginPart.controls.append(self.password)
        LoginPart.controls.append(ft.ElevatedButton("Iniciar Sesión", on_click=lambda _: self.iniciarSesion()))
        LoginPart.controls.append(ft.ElevatedButton("Crear cuenta", on_click=lambda _: self.page.go("/Register")))

        self.cont.controls = [image, LoginPart]