def main():

    name = input()
    attack = int(input())
    deffense = int(input())
    life = int(input())
    damage = int(input())

    if damage - deffense < life:
        print(name + " sobreviveu!!!")
    else:
        print(name + " morreu :(")

if __name__ == "__main__":
    main()