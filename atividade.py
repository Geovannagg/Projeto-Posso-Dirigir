#Meu projeto
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("Verificação de habilitação")
janela.geometry("400x200")

def verificar_habilitacao():
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if not nome or not idade:
        messagebox.showwarning("Campos vazios.", "Preencha os espaços.")

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showwarning("Erro", "A idade precisa ser um número inteiro.")
        return

    if idade >= 18:
        resultado.configure(text=f"{nome}, você pode dirigir!", text_color="purple")
    else:
        resultado.configure(text=f"{nome}, você não pode dirigir.", text_color="yellow")

label_nome = ctk.CTkLabel(janela, text="Informe seu nome")
label_nome.pack()
entrada_nome = ctk.CTkEntry(janela, width=200)
entrada_nome.pack(pady=20)


label_idade = ctk.CTkLabel(janela, text="Informe sua idade")
label_idade.pack()
entrada_idade = ctk.CTkEntry(janela, width=200)
entrada_idade.pack(pady=20)


botao = ctk.CTkButton(janela, text="Analisar", command=verificar_habilitacao)
botao.pack(pady=10)


resultado = ctk.CTkLabel(janela, text="")
resultado.pack(pady=10)

janela.mainloop()

