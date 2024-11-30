import flet as ft
from . import BillingModel

def showBill():
    def bill(page: ft.Page):
        page.controls = [ft.Container(bgcolor=ft.colors.WHITE)]
    ft.app(bill)

