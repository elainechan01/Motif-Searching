from BruteForceMedianSearch import BruteForceMedianSearch
import re, random

def main():
    # input1 (ch4 slides): n=68, l=8, t=5
    dna = """cctgatagacgctatctggctatccacgtacgtaggtcctctgtgcgaatctatgcgtttccaaccat,
    agtactggtgtacatttgatacgtacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc,
    aaacgtacgtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt,
    agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtacgtataca,
    ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaacgtacgtc"""
    dna = [re.sub('\\n','',item.lower()) for item in dna.split(",")]
    # BFMS = BruteForceMedianSearch(dna, 8)
    # print(BFMS.main())

    # input2: n=5, l=3, t=5
    dna = """actga,
    ctgaa,
    gacta,
    caggt,
    ggcgg"""
    dna = [re.sub('\\n','',item.lower()) for item in dna.split(",")]
    BFMS = BruteForceMedianSearch(dna, 3)
    print(BFMS.main())

    # input3: n=3, l=2, t=3
    dna = """cta,
    gat,
    cga"""
    dna = [re.sub('\\n','',item.lower()) for item in dna.split(",")]
    BFMS = BruteForceMedianSearch(dna, 2)
    print(BFMS.main())

    # input4 (randomly generated): n=10, l=5, t=5
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(10)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 5)
    print(BFMS.main())

if __name__ == "__main__":
    main()