N = int(input())
friend = []
msg = []
for s in range(N):
    X = [str(x) for x in input().split()]
    msg.append(X[0])
    friend.append(int(X.pop()))

print(msg, friend)