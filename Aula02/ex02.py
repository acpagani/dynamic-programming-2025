clima = input("Qual o clima de hoje? ")

programacao = ""

if clima == "ensolarado":
    programacao = "dia de futebol e churrasco"
elif clima == "nublado":
    programacao = "dia de ler um livro"
elif clima == "chuvoso":
    programacao = "dia de filme e série"
elif clima == "nevando":
    programacao = "dia de tomar café e chocolate quente"
else:
    programacao = "dia de nada"