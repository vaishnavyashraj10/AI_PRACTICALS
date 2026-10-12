import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i, value in enumerate(state):
        if value != 0:
            target = goal.index(value)
            distance += abs(i//3 - target//3)
            distance += abs(i%3 - target%3)
    return distance

def neighbors(state):
    zero = state.index(0)
    r, c = divmod(zero, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state)
            s[zero], s[j] = s[j], s[zero]
            yield tuple(s)

def solve():
    pq = [(heuristic(start), start)]
    visited = {start: None}

    while pq:
        _, state = heapq.heappop(pq)

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = visited[state]
            return path[::-1]

        for nxt in neighbors(state):
            if nxt not in visited:
                visited[nxt] = state
                heapq.heappush(pq, (heuristic(nxt), nxt))

path = solve()

for state in path:
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()