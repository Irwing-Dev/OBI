# Quadrado Mágico (OBI 2007)

def main():
    N = int(input())
    matriz = [list(map(int, input().split())) for _ in range(N)]

    summ_expected = sum(matriz[0])

    for i in range(N):
        if sum(matriz[i]) != summ_expected:
            print(-1)
            return

    for j in range(N):
        if sum(matriz[i][j] for i in range(N)) != summ_expected:
            print(-1)
            return

    if sum(matriz[i][i] for i in range(N)) != summ_expected:
        print(-1)
        return

    if sum(matriz[i][N-1-i] for i in range(N)) != summ_expected:
        print(-1)
        return

    print(summ_expected)


if __name__ == "__main__":
    main()
