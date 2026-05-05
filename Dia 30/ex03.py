class Pais:
    def __init__(self, id, nome, populacao, area): 
        self.set_id(id)
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)
    def set_id(self, i):
        if i >= 0: self.__id = i
        else: raise ValueError
    def set_nome(self, n):
        if len(n) == 0: raise ValueError
        else: self.__nome = n
    def set_populacao(self, p):
        if p >= 0: self.__populacao = p
        else: raise ValueError
    def set_area(self, a):
        if a > 0: self.__area = a
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.get_populacao / self.get_area
    def __str__(self):
        return f'Id: {self.get_id()} | Nome: {self.get_nome()} | População: {self.get_populacao()} | Área: {self.get_area():.2f} | Densidade demográfica: {self.densidade():.2f}'

class PaisUI:
    paises = []
    @staticmethod
    def main():
        pass
    def menu():
        pass 
    @classmethod
    def inserir(cls):
        id = int(input('Digite o ID do País: \n'))
        nome = input('Digite o nome do País: \n')
        populacao = int(input('Digite a população do País: \n'))
        area = float(input('Digite a área: '))
        o = Pais(id, nome, populacao, area)
        cls.paises.append(o)
    def listar():
        print(n for n in cls.paises)
    def atualizar():
        pass
    def excluir():
        pass
    def mais_populoso():
        pass
    def mais_povoado():
        pass