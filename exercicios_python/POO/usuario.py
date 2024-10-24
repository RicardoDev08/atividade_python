class Usuario():
    MAX_EMPRESTIMO = 3
    def __init__(self,nome,cpf):
        self.nome=nome
        self.cpf=cpf
        self.lista_livros = []
    def pegar_emprestado(self,livro):    
        if len (self.lista_livros) == self.MAX_EMPRESTIMO:
            return 'Limite de emprestimo atingido'
        self.lista_livros.append(livro.nome)
 #continuação

        print()                  

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
        if len(usuario.lista_Livros)==usuario.MAX_EMPRESTIMO:
            return
        self.usuario = usuario.nome
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
    Acervo = []
    @staticmethod
    def emprestar(livros:list[Livro],usuario:Usuario) -> bool:
        for item in livros:
            item.emprestimo
            usuario.pegar_emprestado
        livros.emprestimo(usuario)
        usuario.pegar_emprestado(livros)


# class Biblioteca():
#     def __init__(self,vende_livro,aluga):
#         self.vende_livro = vende_livro
#         self.aluga = aluga



ricardo = Usuario('Ricardo','010101010101','67992262733')
print(vars(ricardo))

dom_casmurgo=Livro('eu e ela','dom casmurgo','romance',1)
velozes_Furiosos=Livro('velozes e furiosos 12','torreto','ação',2)
poder_da_acao=Livro('poder da ação','Paulo coach','conhecimento pessoal',3)
pequeno_principe=Livro('pequeno principe','Ricardo','infantil',4)

#  
ricardo.pegar_emprestado(dom_casmurgo)
ricardo.pegar_emprestado(velozes_Furiosos)
ricardo.pegar_emprestado(poder_da_acao)
ricardo.pegar_emprestado(pequeno_principe)

dom_casmurgo.emprestimo(ricardo)
velozes_Furiosos.emprestimo(ricardo)
poder_da_acao.emprestimo(ricardo)
pequeno_principe.emprestimo(ricardo)


# print(dom_casmurgo.status)
# print(vars(dom_casmurgo))

# ricardo.pegar_emprestado(dom_casmurgo)
# print(vars(ricardo))

