def main():
    n, k = map(int, input().split())
    players = []
    times = [[] for _ in range(k)]
    for _ in range(n):
        j, p = input().split()
        players.append((j, int(p)))

    players.sort(key=lambda x: -x[1])
    
    for i, (player, _) in enumerate(players):
        times[i % k].append(player)
    
    for i in range(k):
        print(f"Time {i+1}")
        for p in sorted(times[i]):
            print(p)
        print()
    
    
if __name__ == "__main__":
    main()