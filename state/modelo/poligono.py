from mvc.modelo.figuras import Figura

class Poligono(Figura):

    
    def __init__(self, x, y, cor_borda="black", cor_preenchimento="", **kwargs):
        super().__init__(cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.vertices = [(x, y)]
    
    def atualizar(self, event):
        self.vertices[-1] = (event.x, event.y)
    
    def adicionar_vertice(self, x, y):
        self.vertices.append((x, y))
    
    def desenhar(self, canvas, dash=None):
        vertices_achatados = []
        for x, y in self.vertices:
            vertices_achatados.extend([x, y])
        
        canvas.create_polygon(
            vertices_achatados,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=dash
        )
    
    def esta_incompleta(self):
        return len(self.vertices) < 3
    
    def salvar(self):
      
        return {
            'tipo': 'Polígono',
            'vertices': self.vertices,
            'cor_borda': self.cor_borda,
            'cor_preenchimento': self.cor_preenchimento
        }
    
    @staticmethod
    def abrir(dados):
       
        vertices = dados['vertices']
        if not vertices:
            return None
        
        poligono = Poligono(
            vertices[0][0], vertices[0][1],
            cor_borda=dados['cor_borda'],
            cor_preenchimento=dados['cor_preenchimento']
        )
        poligono.vertices = vertices  
        return poligono