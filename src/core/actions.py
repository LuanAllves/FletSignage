import flet as ft
import wmi
from pathlib import Path
import shutil
import flet as ft
import os
import threading
import time
import datetime


movie_files = ['gif', 'mp4', 'avi', 'mkv', 'mov']
image_files = ['png', 'jpg', 'jpeg', 'webp', 'svg']
allowed_files = ['png', 'jpg', 'jpeg', 'webp', 'svg', 'gif', 'mp4', 'avi', 'mkv', 'mov']
PASTA_MIDIAS = "src/data/uploads"

# === Funcao para UPLOAD de ARQUIVOS ===
async def select_files(e):
    os.makedirs(PASTA_MIDIAS, exist_ok=True)
    file_picker = ft.FilePicker()
    resultado = await file_picker.pick_files(
        allow_multiple=True,
        allowed_extensions = allowed_files,
    )

    if resultado:
        for arquivo in resultado:
            if arquivo.path:
                origem = Path(arquivo.path)
            destino = Path(PASTA_MIDIAS) / arquivo.name

            try:
                shutil.copy(origem, destino)
                print(f"Salvo em: {destino}")
            except Exception as err:
                print(f"Erro: {err}")


def get_real_monitors():
    try:
        obj_wmi = wmi.WMI(namespace="root\\wmi")
        monitors_id = obj_wmi.WmiMonitorID(Active=True)
        
        monitor_list = []
        for i, m in enumerate(monitors_id):
            model_name = "".join([chr(x) for x in m.UserFriendlyName if x != 0])
            if not model_name:
                model_name = f"Monitor {i+1}"
            monitor_list.append({"id": i, "name": model_name})
        return monitor_list
    except Exception:
        return []


def handle_switch_change(page, e: ft.Event[ft.Switch]):
    if page.theme_mode == ft.ThemeMode.DARK:
        page.theme_mode = ft.ThemeMode.LIGHT
        e.control.thumb_icon = ft.Icons.LIGHT_MODE
    else:
        e.control.thumb_icon = ft.Icons.DARK_MODE
        page.theme_mode = ft.ThemeMode.DARK
    page.update()


_last_files_cache = []

def list_files(playlist_view: ft.ListView, properties, force=False):
    global _last_files_cache
    path = PASTA_MIDIAS
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    arquivos = sorted(os.listdir(path))
    
    # Só atualiza se a lista de arquivos mudou ou se for um "force refresh"
    if arquivos == _last_files_cache and not force:
        return 

    _last_files_cache = arquivos
    playlist_view.controls.clear()
    
    for arquivo in arquivos:
        if os.path.isdir(os.path.join(path, arquivo)):
            continue
            
        ext = arquivo.lower().split(".")[-1]
        icone = ft.Icons.INSERT_DRIVE_FILE
        cor = ft.Colors.GREY_400
        
        if ext in image_files:
            icone = ft.Icons.IMAGE
            cor = ft.Colors.ORANGE_ACCENT
        elif ext in movie_files:
            icone = ft.Icons.MOVIE
            cor = ft.Colors.BLUE_ACCENT

        playlist_view.controls.append(
            ft.ListTile(
                leading=ft.Icon(icone, color=cor),
                title=ft.Text(arquivo, size=14, weight="w500", overflow=ft.TextOverflow.ELLIPSIS),
                subtitle=ft.Text(f"Tipo: {ext.upper()}", size=11),
                on_click=lambda e, a=arquivo, p=properties: display_file_propeties(e, playlist_view.page, a, p)
            )
        )
    
    try:
        if playlist_view.page is not None:
            playlist_view.update()
    except Exception:
        pass

def start_file_monitor(playlist_view: ft.ListView, prop_view):
    """Função que roda em loop infinito em segundo plano"""
    def monitor():
        while True:
            list_files(playlist_view, prop_view)
            time.sleep(5) # Verifica a cada 5 segundos
            
    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()


