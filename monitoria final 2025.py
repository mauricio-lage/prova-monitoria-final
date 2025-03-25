import os

class Movies:
    def __init__(self, name, description, duration, synopsis):
        self.name = name
        self.description = description
        self.duration = duration
        self.synopsis = synopsis

class Sessions:
    def __init__(self):
        self._name = None
        self._seat_number = 0
        self._tax = 0
        self._brindes = {}
        self._movie = None
        self._value= 0


    def agendar_session(self, date, hour, value, movie):
        self._date = date
        self._hour = hour
        self._value = value
        self._movie = movie


    def set_name(self , name):
       self._name = name

    def get_name(self):
        return self._name

    def get_value(self):
     return self._value

    def get_movie(self):
        return self._movie

    def set_seat_number(self, number):
        self._seat_number = number

    def set_tax(self, tax):
        self._tax = tax

    def set_brindes(self, brindes):
        self._brindes = brindes



    def get_seat_number(self):
        return self._seat_number

    def get_tax(self):
        return self._tax

    def get_brindes(self):
        return self._brindes

    @staticmethod
    def get_session_basic ():
      sessions_basic = Sessions()
      sessions_basic.set_name("basic")
      sessions_basic.set_seat_number(20)
      sessions_basic.set_tax(0)
      sessions_basic.set_brindes({ 'Bonequinhos':0 ,  ' pipoca': 0 , 'Refrigerante':0 , "chocolate":0})
      return sessions_basic

    @staticmethod
    def get_session_XD ():
      sessions_XD = Sessions()
      sessions_XD.set_name("XD")
      sessions_XD.set_seat_number(20)
      sessions_XD.set_tax(10/100)
      sessions_XD.set_brindes({ 'Bonequinhos':1 ,  ' pipoca': 0 , 'Refrigerante':0 , "chocolate":0})
      return sessions_XD

    @staticmethod
    def get_session_Super():
      sessions_Super = Sessions()
      sessions_Super.set_name("Super")
      sessions_Super.set_seat_number(15)
      sessions_Super.set_tax(12/100)
      sessions_Super.set_brindes({ 'Bonequinhos':1 ,  ' pipoca': 1 , 'Refrigerante':0 , "chocolate":0})
      return sessions_Super

    @staticmethod
    def get_session_Luxo():
      sessions_Super = Sessions()
      sessions_Super.set_name("Super")
      sessions_Super.set_seat_number(10)
      sessions_Super.set_tax(15/100)
      sessions_Super.set_brindes({ 'Bonequinhos':1 ,  ' pipoca': 1 , 'Refrigerante':1 , "chocolate":1})
      return sessions_Super



