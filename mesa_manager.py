import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

class GerenciamentoMesas:
    def __init__(self):
        self.janela_inicial = None
        self.janela_principal = None
        self.mesas = {i: "Livre" for i in range(1, 11)}
        self.mostrar_tela_inicial()

    def mostrar_tela_inicial(self):
        self.janela_inicial = tk.Tk()
        self.janela_inicial.title("Gerenciamento de Mesas - Restaurante São Miguel BY: Lucas Santana")

        # imagem do estabelecimento
        try:
            imagem_logo = Image.open("logo.png")
            imagem_logo = imagem_logo.resize((800, 600), Image.Resampling.LANCZOS)
            imagem_logo_tk = ImageTk.PhotoImage(imagem_logo)
            tk.Label(self.janela_inicial, image=imagem_logo_tk).pack()
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        tk.Label(self.janela_inicial, text="Gerenciamento de Mesas - Restaurante São Miguel", font=("Helvetica", 24)).pack(pady=20)
        
        entrar_btn = tk.Button(self.janela_inicial, text="Entrar", command=self.abrir_tela_principal, font=("Helvetica", 16), bg="blue", fg="white")
        entrar_btn.pack(pady=10)
        
        links_frame = tk.Frame(self.janela_inicial)
        links_frame.pack(pady=10)

        desenvolvedor_label = tk.Label(links_frame, text="Desenvolvido por Lucas Santana", font=("Helvetica", 12))
        desenvolvedor_label.pack()

        #GITHUB

        github_label = tk.Label(links_frame, text="GitHub: https://github.com/lLucasSantana", font=("Helvetica", 12), fg="blue", cursor="hand2")
        github_label.pack()
        github_label.bind("<Button-1>", lambda e: self.abrir_link("https://github.com/lLucasSantana"))
        
        # LINKEDIN 

        linkedin_label = tk.Label(links_frame, text="LinkedIn: https://www.linkedin.com/in/llucassantana/", font=("Helvetica", 12), fg="blue", cursor="hand2")
        linkedin_label.pack()
        linkedin_label.bind("<Button-1>", lambda e: self.abrir_link("https://www.linkedin.com/in/llucassantana/"))

        self.janela_inicial.mainloop()

    def abrir_tela_principal(self):
        self.janela_inicial.destroy()
        self.janela_principal = tk.Tk()
        self.janela_principal.title("Gerenciamento de Mesas - Restaurante São Miguel BY: Lucas Santana")

        tk.Label(self.janela_principal, text="Tela Principal", font=("Helvetica", 24)).pack(pady=20)

        voltar_btn = tk.Button(self.janela_principal, text="Voltar para Login", command=self.voltar_para_login, font=("Helvetica", 12), bg="red", fg="white")
        voltar_btn.pack(pady=10, anchor="ne", padx=10)

        self.criar_botoes_mesas()

        self.janela_principal.mainloop()

    def voltar_para_login(self):
        self.janela_principal.destroy()
        self.mostrar_tela_inicial()

    def abrir_link(self, url):
        webbrowser.open(url)

    def criar_botoes_mesas(self):
        mesas_frame = tk.Frame(self.janela_principal)
        mesas_frame.pack(pady=20)

        for i in range(1, 11):
            botao = tk.Button(mesas_frame, text=f"Mesa {i} - {self.mesas[i]}", command=lambda mesa=i: self.gerenciar_mesa(mesa), font=("Helvetica", 14), width=20, bg="green" if self.mesas[i] == "Livre" else "red", fg="white")
            botao.grid(row=(i - 1) // 5, column=(i - 1) % 5, padx=10, pady=10)

    def gerenciar_mesa(self, mesa):
        status_atual = self.mesas[mesa]
        
        if status_atual == "Livre":
            novo_status = "Fechada"
            cor = "red"
        else:
            novo_status = "Livre"
            cor = "green"
        
        self.mesas[mesa] = novo_status
        self.atualizar_botoes_mesas()

    def atualizar_botoes_mesas(self):
        for widget in self.janela_principal.winfo_children():
            if isinstance(widget, tk.Frame):
                for botao in widget.winfo_children():
                    if isinstance(botao, tk.Button) and botao.cget("text").startswith("Mesa"):
                        mesa_num = int(botao.cget("text").split()[1])
                        cor = "green" if self.mesas[mesa_num] == "Livre" else "red"
                        botao.config(text=f"Mesa {mesa_num} - {self.mesas[mesa_num]}", bg=cor)

# Inicializar a aplicação
GerenciamentoMesas()
