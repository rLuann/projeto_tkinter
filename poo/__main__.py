from tkinter import *
from tkinter import ttk
from figuras import *
from linhas import Linha  
from rabisco import Rabisco
from retangulo import Retangulo
from circulo import *
from poligono import *
from oval import *

# dicionário para referenciar as classes
MAPA_FIGURAS = {
    'Linha': Linha,
    'Rabisco': Rabisco,
    'Retângulo': Retangulo,
    'Círculo': Circulo,
    'Polígono': Poligono,
    'Oval': Oval
}

def iniciar_figura_nova(event): 
    global figura_nova
    
    cor_borda = cor_borda_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    tipo = tipo_figura_var.get()

    if tipo == 'Polígono':
        # Se já existe um polígono sendo desenhado, adiciona vértice
        if isinstance(figura_nova, Poligono):
            figura_nova.adicionar_vertice(event.x, event.y)
            desenhar_figuras()
            desenhar_figura_nova()
            return
        # Senão, cria um novo polígono
        else:
            figura_nova = Poligono(
                event.x, event.y,
                cor_borda=cor_borda,
                cor_preenchimento=cor_preenchimento
            )
            return
    
    # aqui tá usando o dicionário mapa_figuras para criar a classe certa
    classe_figura = MAPA_FIGURAS[tipo]
    figura_nova = classe_figura(
        event.x, event.y,
        cor_borda = cor_borda,
        cor_preenchimento = cor_preenchimento
    )

def atualizar_figura_nova(event):
    global figura_nova
    
    figura_nova.atualizar(event)
    
    desenhar_figuras()
    desenhar_figura_nova()

def incluir_figura_nova(event): 
    if not figura_nova.esta_incompleta():
        figuras.append(figura_nova)
    desenhar_figuras()

# função para finalizar o polígono, tem que ter mais de 3 vérticies para ser finalizado (finaliza com 2 cliques)
def finalizar_poligono(event=None):
    global figura_nova
    
    if isinstance(figura_nova, Poligono):
        figura_nova.adicionar_vertice(event.x, event.y)
        if not figura_nova.esta_incompleta():
            figuras.append(figura_nova)
            figura_nova = None
            desenhar_figuras()

# adiciona vértice com um click ao polígono
def adicionar_vertice_poligono(event):
    global figura_nova
    
    if isinstance(figura_nova, Poligono):
        figura_nova.adicionar_vertice(event.x, event.y)

# aqui usamos polimorfismo para fazer uma chamada de método para cada subclasse
def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        figura.desenhar(canvas)

def desenhar_figura_nova():
    if figura_nova:
        figura_nova.desenhar(canvas, dash=(4, 2))

def desfazer_ultima_figura(event=None):
    if figuras:
        figuras.pop()
        desenhar_figuras()

#*** MAIN ***#

figuras = []
figura_nova = None

root = Tk()
root.title("Editor de Desenho OO - UFS")

frame = Frame(root)
paddings = {'padx': 5, 'pady': 5}

# Frame para tipo de figura
frame_tipo = Frame(frame)
frame_tipo.grid(column=0, row=0, sticky=W, **paddings)

ttk.Label(frame_tipo, text='Tipo:').grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root)
# Adicionado 'Polígono' nas opções
option_menu = ttk.OptionMenu(
    frame_tipo, tipo_figura_var,
    'Linha', 'Linha', 'Rabisco', 'Círculo', 'Retângulo', 'Polígono', 'Oval'
)
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Frame para cores
frame_cores = Frame(frame)
frame_cores.grid(column=0, row=1, sticky=W, **paddings)

# Cor da borda
cor_borda_var = StringVar(root, value="black")
ttk.Label(frame_cores, text="Cor da Borda:").grid(column=0, row=0, padx=5)
borda_combo = ttk.Combobox(
    frame_cores, textvariable=cor_borda_var,
    values=["black", "red", "blue", "green", "orange",
            "purple", "brown", "pink", "gray", "cyan"],
    state="readonly", width=15
)
borda_combo.grid(column=1, row=0, padx=5)

# Cor de preenchimento
cor_preenchimento_var = StringVar(root, value="")
ttk.Label(frame_cores, text="Cor de Preenchimento:").grid(column=2, row=0, padx=5)
preenchimento_combo = ttk.Combobox(
    frame_cores, textvariable=cor_preenchimento_var,
    values=["", "red", "blue", "green", "yellow",
            "orange", "purple", "pink", "lightblue",
            "lightgreen", "lightgray", "cyan"],
    state="readonly", width=15
)
preenchimento_combo.grid(column=3, row=0, padx=5)

# intruções para o polígono
label_instrucoes = ttk.Label(
    frame,
    text="Polígono: Clique uma vez para adicionar vértices, clique duas vezes para finalizar.",
    font=("Arial", 9)
)
label_instrucoes.grid(column=0, row=2, sticky=W, **paddings)

# Canvas
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=3, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
root.bind('<Control-z>', desfazer_ultima_figura)

# polígono
canvas.bind('<Double-Button-1>', finalizar_poligono)
root.bind('<Control-z>', desfazer_ultima_figura)
root.bind('<Return>', finalizar_poligono)  # enter para finalizar também, além de clique

root.mainloop()