class Bilheteria:
    def __init__(self):
        self.session_basic = Sessions.get_session_basic()
        self.session_XD = Sessions.get_session_XD()
        self.session_Super = Sessions.get_session_Super()
        self.session_Luxo = Sessions.get_session_Luxo()

        self.cadeira_session_basic = {}
        self.cadeira_session_XD = {}
        self.cadeira_session_Super = {}
        self.cadeira_session_Luxo = {}

        self.numero_de_cadeiras_vendidas_basic = 0
        self.numero_de_cadeiras_vendidas_XD = 0
        self.numero_de_cadeiras_vendidas_Super = 0
        self.numero_de_cadeiras_vendidas_Luxo = 0


        self.MontarCadeiras()

    def MontarCadeiras(self):
        self.cadeira_session_basic = {i: "|_|" for i in range(1, self.session_basic.get_seat_number() + 1)}
        self.cadeira_session_XD = {i: "|_|" for i in range(1, self.session_XD.get_seat_number() + 1)}
        self.cadeira_session_Super = {i: "|_|" for i in range(1, self.session_Super.get_seat_number() + 1)}
        self.cadeira_session_Luxo = {i: "|_|" for i in range(1, self.session_Luxo.get_seat_number() + 1)}

    def VenderCadeira(self, cadeira, session_name, nome_cliente, forma_pagamento):
        if session_name == "basic":
            if self.cadeira_session_basic[cadeira] == "|X|":
                print("Cadeira já vendida.")
            elif cadeira > self.session_basic.get_seat_number():
                print("Essa cadeira não está disponível.")
            else:
                self.cadeira_session_basic[cadeira] = "|X|"
                self.numero_de_cadeiras_vendidas_basic += 1
                print(f"Ingresso vendido para {nome_cliente} com pagamento via {forma_pagamento}.")
                valor_final = round((self.session_basic.get_value() *  self.session_basic.get_tax()),2)
                print(f'valor final do ingresso {valor_final}')
                os.system('cls')
                self.MostrarCadeiras( self.cadeira_session_basic)


        if session_name == "XD":

            if self.cadeira_session_XD[cadeira] == "|X|":
                print("Cadeira já vendida.")
            elif cadeira > self.session_XD.get_seat_number():
                print("Essa cadeira não está disponível.")
            else:
                self.cadeira_session_XD[cadeira] = "|X|"
                self.numero_de_cadeiras_vendidas_XD += 1
                print(f"Ingresso vendido para {nome_cliente} com pagamento via {forma_pagamento}.")
                valor_final = round((self.session_XD.get_value() *  self.session_XD.get_tax()),2)
                print(f'valor final do ingresso {valor_final}')
                os.system('cls')
                self.MostrarCadeiras( self.cadeira_session_XD)


        if session_name == "Super":


            if self.cadeira_session_Super[cadeira] == "|X|":
                print("Cadeira já vendida.")
            elif cadeira > self.session_Super.get_seat_number():
                print("Essa cadeira não está disponível.")
            else:
                self.cadeira_session_Super[cadeira] = "|X|"
                self.numero_de_cadeiras_vendidas_Super += 1
                print(f"Ingresso vendido para {nome_cliente} com pagamento via {forma_pagamento}.")
                valor_final = round((self.session_Super.get_value() *  self.session_Super.get_tax()),2)
                print(f'valor final do ingresso {valor_final}')
                os.system('cls')

                self.MostrarCadeiras(self.cadeira_session_Super)

        if session_name == "Luxo":
            if self.cadeira_session_Luxo[cadeira] == "|X|":
                print("Cadeira já vendida.")
            elif cadeira > self.session_Luxo.get_seat_number():
                print("Essa cadeira não está disponível.")
            else:
                self.cadeira_session_Luxo[cadeira] = "|X|"
                self.numero_de_cadeiras_vendidas_Luxo += 1
                print(f"Ingresso vendido para {nome_cliente} com pagamento via {forma_pagamento}.")
                valor_final = round((self.session_Super.get_value() *  self.session_Super.get_tax()),2)
                print(f'valor final do ingresso {valor_final}')
                os.system('cls')
                self.MostrarCadeiras( self.cadeira_session_Luxo)




    def MostrarCadeiras(self, cadeiras):
        for i, (chave, valor) in enumerate(cadeiras.items(), 1):
            print(f"{chave}: {valor}", end=" | " if i % 5 != 0 else "\n")


