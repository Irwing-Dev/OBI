mensagem = input()

divertido = mensagem.count(":-)")
chateado = mensagem.count(":-(")

if divertido > chateado:
    print("divertido")
elif chateado > divertido:
    print("chateado")
else:
    print("neutro")