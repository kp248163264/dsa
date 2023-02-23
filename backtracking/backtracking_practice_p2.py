
# def construct_candidates(a, k, input, c, ncandidates):
#
#     ncan = 2
#     c[0] = True
#     c[1] = False
#     ncandidates[0] = ncan

#
# def process_solution(a, k, input):
#     print("in process_solution")
#     open_bracket = "{"
#     close_bracket = "}"
#     print(f"{open_bracket}")
#     for element in range(k+1):
#         if a[element]:
#             print(f"{element}, ")
#     print(f"{close_bracket}")
#


# def is_a_solution(a,k,input):
#     return input == k
#

# def backtrack(a,k,input):
#     NMAX = 100
#     ncandidates = [NMAX]
#     c = [0] * NMAX
#
#     if is_a_solution(a, k, input):
#         process_solution(a, k, input)
#     else:
#         k += 1
#         construct_candidates(a, k, input, c, ncandidates)
#         for i in range(ncandidates[0]):
#             a[k] = c[i]
#             backtrack(a, k, input)
#     return


# def generate_subsets(n):
#     NMAX = 100
#     a = [0] * NMAX
#     backtrack(a, 0, n)
#     return a
#
# def process_solution_parens(a,k,input):
#     s = ""
#     for i in range(1,k+1):
#         s+=a[i]
#     print(s)
#
# def is_a_solution_parens(a,k,input):
#     return input * 2 == k
#
# def construct_candidates_parens(a,k,input,c,ncandidates):
#     stk = []
#     dict = {"(": 0, ")": 0}
#     parensBalanced = True
#     for i in range(1,k):
#         if a[i] == ")":
#             if stk:
#                 dict[")"] +=1
#                 stk.pop(0)
#             else:
#                 parensBalanced = False
#                 break
#         else:
#             dict["("]+=1
#             stk.append(")")
#     canAddOpen = dict["("] < input and parensBalanced
#     canAddClosed = dict[")"] < input and parensBalanced
#
#     ncan = 0
#     if canAddOpen:
#         c[ncan] = "("
#         ncan+=1
#     if canAddClosed:
#         c[ncan] = ")"
#         ncan+=1
#     ncandidates[0] = ncan
#     return
#
#
#
# def backtrack_parens(a,k,input):
#
#     NMAX = 100
#     ncandidates = [NMAX]
#     c = [0] * NMAX
#     if is_a_solution_parens(a,k,input):
#         process_solution_parens(a,k,input)
#     else:
#         k+=1
#         construct_candidates_parens(a,k,input,c,ncandidates)
#         # print("c: ", c)
#         for i in range(ncandidates[0]):
#             a[k] = c[i]
#             backtrack_parens(a,k,input)
#     return
#
#
# def generate_parens(input):
#     """
#     Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#     Example 1:
#
#     Input: n = 3
#     Output: ["((()))","(()())","(())()","()(())","()()()"]
#     Example 2:
#
#     Input: n = 1
#     Output: ["()"]
#     """
#     NMAX = 100
#     a = [""] * NMAX
#     backtrack_parens(a, 0, n)
#


def process_solution(a,k,input):
    for i in range(k):
        print(a[i])


def is_a_solution(a,k,input):
    return k == input

def construct_candidates(a, k, input, c, ncandidates):

    stk = []
    ct = {"(":0, ")":0}

    stkSat = True

    for i in range(k):
        if a[i] == "(":
            stk.append("(")
            ct[a[i]] += 1
        else:
            if stk:
                stk.pop(0)
                ct[a[i]] += 1
            else:
                stkSat = False
                break

    canAddOpen = stkSat and ct["("] < input
    canAddClosed = stkSat and ct[")"] < input

    ncan = 0
    if canAddOpen:
        c[ncan] = "("
    if canAddClosed:
        c[ncan] = ")"
    ncandidates[0] = ncan
    return



def backtrack(a,k,input):
    NMAX = 100
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
    return



def generate_parentheses(n):
    NMAX = 100
    a = [0] * NMAX
    backtrack(a,0,n)



if __name__ == "__main__":
    n = 3
    generate_parentheses(n)

