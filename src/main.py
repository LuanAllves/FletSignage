import flet as ft
import os
from pathlib import Path
import platform
from gui.desktop import dashboard as desktop_dashboard
from gui.mobile import dashboard as mobile_dashboard


os_is_desktop = True if str.lower(platform.system()) in ["windows", "linux", "darwin"] else False


async def main(page: ft.Page):

    # === Configuracoes de Janela ===
    page.title = "Signage Player"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.min_width = 600
    page.window.min_height = 500
    page.window.max_width = 1366
    page.window.max_height = 768

    dashboard = desktop_dashboard if os_is_desktop else mobile_dashboard

    page.add(dashboard)


ft.run(main, assets_dir="assets")
