consumo_por_km = float(input())
km_a_percorrer = float(input())
combustivel_no_carro = float(input())

divisao_distancia_consumo = km_a_percorrer / consumo_por_km
combustivel_a_pagar = abs(combustivel_no_carro - divisao_distancia_consumo)

if combustivel_no_carro >= divisao_distancia_consumo:
    print(0.0)
else:
    print("{:.1f}".format(combustivel_a_pagar))

# Meu cérebro já estava frito quando fui fazer isso, então taquei tudo em portugûes e dane-se.