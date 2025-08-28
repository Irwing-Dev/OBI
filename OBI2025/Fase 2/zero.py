N = int(input())
arr = []
soma = 0

for i in range(N):
    s = int(input())
    if s == 0:
        arr.pop()
    else:
        arr.append(s)

for a in arr:
    soma += a

if len(arr) == 0:
    print(0)
else:
    print(soma)