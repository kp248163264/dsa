

def construct_candidates(a,k,input,c,ncandidates):
    in_permutation = [False for _ in range(len(input))]

    for i in range(k):
        return





def backtrack(a,k,input):

    NMAX = 100
    c = [0] * NMAX
    ncandidates = [NMAX]

    if is_a_solution(a):
        process_solution(a,k,input)
    else:
        k+=1
        construct_candidates(a,k,input,c,ncandidates)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)
    return


def letter_tile_possibilities(tiles):
    """You have n tiles, where each tile has one letter tiles[i] printed on it.

    Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

    Example 1:

    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
    Example 2:

    Input: tiles = "AAABBC"
    Output: 188
    Example 3:

    Input: tiles = "V"
    Output: 1


    Constraints:

    1 <= tiles.length <= 7
    tiles consists of uppercase English letters."""

    NMAX = 100
    a = [0] * NMAX
    backtrack(a,0,tiles)



if __name__ == "__main__":
    letter_tile_possibilities()