from collections import Counter

palavras = """meu nome é julia, eu gosto muito dos sistemas linerares que a preofessora passo na aula de equações linerares""".lower().split(' ')


palavras_cont = Counter(palavras)

print("Duas palavras mais frequentes")
print(palavras_cont.most_common(2))

print("Três palavras mais frequentes")
print(palavras_cont.most_common(3))

