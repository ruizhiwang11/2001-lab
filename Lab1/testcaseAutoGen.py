import random
import json 

TestingCharlist=['A','C','G','T']
listGen={}
tmpgen={}
testinglist={}

#Parameter you need to set
LOWER_BOUND=7
HIGHER_BOUND=10
REPEAT_TIME=5

def readInPut():

    LOWER_BOUND = input ("Enter LOWER_BOUND :") 
    HIGHER_BOUND = input ("Enter HIGHER_BOUND :") 
    REPEAT_TIME = input ("Enter REPEAT_TIME :") 
    return [LOWER_BOUND,HIGHER_BOUND,REPEAT_TIME]




"""Single String Generation""" 
def singStringGen(charlist,lens=int):
    temp=""
    for i in range (0,lens):
        temp += charlist[random.randint(0,3)]
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
getinput=readInPut()
testinglist=testCaseGen(int(getinput[0]),int(getinput[1]),int(getinput[2]))
