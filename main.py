from src.BruteForceMedianSearch import BruteForceMedianSearch
from src.GreedyMotifSearch import GreedyMotifSearch
import re, random, time

def main():
    conf = {}
    # input1 (ch4 slides): n=68, l=8, t=5
    print("==========INPUT 1==========")
    print("n=68, l=8, t=5\n")
    input1 = open("datasets/input1.txt", "r")
    primer = input1.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = input1.read()
    dna = [re.sub('\\n','',item.upper()) for item in dna.split("\n")]
    BFMS = BruteForceMedianSearch(dna, conf['l'])
    GMS = GreedyMotifSearch(dna, conf['t'], conf['l'])
    BFMS_Times = []
    GMS_Times = []
    for i in range(3):
        print("Iteration no. " + str(i+1))
        # BFMS
        st = time.time()
        res = BFMS.main()
        end = time.time()
        print("Res: " + res + " Brute Force Median Search: " + str(end-st))
        BFMS_Times.append(end-st)
        # GMS
        st = time.time()
        res = GMS.main()
        end = time.time()
        print("Res: " + res + " Greedy Motif Search: " + str(end-st))
        GMS_Times.append(end-st)
    print("Average execution time of BFMS: " + str(sum(BFMS_Times)/3))
    print("Average execution time of GMS: " + str(sum(GMS_Times)/3))
    input1.close()

    # input2: n=5, l=3, t=5
    print("==========INPUT 2==========")
    print("n=5, l=3, t=5\n")
    input2 = open("datasets/input2.txt", "r")
    primer = input2.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = input2.read()
    dna = [re.sub('\\n','',item.upper()) for item in dna.split("\n")]
    BFMS = BruteForceMedianSearch(dna, conf['l'])
    GMS = GreedyMotifSearch(dna, conf['t'], conf['l'])
    BFMS_Times = []
    GMS_Times = []
    for i in range(3):
        print("Iteration no. " + str(i+1))
        # BFMS
        st = time.time()
        res = BFMS.main()
        end = time.time()
        print("Res: " + res + " Brute Force Median Search: " + str(end-st))
        BFMS_Times.append(end-st)
        # GMS
        st = time.time()
        res = GMS.main()
        end = time.time()
        print("Res: " + res + " Greedy Motif Search: " + str(end-st))
        GMS_Times.append(end-st)
    print("Average execution time of BFMS: " + str(sum(BFMS_Times)/3))
    print("Average execution time of GMS: " + str(sum(GMS_Times)/3))
    input2.close()

    # input3 (randomly generated): t=5, l=3
    print("==========t=5, l=3==========")
    # n = 5
    print("\nn=5")
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(5)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    GMS = GreedyMotifSearch(dna_seq, 5, 3)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))
    # n = 30
    print("\nn=30")
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(30)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    GMS = GreedyMotifSearch(dna_seq, 5, 3)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))
    # n = 60
    print("\nn=60")
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(60)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    GMS = GreedyMotifSearch(dna_seq, 5, 3)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))

    # input4 (randomly generated): n=12, l=3
    print("==========n=12, l=3==========")
    # t = 5
    print("\nt=5")
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(10)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    GMS = GreedyMotifSearch(dna_seq, 5, 3)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))
    # t = 10
    print("\nt=10")
    dna_seq = []
    for t in range(10):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(10)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    GMS = GreedyMotifSearch(dna_seq, 10, 3)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))
    # t = 20
    print("\nt=20")
    dna_seq = []
    for t in range(20):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(10)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    GMS = GreedyMotifSearch(dna_seq, 20, 3)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))

    # input5 (randomly generated): n=10, t=5
    print("==========n=30, t=5==========")
    # k = 3
    print("\nk=3")
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(30)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    GMS = GreedyMotifSearch(dna_seq, 5, 3)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))
    # k = 5
    print("\nk=5")
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(30)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 5)
    GMS = GreedyMotifSearch(dna_seq, 5, 5)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))
    # k = 8
    print("\nk=8")
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(30)))
    # print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 8)
    GMS = GreedyMotifSearch(dna_seq, 5, 8)
    # BFMS
    st = time.time()
    res = BFMS.main()
    end = time.time()
    print("Res: " + res + " Brute Force Median Search: " + str(end-st))
    # GMS
    st = time.time()
    res = GMS.main()
    end = time.time()
    print("Res: " + res + " Greedy Motif Search: " + str(end-st))

if __name__ == "__main__":
    main()
