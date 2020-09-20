from KMP import KmpMatcher
from BruteForce import BFMatcher
from BadCharacter import BadCharacter
import time

fileDic = {1: "./Testing/GCF_000005825.2_ASM582v2_genomic.fna",
           2: "./Testing/GCF_000006645.1_ASM664v1_genomic.fna",
           3: "./Testing/GCF_000007085.1_ASM708v1_genomic.fna",
           4: "./Testing/GCF_000007105.1_ASM710v1_genomic.fna",
           5: "./Testing/GCF_000007125.1_ASM712v1_genomic.fna",
           6: "./Testing/GCF_000023865.1_ASM2386v1_genomic.fna",
           7: "./Testing/GCF_000023885.1_ASM2388v1_genomic.fna"}


def main():
    content = ""
    tic, toc = 0, 0

    while True:
        fileIndex = input("Please key in the file index \033[1;32m1~7\033[0m "
                          "(\'\033[1;36mALL\033[0m\' to search in ALL files. \'\033[1;31mEXIT\033[0m\' to exit): ")
        if fileIndex.isdigit():
            if 1 <= int(fileIndex) <= 7:
                testingStr = input('Please key in the pattern:')  # "ACCCCTCA"
                runAlgo(int(fileIndex), testingStr)
            else:
                print("\033[1;31mError input!\033[0m ")
        elif fileIndex.upper() == "ALL":
            # print("RUN ALL")
            testingStr = input('Please key in the pattern:')
            i = 1
            t = [0.00, 0.00, 0.00]
            while i <= 7:
                r = runAlgo(i, testingStr)
                for index in range(len(t)):
                    t[index] += r[index]
                i += 1
            print("\033[1;34mAverage Time Spent:\033[0m")
            print("       Brute Force : ", str(t[0] / 7), "s")
            print("Knuth–Morris–Pratt : ", str(t[1] / 7), "s")
            print("     Bad Character : ", str(t[2] / 7), "s\n")
        elif fileIndex.upper() == "EXIT":
            print("Thank you for using! \n\033[1;31mEXIT\033[0m ")
            exit(1)
        else:
            print("\033[1;31mError input!\033[0m ")


def runAlgo(fileIndex, testingStr):
    with open(fileDic[fileIndex], "r") as fna:
        content = fna.read()

    print("Searching\033[1;36m", testingStr.upper(), "\033[0min\033[1;36m", fileDic[fileIndex], "\033[0m......")

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
        print("\033[1;34m", len(bf_result), "\033[0mpositions are found!\n\n\033[1;32mTime Spent:\033[0m")
        print("       Brute Force : ", str(bf_time_spent), "s")
        print("Knuth–Morris–Pratt : ", str(kmp_time_spent), "s")
        print("     Bad Character : ", str(bc_time_spent), "s\n")
        return [bf_time_spent, kmp_time_spent, bc_time_spent]
    else:
        print('\033[1;31mThe results do not match!\033[0m')
        print('\033[1;31mEXIT\033[0m')
        exit(0)


if __name__ == "__main__":
    main()
