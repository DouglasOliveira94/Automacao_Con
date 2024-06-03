import tkinter as tk
from tkinter import messagebox
def perguntar_se_prossegue(mensagem):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    resposta = messagebox.askyesno("Prosseguir", mensagem)
    root.destroy()
    return resposta
def informar_usuario(mensagem):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Informação", mensagem)
    root.destroy()
