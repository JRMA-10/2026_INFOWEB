class Agua: 
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
    def calculo(self):
        primeiro = self.consumo - 10
        segundo = primeiro - 10
        terceiro = self.consumo - segundo
        valor = 0
        if primeiro <= 0: valor += 38
        elif segundo <= 10: valor += segundo * 5
        elif terceiro > 0: valor += terceiro * 6
        return valor

p1 = Agua(1, 2010, 31)
print(p1.calculo())