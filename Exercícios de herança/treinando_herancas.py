class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Chama o construtor da classe pai
        self.modelo = modelo

c = Carro("Toyota", "Corolla")
print(c.marca, c.modelo)
