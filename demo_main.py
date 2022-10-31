from src.GreedyMotifSearch import GreedyMotifSearch
from src.BruteForceMedianSearch import BruteForceMedianSearch
import re, time

def main():
    conf = {}
    # Brute Force Median Search
    bfms_dataset = open("datasets/bfms_demo.txt", "r")
    bfms_dataset.readline()     # skip header
    primer = bfms_dataset.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = bfms_dataset.read()
    dna = [re.sub('\\n','',item.lower()) for item in dna.split("\n")]
    BFMS = BruteForceMedianSearch(dna, conf['l'])
    st = time.time()
    print(BFMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    bfms_dataset.close()

    # Greedy Motif Search
    gms_dataset = open("datasets/gms_demo.txt", "r")
    gms_dataset.readline()     # skip header
    primer = gms_dataset.readline().strip().split(",")
    for config in primer:
        conf[config[0]] = int(config[2:])
    dna = gms_dataset.read()
    dna = [re.sub('\\n','',item.upper()) for item in dna.split("\n")]
    GMS = GreedyMotifSearch(dna, conf['t'], conf['k'])
    st = time.time()
    print(GMS.main())
    end = time.time()
    execution = end - st
    print(execution)
    gms_dataset.close()

if __name__ == "__main__":
    main()
