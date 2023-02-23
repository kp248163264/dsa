


def process_solution(a,k,input):
    print("processing sol")
    open_bracket = "{"
    closed_bracket = "}"
    m = {}
    for i in range(len(input)):
        m[i] = input[i]
    print("m: ", m)
    print(f"{open_bracket} ")
    for ind in range(len(a)):
        if ind in m:
            print(m[ind])
    print(f"{closed_bracket}")



def is_a_solution(a,k,input):
    return k == len(input)


def construct_candidates(a,k,input,c,ncandidates):
    in_permutation = [False for _ in range(len(input) + 1)]
    for i in range(k):
        in_permutation[a[i]] = True

    ncan = 0
    for i in range(len(in_permutation)):
        if not in_permutation[i]:
            c[ncan] = i
            ncan+=1
    ncandidates[0] = ncan




def backtrack(a, k, input):
    NMAX = 100
    c = [""] * NMAX
    ncandidates = [NMAX]
    if is_a_solution(a, k, input):
        print("in if")
        process_solution(a,k,input)
    else:
        k+=1
        construct_candidates(a,k,input,c,ncandidates)
        for i in range(ncandidates[0]):
            a[k] = c[i]
            backtrack(a,k,input)
    return



def string_permutations(s):
    NMAX = 100
    a = [0] * NMAX
    backtrack(a, 0, s)


if __name__ == "__main__":
    s = "AAB"
    string_permutations(s)
