class Desenho:
    def __init__(self):
        self.figuras = []       
        self.figura_atual = None  
    
    def adicionar_figura(self, figura):
        self.figuras.append(figura)
    
    def definir_figura_atual(self, figura):
        self.figura_atual = figura
    
    def tem_figura_atual(self):
        return self.figura_atual is not None
    
    def finalizar_figura_atual(self):
        if self.figura_atual and not self.figura_atual.esta_incompleta():
            self.figuras.append(self.figura_atual)
            self.figura_atual = None
            return True
        return False
    
    def remover_ultima_figura(self):
        if self.figuras:
            self.figuras.pop()
            return True
        return False
    
    def get_todas_figuras_para_desenhar(self):
        figuras_desenho = []
        for figura in self.figuras:
            figuras_desenho.append((figura, None)) 
        
        if self.figura_atual:
            figuras_desenho.append((self.figura_atual, (4, 2))) 
        
        return figuras_desenho
    
    def limpar_tudo(self):
        self.figuras.clear()
        self.figura_atual = None