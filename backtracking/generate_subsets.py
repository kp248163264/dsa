from backtracking.backtrack_template import backtrack

class GenerateSubsets:
    def __init__(self, ncandidates = 0):
        self.ncandidates = ncandidates
    def construct_candidates(self, a, k, n, c, ncandidates):
        """

        What are the possible choices for the ith position in the permutation/subset? Will either include the ith
        element or not. So if representing solution as array of trues and falses, candidate 1 will be True, candidate 2
        will be False. There are 2 potential candidates.

        Constructing an array/vector of n cells, where value of a_i (True/False) signifies whether ith item is in
        given subset.


        Pruning happens when you're smart about constructing candidates.
        """
        c[0] = True
        c[1] = False
        ncandidates[0] = 2

    def process_solution(self,a,k, input=None):
        i = 0
        open = "{"
        closed = "}"

        print(f"{open}")
        for i in range(k+1):
            if a[i]:
                print(f" {i}")
        print(f"{closed}\n")

    def is_a_solution(self, a, k, n):
        """
        Checks if 'a' is a solution. 'a' is a solution whenever k = n.
        """
        return k == n

    def generate_subsets(self, n):
        """
        Generate subsets of an n-element set. There are 2^n subsets.
        Examples:
            (a) There are 2 subsets for n=1, namely {} and {1}
            (b) There are 4 subsets for n = 2, namely {}, {1}, {2}, {1,2}
            (c) There are 8 subsets for n = 3, namely {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}
        :param n: n-element set you want to generate subsets for
        :return:
            print 2^n solutions where value in one of the vectors is True/False if the value is included in the set.
            ex:
                before printing, for n = 2, prints out [False, False], [True,False], [False, True], [True,True]
                We process this to print out only the numbers in the process_solution method.
        """
        NMAX = 100
        a = [0] * (NMAX)
        backtrack(a, 0, n, construct_candidates=self.construct_candidates, process_solution=self.process_solution,
                  is_a_solution=self.is_a_solution)
        return 0

if __name__ == '__main__':
    g = GenerateSubsets(3)
    g.generate_subsets(3)