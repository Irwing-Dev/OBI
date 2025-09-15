# Pirâmide

def main():

    N = int(input())

    matriz = [[0 for _ in range(N)] for _ in range(N)]
    base = 0
    camada = 1
    fim = N - 1

    while base <= fim:
        for i in range(base, fim + 1):
            for j in range(base, fim + 1):
                matriz[i][j] = camada
        camada += 1
        base += 1
        fim -= 1

    for l in range(N):
        print(" ".join(map(str, matriz[l])))

if __name__ == "__main__":
    main()