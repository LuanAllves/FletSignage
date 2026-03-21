from pathlib import Path
import shutil
import flet as ft
import os


allowed_files = ['png', 'jpg', 'jpeg', 'webp', 'svg', 'gif', 'mp4', 'avi', 'mkv']
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