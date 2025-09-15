# Fila

N = int(input())
H = list(map(int, input().split()))

i = 0
higher = 0

for s in reversed(H):
    if s > higher:
        higher = s
    else:
        i += 1

print(i)