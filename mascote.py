"""
MascoteApp - Mantenha-se ativo no Teams

Este aplicativo simula atividade no computador para evitar status "ausente" em aplicativos como o Microsoft Teams.
Funcionalidades:
- Mascote animado (GIF) exibido na interface.
- Movimenta o mouse e pressiona teclas periodicamente.
- Permite configurar o intervalo entre ações.
- Emite som opcional a cada ciclo.
- Registra cada ciclo em um arquivo de log (cycle_log.txt).
- Interface gráfica fixa, com ícone personalizado.

Requisitos:
- Python 3.x
- Bibliotecas: tkinter, pillow, pyautogui

Autor: Christian Vladimir Uhdre Mulato
Data: Campo Largo, segunda-feira, 09 de Junho de 2025.
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui
import subprocess
import datetime
import os
from PIL import Image, ImageTk

class MascoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Move Mascote")
        self.running = False
        self.interval = 5
        self.remaining = 5
        self.cycle_count = 0

        # Garante que o arquivo de log exista
        if not os.path.exists("cycle_log.txt"):
            with open("cycle_log.txt", "w", encoding="utf-8") as f:
                f.write("Log de ciclos iniciado.\n")

        # Mascote animado
        self.frames = []
        try:
            gif = Image.open("mascote.gif")
            for frame in range(0, getattr(gif, "n_frames", 1)):
                gif.seek(frame)
                frame_image = ImageTk.PhotoImage(gif.copy())
                self.frames.append(frame_image)
        except Exception as e:
            print("Erro ao carregar mascote.gif:", e)
            self.frames = []

        self.img_label = tk.Label(root)
        self.img_label.pack()
        self.current_frame = 0
        if self.frames:
            self.animate_gif()

        # Interface
        self.lbl_intervalo = tk.Label(root, text="Intervalo (segundos):")
        self.lbl_intervalo.pack()
        self.edt_intervalo = tk.Entry(root)
        self.edt_intervalo.insert(0, "300")
        self.edt_intervalo.pack()
        self.lbl_contagem = tk.Label(root, text="Proximo movimento em: 0")
        self.lbl_contagem.pack()
        self.lbl_ciclos = tk.Label(root, text="Ciclos executados: 0")
        self.lbl_ciclos.pack()
        self.chk_som_var = tk.BooleanVar()
        self.chk_som = tk.Checkbutton(root, text="Som", variable=self.chk_som_var, command=self.on_toggle_sound)
        self.chk_som.pack()
        self.btn_desativar = tk.Button(root, text="Ativar", command=self.toggle)
        self.btn_desativar.pack()

        self.timer_thread = None

        # Loga inicialização
        self.log_event("Aplicação iniciada.")

    def log_event(self, mensagem):
        log_line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} - EVENTO: {mensagem}"
        with open("cycle_log.txt", "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

    def animate_gif(self):
        if self.frames:
            self.img_label.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(100, self.animate_gif)

    def toggle(self):
        if self.running:
            self.running = False
            self.btn_desativar.config(text="Ativar")
            self.log_event("Ciclo desativado pelo usuário.")
        else:
            try:
                self.interval = int(self.edt_intervalo.get())
            except ValueError:
                self.interval = 5
            if self.interval < 1:
                self.interval = 5
            self.remaining = self.interval
            self.cycle_count = 0
            self.lbl_ciclos.config(text="Ciclos executados: 0")
            self.running = True
            self.btn_desativar.config(text="Desativar")
            self.log_event(f"Ciclo ativado pelo usuário. Intervalo: {self.interval} segundos.")
            self.start_timer()

    def on_toggle_sound(self):
        if self.chk_som_var.get():
            self.log_event("Som ativado pelo usuário.")
        else:
            self.log_event("Som desativado pelo usuário.")

    def start_timer(self):
        def run():
            while self.running:
                self.lbl_contagem.config(text=f"Proximo movimento em: {self.remaining}")
                if self.remaining <= 0:
                    self.move_mouse()
                    self.press_key()
                    self.click_on_teams_icon()
                    self.keep_teams_active()
                    if self.chk_som_var.get():
                        self.root.bell()
                    self.cycle_count += 1
                    self.lbl_ciclos.config(text=f"Ciclos executados: {self.cycle_count}")
                    self.log_cycle_count()
                    self.log_event("Ciclo automático executado.")
                    self.remaining = self.interval
                else:
                    self.remaining -= 1
                time.sleep(1)
        self.timer_thread = threading.Thread(target=run, daemon=True)
        self.timer_thread.start()

    def move_mouse(self):
        x, y = pyautogui.position()
        if x % 2 == 0:
            pyautogui.moveTo(x + 50, y + 50)
        else:
            pyautogui.moveTo(x - 50, y - 50)

    def press_key(self):
        # F15 pode não existir, use outra tecla se necessário
        pyautogui.press('f15')

    def click_on_teams_icon(self):
        # Ajuste a posição conforme necessário para o seu Teams
        pyautogui.moveTo(50, 1050)
        pyautogui.click()

    def keep_teams_active(self):
        # Envia Scroll Lock multiplataforma usando pyautogui
        try:
            pyautogui.press('scrolllock')
            self.log_event("Scroll Lock enviado via pyautogui.")
        except Exception as e:
            self.log_event(f"Falha ao enviar Scroll Lock: {e}")

    def log_cycle_count(self):
        log_line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} - Total de ciclos: {self.cycle_count}"
        with open("cycle_log.txt", "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

if __name__ == "__main__":
    # Constantes de layout para facilitar futuros ajustes
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 520

    root = tk.Tk()
    root.iconbitmap("mascote.ico")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # Tamanho fixo da janela
    root.resizable(False, False)  # Impede redimensionamento
    app = MascoteApp(root)
    root.mainloop()
