import re
from Automate import *


lines= open("a0.descr",'r').read().splitlines()

automate = Automate()

statesToAdd = 0
statesInit = ""
statesEnd = ""
for line in lines :


    line = re.split(" ",line)
    c = line[0]
    # On parcours la première lettre de chaque ligne

    if c =='C':
        # add comment
        pass
    elif c == 'M':
        automate.addMeta(line[1])
    elif c == 'V':
        automate.addVocabEntree(re.sub('"','',line[1]))
    elif c == 'O':
        automate.addVocabSortie(re.sub('"', '', line[1]))
    elif c == 'E':
        statesToAdd = int(line[1])
    elif c == 'I':
        l = line [1:]
        statesInit = [i for i in l]
    elif c == 'F':
        l = line[1:]
        statesEnd = [i for i in l]
        print(statesEnd)
    elif c == 'T':
        if len(line) == 4:
            line.append('')
        automate.addTransition(int(line[1]),int(line[3]),line[2],line[4])
    elif c =='':
        pass
    else:
        print("The character :"+c+ " is an invalid input")

#Add init states
for s in statesInit:
    automate.addInitState(int(s))
#Add end states
for s in statesEnd:
    automate.addFinalState(int(s))
#Add remaining states
automate.addNumEtat(statesToAdd)
automate.verify()
print(automate)