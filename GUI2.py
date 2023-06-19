from tkinter import *
class aplication:
    def __init__(self,master=None):
        self.container1 = Frame(master, pady = 10)
        self.container2 = Frame(master, padx = 20)
        self.container3 = Frame(master, padx = 20)
        self.container4 = Frame(master, padx = 20)

        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        self.container4.pack()

        self.titulo = Label(self.container1, text = "Dados do usuario")
        self.titulo.pack()

        self.nomeLabel = Label(self.container2, text = "Nome")
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.container2, width = 20)
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.container3, text = "Senha")
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.container3, width = 30, show="*")
        self.senha.pack(side=LEFT)

        self.logar = Button(self.container4, text = "Login", width=12)
        self.logar["command"] = self.verificaSenha
        self.logar.pack()

        self.mensagem = Label(self.container4, text="")
        self.mensagem.pack()

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if(len(senha) == 0):
            self.mensagem["text"] = "A senha deve ser informada"
            senha = self.senha.get()
        else:
            self.mensagem["text"] = "Usuario logado"

raiz = Tk()
aplication(raiz)
raiz.mainloop()