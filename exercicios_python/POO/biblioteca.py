class Usuario():
    MAX_QUANTIDADE = 3
    def __init__(self,nome,cpf):
        self.nome=nome
        self.cpf=cpf
        self.lista_livros = []
    def pegar_emprestado(self,livro):    
        if len (self.lista_livros) == self.MAX_QUANTIDADE:
 #continuação
class Livro():
    def __init__(self,titulo,autor,genero,cod_livro):  # métodos emprestimo,cadastro
        self.status = 'Disponível'
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro
        self.usuario=None

    def emprestimo(self,usuario):
        if self.status !='Disponível':
            return
        self.usuario = usuario
        self.status = 'Emprestado'
    def devolver_livro(self):
        if self.status!='Emprestado':
            return 
        self.usuario = None
        self.status ='Disponível'

    def cadastro(self):
        print()
    def listar(self):
        print()                  

class Biblioteca():
    def __init__(self,vende_livro,aluga):
        self.vende_livro = vende_livro
        self.aluga = aluga



