from KMP import KmpMatcher
from BruteForce import BFMatcher
from BadCharacter import BadCharacter
import time


def main():
    content = ""
    tic, toc = 0, 0
    with open("./Testing/GCF_000006645.1_ASM664v1_genomic.fna", "r") as fna:
        content = fna.read()
    testingStr = "ACCCCTCA"

    """Brute Force"""
    bfmatcher = BFMatcher(testingStr, content)
    tic = time.time()
    bf_result = bfmatcher.bfSearch()
    toc = time.time()
    print("postion list from Brute Force - ", bf_result)
    bf_time_spent = toc - tic
    print("Brute force spent " + str(bf_time_spent))
    """KMP"""
    kmpMatcher = KmpMatcher(testingStr, content)
    tic = time.time()
    kmp_result = kmpMatcher.kmpSearch()
    toc = time.time()
    print("postion list from KMP - ", kmp_result)
    kmp_time_spent = toc - tic
    print("KMP spent " + str(kmp_time_spent))
    """Bad Character"""
    badCharacter = BadCharacter(testingStr, content)
    tic = time.time()
    bc_result = badCharacter.search()
    toc = time.time()
    print("postion list from Bad Character - ", bc_result)
    bc_time_spent = toc - tic
    print("Bad Character spent " + str(bc_time_spent))


if __name__ == "__main__":
    main()
