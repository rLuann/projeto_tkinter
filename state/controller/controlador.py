from state.modelo.linhas import Linha
from state.modelo.rabisco import Rabisco
from state.modelo.retangulo import Retangulo
from state.modelo.circulo import Circulo
from state.modelo.oval import Oval
from state.modelo.poligono import Poligono
from state.controller.estados import EstadoOcioso, EstadoDesenhandoFiguraSimples, EstadoCriandoPoligono


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
        # Botões de arquivo
        self.interface.botao_salvar.config(command=self._salvar)
        self.interface.botao_abrir.config(command=self._abrir)

        # Atalhos de teclado
        self.interface.root.bind('<Control-s>', self._salvar)  # Ctrl+S para salvar
        self.interface.root.bind('<Control-o>', self._abrir)   # Ctrl+O para abrir


    # Adicione estes métodos no final da classe:

    def _salvar(self, event=None):
        """Salva o desenho em arquivo."""
        # Se já tem arquivo, salva direto. Senão, pede caminho.
        if self.desenho.tem_arquivo_salvo():
            caminho = self.desenho.get_arquivo_atual()
        else:
            caminho = self.interface.pedir_arquivo_para_salvar()
        
        if caminho:
            if self.desenho.salvar_em_arquivo(caminho):
                self.interface.mostrar_mensagem(
                    "Sucesso", 
                    f"Desenho salvo em:\n{caminho}"
                )

    def _abrir(self, event=None):
        """Abre um desenho de arquivo."""
        # Verifica se há alterações não salvas
        if self.desenho.figuras:
            confirmar = self.interface.pedir_confirmacao(
                "Abrir Desenho",
                "Há um desenho atual. Deseja abrir um novo arquivo?\n"
                "(As alterações não salvas serão perdidas)"
            )
            if not confirmar:
                return
        
        caminho = self.interface.pedir_arquivo_para_abrir()
        
        if caminho:
            if self.desenho.carregar_de_arquivo(caminho):
                # Volta para estado ocioso
                self.mudar_estado(EstadoOcioso(self))
                
                # Atualiza a tela
                self._atualizar_tela()
                
                self.interface.mostrar_mensagem(
                    "Sucesso",
                    f"Desenho carregado de:\n{caminho}"
                )
    

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