from figuras import *

# criando subclasse retangulo
class Retangulo(Figura):    
    def __init__(self, x1, y1, cor_borda = "black", cor_preenchimento = "", **kwargs):
        super().__init__(cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
    
    def atualizar(self, event):
        self.x2 = event.x
        self.y2 = event.y
    
    def desenhar(self, canvas, dash=None):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill = self.cor_preenchimento, dash = dash)
    
    def esta_incompleta(self):
        return self.x1 == self.x2 or self.y1 == self.y2