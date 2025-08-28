def main():
    N = int(input())
    quadrados_por_fita = list(map(int, input().split()))
    acc = 0
    higher = 0
    for qf in range(len(quadrados_por_fita)):
        if quadrados_por_fita[qf] == -1:
            acc += 1
            quadrados_por_fita[qf] = acc
        else:
            acc = 0
    
    print(quadrados_por_fita, higher)
    
if __name__ == "__main__":
    main()