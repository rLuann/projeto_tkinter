<<<<<<< HEAD
from state.modelo.figuras import *
=======
from mvc.modelo.figuras import Figura
>>>>>>> e71811bc6e3566d7f1fe3aa95e7eb41917c7498c

class Linha(Figura):

    
    def __init__(self, x1, y1, cor_borda="black", **kwargs):
        super().__init__(cor_borda=cor_borda, cor_preenchimento=None)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1  
        self.y2 = y1
    
    def atualizar(self, event):
        self.x2 = event.x
        self.y2 = event.y
    
    def desenhar(self, canvas, dash=None):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, 
            fill=self.cor_borda, 
            dash=dash
        )
    
    def esta_incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2)
    
    def salvar(self):
        return {
            'tipo': 'Linha',
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'y2': self.y2,
            'cor_borda': self.cor_borda
        }
    
    @staticmethod
    def abrir(dados):
        linha = Linha(dados['x1'], dados['y1'], cor_borda=dados['cor_borda'])
        linha.x2 = dados['x2']
        linha.y2 = dados['y2']
        return linha