from src.BruteForceMedianSearch import BruteForceMedianSearch
import re, random, time

def main():
    conf = {}
    # input1 (ch4 slides): n=68, l=8, t=5
    input1 = open("datasets/input1.txt", "r")
    primer = input1.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = input1.read()
    dna = [re.sub('\\n','',item.lower()) for item in dna.split("\n")]
    BFMS = BruteForceMedianSearch(dna, conf['l'])
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    input1.close()

    # input2: n=5, l=3, t=5
    input2 = open("datasets/input2.txt", "r")
    primer = input2.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = input2.read()
    dna = [re.sub('\\n','',item.lower()) for item in dna.split("\n")]
    BFMS = BruteForceMedianSearch(dna, conf['l'])
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    input2.close()

    # input3: n=3, l=2, t=3
    input3 = open("datasets/input3.txt", "r")
    primer = input3.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = input3.read()
    dna = [re.sub('\\n','',item.lower()) for item in dna.split("\n")]
    BFMS = BruteForceMedianSearch(dna, conf['l'])
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    input1.close()

    # input4 (randomly generated): t=5, l=3
    # n = 5
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(5)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    # n = 10
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(10)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    # n = 30
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(30)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)

    # input4 (randomly generated): n=5, l=3
    # t = 4
    dna_seq = []
    for t in range(4):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(5)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    # t = 10
    dna_seq = []
    for t in range(10):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(5)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    # t = 15
    dna_seq = []
    for t in range(15):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(5)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)

    # input4 (randomly generated): n=10, t=5
    # l = 2
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(10)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 2)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    # l = 3
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(10)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 3)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    # l = 5
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('acgt') for _ in range(10)))
    print(dna_seq)
    BFMS = BruteForceMedianSearch(dna_seq, 5)
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)

if __name__ == "__main__":
    main()
