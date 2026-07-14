from mvc.modelo.linhas import Linha
from mvc.modelo.rabisco import Rabisco
from mvc.modelo.retangulo import Retangulo
from mvc.modelo.circulo import Circulo
from mvc.modelo.oval import Oval
from mvc.modelo.poligono import Poligono

class ControladorDesenho:
    def __init__(self, interface, desenho):
        self.interface = interface    
        self.desenho = desenho        
        self._mapa_figuras = {
            'Linha': Linha,
            'Rabisco': Rabisco,
            'Retângulo': Retangulo,
            'Círculo': Circulo,
            'Oval': Oval,
            'Polígono': Poligono
        }
        self._configurar_eventos()
    
    def _configurar_eventos(self):
        canvas = self.interface.canvas
        canvas.bind('<ButtonPress-1>', self._on_mouse_press)
        canvas.bind('<B1-Motion>', self._on_mouse_drag)
        canvas.bind('<ButtonRelease-1>', self._on_mouse_release)
        canvas.bind('<Double-Button-1>', self._on_double_click)
        self.interface.root.bind('<Control-z>', self._desfazer)
        self.interface.root.bind('<Return>', self._on_enter)
    
    
    
    def _on_mouse_press(self, event):
        tipo = self.interface.get_tipo_figura()
        cor_borda = self.interface.get_cor_borda()
        cor_preenchimento = self.interface.get_cor_preenchimento()
        
        if tipo == 'Polígono':
            self._iniciar_ou_continuar_poligono(event, cor_borda, cor_preenchimento)
            return
        
        figura = self._criar_figura(tipo, event.x, event.y, cor_borda, cor_preenchimento)
        self.desenho.definir_figura_atual(figura)
        self._atualizar_tela()
    
    def _on_mouse_drag(self, event):
        if self.desenho.tem_figura_atual():
            self.desenho.figura_atual.atualizar(event)
            self._atualizar_tela()
    
    def _on_mouse_release(self, event):
        if isinstance(self.desenho.figura_atual, Poligono):
            return
        
        self.desenho.finalizar_figura_atual()
        self._atualizar_tela()
    
    def _on_double_click(self, event):
        self._finalizar_poligono(event)
    
    def _on_enter(self, event):
        self._finalizar_poligono(event)
    
    def _criar_figura(self, tipo, x, y, cor_borda, cor_preenchimento):
        classe = self._mapa_figuras.get(tipo)
        if classe is None:
            raise ValueError(f"Tipo de figura desconhecido: {tipo}")
        
        return classe(
            x, y,
            cor_borda=cor_borda,
            cor_preenchimento=cor_preenchimento
        )
    
    def _iniciar_ou_continuar_poligono(self, event, cor_borda, cor_preenchimento):
        if isinstance(self.desenho.figura_atual, Poligono):
            self.desenho.figura_atual.adicionar_vertice(event.x, event.y)
        else:
            poligono = Poligono(
                event.x, event.y,
                cor_borda=cor_borda,
                cor_preenchimento=cor_preenchimento
            )
            self.desenho.definir_figura_atual(poligono)
        
        self._atualizar_tela()
    
    def _finalizar_poligono(self, event=None):
        if isinstance(self.desenho.figura_atual, Poligono):
            if event:
                self.desenho.figura_atual.adicionar_vertice(event.x, event.y)
            
            self.desenho.finalizar_figura_atual()
            self._atualizar_tela()
    
    def _desfazer(self, event=None):
        if self.desenho.remover_ultima_figura():
            self._atualizar_tela()
    
   
    # redesenha todo o canvas baseado no estado atual do modelo.
    def _atualizar_tela(self):
        self.interface.limpar_canvas()        
        figuras_para_desenhar = self.desenho.get_todas_figuras_para_desenhar()        
        for figura, dash in figuras_para_desenhar:
            self.interface.desenhar_figura(figura, dash=dash)