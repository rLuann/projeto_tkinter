from abc import ABC, abstractmethod
from modelo.poligono import Poligono


# superclasse para todos os estados do controlador
class EstadoDesenho(ABC):
    def __init__(self, controlador):
        self.controlador = controlador
    
    @abstractmethod
    # mouse pressionado
    def on_mouse_press(self, event):
        pass
    
    @abstractmethod
    # mouse arrastado
    def on_mouse_drag(self, event):
        pass
    
    @abstractmethod
    # mouse solto
    def on_mouse_release(self, event):
        pass
    
    # duplo clique no mouse
    def on_double_click(self, event):
        pass
    
    # tecla enter
    def on_enter_key(self, event):
        pass
    
    # retorna o nome do estado atual
    def get_nome(self):
        return self.__class__.__name__


# quando nenhuma figura está sendo desenhada
class EstadoOcioso(EstadoDesenho):
    def on_mouse_press(self, event):
        tipo = self.controlador.interface.get_tipo_figura()
        cor_borda = self.controlador.interface.get_cor_borda()
        cor_preenchimento = self.controlador.interface.get_cor_preenchimento()
        
        if tipo == 'Polígono':
            poligono = Poligono(event.x, event.y, cor_borda = cor_borda, cor_preenchimento = cor_preenchimento
            )
            self.controlador.desenho.definir_figura_atual(poligono)
            self.controlador.mudar_estado(EstadoCriandoPoligono(self.controlador))
        else:
            figura = self.controlador._criar_figura (tipo, event.x, event.y, cor_borda, cor_preenchimento)
            self.controlador.desenho.definir_figura_atual(figura)
            self.controlador.mudar_estado(EstadoDesenhandoFiguraSimples(self.controlador))
        
        self.controlador._atualizar_tela()
    
    def on_mouse_drag(self, event):
        pass
    
    def on_mouse_release(self, event):
        pass


# para figuras simples como linha, retangulo e etc
class EstadoDesenhandoFiguraSimples(EstadoDesenho):
    def on_mouse_press(self, event):
        self.controlador.mudar_estado(EstadoOcioso(self.controlador))
        self.controlador.estado_atual.on_mouse_press(event)
    
    def on_mouse_drag(self, event):
        if self.controlador.desenho.tem_figura_atual():
            self.controlador.desenho.figura_atual.atualizar(event)
            self.controlador._atualizar_tela()
    
    def on_mouse_release(self, event):
        self.controlador.desenho.finalizar_figura_atual()
        self.controlador._atualizar_tela()
        self.controlador.mudar_estado(EstadoOcioso(self.controlador))


# para poligonos
class EstadoCriandoPoligono(EstadoDesenho):
    def on_mouse_press(self, event):
        if isinstance(self.controlador.desenho.figura_atual, Poligono):
            self.controlador.desenho.figura_atual.adicionar_vertice(event.x, event.y)
            self.controlador._atualizar_tela()
    
    def on_mouse_drag(self, event):
        if isinstance(self.controlador.desenho.figura_atual, Poligono):
            self.controlador.desenho.figura_atual.atualizar(event)
            self.controlador._atualizar_tela()
    
    def on_mouse_release(self, event):
        pass  
    
    def on_double_click(self, event):
        self._finalizar_poligono(event)
    
    def on_enter_key(self, event):
        self._finalizar_poligono(event)
    
    def _finalizar_poligono(self, event=None):
        if isinstance(self.controlador.desenho.figura_atual, Poligono):
            if event:
                self.controlador.desenho.figura_atual.adicionar_vertice(event.x, event.y)
            
            if self.controlador.desenho.finalizar_figura_atual():
                self.controlador._atualizar_tela()
                self.controlador.mudar_estado(EstadoOcioso(self.controlador))