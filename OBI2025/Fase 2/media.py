def main():
    [a,b] = map(int, input().split())
    c = 0

    media = (a + b)//3

    if media == 0:
        print(media)
    else:
        while media > 0 or media < 0:
            c += 1
            print(c)

if __name__ == "__main__":
    main()