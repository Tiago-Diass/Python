class Livro:
    def __init__(self,nome,autor,ano,estado="disponivel"):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.estado = estado
    
    def __str__(self):
        return f"{self.nome} - {self.autor} ({self.ano}) [{self.estado}]"

    def emprestar(self):
        if self.estado == "disponivel":
            self.estado = "emprestado"
            return True
        return False

    def devolver(self):
        self.estado = "disponivel"