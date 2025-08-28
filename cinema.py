ia = int(input())
ib = int(input())

r_ia = 0
r_ib = 0

if ia > 0 and ia <= 17:
    r_ia = 15
if ib > 0 and ib <= 17:
    r_ib = 15
if ia > 17 and ia <= 59:
    r_ia = 30
if ib > 17 and ib <= 59:
    r_ib = 30
if ia > 59:
    r_ia = 20
if ib > 59:
    r_ib = 20


# if ia > 17 and ia <= 59 or ib > 17 and ib <= 59:
#     r_ia = 30
#     r_ib = 30
# if ia > 59 or ib > 59:
#     r_ia = 20
#     r_ib = 20

print(r_ia + r_ib)