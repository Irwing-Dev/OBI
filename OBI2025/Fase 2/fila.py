N = int(input())
fila = list(map(int, input().split()))
K = int(input())
fila2 = list(map(int, input().split()))

for f in fila2:
    fila.remove(f)
print(*fila)