def display_file_propeties(e, page:ft.Page, name_file:str, prop_column:ft.Column):
    ext = name_file.lower().split(".")[-1]
    caminho_completo = os.path.join(PASTA_MIDIAS, name_file)

    size_mb = os.path.getsize(caminho_completo) / (1024 * 1024)

    page.snack_bar = ft.SnackBar(ft.Text(f"Selecionado: {name_file}"))

    txt_inicio = ft.TextField(
        label = "Inicio (DD/MM/AAAA)",
        value = "00/00/0000",
        expand = True,
        focused_border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
        border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
    )
    txt_fim = ft.TextField(
        label = "Fim (DD/MM/AAAA)",
        value = "00/00/0000",
        expand = True,
        focused_border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
        border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
    )
    picker_inicio = configurar_calendario(page, txt_inicio)
    picker_fim = configurar_calendario(page, txt_fim)

    txt_inicio.suffix = ft.IconButton(
        icon = ft.Icons.CALENDAR_MONTH,
        on_click = lambda e: abrir_calendario(e, picker_inicio, page)
    )
    txt_fim.suffix = ft.IconButton(
        icon = ft.Icons.CALENDAR_MONTH,
        on_click = lambda e: abrir_calendario(e, picker_fim, page)
    )

    details = ft.Row(
        expand = True,
        controls = [
            ft.Column(
                scroll = ft.ScrollMode.ADAPTIVE,
                expand = True,
                controls = [
                    ft.Divider(height=3, color='transparent'),
                    ft.TextField(
                        label="Nome do Arquivo", 
                        value=name_file, 
                        focused_border_color=ft.Colors.LIGHT_BLUE_ACCENT_400,
                        border_color = ft.Colors.LIGHT_BLUE_ACCENT_400,
                        multiline = True,
                    ),
                    ft.ResponsiveRow(
                        alignment = ft.MainAxisAlignment.SPACE_AROUND,
                        controls = [
                            ft.Text(f"Tipo: {ext.upper()}"),
                            ft.Text(f"Tamanha: {size_mb:.2f} MB"),
                        ]
                    ),
                    ft.Divider(height=20, color=ft.Colors.WHITE),
                    ft.Text("Configuracao de Exibicao: ", color=ft.Colors.LIGHT_BLUE_ACCENT_400, size=17),
                    ft.Text("Duracao: ", color=ft.Colors.LIGHT_BLUE_ACCENT_400, size=12),
                    ft.TextField(label="Duracao (segundos)", value="10", width=150, focused_border_color=ft.Colors.LIGHT_BLUE_ACCENT_400, border_color = ft.Colors.LIGHT_BLUE_ACCENT_400),
                    ft.Text("Validae: ", color=ft.Colors.LIGHT_BLUE_ACCENT_400, size=12),
                    txt_inicio,
                    txt_fim,
                    ft.Divider(color=ft.Colors.WHITE),
                    ft.ResponsiveRow(
                        expand = True,
                        alignment = ft.MainAxisAlignment.CENTER,
                        align = ft.Alignment.BOTTOM_CENTER,
                        controls = [
                            ft.Button(
                                "SALVAR ALTERAÇÕES", 
                                icon=ft.Icons.SAVE_AS, 
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                on_click=lambda _: print("Salvando no JSON/Banco...") # Próximo passo!
                            ),
                            
                            ft.OutlinedButton(
                                "REMOVER MÍDIA", 
                                icon=ft.Icons.DELETE_FOREVER,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                on_click=lambda _: print("Deletando arquivo...")
                            )
                        ]
                    ),
                ]
            ),
        ]
    )
    prop_column.controls[2].content = details
    page.snack_bar.open = True
    prop_column.update()
    page.update()


def configurar_calendario(page: ft.Page, target_textfield: ft.TextField):

    def handle_change(e):
        if e.control.value:
            data_formatada = e.control.value.strftime("%d/%m/%Y/")
            target_textfield.value = data_formatada
            target_textfield.update()

    date_picker = ft.DatePicker(
        on_change = handle_change,
        first_date = datetime.datetime(2024, 1, 1),
        last_date = datetime.datetime(2030, 12, 31),
    )

    page.overlay.append(date_picker)
    page.update()

    return date_picker

def abrir_calendario(e, date_picker, page):
    page.show_dialog(date_picker)
