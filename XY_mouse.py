import tkinter as tk
import pyautogui

def update_coordinates():
    # Obtém as coordenadas do mouse
    x, y = pyautogui.position()
    
    # Atualiza o texto na label
    label.config(text=f"X: {x}, Y: {y}")
    
    # Agendando a função para ser chamada novamente após 100ms
    root.after(100, update_coordinates)

# Criando a janela principal
root = tk.Tk()
root.title("Coordenadas do Mouse")

# Definindo a janela como sempre visível
root.wm_attributes("-topmost", 1)

# Criando uma label para mostrar as coordenadas
label = tk.Label(root, font=("Arial", 14))
label.pack(padx=10, pady=10)

# Chamando a função para atualizar as coordenadas
update_coordinates()

# Executando o loop principal da aplicação
root.mainloop()
