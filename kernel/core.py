#!/usr/bin/python
#grammar ripper word processor
#NLTK? maybe later, i'm gonna use it
#just an example, this core is still on massive development

from tobe import *
from random import shuffle
from random import choice
from personalpronoment import *
from engine import *

person = personal()

#person.pronoment[0] == 'i'
#person.pronoment[1] == 'you'
#personal.pronoment[0] == 'i'
#personal.pronoment[1] == 'you'
#personal.pronoment[2] == 'she'
#personal.pronoment[3] == 'he'
#personal.pronoment[4] == 'it'
#personal.pronoment[5] == 'we'
#personal.pronoment[6] == 'they'

tobes = [to.i, to.you, to.we, to.they, to.he, to.she]

def shuffletobesandpickonetobe():
    #the function name is fuckin long eh?
    shuffle(tobes)
    return choice(tobes) #return one of shuffled tobe
 
def ripp(sentence):
    return sentence.split(' ')

def ripthegrammar(rippedsentence):
    # grammatical error
    # i am stupid --> i are stupid || --> i is stupid
    personname=rippedsentence[0]
    rippedsentencetobe=rippedsentence[1]
    etc=rippedsentence[2]
    if personname == person.pronoment[0] and rippedsentence[1] == to.i:
        newtobe = shuffletobesandpickonetobe()
        if newtobe != to.i:
            return rippedsentence[0]+ ' ' +newtobe +' '+rippedsentence[2]
        else:
            pass
    elif personname == person.pronoment[1] and rippedsentence[1] == to.he:
        newtobe = shuffletobesandpickonetobe()
        if newtobe != to.he:
            return rippedsentence[0]+' '+newtobe+' '+rippedsentence[2]
        else:
            pass
    else:
        pass
