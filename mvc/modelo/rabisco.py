from mvc.modelo.figuras import *

class Rabisco(Figura):
    def __init__(self, x, y, cor_borda = "black", **kwargs):
        super().__init__(cor_borda = cor_borda, cor_preenchimento = None)
        self.pontos = [(x, y)]
    
    def atualizar(self, event):
        self.pontos.append((event.x, event.y))
    
    def desenhar(self, canvas, dash = None):
        pontos_achatados = []
        for x, y in self.pontos:
            pontos_achatados.extend([x, y])
        
        canvas.create_line(
            pontos_achatados,
            fill=self.cor_borda,
            dash=dash
        )
    
    def esta_incompleta(self):
        return len(self.pontos) <= 1
