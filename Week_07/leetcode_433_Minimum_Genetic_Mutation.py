"""
leetcode 433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with 
choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" 
to "end"), where ONE mutation is defined as ONE single character 
changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid 
gene mutations. A gene must be in the bank to make it a valid gene 
string.

Now, given 3 things - start, end, bank, your task is to determine 
what is the minimum number of mutations needed to mutate from "start" 
to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included 
in the bank.

If multiple mutations are needed, all mutations during in the sequence 
must be valid.

You may assume start and end string is not the same.

"""

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        bfs = collections.deque()
        bfs.append((start, 0))
        bankset = set(bank)
        while bfs:
            gene, step = bfs.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for x in "ACGT":
                    newGene = gene[:i] + x + gene[i+1:]
                    if newGene in bank and newGene != gene:
                        bfs.append((newGene, step + 1))
                        bank.remove(newGene)
        return -1