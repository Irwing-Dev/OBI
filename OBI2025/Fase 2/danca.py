def main():
    [line, col, steps] = map(int, input().split())
    lines = list(range(line))
    cols = list(range(col))
    
    for _ in range(steps):
        [position, n_str, k_str] = map(str, input().split())
        n = int(n_str) - 1
        k = int(k_str) - 1
        if position == "C":
            cols[n], cols[k] = cols[k], cols[n]
        elif position == "L":
            lines[n], lines[k] = lines[k], lines[n]

    for i in range(line):
        l = []
        for j in range(col):
            elements = lines[i] * col + cols[j] + 1
            l.append(elements)
        print(*l)

if __name__ == "__main__":
    main()