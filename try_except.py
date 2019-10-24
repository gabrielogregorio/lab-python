try: # Tente
    # Descomente um comando.
    print(0/0)                 # divisão por zero
    #print("gabriel" / 10)      # dividindo string por número
    #print("Iai, tudo beleza?") # Exibindo uma mensagem na tela

except ZeroDivisionError: # Capturando um erro especifico
    print("Você não pode dividir um número por zero!")

except Exception as erro: # Capturando qualquer erro
    print("Aconteceu um erro ",erro)

else: # Se não acontecer nenhum erro
    print("Não aconteceu nenhum erro")

finally: # Em qualquer caso
    print("Tentativa finalizada")
