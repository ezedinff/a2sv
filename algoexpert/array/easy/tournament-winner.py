def getTournamentWinner(competions, results):
    d = {}
    for i in range(len(competions)):
        if results[i] == 0:
            d[competions[i][1]] = d.get[competions[i][1], 0] + 3
        else:
            d[competions[i][0]] = d.get[competions[i][0], 0] + 3
    return max(d, key=d.get)