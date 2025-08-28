# ------------------------------------------------------------------------ SOMA DAS LINHAS -----------------------------------------------------------------------------

# def main():
#     matriz = []

#     for _ in range(3):
#         line = []
#         for _ in range(3):
#             s = int(input())
#             line.append(s)
#         matriz.append(line)

#     for i, line in enumerate(matriz):
#         sum_of_lines = sum(line)

#         print(f"Linha {i}: {sum_of_lines}")



# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------ SOMA DAS COLUNAS -----------------------------------------------------------------------------

# def main():
#     matriz = []
#     sum_of_col = 0

#     for _ in range(3):
#         line = []
#         for _ in range(3):
#             s = int(input())
#             line.append(s)
#         matriz.append(line)

#     for i in range(3):
#         for j in range(3):
#             sum_of_col += matriz[j][i]    
#         print(f"Coluna {i}: {sum_of_col}")
#         sum_of_col = 0
            



# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------ SOMA DAS DIAGONAIS -----------------------------------------------------------------------------

# def main():
#     matriz = []

#     for _ in range(3):
#         line = []
#         for _ in range(3):
#             s = int(input())
#             line.append(s)    
#         matriz.append(line)

#     acc_dig = sum(matriz[i][i] for i in range(3))
#     acc_dig2 = sum(matriz[i][3-1-i] for i in range(3))

#     print(f"Diagonal principal: {acc_dig}")
#     print(f"Diagonal secundaria: {acc_dig2}")


# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------ SUBSTITUIÇÃO DO MAIOR -----------------------------------------------------------------------------

# def main():
#     matriz = []
#     h = 0

#     for _ in range(3):
#         line = []
#         for _ in range(3):
#             s = int(input())
#             line.append(s)
#         matriz.append(line)

#     for i in range(len(matriz)):
#         for j in range(len(matriz)):
#             if matriz[i][j] >= h:
#                 h = matriz[i][j]

#     for i in range(len(matriz)):
#         for j in range(len(matriz)):
#             if matriz[i][j] == h:
#                 matriz[i][j] = -1
    
#     for l in matriz:
#         print(" ".join(map(str, l)))

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------ MATRIZ ESCADA -----------------------------------------------------------------------------
# ------------------------------------------------------------------------ NÃO COMPLETADO ----------------------------------------------------------------------------

# def main():
#     [n,k] = [int(x) for x in input().split()]
#     matriz = []
#     diff = 0

#     for _ in range(n):
#         lines = [int(x) for x in input().split()]
#         matriz.append(lines)

#     for i in range(1, n):
#         for j in range(k):
#             if i+1 < len(matriz) - 1:
#                 if matriz[i][j] != 0 and matriz[i+1][j] != 0:
#                     diff = 1
#                     break
#                 else: 
#                     continue
#             else:
#                 if matriz[i][j] != 0:
#                     diff = 0

#     if diff == 1:
#         print("N")
#     else:
#         print("S")


# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------ DETERMINANTE DA MATRIZ -----------------------------------------------------------------------------

# def main():
#     matriz = []
#     for _ in range(3):
#         line = [int(x) for x in input().split()]
#         matriz.append(line)
    
#     left_side = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1])
#     right_side = (matriz[0][0] * matriz[1][2] * matriz[2][1]) + (matriz[0][1] * matriz[1][0] * matriz[2][2]) + (matriz[0][2] * matriz[1][1] * matriz[2][0])
#     determinant = left_side - right_side

#     print(determinant)


# if __name__ == "__main__":
#     main()