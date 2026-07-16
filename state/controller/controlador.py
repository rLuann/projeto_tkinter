from modelo.linhas import Linha
from modelo.rabisco import Rabisco
from modelo.retangulo import Retangulo
from modelo.circulo import Circulo
from modelo.oval import Oval
from modelo.poligono import Poligono
from controller.estados import EstadoOcioso


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
        self.estado_atual = EstadoOcioso(self)
        self._configurar_eventos()
    
    # muda o estado
    def mudar_estado(self, novo_estado):
        self.estado_atual = novo_estado
        print(f"[State] Mudou para: {novo_estado.get_nome()}")  # Debug
    
    def _configurar_eventos(self):
        canvas = self.interface.canvas
        canvas.bind('<ButtonPress-1>', self._on_mouse_press)
        canvas.bind('<B1-Motion>', self._on_mouse_drag)
        canvas.bind('<ButtonRelease-1>', self._on_mouse_release)
        canvas.bind('<Double-Button-1>', self._on_double_click)
        self.interface.root.bind('<Control-z>', self._desfazer)
        self.interface.root.bind('<Return>', self._on_enter)
        self.interface.botao_desfazer.config(command=self._desfazer)
    

    def _on_mouse_press(self, event):
        
        self.estado_atual.on_mouse_press(event)
    
    def _on_mouse_drag(self, event):
        self.estado_atual.on_mouse_drag(event)
    
    def _on_mouse_release(self, event):
        self.estado_atual.on_mouse_release(event)
    
    def _on_double_click(self, event):
        self.estado_atual.on_double_click(event)
    
    def _on_enter(self, event):
        self.estado_atual.on_enter_key(event)
    
    def _criar_figura(self, tipo, x, y, cor_borda, cor_preenchimento):
        classe = self._mapa_figuras.get(tipo)
        if classe is None:
            raise ValueError(f"Tipo de figura desconhecido: {tipo}")
        return classe(
            x, y,
            cor_borda=cor_borda,
            cor_preenchimento=cor_preenchimento
        )
    
    def _desfazer(self, event=None):
        if self.desenho.remover_ultima_figura():
            self._atualizar_tela()
    
    def _atualizar_tela(self):
        self.interface.limpar_canvas()
        figuras_para_desenhar = self.desenho.get_todas_figuras_para_desenhar()
        for figura, dash in figuras_para_desenhar:
            self.interface.desenhar_figura(figura, dash=dash)