class Times:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
        self.jogadores = []
    def set_id(self, i):
        if i >= 0: self.__id = i
        else: raise ValueError
    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def set_estado(self, e):
        if len(e) > 0: self.__estado = e
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
    def jogadores(self):
        return self.jogadores()
    def __str__(self):
        return f'ID: {self.get_id()} | NOME: {self.get_nome()} | ESTADO: {self.get_estado()}'

class Jogadores(Times):
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)
    def set_id(self, i):
        if i >= 0: self.__id = i
        else: raise ValueError
    def set_idTime(self, it):
        if it >= 0: self.__it = it
        else: raise ValueError
    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def set_camisa(self, c):
        if c >= 0: self.__camisa = c
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_it(self):
        return self.__it
    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def __str__(self): 
        return f'ID : {self.get_id()} | IdTime : {self.get_it()} | Nome : {self.get_nome()} | Camisa : {self.get_camisa()}'

class UI():
    lista_de_times = []
    def main():
        pass
    def menu():
        pass
    @classmethod
    def inserir_time(cls):
        id = int(input('Informe o ID do time: '))
        nome = input('Informe o nome do Time: ')
        estado = input('Informe o nome do Estado do time: ')
        time = Times(id, nome, estado)
        cls.lista_de_times.append(time)
    @classmethod
    def listar_time(cls):
        for i in cls.lista_de_times: print(i)
    @classmethod
    def atualizar_time(cls):
        UI.listar_time()
        id = int(input('Informe o ID do time que você deseja fazer a alteração: '))
        for i in cls.lista_de_times: 
            if i.get_id() == id: 
                i.set_nome(input('Informe o novo nome: '))
                i.set_estado(input('Informe o novo nome do Estado: '))
    @classmethod
    def excluir_time(cls):
        UI.listar_time()
        id = int(input('Informe o ID do time que você deseja excluir: '))
        for i in cls.lista_de_times:
            if i.get_id() == id:
                cls.lista_de_times.remove(i)
    @classmethod
    def inserir_jogador(cls): 
        id = int(input('Informe o ID do Jogador: '))
        it = int(input('Informe o ID do seu time: '))
        nome = input('Informe o nome do jogador: ')
        camisa = input('Informe o número da camisa do seu jogador: ')
        jogadores = Jogadores(id, it, nome, camisa)
        for i in cls.lista_de_times:
            if i.id == id:
                i.adicionar_jogador(jogadores)
    def listar_jogador():
        pass
    def atualizar_jogador():
        pass
    def excluir_jogador():
        pass
    def listar_jogadores_do_time():
        pass
    def transferir_jogador():
        pass



"""""
Um time precisa herdar todas as informações dos jogadore? 




"""