from mvc.modelo.figuras import *

# criando subclasse linha
class Linha(Figura):
    # aqui utilizamos os kwargs (keyword arguments) para que ela guardasse a cor_preenchimento, já que a linha não tem. Porque a função do main passa cor_preenchimento para todas as subclasses. Iraemos adicionar os kwargs em outras classes.
    def __init__(self, x1, y1, cor_borda = "black", **kwargs):
        super().__init__(cor_borda = cor_borda, cor_preenchimento = None)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1  
        self.y2 = y1
    
    def atualizar(self, event):
        self.x2 = event.x
        self.y2 = event.y
    
    def desenhar(self, canvas, dash=None):
        canvas.create_line( self.x1, self.y1, self.x2, self.y2, fill = self.cor_borda, dash = dash)
    
    def esta_incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2)