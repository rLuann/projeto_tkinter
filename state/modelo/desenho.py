import json
from modelo.linhas import Linha
from modelo.rabisco import Rabisco
from modelo.retangulo import Retangulo
from modelo.circulo import Circulo
from modelo.oval import Oval
from modelo.poligono import Poligono


class Desenho:
 
    

    MAPA_RECRIACAO = {
        'Linha': Linha,
        'Rabisco': Rabisco,
        'Retângulo': Retangulo,
        'Círculo': Circulo,
        'Oval': Oval,
        'Polígono': Poligono
    }
    
    def _init_(self):
        self.figuras = []
        self.figura_atual = None
        self.arquivo_atual = None  
    
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
    
   
    
    def salvar_em_arquivo(self, caminho_arquivo):
 
        try:
            
            dados = []
            for figura in self.figuras:
                dados.append(figura.to_dict())
            
            # Salva como JSON
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=2, ensure_ascii=False)
            
            self.arquivo_atual = caminho_arquivo
            return True
        
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False
    
    def carregar_de_arquivo(self, caminho_arquivo):

        try:
    
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            
        
            self.figuras.clear()
            self.figura_atual = None
            
    
            for item in dados:
                tipo = item.get('tipo')
                classe = self.MAPA_RECRIACAO.get(tipo)
                
                if classe and hasattr(classe, 'from_dict'):
                    figura = classe.from_dict(item)
                    if figura:
                        self.figuras.append(figura)
            
            self.arquivo_atual = caminho_arquivo
            return True
        
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {caminho_arquivo}")
            return False
        except Exception as e:
            print(f"Erro ao carregar: {e}")
            return False
    
    def tem_arquivo_salvo(self):
       
        return self.arquivo_atual is not None
    
    def get_arquivo_atual(self):
     
        return self.arquivo_atual