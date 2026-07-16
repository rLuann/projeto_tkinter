from abc import ABC, abstractmethod

# classe pai
class Figura(ABC):
    def __init__(self, cor_borda = 'black', cor_preenchimento = ''):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    # criando métodos abstratos, para as filhas implementarem
    @abstractmethod
    def atualizar(self, event):
        pass

    @abstractmethod
    def desenhar(self, canvas, dash = None):
        pass

    @abstractmethod
    def esta_incompleta(self):
        pass

