
def construct_candidates(a,k,input,c,ncandidates):
    NMAX = 100
    in_sol = [False]*NMAX
    for i in range(k):
        in_sol[a[i]] = True

    ncan = 0
    most_recent_node = a[k-1]

    if k == 1:
        c[0] = 0
        ncandidates[0] = 1
        return


    neighbors = input[most_recent_node]
    for n in neighbors:
        if not in_sol[n]:
            c[ncan] = n
            ncan+=1
    ncandidates[0] = ncan


def is_a_solution(a,k,input):
    return a[k] == len(input)-1

def process_solution(a,k,t):
    newline = "\n"
    for i in range(1, k+1):
        print(f" -> {a[i]}")
    print(f"{newline}")



def backtrack(a,k,input):
    NMAX = 100
    c = [0] * NMAX
    ncandidates = [NMAX]

    if is_a_solution(a,k,input):
        process_solution(a,k,input)
    else:
        k += 1
        construct_candidates(a,k,input,c,ncandidates)
        for i in range(ncandidates[0]):
            a[k] = c[i]
            backtrack(a,k,input)
    return


def all_paths_from_source_to_target(graph):
    """Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to
    node n - 1 and return them in any order.

    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed
    edge from node i to node graph[i][j])."""

    NMAX = 100
    a = [0] * NMAX
    backtrack(a, 0, graph)


if __name__ == "__main__":
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    all_paths_from_source_to_target(graph)

