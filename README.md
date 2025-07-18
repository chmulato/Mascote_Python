# MascoteApp

Mantenha-se ativo no Teams!  
Este aplicativo simula atividade no computador para evitar que o status fique como "ausente" em aplicativos como o Microsoft Teams.

## Funcionalidades

 Permite configurar o intervalo entre ações.
 Emite som opcional a cada ciclo.
 **Registra todos os eventos do usuário e da aplicação em um arquivo de log (`cycle_log.txt`).**
 Interface gráfica simples e objetiva.
+- Movimenta o mouse e pressiona teclas periodicamente.
- Permite configurar o intervalo entre ações.
- Emite som opcional a cada ciclo.
- **Registra todos os eventos do usuário e da aplicação em um arquivo de log (`cycle_log.txt`).**
- Interface gráfica simples e objetiva.

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `pillow`, `pyautogui`

## Instalação

1. Clone este repositório ou baixe os arquivos.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. (Opcional) Para ativar o som, certifique-se de que seu sistema está com áudio habilitado.

## Uso

Execute o aplicativo com:

```bash
python mascote.py
```


## Como gerar um executável para Windows

Você pode criar um executável do MascoteApp usando o [PyInstaller](https://pyinstaller.org/):

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Gere o executável com o comando:

```bash
pyinstaller --onefile --windowed mascote.py
```

- O parâmetro `--onefile` cria um único arquivo `.exe`.
- O parâmetro `--windowed` faz com que o executável seja criado **sem abrir o console** ao ser executado.

1. O executável será criado na pasta `dist`.

## Observações

---

**Autor:** Christian Vladimir Uhdre Mulato  
**Data:** Campo Largo, segunda-feira, 09 de Junho de 2025.
+
## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.