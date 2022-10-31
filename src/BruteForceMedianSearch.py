import itertools

class BruteForceMedianSearch:
    """Class to implement the Brute Force Median Search algorithm to find the median motif"""
    def __init__(self, dna: list, l: int) -> None:
        """Init method

        Required Args
            dna (list): DNA sequences
            l (int): length of l-mer
        """
        self.dna = dna
        self.l = l

    def TotalDistance(self, optimisticWord: str) -> int:
        """Method to calculate the minimum hamming distance of a pattern

        Required Args
            optimisticWord (str): prospective motif pattern

        Returns
            int: minimum hamming distance of a prospective pattern
        """
        totalDist = 0
        # iterate through each dna sequence
        for pattern in self.dna:
            hammingDistance = []
            # iterate through each l-mer
            for i in range(len(pattern) - self.l + 1):
                word = pattern[i:i+self.l]
                hammingDistance.append(sum(c1!=c2 for c1,c2 in zip(word, optimisticWord)))          # calculate hamming distance for current dna pattern                                 
            totalDist += min(hammingDistance)                                                       # add minimum hamming distance to total distance
        return totalDist

    def main(self) -> str:
        """Method to carry out the algorithm

        Returns
            str: median motif
        """
        bestWord = ""
        bestDist = len(self.dna) * ((len(self.dna[0]) - self.l + 1) * self.l)
        for lmer in itertools.product('acgt', repeat=self.l):
            optimisticWord = "".join(lmer)
            if self.TotalDistance(optimisticWord) < bestDist:
                bestDist = self.TotalDistance(optimisticWord)
                bestWord = optimisticWord
        return bestWord
