
import flet as ft
 

class EmployeeView(ft.View):
    def __init__(self, title: str = "Default Title", controls: list = None, **kwargs):
        super().__init__(route="/login", **kwargs)  # You must provide a `route` for the view
        self.title = title
        self.controls = controls if controls else []
        self._setup_view()

    def _setup_view(self):
        # Add a title at the top
        self.controls.insert(0, ft.Text(self.title, size=24, weight="bold"))
        # Add a divider for visual separation
        self.controls.insert(1, ft.Divider())