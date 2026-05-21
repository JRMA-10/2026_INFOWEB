from datetime import datetime

class Paciente: 
    def __init__(self, cpf, telefone, nascimento):
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_cpf(self, c):
        if len(c) == 11: self.__cpf = c
        else: raise ValueError
        int(self.__cpf)
    def set_telefone(self, t): 
        if len(t) == 11: self.__telefone = t
        else: raise ValueError
    def set_nascimento(self, n):
        self.__nascimento = n
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento
    def idade(self):
        data_atual = datetime.now()
        x = data_atual - self.get_nascimento()
        anos = x.days // 365 
        meses = x.days % 365 // 30
        return anos, meses
    def __str__(self):
        pass

class PacienteUI:
    def main():
        pass
    def menu():
        pass
    def inserir():
        cpf = input('Informe o seu CPF: \n').strip()
        telefone = input('Informe o seu telefone: \n').strip()
        nascimento = datetime.strptime(input("Informe a data de nascimento: "), '%d/%m/%Y')
        x = Paciente(cpf, telefone, nascimento)
    def listar():
        pass
    def atualizar(): 
        pass
    def excluir(): 
        pass
    def pesquisar():
        pass