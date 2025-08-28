def main():
    line, elements = map(int, input().split())
    list_of_elements = [int(x) for x in input().split()]
    list_of_acc = []
    for _ in range(elements):
        pos1, pos2 = map(int, input().split())
        acc = 0
        for i in range(pos1-1, pos2):
            acc += list_of_elements[i]
        list_of_acc.append(acc)
    
    prefix = [0] * (line + 1)
    print(prefix)

if __name__ == "__main__":
    main()