class Veiculo:
    def __init__(self,matricula,marca,num_pneus):
        self.__matricula = matricula # __ para fazer com que o atributo seja privado
        self.marca = marca
        self.num_pneus = num_pneus

    @property # GET
    def matricula(self):
        return self.__matricula

    @matricula.setter # SET
    def matricula(self,nova_matricula):
        self.__matricula = nova_matricula

    def fazer_barulho(self):
        print("vrummmmm")

class Moto(Veiculo):
    def __init__(self, matricula, marca, num_pneus, cilindrada):
        super().__init__(matricula, marca, num_pneus)
        self.cilindrada = cilindrada

    def __str__(self): # Para fazer o print simples (v1,v2, etc...)
         return f"{self.matricula} - Moto da marca {self.marca}"

    def __eq__(self, outra_moto): # Para fazer Comparação
         return self.marca == outra_moto.marca

    def fazer_barulho(self):
            print("bibibibi")


v1 = Veiculo("32-57-NT", "Fiat", 4) # Criar Veiculo
v1.matricula = "33-22-XY" # Alterar Matricula
v1.fazer_barulho()
print(v1.matricula)

v2 = Moto("67-69-NG", "TomPearl", 2, 2000)
v3 = Moto("HI-TE-67", "TomPearl", 2, 1500)
v2.fazer_barulho()
print(v2)
if v2 == v3:
     print("Mesma marca")

# Class HotelModel - Resultar em uma tabela chamada hoteis
# hotel = "HBO"
# x = HotelModel.query.filter_by(hotel=hotel).first()
# SELECT * FROM hoteis WHERE hotel = h LIMIT 1