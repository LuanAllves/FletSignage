import flet as ft
from components.widgets import create_title
from core.upload_files import select_files
from core.monitor import get_real_monitors


monitors = get_real_monitors()
monitor_radios = ft.RadioGroup(
    content=ft.Column([ft.Radio(value=str(m['id']), label=m['name']) for m in monitors])
)

ferramentas = ft.Column(
    controls = [
        ft.Divider(height = 10, color='transparent'),
        ft.Row(
            alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                # Botoes de Play, Pause e Pare
                ft.IconButton(icon=ft.Icons.PLAY_ARROW),
                ft.IconButton(icon=ft.Icons.PAUSE),
                ft.IconButton(icon=ft.Icons.STOP),
            ]
        )
    ]
)

configuracoes = ft.Column(
    expand = 1,
    height = 500,
    controls = [
        ft.Divider(height = 10, color='transparent'),
        create_title("CONFIGURACOES", 20),
        ft.TextField(
            label="Playlist Externa",
            hint_text="exemple.com/playlist/",
            border=ft.InputBorder.UNDERLINE, 
            prefix="https://",
            focused_border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
            border_color = ft.Colors.SURFACE_TINT,
            hint_style = ft.TextStyle(color = ft.Colors.GREY),
            prefix_style = ft.TextStyle(color = ft.Colors.LIGHT_BLUE_ACCENT_400),
        ),
        ft.Button("UPLOAD FILES", on_click=select_files),
        ft.Divider(),
        create_title("Telas Disponiveis", 17),
        monitor_radios,
    ],
    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
)

playlist = ft.Column(
    height = 500,
    expand = 2,
    controls = [
        ft.Divider(height = 10, color='transparent'),
        create_title("PLAYLIST", 20),
    ],
    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
)

propriedades = ft.Column(
    height = 500,
    expand = 1,
    controls = [
        ft.Divider(height = 10, color='transparent'),
        create_title("PROPRIEDADES", 20),

    ],
    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
)

dashboard = ft.Column(
    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
    controls = [
        create_title("Signage Player", 30),
        ferramentas,
        ft.Row(
            alignment = ft.MainAxisAlignment.SPACE_AROUND,
            controls = [
                configuracoes,
                playlist,
                propriedades,
            ]
        )
    ]
)

