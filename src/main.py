import flet as ft
import os
from pathlib import Path
import platform
from gui.desktop import init_dashboard as desktop_dashboard
from gui.mobile import init_dashboard as mobile_dashboard


os_is_desktop = True if str.lower(platform.system()) in ["windows", "linux", "darwin"] else False


async def main(page: ft.Page):

    # === Configuracoes de Janela ===
    page.title = "Signage Player"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.min_width = 768
    page.window.maximized = True

    dashboard = desktop_dashboard(page) if os_is_desktop else mobile_dashboard(page)

    page.add(dashboard)


ft.run(main)
