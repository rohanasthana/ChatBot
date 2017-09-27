from nltk.tag import pos_tag
import time
import datetime

import sys
import random
from textblob import TextBlob

now=datetime.datetime.now()

def polarity(sen):
    sentence=TextBlob(sen)
    
    p=sentence.sentiment.polarity
    return p

def subjectivity(sen):
    sentence=TextBlob(sen)
    s=sentence.sentiment.subjectivity
    return s
def check(sen):
    if(polarity(sen)<0 and subjectivity(sen)>=0.5):
        print ("Hey..you need to calm down..I just asked your name")
        print ("Come back when you are calm.. Byeee")
        sys.exit()
print("Have you eaten yet? Its past " +str(now.hour))
sen=raw_input()

        

a=["Hey there. I couldn't recognize you. You are...??",
   "Hello there. May I know your name?",
   "Yoo.. You look cute ;). What's your name?"]
print(random.choice(a))
sen=raw_input()
check(sen)
    
tagged_sent = pos_tag(sen.split())
name=[word for word,pos in tagged_sent if pos=='NNP']
print(" ".join(str(word) for word in name)+ "?" )
flag=raw_input()
if (polarity(flag)<0.2):
    print("Ohh sorry.. I'm not that smart I guess.. Now Input your name as a string buddy")
    name=raw_input()
    print(name + " ..Gotcha.!! ")
print("All right. Now what's your gender.Male or female?")
gender=raw_input()
gender=gender.upper()
if(gender != "MALE" and gender !="FEMALE"):
          print("One word please.. Male or female?")
          gender=raw_input()    

check(gender)
a=["Great. Let's talk.",
   "Awesome. So let's get started "
   "Ohkk...So let's start talking"]
print(random.choice(a))
time.sleep(3)
print("What was the last movie you watched?")
sen=raw_input()
print("Oh wow.. I want to watch that movie too..!! How is it?")
sen=raw_input()
if(polarity(sen)>=0.7):
          print("I knew it would be fantastic..Gotta watch it soon")
if(polarity(sen)>=0.5 and polarity(sen)<=0.7):
          print("Hmmm...it is quite good according to you. Anyway..will watch it soon")
if(polarity(sen)>=0 and polarity(sen) <=0.4):
          print("So it was a average movie according to you.. You got me thinking buddy")
if(polarity(sen)<0 and polarity(sen)>=-0.5):
          print("Oh..so it was a quite bad movie")
if (polarity(sen)<-0.5):
          print("Oh No...Was it that bad? I hope the tickets get refunded")

print("Have you eaten yet? Its past " +str(now.hour))
sen=raw_input()
if(polarity(sen)>0.5):
    
    print("Good. I haven't. Bye")
else:
    print("So let's first eat then talk.Byee")













