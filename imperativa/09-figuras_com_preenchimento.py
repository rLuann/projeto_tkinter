from tkinter import *
from tkinter import ttk

#*** FUNÇÕES ***#

def iniciar_figura_nova(event): 
    global figura_nova
    cor_borda = cor_borda_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_borda, None)
    elif tipo_figura_var.get() == 'Rabisco':
        figura_nova = ("rabisco", [(event.x, event.y)], cor_borda, None)
    elif tipo_figura_var.get() == 'Círculo':
        figura_nova = ("circulo", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'Retângulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)

def atualizar_figura_nova(event):
    global figura_nova
    
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), 
                      figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "circulo":
        figura_nova = ("circulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), 
                      figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "retangulo":
        figura_nova = ("retangulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), 
                      figura_nova[2], figura_nova[3])
    
    desenhar_figuras()
    desenhar_figura_nova()

def incluir_figura_nova(event): 
    if not incompleta(figura_nova):
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, cor_borda, cor_preenchimento in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_borda)
        elif fig == "rabisco":
            canvas.create_line(values, fill=cor_borda)
        elif fig == "circulo":
            canvas.create_oval(values[0], values[1], values[2], values[3],
                             outline=cor_borda, fill=cor_preenchimento)
        elif fig == "retangulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3],
                                  outline=cor_borda, fill=cor_preenchimento)

def desenhar_figura_nova():
    fig, values, cor_borda, cor_preenchimento = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], 
                         fill=cor_borda, dash=(4, 2))
    elif fig == "rabisco":
        canvas.create_line(values, fill=cor_borda, dash=(4, 2))
    elif fig == "circulo":
        canvas.create_oval(values[0], values[1], values[2], values[3],
                         outline=cor_borda, fill=cor_preenchimento, dash=(4, 2))
    elif fig == "retangulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3],
                              outline=cor_borda, fill=cor_preenchimento, dash=(4, 2))

def incompleta(figura):
    fig, values, cor_borda, cor_preenchimento = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1
    elif fig == "retangulo":
        x1, y1, x2, y2 = values
        return x1 == x2 or y1 == y2
    elif fig == "circulo":
        x1, y1, x2, y2 = values
        return x1 == x2 and y1 == y2

def desfazer_ultima_figura(event=None):
    if figuras:
        figuras.pop()
        desenhar_figuras()

#*** MAIN ***#

figuras = []
figura_nova = None

root = Tk()
root.title("Editor de Desenho - UFS")

frame = Frame(root)
paddings = {'padx': 5, 'pady': 5}

# Frame para tipo de figura
frame_tipo = Frame(frame)
frame_tipo.grid(column=0, row=0, sticky=W, **paddings)

ttk.Label(frame_tipo, text='Tipo:').grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(frame_tipo, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Círculo', 'Retângulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Frame para cores (borda e preenchimento)
frame_cores = Frame(frame)
frame_cores.grid(column=0, row=1, sticky=W, **paddings)

# parte de adicionar cor da borda
cor_borda_var = StringVar(root, value="black")
ttk.Label(frame_cores, text="Cor da Borda:").grid(column=0, row=0, padx=5)
borda_combo = ttk.Combobox(frame_cores, textvariable=cor_borda_var,
                           values=["black", "red", "blue", "green", "orange",
                                  "purple", "brown", "pink", "gray", "cyan"],
                           state="readonly", width=15)
borda_combo.grid(column=1, row=0, padx=5)

# parte de adicionar cor de preenchimento
cor_preenchimento_var = StringVar(root, value="")
ttk.Label(frame_cores, text="Cor de Preenchimento:").grid(column=2, row=0, padx=5)
preenchimento_combo = ttk.Combobox(frame_cores, textvariable=cor_preenchimento_var,
                                   values=["", "red", "blue", "green", "yellow",
                                          "orange", "purple", "pink", "lightblue",
                                          "lightgreen", "lightgray", "cyan"],
                                   state="readonly", width=15)
preenchimento_combo.grid(column=3, row=0, padx=5)

# Canvas
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=2, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
root.bind('<Control-z>', desfazer_ultima_figura)

root.mainloop()