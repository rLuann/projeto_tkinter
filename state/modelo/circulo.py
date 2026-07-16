from state.modelo.figuras import Figura
import math

class Circulo(Figura):

    
    def __init__(self, x1, y1, cor_borda="black", cor_preenchimento="", **kwargs):
        super().__init__(cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.centro_x = x1
        self.centro_y = y1
        self.raio = 0 

    def atualizar(self, event):
        dx = event.x - self.centro_x
        dy = event.y - self.centro_y
        self.raio = math.sqrt(dx*2 + dy*2)

    def desenhar(self, canvas, dash=None):
        x1 = self.centro_x - self.raio
        y1 = self.centro_y - self.raio
        x2 = self.centro_x + self.raio
        y2 = self.centro_y + self.raio
        canvas.create_oval(
            x1, y1, x2, y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=dash
        )

    def esta_incompleta(self):
        return self.raio == 0
    
    def to_dict(self):
      
        return {
            'tipo': 'Círculo',
            'centro_x': self.centro_x,
            'centro_y': self.centro_y,
            'raio': self.raio,
            'cor_borda': self.cor_borda,
            'cor_preenchimento': self.cor_preenchimento
        }
    
    @staticmethod
    def from_dict(dados):
      
        circulo = Circulo(
            dados['centro_x'], dados['centro_y'],
            cor_borda=dados['cor_borda'],
            cor_preenchimento=dados['cor_preenchimento']
        )
        circulo.raio = dados['raio']
        return circulo