

final = []
def process_solution(a,k,input):
    for i in range(k+1):
        print(a[i])
    final.append(a)


def is_a_solution(a,k,input):
    if k<=1:
        return False
    incr = True
    for i in range(1, k+1):
        incr = incr and a[i] > a[i-1]
    return incr


def construct_candidates(a,k,input,c,ncandidates, start):
    if k == 1:
        print("k is 1: ", k)
        c[0] = input[start]
        ncan = 1
    else:
        prev = a[k-1]
        ncan = 0
        for i in range(start,len(input)):
            if input[i] > prev:
                c[ncan] = input[i]
    ncandidates[0] = ncan



def backtrack(a, k, input, start):
    NMAX = 100
    c = [0] * NMAX
    ncandidates = [NMAX]

    if is_a_solution(a,k,input):
        process_solution(a, k, input)
    else:
        k += 1
        print("k: ", k)
        construct_candidates(a, k, input, c, ncandidates, start)
        print("c: ", c)
        for i in range(ncandidates[0]):
            a[k] = c[i]
            backtrack(a,k,input, start)
        start += 1
    return




def non_decreasing_subsequences(nums):
    """
    Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with
    at least two elements. You may return the answer in any order.


    Example 1:

    Input: nums = [4,6,7,7]
    Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    Example 2:

    Input: nums = [4,4,3,2,1]
    Output: [[4,4]]
    """
    NMAX = 100
    a = [0] * NMAX
    start = 0
    backtrack(a, 0, nums, start)



if __name__ == "__main__":
    nums = [4, 6, 7, 7]
    non_decreasing_subsequences(nums)