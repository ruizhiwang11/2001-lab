from KMP import KmpMatcher
from BruteForce import BFMatcher
from BadCharacter import BadCharacter
import time


def main():
    content = ""
    tic, toc = 0, 0
    fileDic = {1: "./Testing/GCF_000005825.2_ASM582v2_genomic.fna",
               2: "./Testing/GCF_000006645.1_ASM664v1_genomic.fna",
               3: "./Testing/GCF_000007085.1_ASM708v1_genomic.fna",
               4: "./Testing/GCF_000007105.1_ASM710v1_genomic.fna",
               5: "./Testing/GCF_000007125.1_ASM712v1_genomic.fna",
               6: "./Testing/GCF_000023865.1_ASM2386v1_genomic.fna",
               7: "./Testing/GCF_000023885.1_ASM2388v1_genomic.fna"}
    fileIndex = int(input('Please key in the file index (1~7):'))

    with open(fileDic[fileIndex], "r") as fna:
        content = fna.read()
    testingStr = input('Please key in the pattern:')  # "ACCCCTCA"
    print("Searching\033[1;36m", testingStr, "\033[0min\033[1;36m", fileDic[fileIndex], "\033[0m......")

    """Brute Force"""
    bfmatcher = BFMatcher(testingStr, content)
    tic = time.time()
    bf_result = bfmatcher.bfSearch()
    toc = time.time()
    print("Position list from Brute Force :        ", bf_result)
    bf_time_spent = toc - tic

    """KMP"""
    kmpMatcher = KmpMatcher(testingStr, content)
    tic = time.time()
    kmp_result = kmpMatcher.kmpSearch()
    toc = time.time()
    print("Position list from Knuth–Morris–Pratt : ", kmp_result)
    kmp_time_spent = toc - tic

    """Bad Character"""
    badCharacter = BadCharacter(testingStr, content)
    tic = time.time()
    bc_result = badCharacter.search()
    toc = time.time()
    print("Position list from Bad Character :      ", bc_result)
    bc_time_spent = toc - tic

    if bf_result == kmp_result == bc_result:
        print('\033[1;36mThe results match!\033[0m')
        print(len(bf_result), "positions are found!\n\n\033[1;32mTime Spent:\033[0m")
        print("       Brute Force : ", str(bf_time_spent), "s")
        print("Knuth–Morris–Pratt : ", str(kmp_time_spent), "s")
        print("     Bad Character : ", str(bc_time_spent), "s")
    else:
        print('The results do not match!')


if __name__ == "__main__":
    main()
