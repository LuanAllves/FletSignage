import flet as ft
from components.widgets import create_title
from core.actions import (handle_switch_change, get_real_monitors, select_files, list_files, start_file_monitor)


monitors = get_real_monitors()
monitor_radios = ft.RadioGroup(
    content=ft.Column([ft.Radio(value=str(m['id']), label=m['name']) for m in monitors])
)


file_id = "ID"
file_name = "NAME"
start_of_playback = "DD/MM/AAAA"
end_of_playback = "DD/MM/AAAA"
file_time = 0

lista_midias = ft.ListView(
    expand = True,
    spacing = 10,
    padding = 10,
)


def section_tools(page: ft.Page, prop_view):

    # Botão de Refresh Manual
    btn_refresh = ft.IconButton(
        icon=ft.Icons.REFRESH,
        tooltip="Forçar atualização",
        on_click=lambda _: list_files(lista_midias, prop_view, force=True)
    )

    start_file_monitor(lista_midias, prop_view)

    return ft.Column(
        controls = [
            ft.Divider(height = 10, color='transparent'),
            ft.Row(
                alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    ft.Container(
                        bgcolor = ft.Colors.SURFACE_CONTAINER_LOWEST,
                        border = ft.Border.all(2, color=ft.Colors.LIGHT_BLUE_ACCENT_400),
                        border_radius = 15,
                        width = 400,
                        padding = 10,
                        content = ft.Row(
                            alignment = ft.CrossAxisAlignment.CENTER,
                            controls = [
                                ft.Row(
                                    expand = True,
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    controls = [
                                        ft.IconButton(icon=ft.Icons.PLAY_ARROW),
                                        ft.IconButton(icon=ft.Icons.PAUSE),
                                        ft.IconButton(icon=ft.Icons.STOP),
                                    ]
                                ),
                                btn_refresh,
                                ft.Switch(
                                    thumb_icon=ft.Icons.DARK_MODE,
                                    on_change=lambda e: handle_switch_change(page, e)
                                ),
                            ]
                        )
                    ),
                    
                ]
            )
        ]
    )

def section_config(page:ft.Page):
    return ft.Column(
        expand = 1,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            ft.Divider(height = 10, color='transparent'),
            create_title("CONFIGURACOES", 20),
            ft.Container(
                expand = True,
                bgcolor = ft.Colors.SURFACE_CONTAINER_LOWEST,
                border_radius = 10,
                border = ft.Border.all(2, ft.Colors.LIGHT_BLUE_ACCENT_400),
                padding = 20,
                content = ft.Row(
                    expand = True,
                    controls = [
                        ft.Column(
                            expand = True,
                            controls = [
                                ft.TextField(
                                    label="Playlist Externa",
                                    hint_text="exemple.com/playlist/",
                                    #border=ft.InputBorder.UNDERLINE, 
                                    prefix="https://",
                                    focused_border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
                                    border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
                                    hint_style = ft.TextStyle(color = ft.Colors.GREY),
                                    prefix_style = ft.TextStyle(color = ft.Colors.LIGHT_BLUE_ACCENT_400),
                                ),
                                ft.Button("UPLOAD FILES", on_click=select_files),
                                ft.Divider(height=20, color=ft.Colors.WHITE),
                                create_title("Telas Disponiveis", 17),
                                monitor_radios,
                            ]
                        )
                    ]
                ) 
            )
        ],
    )

def section_playlist(page:ft.Page, prop_view):

    list_files(lista_midias, prop_view)

    return ft.Column(
        expand = 2,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            ft.Divider(height = 10, color='transparent'),
            create_title("PLAYLIST", 20),
            ft.Container(
                expand = True,
                bgcolor = ft.Colors.SURFACE_CONTAINER_LOWEST,
                border_radius = 10,
                border = ft.Border.all(2, ft.Colors.LIGHT_BLUE_ACCENT_400),
                padding = 20,
                content = ft.Row(
                    expand = True,
                    alignment = ft.MainAxisAlignment.SPACE_AROUND,
                    align = ft.Alignment.TOP_CENTER,
                    controls = [
                        lista_midias,
                    ]
                )
            ),
        ],
    )

def section_properties(page:ft.Page):
    return ft.Column(
        expand = 1,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            ft.Divider(height = 10, color='transparent'),
            create_title("PROPRIEDADES", 20),
            ft.Container(
                expand = True,
                bgcolor = ft.Colors.SURFACE_CONTAINER_LOWEST,
                border_radius = 10,
                border = ft.Border.all(2, ft.Colors.LIGHT_BLUE_ACCENT_400),
                padding = 20,
                content = ft.Row(
                    expand = True,
                    controls = [
                        ft.Column(
                            expand = True,
                            controls = [
                                ft.TextField(label="Nome do Arquivo", value="NONE"),
                                ft.Row(
                                    alignment = ft.MainAxisAlignment.SPACE_AROUND,
                                    controls = [
                                        ft.Text(f"Tipo: NONE"),
                                        ft.Text(f"Tamanha: 00 MB"),
                                    ]
                                ),
                                ft.Divider(height=20, color=ft.Colors.WHITE),
                                ft.Text("Configuracao de Exibicao: ", color=ft.Colors.LIGHT_BLUE_ACCENT_400, size=17),
                                ft.Text("Duracao: ", color=ft.Colors.LIGHT_BLUE_ACCENT_400, size=12),
                                ft.TextField(label="Duracao (segundos)", value="10",),
                                ft.Text("Validae: ", color=ft.Colors.LIGHT_BLUE_ACCENT_400, size=12),
                                ft.TextField(label="Inicio (DD/MM/AAAA)", value="00/00/0000"),
                                ft.TextField(label="Fim (DD/MM/AAAA)", value="00/00/0000"),
                            ]
                        )
                    ]
                )
            )
        ],
    )

def section_footer(page:ft.Page):
    return ft.Row(
        controls = [
            ft.Container(
                expand = True,
                padding = 20,
                content = ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        ft.Text("Esse e o FOOTER!..."),
                    ]
                )
            )
        ]
    )

def dashboard(page: ft.Page):

    col_properties = section_properties(page)
    col_playlist = section_playlist(page, col_properties)
    col_tools = section_tools(page, col_properties)

    return ft.Column(
        expand = True,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            create_title("Signage Player", 30),
            col_tools,
            ft.Row(
                expand = True,
                spacing = 20,
                controls = [
                    section_config(page),
                    col_playlist,
                    col_properties,
                ]
            ),
            section_footer(page),
        ]
    )

def init_dashboard(page: ft.Page):
    return dashboard(page)

