from KMP import KmpMatcher
from BruteForce import BFMatcher
import time

def main():
    content = ''
    tic , toc = 0 , 0
    with open('./Testing/GCF_000006645.1_ASM664v1_genomic.fna', 'r') as fna:
        content = fna.read()
    testingStr = "ACCCCTCA"
    bfmatcher = BFMatcher(testingStr , content)
    tic = time.time()
    bfmatcher.bfSearch()
    toc = time.time()
    bf_time_spent = toc - tic
    print("Brute force spent "+ str(bf_time_spent))
    kmpMatcher = KmpMatcher(testingStr, content)
    tic = time.time()
    kmpMatcher.kmpSearch()
    toc = time.time()
    kmp_time_spent = toc - tic
    print("KMP spent "+ str(kmp_time_spent))
if __name__ == "__main__":
    main()