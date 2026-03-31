class Pais:
    def __init__(self, nome, populacao, area):
        self.populacao = populacao
        self.area = area
        self.nome = nome
    
    def densidade(self):
        return self.populacao / self.area

    def biblioteca(self):
        return {self.nome : self.densidade()}
    

lista_de_paises = []
lista_de_densidades = []
for i in range(10):
    c = Pais(input('Nome: '), float(input('População: ')), float(input('Área: '))).biblioteca()
    lista_de_paises.append(c)


p1 = Pais('Brasil', 215000000, 8515.05).biblioteca()
p2 = Pais('Eua', 348667, 9147).biblioteca()
