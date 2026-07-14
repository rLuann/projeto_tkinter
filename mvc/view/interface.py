from tkinter import *
from tkinter import ttk

class InterfaceDesenho:

    CORES = [
        "", "red", "blue", "green", "yellow",
        "orange", "purple", "pink", "lightblue",
        "lightgreen", "lightgray", "cyan", "brown",
        "black", "magenta", "navy", "teal",
        "white", "gray", "darkgray", "darkgreen",
        "darkblue", "darkred", "darkorange", "gold",
        "goldenrod", "khaki", "beige", "ivory",
        "lavender", "violet", "plum", "orchid",
        "indigo", "turquoise", "aquamarine", "coral",
        "salmon", "tomato", "crimson", "maroon",
        "olive", "lime", "limegreen", "forestgreen",
        "seagreen", "springgreen", "mintcream",
        "skyblue", "deepskyblue", "dodgerblue",
        "steelblue", "royalblue", "slateblue",
        "mediumblue", "midnightblue", "aliceblue",
        "powderblue", "cadetblue", "darkcyan",
        "darkturquoise", "paleturquoise",
        "hotpink", "deeppink", "lightpink",
        "palevioletred", "mediumvioletred",
        "thistle", "snow", "honeydew",
        "azure", "wheat", "tan", "chocolate",
        "sienna", "peru", "burlywood",
        "sandybrown", "rosybrown", "firebrick",
        "gainsboro", "silver", "dimgray",
        "slategray", "darkslategray"
    ]
    
    TIPOS_FIGURA = ['Linha', 'Rabisco', 'Retângulo', 'Círculo', 'Oval', 'Polígono']
    
    def _init_(self, root):
        self.root = root
        self.root.title("Editor de Desenho OO - UFS")
        
        self.tipo_figura_var = StringVar(root, value='Linha')
        self.cor_borda_var = StringVar(root, value="black")
        self.cor_preenchimento_var = StringVar(root, value="")
        

        self._criar_widgets()
    
    def _criar_widgets(self):
        paddings = {'padx': 5, 'pady': 5}
        

        self.frame = Frame(self.root)
        self.frame.pack()
        
        self._criar_frame_tipo(paddings)
        
        self._criar_frame_cores(paddings)
        
        self._criar_instrucoes(paddings)
        
        self._criar_canvas(paddings)
    
    def _criar_frame_tipo(self, paddings):
        frame_tipo = Frame(self.frame)
        frame_tipo.grid(column=0, row=0, sticky=W, **paddings)
        
        ttk.Label(frame_tipo, text='Tipo:').grid(
            column=0, row=0, sticky=W, **paddings
        )
        
        self.option_menu = ttk.OptionMenu(
            frame_tipo, 
            self.tipo_figura_var,
            self.TIPOS_FIGURA[0], 
            *self.TIPOS_FIGURA
        )
        self.option_menu.grid(column=1, row=0, sticky=W, **paddings)
        
    
        self.botao_desfazer = ttk.Button(
            frame_tipo, 
            text="Desfazer (Ctrl+Z)"
        )
        self.botao_desfazer.grid(column=2, row=0, sticky=W, **paddings)
    
    def _criar_frame_cores(self, paddings):
        frame_cores = Frame(self.frame)
        frame_cores.grid(column=0, row=1, sticky=W, **paddings)
        
    
        ttk.Label(frame_cores, text="Cor da Borda:").grid(
            column=0, row=0, padx=5
        )
        self.borda_combo = ttk.Combobox(
            frame_cores, 
            textvariable=self.cor_borda_var,
            values=self.CORES,
            state="readonly", 
            width=15
        )
        self.borda_combo.grid(column=1, row=0, padx=5)
      
        ttk.Label(frame_cores, text="Cor de Preenchimento:").grid(
            column=2, row=0, padx=5
        )
        self.preenchimento_combo = ttk.Combobox(
            frame_cores, 
            textvariable=self.cor_preenchimento_var,
            values=self.CORES,
            state="readonly", 
            width=15
        )
        self.preenchimento_combo.grid(column=3, row=0, padx=5)
    
    def _criar_instrucoes(self, paddings):
        self.label_instrucoes = ttk.Label(
            self.frame,
            text="Polígono: Clique para adicionar vértices, duplo clique para finalizar.",
            font=("Arial", 9)
        )
        self.label_instrucoes.grid(
            column=0, row=2, sticky=W, **paddings
        )
    
    def _criar_canvas(self, paddings):
        self.canvas = Canvas(
            self.frame, 
            bg='white', 
            width=600, 
            height=600
        )
        self.canvas.grid(
            column=0, row=3, columnspan=2, sticky=W, **paddings
        )

    def get_tipo_figura(self):
        return self.tipo_figura_var.get()
    
    def get_cor_borda(self):
        return self.cor_borda_var.get()
    
    def get_cor_preenchimento(self):
        return self.cor_preenchimento_var.get()
    
    # Métodos de manipulação do canvas
    def limpar_canvas(self):
        self.canvas.delete("all")
    
    def desenhar_figura(self, figura, dash=None):
        figura.desenhar(self.canvas, dash=dash)
    
    def atualizar_instrucoes(self, texto):
        self.label_instrucoes.config(text=texto)