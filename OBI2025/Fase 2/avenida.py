D = int(input())

summ = 0

if D == 2000:
    summ = 0
elif D < 2000 and D >= 1800:
    summ = 2000 - D
elif D > 1600 and D < 1800:
    summ = D - 1600
elif D == 1600:
    summ = 0
elif D < 1600 and D >= 1200:
    summ = 1600 - D
elif D > 1200 and D < 1400:
    summ = D - 1200
elif D == 1200:
    summ = 0
elif D < 1200 and D >= 1000:
    summ = 1200 - D
elif D > 800 and D < 1000:
    summ = D - 800
elif D == 800:
    summ = 0
elif D < 800 and D >= 600:
    summ = 800 - D
elif D > 400 and D < 600:
    summ = D - 400
elif D == 400:
    summ = 0
elif D < 400 and D >= 200:
    summ = 400 - D
elif D > 0 and D < 200:
    summ = D - 0
elif D == 0:
    summ = 0

print(summ)

# Sucessfully