def dfs():
    stack = [((0, 0), [(0, 0)])]
    visited = set()

    while stack:
        (a, b), path = stack.pop()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        if a == 2 or b == 2:
            return path

        p = min(a, 3 - b)
        q = min(b, 4 - a)

        next_states = [
            (4, b), (a, 3), (0, b), (a, 0),
            (a-p, b+p), (a+q, b-q)
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state, path + [state]))

    return None

result = dfs()
print("Solution path:")
for state in result:
    print(state)