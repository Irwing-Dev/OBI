# Cálculo rápido - Turno B

S = int(input())
A = int(input())
B = int(input())

index = 0

for x in range(A, (B + 1)):
    arr = [int(d) for d in str(x)]
    summart = 0
    for n in range(0, len(arr)):
        summart += arr[n]
    if summart == S:
        index += 1

print(index)