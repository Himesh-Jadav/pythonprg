# Best batsman, wicket-taker and team
teams = {
    "India": {"Virat": (80, 0), "Bumrah": (10, 3)},
    "Australia": {"Smith": (60, 0), "Starc": (15, 2)}
}

runs, wickets, totals = {}, {}, {}
for team, players in teams.items():
    totals[team] = 0
    for name, (r, w) in players.items():
        runs[name] = r
        wickets[name] = w
        totals[team] += r

print("Best batsman:", max(runs, key=runs.get))
print("Top wicket-taker:", max(wickets, key=wickets.get))
print("Best team:", max(totals, key=totals.get))
