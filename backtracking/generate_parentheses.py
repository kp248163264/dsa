

def process_solution(a,k,input):
    p = ""
    for paren in a:
        if paren == "(" or paren == ")":
            p += str(paren)
    print(p)


def construct_candidates(a,k,input,c,ncandidates):
    numCand = 0
    numEach = {"(":0, ")":0}
    stk = []
    for i in range(k):
        if a[i] == "(":
            numEach[a[i]]+=1
            stk.append("(")
        elif a[i] == ")":
            numEach[a[i]]+=1
            if len(stk) > 0:
                stk.pop()
            else:
                ncandidates[0] = 0
                return
    canDoOpen = numEach["("] < input
    canDoClose = numEach[")"] < input
    if canDoOpen:
        c[numCand] = "("
        numCand+=1
    if canDoClose:
        c[numCand] = ")"
        numCand+=1
    ncandidates[0] = numCand


def is_a_solution(a,k,input):
    return k == input * 2


def backtrack(a,k,input):
    NMAX = 100
    c = [0] * NMAX
    ncandidates = [NMAX]
    finished = False

    if is_a_solution(a, k, input):
        process_solution(a, k, input)
    else:
        k+=1
        print("k: ", k)
        construct_candidates(a,k,input,c,ncandidates)
        for i in range(ncandidates[0]):
            a[k] = c[i]
            backtrack(a,k,input)
            if finished:
                return


def generate_parentheses(n):
    NMAX = 100
    a = [0] * NMAX
    backtrack(a, 0, n)


if __name__ == '__main__':
   generate_parentheses(3)