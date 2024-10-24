class Carro:
    def __init__(self,marca,modelo,cor,ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano       
        fusca = Carro("Volksvagen","Fusca","Azul",1945)
    def abrir_porta (self):
        print(f"O carro da marca{self.marca} do ano{self.ano} abriu a porta!")   
class Moto:
    def __init__(self,marca,modelo,cor,ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def acelerar(self):
        print(f"O {self.modelo} da marca {self.marca} está acelerando!")    

hornet = ("Honda","CB750","Preto",2021)        

opcao_carro=(input(""))
print(dir(fusca))
# print(vars())
