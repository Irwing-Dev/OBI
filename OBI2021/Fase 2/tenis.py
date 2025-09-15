# Duplas de tênis - Turno A

# ChatGPT
a = int(input())
b = int(input())
c = int(input())
d = int(input())

diff1 = abs((a + b) - (c + d))
diff2 = abs((a + c) - (b + d))
diff3 = abs((a + d) - (b + c))

res = min(diff1, diff2, diff3)

print(res)