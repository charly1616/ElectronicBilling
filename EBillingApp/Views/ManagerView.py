import flet as ft
 

class ManagerView(ft.View):
    def __init__(self, title: str = "Default Title", controls: list = None, **kwargs):
        super().__init__(route="/login", **kwargs)  # You must provide a `route` for the view
        self.title = title
        self.cont = ft.Row(controls=[], expand=True)
        self.controls = [self.cont]
        self._setup_view()

    def _setup_view(self):
        content = self.cont

        content.controls.append(ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Second",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        ))
        content.controls.append(ft.VerticalDivider(width=1))
        self.controls.insert(0, ft.Text(self.title, size=24, weight="bold"))
        # Add a divider for visual separation
        self.controls.insert(1, ft.Divider())
    
    
    def changePage(p):
        pass