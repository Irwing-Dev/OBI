def main():
    N = int(input())
    sum_of_broken_glasses = 0

    for _ in range(N):
        [l,c] = list(map(int, input().split()))
        difference = c - l
        if difference < 0:
            sum_of_broken_glasses += c

    print(sum_of_broken_glasses)

if __name__ == "__main__":
    main()
