def partition(players):
    for i in range(len(players)):
        if players[i][0] >= 'A' and players[i][0] <= 'M':
            print(players[i])

partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])