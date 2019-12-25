import os
class pessoa:
    def __init__(self,nome,email,telefone,senha):
        self.nome = nome          # O nome é um atributo publico
        self.email = email        # O email é um atributo publico
        self.telefone = telefone  # O telefone é um atributo publico
        self.__senha = senha      # A senha é um argumento privado da classe

    def acessarPerfil(self):
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        # Se digitar o e-mail e senha corretos
        if email == self.email and senha == self.__senha:
            while True:
                os.system("clear")

                print(" ____________________ ")
                print("|O que deseja fazer? |")
                print("|--------------------|")
                print("| 1. Ver nome        |")
                print("| 2. Ver email       |")
                print("| 3. Ver telefone    |")
                print("| 4. Trocar Senha    |")
                print("| 5. sair            |")
                print("\\____________________/")

                opc = input()
                if opc == "1":
                    print(self.nome)

                elif opc == "2":
                    print(self.email)

                elif opc == "3":
                    print(self.telefone)

                elif opc == "4":
                    # Da classe, acesse essa funçao privada
                    print(self.__gerarNovaSenha())

                elif opc == "5":
                    break

                else:
                    print("Digite um valor válido!")

                i = input("<< pressione enter >>")
        else:
            print("Dados inválidos!")

    # Gera uma nova senha
    def __gerarNovaSenha(self):
        senhaDigitada = input("Digite a senha antiga: ")

        # se digitou a senha antiga
        if senhaDigitada == self.__senha:
            novaSenha = input("Digite a nova senha: ")
            # Atualize a senha privada a classe
            self.__senha = novaSenha
            return "Senha alterado com sucesso"

        return "A senha digitada é inválida!"

beatriz = pessoa("Beatriz Zara","abc@email.com","17987654321","bia123")
beatriz.acessarPerfil()
