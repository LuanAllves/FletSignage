import flet as ft
import os
import shutil
from pathlib import Path
PASTA_MIDIAS = "midias"  # Por enquanto, depois mudar para algo melhor

async def main(page: ft.Page):
    page.title = "WL Signage Digital Player"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    titulo = ft.Text(
        value="Signage Player",
        size=30,
        weight=ft.FontWeight.BOLD,
        )
    
    def titulo_secao(texto: str):
        return ft.Text(
            value=texto,
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_ACCENT,
            italic=True
        )

    # Criar pasta se não existir
    os.makedirs(PASTA_MIDIAS, exist_ok=True)

    file_picker = ft.FilePicker()

    async def selecionar_arquivos(e):
        resultado = await file_picker.pick_files(
            allow_multiple=True
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

    btn = ft.Button(
        "Selecionar arquivos",
        on_click=selecionar_arquivos
    )

    page.add(
        ft.Column(
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls=[
                titulo,
                ft.Row(
                    alignment = ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Column(
                            controls=[
                                titulo_secao("Ferramentas"), 
                            ]
                        ),
                        ft.Column(
                            controls=[
                                titulo_secao("Playlist Miniatura"),
                            ]
                        ),
                        ft.Column(
                            controls=[
                                titulo_secao("Propriedades"),
                            ]
                        ),

                    ]
                )
            ]
        )
    )

ft.run(main, assets_dir="assets")