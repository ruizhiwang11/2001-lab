from KMP import KmpMatcher
from BruteForce import BFMatcher
from BadCharacter import BadCharacter
import testcaseAutoGen
import time
import json
import plotgraph as pg

resultlist={
    "Brute_Force": [],
    "KMP": [],
    "Boyer-Moore": [],
    'y':[]
}
bf_time_spent=0
kmp_time_spent=0
bc_time_spent=0

def main():
    content = ""
    tic, toc = 0, 0
    with open("./Testing/GCF_000006645.1_ASM664v1_genomic.fna", "r") as fna:
        content = fna.read()
    load_string_list(content)
    pg.plotAGraph()



"""Brute Force"""
def Brute_Force(testingStr,content):
    bfmatcher = BFMatcher(testingStr, content)
    tic = time.time()
    bf_result = bfmatcher.bfSearch()
    toc = time.time()
    #print(" - postion list from Brute Force - ")
    #print(bf_result)
    print (len(bf_result))

    global bf_time_spent
    bf_time_spent = toc - tic
    #print("Brute force spent " + str(bf_time_spent))
    


"""KMP"""
def KMP(testingStr,content):
    kmpMatcher = KmpMatcher(testingStr, content)
    tic = time.time()
    kmp_result = kmpMatcher.kmpSearch()
    toc = time.time()
    #print(" - postion list from KMP - ")
    #print(kmp_result)
    print (len(kmp_result))

    global kmp_time_spent
    kmp_time_spent = toc - tic
    #print("KMP spent " + str(kmp_time_spent))


"""Bad Character"""
def Bad_Character(testingStr,content):
    badCharacter = BadCharacter(testingStr, content)
    tic = time.time()
    bc_result = badCharacter.search()
    toc = time.time()
    #print(" - postion list from Bad Character - ")
    #print(bc_result)
    print (len(bc_result))
    global bc_time_spent
    bc_time_spent = toc - tic
    #print("Bad Character spent " + str(bc_time_spent))


"""load test string list from auto generation for each test"""
def load_string_list(content):
    testingStrlist = testcaseAutoGen.testinglist
    for lens in testingStrlist:
        #print ("\n")
        print ("There are string of "+ str(lens) +" lens tested: ")
        #print (testingStrlist[lens])
        for string in testingStrlist[lens]:
             print (string)
             Brute_Force(string,content)
             KMP(string,content)
             Bad_Character(string,content)
             
             resultlist["Brute_Force"].append(round(bf_time_spent,4))
             resultlist["KMP"].append(round(kmp_time_spent,4))
             resultlist["Boyer-Moore"].append(round(bc_time_spent,4))
             resultlist["y"].append(lens)

             #resultlist.update({"Brute_Force":[bf_time_spent],"KMP":[kmp_time_spent],"Bad_Character":[bc_time_spent]})
             #resultlist.update({string:[bf_time_spent,kmp_time_spent,bc_time_spent]})
             print (bf_time_spent,kmp_time_spent,bc_time_spent)
             print ("\n")
            
    print (json.dumps(resultlist, indent=4))
    f = open("testResult.json", "w")
    f.write(json.dumps(resultlist, indent=4))
    f.close()

if __name__ == "__main__":
    main()
