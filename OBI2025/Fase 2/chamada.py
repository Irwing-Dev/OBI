[n,k] = [int(x) for x in input().split()]
people = []

for _ in range(n):
    p = input()
    people.append(p)

people.sort()

print(people[k-1])