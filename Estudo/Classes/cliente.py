class Cliente:
    # Atributos da classe
    total_clientes = 0
    def __init__(self, nome, peso, altura):
        # Atributos da intância
        self.nome = nome
        self.peso = peso
        self.altura = altura
        Cliente.total_clientes += 1

    # Métodos especiais - dunder methods
    def __str__(self):
        return f"Nome: {self.nome}, Peso: {self.peso}, Altura: {self.altura}"

    def __repr__(self):
        return f"Cliente({self.nome}, {self.peso}, {self.altura})"

    def __eq__(self,c1):
        return self.nome == c1.nome

    # Método da classe
    @classmethod
    def procurar(cls, cliente_a_pesquisar):
        if cliente_a_pesquisar == "Ana":
            return True
        return False

c1 = Cliente("Ana", 62, 1.65)
c2 = Cliente("Maria", 71, 1.74)
c3 = Cliente("Maria", 62, 1.65)
lista = [c1, c2, c3]

print(c1)
print(c2)
print(c3)

if c1 == c2:
    print("São iguais")
if c2 == c3:
    print("São iguais 2")

print(f"Total de clientes: {Cliente.total_clientes}")

for c in lista:
    if Cliente.procurar(c.nome):
        print(f"Cliente {c} encontrado!")