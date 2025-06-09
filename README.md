# MascoteApp

Mantenha-se ativo no Teams!  
Este aplicativo simula atividade no computador para evitar que o status fique como "ausente" em aplicativos como o Microsoft Teams.

## Funcionalidades

- Mascote animado (GIF) exibido na interface.
- Movimenta o mouse e pressiona teclas periodicamente.
- Permite configurar o intervalo entre ações.
- Emite som opcional a cada ciclo.
- **Registra todos os eventos do usuário e da aplicação em um arquivo de log (`cycle_log.txt`).**
- Interface gráfica fixa, com ícone personalizado.

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `pillow`, `pyautogui`

## Instalação

1. Clone este repositório ou baixe os arquivos.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Certifique-se de que o arquivo `mascote.gif` e (opcionalmente) `mascote.ico` estejam na mesma pasta do script.

## Uso

Execute o aplicativo com:
```
python mascote.py
```

- Defina o intervalo desejado (em segundos).
- Clique em "Ativar" para iniciar o ciclo.
- O mascote animado será exibido e as ações automáticas começarão.
- **Todas as ações do usuário (ativar/desativar, alternar som, etc.) e eventos da aplicação são registrados em `cycle_log.txt`.**
- O arquivo de log é criado automaticamente na mesma pasta do script, caso não exista.

## Como gerar um executável para Windows

Você pode criar um executável do MascoteApp usando o [PyInstaller](https://pyinstaller.org/):

1. Instale o PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Gere o executável com o comando:
   ```
   pyinstaller --onefile --windowed --icon=mascote.ico mascote.py
   ```
   - O parâmetro `--onefile` cria um único arquivo `.exe`.
   - O parâmetro `--windowed` faz com que o executável seja criado **sem abrir o console** ao ser executado.
   - O parâmetro `--icon=mascote.ico` define o ícone do executável (opcional).

3. O executável será criado na pasta `dist`. Certifique-se de copiar também o arquivo `mascote.gif` para a mesma pasta do `.exe` gerado.

## Observações
- O aplicativo foi desenvolvido para ser simples e fácil de usar.
- A animação do mascote é um GIF que deve ser colocado na mesma pasta do script.
- O movimento do mouse e o pressionamento de teclas podem ser ajustados no código conforme necessário.
- O ícone da janela pode ser alterado substituindo o arquivo `mascote.ico`.
- Para uso no Windows.

---

**Autor:** Christian Vladimir Uhdre Mulato  
**Data:** Campo Largo, segunda-feira, 09 de Junho de 2025.