# Criar um sistema de classificação de animais vertebrados usando programação orientada a objetos (POO) em Python, representando subdivisões até chegar a classes específicas como Ornitorrinco,
#  Morcego e Baleia.

# Criação das Classes Principais:

# Inicie com a classe geral Animal que conterá características comuns a todos os animais (ex: nome científico).
# Crie subclasses que representem Vertebrados e, a partir daí, vá subdividindo em classes menores (por exemplo, Mamíferos, Répteis, etc.).
# Características Específicas:

# Cada classe deve conter atributos e métodos específicos de cada subdivisão. Por exemplo:
# Mamíferos: método amamentar().
# Aves: método voar().
# Chegue até as classes mais específicas: Ornitorrinco, Morcego e Baleia.
# Atributos e Métodos:

# Atributos como esqueleto, habitat e alimentacao devem ser herdados pelas subclasses.
# Métodos devem ser implementados para ações comuns (ex: seMovimentar()) e específicas (ex: botarOvo() para algumas classes). 
class Animal:
    def __init__(self, nome_cient, pluricelular, especie):
        self.nome_cient = nome_cient
        self.pluricelular = pluricelular
        self.especie = especie

    def seMovimentar(self):
        print("Animal se movimenta!")

class Vertebrados(Animal):
    def __init__(self, nome_cient, pluricelular, especie):
        super().__init__(nome_cient, pluricelular, especie)
        self.esqueleto = True
        self.cranio = True
        self.coluna_vertebral = True

    def mostrar_esqueleto(self):
        print("Esse animal tem esqueleto!")

class Mamifero(Vertebrados):
    def __init__(self, nome_cient, pluricelular, especie):
        super().__init__(nome_cient, pluricelular, especie)
        self.amamenta = True

    def amamentar(self):
        print("Este mamífero está amamentando!")

class Baleia(Mamifero):
    def __init__(self, nome_cient, pluricelular, especie):
        super().__init__(nome_cient, pluricelular, especie)

    def nadar(self):
        print("A baleia está nadando!")

class Morcego(Mamifero):
    def __init__(self, nome_cient, pluricelular, especie):
        super().__init__(nome_cient, pluricelular, especie)

    def voar(self):
        print("O morcego está voando!")

    def seMovimentar(self):
        self.voar()

class Ornitorrinco(Mamifero):
    def __init__(self, nome_cient, pluricelular, especie):
        super().__init__(nome_cient, pluricelular, especie)
    
    def botar_ovo(self):
        print("O ornitorrinco botou um ovo!")

# Testes com as classes específicas
batman = Morcego("Desmodus rotundus", True, "Morcego Vampiro")
batman.seMovimentar()

baleia_azul = Baleia("Balaenoptera musculus", True, "Baleia Azul")
baleia_azul.nadar()

ornitorrinco = Ornitorrinco("Ornithorhynchus anatinus", True, "Ornitorrinco")
ornitorrinco.botar_ovo()

# Print dos atributos do morcego
print(vars(batman))



# vaca=Mamifero("Vacus","Pluricelular","mamifero")
# vaca.amamentar()
# cobra = Vertebrados("Cobris","pluricelualr","invertebrado","não_esqueleto","não tem cranio","nao tem coluna")
# print(vars(vaca))        


# class Mamifero(Vertebrados):
#     def __init__(self,esqueleto,cranio,coluna_vertebral,armamentar):
#        self.armamentar = armamentar
#        super(). __init__(self,esqueleto,cranio,coluna_vertebral)
#     def armamentar():
#         print("Armamenta!!!")

# class Repteis(Vertebrados):
#     def __init__(self,esqueleto,cranio,coluna_vertebral,armamentar,respiracao_pulmonar):
#         self.respiracao_pulmonar = respiracao_pulmonar
#         super(). __init__(self,esqueleto,cranio,coluna_vertebral,armamentar)
#     def     
    


