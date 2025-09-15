# Alfabeto Alienígena

[k, n] = [int(x) for x in input().split()]

K = str(input())
N = str(input())

alien_alphabet = set(K)
phrase = set(N)
difference_of_conjunts = phrase.difference(alien_alphabet)

if len(difference_of_conjunts) > 0:
    print("N")
else:
    print("S")