from figuras import *



class Poligono(Figura):
    
    def _init_(self, x, y, cor_borda="black", cor_preenchimento="", **kwargs):
        super()._init_(cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.vertices = [(x, y)]  # Lista de vértices
    
    def atualizar(self, event):
        self.vertices[-1] = (event.x, event.y)
    
    def adicionar_vertice(self, x, y):
        self.vertices.append((x, y))
    
    def desenhar(self, canvas, dash=None):
        # Achata a lista de vértices
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


