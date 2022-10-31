from cProfile import Profile
from collections import Counter
import math

class GreedyMotifSearch:
    """Class to implement the Greedy Motif Search algorithm to find the best motifs of a dna sequence"""
    def __init__(self, dna: list, t: int, k: int) -> None:
        """Init method

        Required Args
            dna (list): DNA sequences
            t (int): no. of DNA sequences
            k (int): length of kmer
        """
        self.dna = dna
        self.n = len(self.dna[0])
        self.t = t
        self.k = k

    def CreateCountMatrix(self, MotifMatrix: list) -> list:
        """Method to calculate the Count Matrix
        
        Required Args
            MotifMatrix (list): 

        Returns
            list: count matrix of ACGT nucleotides
        """
        CountMatrix = []
        for i in range(self.k):     # TODO: laplace's rule of succession
            ColCount = {
                'A': 0,
                'C': 0,
                'G': 0,
                'T': 0
            }
            # calculate occurences of ACGT nucletides in each column
            for j in range(len(MotifMatrix)):
                ColCount[MotifMatrix[j][i]] += 1
            CountMatrix.append(ColCount)
        return CountMatrix

    def CreateProfileMatrix(self, MotifMatrix: list) -> list:
        """Method to calculate the Profile Matrix

        Required Args
            MotifMatrix (list): Motif Matrix of dna sequences

        Returns
            list: profile matrix of ACGT nucleotides
        """
        CountMatrix = self.CreateCountMatrix(MotifMatrix)
        ProfileMatrix = []
        # re-evaluate Count matrix as a means of probability
        for row in CountMatrix:
            ColProfile = {key: 1.0 * val/len(MotifMatrix) for key,val in row.items()}
            ProfileMatrix.append(ColProfile)
        return ProfileMatrix

    def FindMostProbableKmer(self, ProfileMatrix: list, dna: str) -> str:
        """Method to find the most probable kmer of a dna string
        
        Required Args
            ProfileMatrix (list): Profile Matrix
            dna (str): dna string
        """
        BestPattern = dna[0:self.k]
        BestProbability = 0
        # iterate through each k-mer of dna string
        for start in range(self.n - self.k + 1):
            OptimisticPattern = dna[start:start+self.k]
            OptimisticProbability = 1
            i = 0
            # find the most probable k-mer based on the ProfileMatrix
            for nuc in OptimisticPattern:
                OptimisticProbability *= ProfileMatrix[i][nuc]
                i += 1
            if OptimisticProbability > BestProbability:
                BestPattern = OptimisticPattern
                BestProbability = OptimisticProbability
        return BestPattern

    def CalculateScore(self, MotifMatrix: list) -> int:
        """Method to calculate score of Motif Matrix

        Required Args
            MotifMatrix (list): Motif Matrix of k-mers
        """
        # calculate consensus string
        consensus = ''
        for i in range(len(MotifMatrix[0])):
            colCount = Counter(row[i] for row in MotifMatrix)
            consensus += max(colCount, key=colCount.get)
        total = 0
        # calculate hamming distance between all rows in MotifMatrix and consensus string
        for kmer in MotifMatrix:
            total += sum(c1!=c2 for c1,c2 in zip(kmer, consensus))
        return total

    def main(self) -> list:
        """Method to carry out the algorithm
        Reference: https://www.mrgraeme.com/greedy-motif-search/

        Returns
            list: best motifs
        """
        # Create Motif matrix based on first k-mers
        BestMotifMatrix = [row[:self.k] for row in self.dna]
        # iterate through each k-mer in first row
        for start in range(self.n - self.k + 1):
            OptimisticMotifMatrix = []
            kmer = self.dna[0][start:start+self.k]
            OptimisticMotifMatrix.append(kmer)
            # Select kmer with highest probability and add to motif matrix
            for row in self.dna[1:]:
                ProfileMatrix = self.CreateProfileMatrix(OptimisticMotifMatrix)
                OptimisticMotifMatrix.append(self.FindMostProbableKmer(ProfileMatrix, row))
            # compare scores of current motif matrix and best motif matrix
            if self.CalculateScore(OptimisticMotifMatrix) < self.CalculateScore(BestMotifMatrix):
                BestMotifMatrix = OptimisticMotifMatrix
        return BestMotifMatrix
