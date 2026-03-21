import flet as ft


def create_title(value: str, size: int = 20):
    return ft.Text(
        value=value, 
        size=size, 
        weight=ft.FontWeight.BOLD
    )