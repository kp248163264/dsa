

def construct_candidates(a,k,input,c,ncandidates):
    ncandidates[0] = 2
    c[0] = True
    c[1] = False
    return

def is_a_solution(a,k,input):
    return k == input

def process_solution(a,k,input):
    open = "{"
    close = "}"
    print(f'{open}')
    for i in range(k+1):
        if a[i]==1:
            print(f"{i}")
    print(f'{close}\n')

def backtrack(a, k, input):
    NMAX = 100
    c = [0] * NMAX
    ncandidates = [NMAX]
    finished = False
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


def generate_subsets(n):
    NMAX = 100
    a = [0]*NMAX
    backtrack(a,0,n)



if __name__ == "__main__":
    generate_subsets(3)