from tkinter import *
class aplication:
    def __init__(self,master=None):
        self.fr1 = Frame(master)
        self.fr1.pack()
        self.msg = Label(self.fr1, text="Clique em Login")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        self.logar=Button(self.fr1, text="Login")
        self.logar["background"] = "blue"
        self.logar.bind("<Button-1>", self.mudarTexto)
        #self.sair["command"] = self.fr1.quit
        self.logar.pack()

    def mudarTexto(self,evento):
            if self.msg["text"] == "Clique em Login":
                self.msg["text"] = "Login Realizado com Sucesso"


raiz = Tk()
aplication(raiz)
raiz.mainloop()