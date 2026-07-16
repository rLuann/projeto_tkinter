from mvc.modelo.figuras import Figura

class Oval(Figura):
 
    
    def __init__(self, x1, y1, cor_borda="black", cor_preenchimento="", **kwargs):
        super().__init__(cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1  
        self.y2 = y1
    
    def atualizar(self, event):
        self.x2 = event.x
        self.y2 = event.y
    
    def desenhar(self, canvas, dash=None):
        canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=dash
        )
    
    def esta_incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2
    
    def salvar(self):
       
        return {
            'tipo': 'Oval',
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'y2': self.y2,
            'cor_borda': self.cor_borda,
            'cor_preenchimento': self.cor_preenchimento
        }
    
    @staticmethod
    def abrir(dados):
   
        oval = Oval(
            dados['x1'], dados['y1'],
            cor_borda=dados['cor_borda'],
            cor_preenchimento=dados['cor_preenchimento']
        )
        oval.x2 = dados['x2']
        oval.y2 = dados['y2']
        return oval