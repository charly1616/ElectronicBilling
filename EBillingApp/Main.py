import flet as ft
from Views.LoginView import LoginView
from Views.RegisterView import RegisterView
from Views.ManagerView import ManagerView
from Views.EmployeeView import EmployeeView

def main(page: ft.Page):
    page.window_width = 900
    page.window_height = 600
    loginView = LoginView(title="Login Page")
    registerView = RegisterView(title="Register Page")
    managerView = ManagerView(title="Manager")
    employeeView = EmployeeView()

    page.route = "Manager"
    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list
    
    def route_change(e):
        routeList = get_route_list(page.route)

        page.views.clear()
        page.views.append(loginView)

        if len(routeList) == 0:
            page.update()
            return
        
        if routeList[0] == "Register":
            page.views.append(registerView)
        elif routeList[0] == "Manager":
            page.views.append(managerView)
            if len(routeList) == 2:
                managerView.changePage(routeList[1])
        elif routeList[0] == "Employee":
            page.views.append(employeeView)
            
        
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main)