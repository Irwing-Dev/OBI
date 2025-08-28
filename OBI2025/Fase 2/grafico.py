N = int(input())
H = [int(x) for x in input().split()]
maximum = 0
for h in H:
    if h > maximum:
        maximum = h
    
matriz = [[0 for _ in range(N)] for _ in range(maximum)]

for i in range(maximum):
    for j in range(N):
        if H[j] >= maximum - i:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0


for line in matriz:
    print(*line)