

d = {
    '1':[],
    '2':["a", "b", "c"],
    '3':["d","e","f"],
    '4':["g","h","i"],
    '5':["j", "k", "l"],
    '6':["m","n","o"],
    '7':["p","q","r","s"],
    '8':["t","u","v"],
    '9':["w","x","y","z"]
}
def process_solution(a,k,input):
    p = ""
    for s in a:
        if s:
            p+=s
    print(p)

def is_a_solution(a,k,input):
    return k == len(input)

def construct_candidates(a,k,input,c,ncandidates):
    n_cand = 0
    l = d[input[k-1]]
    for val in l:
        c[n_cand] = val
        n_cand+=1
    ncandidates[0] = n_cand


def backtrack(a, k, input):
    NMAX = 100
    finished = False
    ncandidates = [NMAX]
    c = [0] * NMAX

    if is_a_solution(a,k,input):
        process_solution(a,k,input)
    else:
        k+=1
        construct_candidates(a,k,input,c,ncandidates)
        for i in range(ncandidates[0]):
            a[k] = c[i]
            backtrack(a,k,input)
            if finished:
                return

def letterCombinations(digits):
    """Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
    could represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
    letters."""
    NMAX = 100
    a = [0] * NMAX
    backtrack(a,0,digits)



if __name__ == '__main__':
    letterCombinations("23")