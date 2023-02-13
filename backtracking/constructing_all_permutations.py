from backtracking.backtrack_template import backtrack

def is_a_solution(a,k,n):
    return k == n

def construct_candidates_nonoptimal(a, k, n, c, ncandidates):
    """
    c will be an array with values up to n not already in a
    """
    all_values_up_to_n = [i for i in range(n+1)]
    for v in all_values_up_to_n:
        if v not in a:
            c.append(v)
    ncandidates[0] = len(c)

def construct_candidates_optimal(a, k, n, c, ncandidates):
    in_permutation = [False for _ in range(n+1)]
    # NOTE: cannot do below code when building in_permutation vector. This is because a is being mutated and might
    # contain values from previous calls. That's why we need to constrict our search through a to the first k indices.
    # for v in a:
    #     in_permutation[v] = True

    for i in range(k):
        in_permutation[a[i]] = True

    nc = 0
    for i in range(len(in_permutation)):
        if not in_permutation[i]:
            c[nc] = i
            nc+=1

    ncandidates[0] = nc

def process_solution(a, k, input = None):
    open_brace = "{"
    close_brace = "}"
    print(f"{open_brace}")
    for i in range(1,len(a)):
        if a[i]!=0:
            print(a[i])
    print(f"{close_brace}")

def construct_all_permutations(n):
    NMAX = 100
    a = [0] * NMAX
    backtrack(a, 0, n, construct_candidates=construct_candidates_optimal, process_solution=process_solution,
              is_a_solution=is_a_solution, )


if __name__ == '__main__':
    construct_all_permutations(3)