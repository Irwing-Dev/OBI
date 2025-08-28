def main():
    n = list(map(int, input()))
    k = list(map(int, input()))
    list_n = []
    list_k = []
    num_n = 0
    num_k = 0
    
    diff = abs(len(n) - len(k))
    
    if len(n) > len(k):
        for _ in range(diff):
            k.insert(0, 0)
    elif len(n) < len(k):
        for _ in range(diff):
            n.insert(0, 0)
    
    for f in range(len(n)):
        if n[f] > k[f]:
            list_n.append(n[f])
        elif n[f] < k[f]:
            list_k.append(k[f])
        elif n[f] == k[f]:
            list_k.append(k[f])
            list_n.append(n[f])
    
    for s in range(len(list_n)):
        num_n += list_n[s]*10**(len(list_n)-1-s)
    for s in range(len(list_k)):
        num_k += list_k[s]*10**(len(list_k)-1-s)
    if len(list_k) == 0:
        num_k = -1
    elif len(list_n) == 0:
        num_n = -1
    print(num_k, num_n)
    

if __name__ == "__main__":
    main()