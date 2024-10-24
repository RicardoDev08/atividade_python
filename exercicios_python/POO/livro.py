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
        