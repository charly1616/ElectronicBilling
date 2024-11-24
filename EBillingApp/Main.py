import flet as ft
from Views.LoginView import LoginView
from Views.RegisterView import RegisterView
from Views.ManagerView import ManagerView
from Views.EmployeeView import EmployeeView

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 500
    loginView = LoginView(title="Login Page")
    registerView = ft.View()

    
    def route_change(e):
        page.views.clear()
        page.views.append(loginView)
        if page.route == "/Register":
            page.views.append(registerView)
        elif page.route == "/Manager":
            page.views.append(registerView)
        elif page.route == "/Employee":
            page.views.append(registerView)
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main)