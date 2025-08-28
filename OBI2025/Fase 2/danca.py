def main():
    [line, col, steps] = map(int, input().split())
    matriz = [[0 for _ in range(col)] for _ in range(line)]
    index = 1
    for i in range(line):
        for j in range(col):
            matriz[i][j] = index
            index += 1
    
    for _ in range(steps):
        [position, n_str, k_str] = map(str, input().split())
        n = int(n_str)
        k = int(k_str)
        if position == "C":
            for i in range(line):
                nums = []
                nums.append(matriz[i][n-1])
                nums.append(matriz[i][k-1])
                matriz[i][n-1] = nums.pop()
                matriz[i][k-1] = nums.pop()
        elif position == "L":
            for i in range(col):
                nums = []
                nums.append(matriz[n-1][i])
                nums.append(matriz[k-1][i])
                matriz[n-1][i] = nums.pop()
                matriz[k-1][i] = nums.pop()

    for l in matriz:
        print(*l)

if __name__ == "__main__":
    main()