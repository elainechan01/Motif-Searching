from src.GreedyMotifSearch import GreedyMotifSearch
import re, random, time

def main():
    conf = {}
    # input1 (ch4 slides): n=68, l=8, t=5
    input1 = open("datasets/input1.txt", "r")
    primer = input1.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = input1.read()
    dna = [re.sub('\\n','',item.upper()) for item in dna.split("\n")]
    GMS = GreedyMotifSearch(dna, conf['t'], conf['l'])
    st = time.time()
    print(GMS.main())
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
    dna = [re.sub('\\n','',item.upper()) for item in dna.split("\n")]
    GMS = GreedyMotifSearch(dna, conf['t'], conf['l'])
    st = time.time()
    print(GMS.main())
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
    dna = [re.sub('\\n','',item.upper()) for item in dna.split("\n")]
    GMS = GreedyMotifSearch(dna, conf['t'], conf['l'])
    st = time.time()
    print(GMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    input1.close()

    # input4 (randomly generated): n=10, l=5, t=5
    dna_seq = []
    for t in range(5):
        dna_seq.append(''.join(random.choice('ACGT') for _ in range(10)))
    print(dna_seq)
    GMS = GreedyMotifSearch(dna_seq, 5, 5)
    st = time.time()
    print(GMS.main())
    end = time.time()
    execution = end - st
    print(execution)

if __name__ == "__main__":
    main()