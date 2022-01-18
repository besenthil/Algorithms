# O(n) - time
# o(n) - space
def tournamentWinner(competitions, results):
    hash_points = {}
    for fight, teams in enumerate(competitions):
        winner = 0 if results[fight] else 1
        hash_points[competitions[fight][winner]] = hash_points.get((competitions[fight][winner]), 3) + 3
    current_winner = ''
    current_points = 0
    for item in hash_points.items():
        if item[1] > current_points:
            current_winner = item[0]
            current_points = item[1]

    return current_winner