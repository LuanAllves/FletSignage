# 🎬 Flet Signage Player

Sistema de Digital Signage desenvolvido em Python utilizando **Flet**, com foco em reprodução de mídias locais (imagens e vídeos) em loop.

---

## 🚀 Objetivo

Criar uma aplicação multiplataforma para exibição de conteúdos em telas, semelhante a soluções como 4YouSee, porém rodando localmente.

---

## 🛠️ Tecnologias

* Python 3.x
* Flet (UI moderna baseada em Flutter)
* Pathlib (manipulação de arquivos)
* Shutil (cópia de arquivos)

---

## 📂 Estrutura do Projeto

```
FletSignage/
│                     # Ícones e arquivos estáticos
├── src/
│   ├── assets/
│   └── main.py       # Código principal
├── midias/           # (Gerado automaticamente) arquivos enviados
├── pyproject.toml
└── README.md
```

---

## 📦 Funcionalidades atuais

* 📁 Seleção de arquivos (File Picker)
* 💾 Upload de mídias para pasta local
* 📂 Criação automática da pasta `midias`

---

## 🚧 Em desenvolvimento

* 🎞️ Player automático (imagens e vídeos)
* 🔁 Loop de reprodução
* 🧠 Controle de tempo por mídia
* 📱 Layout responsivo (Mobile/Desktop)
* 🌙 Configurações e dashboard

---

## ▶️ Como executar

```bash
pip install flet
flet run src/main.py
```

---

## 📌 Observações

* O sistema salva as mídias em uma pasta local (`midias`)
* Em versões futuras será utilizado `app_storage_path` para compatibilidade multiplataforma

---

## 🧠 Roadmap

* [ ] Listagem de mídias na interface
* [ ] Player com autoplay
* [ ] Suporte a vídeos
* [ ] Configuração via JSON
* [ ] Build para desktop

---

## 🤝 Contribuição

Sinta-se à vontade para contribuir ou sugerir melhorias.

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por Luan Cristian 🚀