class CineBCtec:
    def __init__(self):
        self.Bilheteria = Bilheteria()
        self.cadastrada = {
            1: False,
            2: False,
            3: False,
            4: False
        }

        self.salas = {
            1: {"Nome": "Básica", "Numero de Cadeiras": 20, "Acréscimo": "0%", "Brinde": "Sem brindes"},
            2: {"Nome": "XD", "Numero de Cadeiras": 20, "Acréscimo": "10%", "Brinde": "Bonequinho do BCTec"},
            3: {"Nome": "Super Confortável", "Numero de Cadeiras": 15, "Acréscimo": "12%", "Brinde": "Bonequinho do BCTec, mais um combo de pipoca"},
            4: {"Nome": "Luxo", "Numero de Cadeiras": 10, "Acréscimo": "15%", "Brinde": "Bonequinho do BCTec, mais um combo de pipoca, refrigerante e chocolate"},
        }

    def mostrar_salas(self):
        print("Salas disponíveis:")
        for num, sala in self.salas.items():
            if not self.cadastrada[num]:
                print(f"{num} - Nome: {sala['Nome']}, Numero de Cadeiras: {sala['Numero de Cadeiras']}, Porcentagem de acréscimo: {sala['Acréscimo']}, Brinde: {sala['Brinde']} - Não Cadastrada")
            else:
                print(f"{num} - Nome: {sala['Nome']} - Sala Cadastrada ")

    def cadastrar_sala(self, numero):
        if numero in self.salas:
            if(self.cadastrada[numero] == False):
                self.cadastrada[numero] = True
                date = input("Digite o dia:")
                hour = input("Digite a hora:")
                value = float(input("Digite o preço do ingresso: "))
                movie = input("Digite o nome do filme:")

                if(numero == 1):
                    self.Bilheteria.session_basic.agendar_session(date, hour, value, movie)
                    filme = self.Bilheteria.session_basic.get_movie()
                    valor = self.Bilheteria.session_basic.get_value() * (1 +self.Bilheteria.session_basic.get_tax())
                elif(numero == 2):
                    self.Bilheteria.session_XD.agendar_session(date, hour, value, movie)
                    filme = self.Bilheteria.session_XD.get_movie()
                    valor = self.Bilheteria.session_XD.get_value() * (1+ self.Bilheteria.session_XD.get_tax())
                elif(numero == 3):
                        self.Bilheteria.session_Super.agendar_session(date, hour, value, movie)
                        filme = self.Bilheteria.session_Super.get_movie()
                        valor = self.Bilheteria.session_Super.get_value() * (1+ self.Bilheteria.session_Super.get_tax())
                elif(numero == 4):
                    self.Bilheteria.session_Luxo.agendar_session(date, hour, value, movie)
                    filme = self.Bilheteria.session_Luxo.get_movie()
                    valor = self.Bilheteria.session_Luxo.get_value() * (1 + self.Bilheteria.session_Luxo.get_tax())
            else:
                print("Essa sala já estar cadastrada")

            print('\n\n')
            print(f"Sala {numero} cadastrada com sucesso!")

            print(f"Filme: {filme} | Ingresso: R$ {valor:.2f}")

            print('\n\n')




        else:
            print("Número de sala inválido!")



    def vender_ingresso(self):
        while(True):
              self.mostrar_salas()

              sala_selecionada = int(input("Selecione uma sala CADASTRADA para Vender os Ingressos ou  Digite Zero para Sair "))

              if sala_selecionada == 1:
                  if(self.cadastrada[sala_selecionada] == True):
                     cadeira = int(input("Escolha o número da cadeira: "))
                     nome_cliente = input("Digite o nome do cliente: ")
                     forma_pagamento = input("Digite a forma de pagamento (ex: Cartão, Dinheiro, Pix): ")

                     self.Bilheteria.VenderCadeira(cadeira, "basic", nome_cliente, forma_pagamento)
                  else:
                      print("Essa sala não foi definida")
              elif sala_selecionada == 2:
                  if(self.cadastrada[sala_selecionada] == True):
                     cadeira = int(input("Escolha o número da cadeira: "))
                     nome_cliente = input("Digite o nome do cliente: ")
                     forma_pagamento = input("Digite a forma de pagamento (ex: Cartão, Dinheiro, Pix): ")


                     self.Bilheteria.VenderCadeira(cadeira, "XD", nome_cliente, forma_pagamento)
                  else:
                      print("Essa sala não foi definida")
              elif sala_selecionada == 3:
                  if(self.cadastrada[sala_selecionada] == True):
                     cadeira = int(input("Escolha o número da cadeira: "))
                     nome_cliente = input("Digite o nome do cliente: ")
                     forma_pagamento = input("Digite a forma de pagamento (ex: Cartão, Dinheiro, Pix): ")


                     self.Bilheteria.VenderCadeira(cadeira, "Super", nome_cliente, forma_pagamento)
                  else:
                      print("Essa sala não foi definida")
              elif sala_selecionada == 4:
                  if(self.cadastrada[sala_selecionada] == True):
                     cadeira = int(input("Escolha o número da cadeira: "))
                     nome_cliente = input("Digite o nome do cliente: ")
                     forma_pagamento = input("Digite a forma de pagamento (ex: Cartão, Dinheiro, Pix): ")
                     self.Bilheteria.VenderCadeira(cadeira, "Luxo", nome_cliente, forma_pagamento)
                  else:
                      print("Essa sala não foi definida")
              elif  sala_selecionada == 0:
                  break

    def definir_sessoes(self):
         while True:
            self.mostrar_salas()
            num = int(input("Digite o número da sala para cadastrar, ou zero para sair: "))
            if num == 0:
                break

            self.cadastrar_sala(num)






    def gerar_relatorios_vendas(self):

        Salas = {
            "Básico": {
                "Ingressos vendidos": self.Bilheteria.numero_de_cadeiras_vendidas_basic,
                "Brindes vendidos": {brinde: quantidade for brinde, quantidade in self.Bilheteria.session_basic.get_brindes().items()},
                "Valor total arrecadado": self.Bilheteria.numero_de_cadeiras_vendidas_basic * (self.Bilheteria.session_basic.get_value() * (1 + self.Bilheteria.session_basic.get_tax()))
            },
            "XD": {
                "Ingressos vendidos": self.Bilheteria.numero_de_cadeiras_vendidas_XD,
                "Brindes vendidos": {brinde: quantidade for brinde, quantidade in self.Bilheteria.session_XD.get_brindes().items()},
                "Valor total arrecadado": self.Bilheteria.numero_de_cadeiras_vendidas_XD * (self.Bilheteria.session_XD.get_value() * (1 + self.Bilheteria.session_XD.get_tax()))
            },
            "Super Confortável": {
                "Ingressos vendidos": self.Bilheteria.numero_de_cadeiras_vendidas_Super,
                "Brindes vendidos": {brinde: quantidade for brinde, quantidade in self.Bilheteria.session_Super.get_brindes().items()},
                "Valor total arrecadado": self.Bilheteria.numero_de_cadeiras_vendidas_Super * (self.Bilheteria.session_Super.get_value() * (1 + self.Bilheteria.session_Super.get_tax()))
            },
            "Luxo": {
                "Ingressos vendidos": self.Bilheteria.numero_de_cadeiras_vendidas_Luxo,
                "Brindes vendidos": {brinde: quantidade for brinde, quantidade in self.Bilheteria.session_Luxo.get_brindes().items()},
                "Valor total arrecadado": self.Bilheteria.numero_de_cadeiras_vendidas_Luxo * (self.Bilheteria.session_Luxo.get_value() * (1 + self.Bilheteria.session_Luxo.get_tax()))
            }
        }

        print("\n===== RELATÓRIO DE VENDAS =====\n")
        for nome_sala, dados in Salas.items():
            print(f" Sala: {nome_sala}")
            print(f"Ingressos vendidos: {dados['Ingressos vendidos']}")
            print(" Brindes vendidos:")
            for brinde, quantidade in dados["Brindes vendidos"].items():
                print(f"   - {brinde}: {quantidade * dados['Ingressos vendidos'] } unidades")
            print(f"Valor total arrecadado: R$ {dados['Valor total arrecadado']:.2f}")
            print("-" * 40)





    def run(self):
        print("Bem-vindo ao sistema CineBCTEC")
        self.definir_sessoes()
        os.system('cls')


        while True:
            operação = input(
                "Digite:\n"
                "1 - Para vender ingresso\n"
                "2 - Para definir uma sala\n"
                "3 - Para gerar relatório de vendas\n"
                "4 - Para sair\n"
                "Opção: "
            )

            if operação == "1":
                self.vender_ingresso()
            elif operação == "2":
                self.definir_sessoes()
            elif operação == "3":
                self.gerar_relatorios_vendas()
            elif operação == "4":
                break
            else:
                print("Opção inválida, tente novamente.")



        print("Sistema encerrado!")


if __name__ == "__main__":
    Cinema = CineBCtec()
    Cinema.run()
