import sys
from pathlib import Path
from tkinter import Tk

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from state.modelo.desenho import Desenho
from state.view.interface import InterfaceDesenho
from state.controller.controlador import ControladorDesenho

def main():

    root = Tk()
    modelo = Desenho()
    visao = InterfaceDesenho(root)
    controlador = ControladorDesenho(visao, modelo)
    root.mainloop()

if __name__ == "__main__":
    main()