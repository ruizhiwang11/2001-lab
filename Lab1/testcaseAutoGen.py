import random
import json 
TestingCharlist=['A','C','G','T','U']
listGen={}
tmpgen={}
testinglist={}

#Parameter you need to set
LOWER_BOUND=5
HIGHER_BOUND=15
REPEAT_TIME=4

"""Single String Generation""" 
def singStringGen(charlist,lens=int):
    temp=""
    for i in range (0,lens):
        temp += charlist[random.randint(0,4)]
    #print (temp)
    #print (len(temp))
    return temp

"""list of string generation"""
def testCaseGen(start,end,numb):
    for i in range (start,end+1):
        tmpgen={i:[]}
        for j in range(numb):
            x=singStringGen(TestingCharlist,i)
                    
            tmpgen[i].append(x)
                
        listGen.update(tmpgen)
        
    #print (json.dumps(listGen, indent=4))     
    return listGen 
   
    
"""call for the function"""
testinglist=testCaseGen(LOWER_BOUND,HIGHER_BOUND,REPEAT_TIME)
