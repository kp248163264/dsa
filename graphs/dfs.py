


def dfs(g):

    visited.add(g)

    for n in neighbors[g]:
        if n not in visited:
            dfs(n)