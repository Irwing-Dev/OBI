# Arara!

araras, gaiolas = map(int, input().split())

if gaiolas <= ((araras - 1) * 5):
    print("N")
else:
    print("S")