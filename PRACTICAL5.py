import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    total = 0
    for i, v in enumerate(state):
        if v:
            j = goal.index(v)
            total += abs(i//3 - j//3) + abs(i%3 - j%3)
    return total

def neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr*3 + nc
            s = list(state)
            s[z], s[j] = s[j], s[z]
            yield tuple(s)

def astar():
    pq = [(h(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        _, g, state = heapq.heappop(pq)

        if g != cost[state]:
            continue

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in neighbors(state):
            new_g = g + 1
            if new_g < cost.get(nxt, float("inf")):
                cost[nxt] = new_g
                parent[nxt] = state
                heapq.heappush(pq, (new_g+h(nxt), new_g, nxt))

path = astar()
for state in path:
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()