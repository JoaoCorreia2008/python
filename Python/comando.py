class ComandoTv:
    def __init__(self,marca,ano_fabrico,canal):
        self.marca = marca
        self.ano_fabrico = ano_fabrico
        self.canal = canal
        self.volume = 0
        self.ligado = False

    def mudarCanal(self,novo_canal):
        if novo_canal < 1 or novo_canal > 99:
            novo_canal = self.canal
            print("Canal Invalido")
        return novo_canal
    def alterarVolume(self,sinal):
        if self.volume > 0 and sinal == '-':
            self.volume -= 1
        if self.volume < 50 and sinal == '+':
            self.volume += 1

    def mute(self):
        self.volume = 0
    
    def on_of(self):
        if self.ligado == True:
            self.ligado = False
            print("Comando ligado")
        else:
            self.ligado = True
            print("Comando ligado")

    def dadosAtuais (self):
        return f'O Comando {self.marca} de {self.ano_fabrico} está no canal {self.canal}'


c = ComandoTv('LG',1999,32)

c.alterarVolume('+')
c.alterarVolume('+')
c.alterarVolume('+')
c.alterarVolume('+')

print(c.dadosAtuais())

       
        