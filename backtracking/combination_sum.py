
def construct_candidates(a, k, input, c, ncandidates, start):
    available_cands = input[0]
    ncan = 0
    sum_so_far = 0

    for i in range(k):
        sum_so_far += a[i]
    for i in range(start, len(available_cands)):
        if sum_so_far + available_cands[i] <= target:
            c[ncan] = available_cands[i]
            ncan += 1

    ncandidates[0] = ncan


def target_surpassed(a,k,input):
    return sum(a) > input


def is_a_solution(a, k, input):
    sum_so_far = 0
    for i in range(k+1):
        sum_so_far += a[i]
    return sum_so_far == input


def process_solution(a,k,input):
    open_bracket = "{"
    closed_bracket = "}"
    print(f"{open_bracket}")
    for i in range(k+1):
        if a[i] != 0:
            print(a[i])
    print(f"{closed_bracket}")


def backtrack(a, k, input, start):
    NMAX = 100
    c = [0] * NMAX
    ncandidates = [NMAX]

    if is_a_solution(a, k, input[1]):
        process_solution(a,k,input)
    else:
        k+=1
        construct_candidates(a, k, input, c, ncandidates, start)
        for i in range(ncandidates[0]):
            a[k] = c[i]
            backtrack(a, k, input, start)
            start += 1
    return


def combination_sum(candidates, target):
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
    frequency
     of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



    Example 1:

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
    Example 2:

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
    Example 3:

    Input: candidates = [2], target = 1
    Output: []
    """


    NMAX = 100
    a = [0] * NMAX
    backtrack(a, 0, [candidates, target], 0)



if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    combination_sum(candidates, target)
