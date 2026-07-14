__main__.py:
from tkinter import Tk
from modelo.desenho import Desenho
from view.interface import InterfaceDesenho
from controle.controlador import ControladorDesenho

def main():

    root = Tk()
    modelo = Desenho()
    visao = InterfaceDesenho(root)
    controlador = ControladorDesenho(visao, modelo)
    root.mainloop()

if _name_ == "_main_":
    main()