def is_a_solution_default(a, k, input):
    """
    "Is what I have done a complete solution". ex. Sudoku - is the board filled in?
    Test whether first k elements of a vector a form a complete solution for the given problem

    :param a: vector representing the partial solution (a1,...,ak) we try to extend at each step in the backtracking algorithm
    :param k: first k elements of vector a
    :param input: any baggage I need to tell whether or not I have a solution
        ex. Sudoku: need to know other numbers on board
        ex. Travelling Salesman: need complete copy of graph
    allows us to pass general information into the method; can use it to specify n, the size of a target solution
      makes sense when constructing permutations or subsets of n elements , but other data could be relevant when
      constructing variable-sized objects like moves in a  game
    :return: boolean
    """
    return


def construct_candidates_default(a, k, input, c, ncandidates):
    """
    What are the possible choices for the kth position of the solution given whatever the input was and first k choices.
        ex. Sudoku: have Sudoku board originally filled in, k-1 filled in other numbers, now if I want to know
        candidates for next open spot, which numbers don't violate constraint so far

        ex. Traveling Salesman: what is the choice for kth spot on Traveling Salesman tour given graph and first
            k-1 choices. It's what are outgoing edges on vertex that go to vertices I haven't already had on my tour.
            In traveling salesman, keep track of smallest permutation/tour and return that.

    This is also the correct time to throw out anything that will lead to a non-solution.
    Better to avoid checking too much in is_a_solution.

    Fills an array c with the complete set of possible candidates for the kth position of a given the contents of the
    first k-1 position
    :param a: vector representing the partial solution (a1,...,ak) we try to extend at each step in the backtracking algorithm
    :param k: kth position of a
    :param input: allows us to pass general information into the method (like in is_a_solution)
    :param c: routine fills an array c with complete set of possible candidates for kth position of a given contents of
    first k-1 positions.
    :param ncandidates: number of candidates returned in c
    :return: c
    """
    return


def process_solution_default(a, k, input=None):
    """
    Once you have the solution, there's something you might want to do with it.

    Prints, counts, or however processes a complete solution
    :param a: vector representing the partial solution (a1,...,ak) we try to extend at each step in the backtracking algorithm
    :param k: kth position of a
    :param input: allows us to pass general information into the method (like in is_a_solution)
    :return:
    """
    return


def make_move(a, k, input):
    """
    Enables us to modify a data structure in response to the latest move as well as clean up the data structure if we decide
    to take back a move.
    :param a: vector representing the partial solution (a1,...,ak) we try to extend at each step in the backtracking algorithm
    :param k: kth position of a
    :param input: allows us to pass general information into the method (like in is_a_solution)
    :return: None
    """
    return


def unmake_move(a, k, input):
    """
    Enables us to modify a data structure in response to the latest move as well as clean up the data structure if we decide
    to take back a move.
    :param a: vector representing the partial solution (a1,...,ak) we try to extend at each step in the backtracking algorithm
    :param k: kth position of a
    :param input: allows us to pass general information into the method (like in is_a_solution)
    :return: None
    """
    return


def backtrack(a, k, input, construct_candidates=construct_candidates_default, process_solution=process_solution_default, is_a_solution=is_a_solution_default):
    """
    Backtrack template works for any problem, just need to specify the 3 parameter functions based on the problem.

    Runtime of recursive functions is often O(branches^depth), so runtime of backtracking algorithms is often
    exponential.

    """
    finished = False  # allows for premature termination
    MAXCANDIDATES = 100
    ncandidates = [MAXCANDIDATES]
    c = [0] * MAXCANDIDATES  # candidates for next position

    if is_a_solution(a, k, input): # if current solution vector a filled up to the kth solution is a solution,
        # then do something with it
        process_solution(a, k, input)
    else: # if not k goes to k+1
        k += 1
        construct_candidates(a, k, input, c, ncandidates) # construct candidates for the now kth position given a;
        # fill the candidates in array c, and tell me how many there are
        for i in range(ncandidates[0]):
            a[k] = c[i] # while there are remaining candidates I haven't looked at, copy ith candidate into kth spot
            make_move(a, k, input)
            backtrack(a, k, input, construct_candidates=construct_candidates, process_solution=process_solution,
                      is_a_solution=is_a_solution) # backtrack to see if we will eventually get to the next position
            unmake_move(a, k, input)
            if finished: # if we've succeeded, return, otherwise try next candidate
                return
