N = int(input())

# parenteses1 = 0
# parenteses2 = 0
# colchetes1 = 0
# colchetes2 = 0
# chaves1 = 0
# chaves2 = 0

# res = []

# for _ in range(N):
#     caracteres = input()
#     parenteses1 += caracteres.count("(")
#     parenteses2 += caracteres.count(")")
#     colchetes1 += caracteres.count("[")
#     colchetes2 += caracteres.count("]")
#     chaves1 += caracteres.count("{")
#     chaves2 += caracteres.count("}")
#     if caracteres.__contains__("(") or caracteres.__contains__(")") or caracteres.__contains__("[") or caracteres.__contains__("]") or caracteres.__contains__("{") or caracteres.__contains__("}"):
#         if ((parenteses1 + parenteses2) % 2 == 0) and ((colchetes1 + colchetes2) % 2 == 0) and ((chaves1 + chaves2) % 2 == 0):
#             res.append("S")
#         else:
#             res.append("N")

# print(res)

# print(parenteses1,parenteses2,chaves1,chaves2,colchetes1,colchetes2)

parenteses = 0
colchetes = 0
chaves = 0

for _ in range(N):
    caracteres = input() 

print(parenteses,colchetes,chaves)