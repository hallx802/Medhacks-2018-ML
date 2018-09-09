{\rtf1\ansi\ansicpg1252\cocoartf1561
{\fonttbl\f0\fnil\fcharset134 PingFangSC-Regular;\f1\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \uc0\u65056 
\f1 61762b1b-2643-4787-bf58-1b0ba955abf8s
\f0 \uc0\u65056 
\f1 \
import numpy as np\
import matplotlib.pyplot as plt\
import sys, os\
\
inputString = "All around me are familiar faces Worn out places, worn out faces Bright and early for their daily races Going nowhere, going nowhere Their tears are filling up their glasses No expression, no expression Hide my head, I want to drown my sorrow No tomorrow, no tomorrow And I find it kinda funny, I find it kinda sad The dreams in which I'm dying are the best I've ever had I find it hard to tell you, I find it hard to take When people run in circles it's a very very Mad world, mad world Children waiting for the day, they feel good Happy birthday, happy birthday Made to feel the way that every child should Sit and listen, sit and listen Went to school and I was very nervous No one knew me, no one knew me Hello teacher, tell me what's my lesson Look right through me, look right through me And I find it kinda funny, I find it kinda sad The dreams in which I'm dying are the best I've ever had I find it hard to tell you, I find it hard to take When people run in circles it's a very very Mad world, mad world Enlarge your world Mad world"\
inputStringList = (inputString.lower().replace(",","")).split(" ")\
\
angerString = "Anger angry aggravate agress attack assault bitter blackmail blacklist cold coldhearted combat compet crab cross cynic contempt detest deviant deviate danger demand disgruntled disgust enrage ego frustrate fury furious grouch grump piss hate hatred hating heartless hostile impuls temper ignorant inebriate intoxicate irrita irration infuriate jade jealous selfish snap quarrel shout spite provoke rage resent revenge rot sadist mad masochist annoy argument"\
anger = ("".join(angerString.lower()).split(" "))\
\
sadString = "ashame,alone,beat,awful,insult,isolate,judg,mess,negative,bad,betray,blame,bother,detach,devoid,anguish,hopeless,punish,quiet,disapprove,ridicule,disbelieve,discard,discriminate,disgrace,rob,exclude,sterotype,imbalance,belittle,coward,criticize,deceive,defame,defect,dehuman,defenseless,poop,berate,evade,bully,bullie,evasive,elusive,elude,elus,cheat,bum,broke,break,stupid,responsible,ignore,imprison,inadequate,regret,reject,single,incapable,incompetant,burden,abandon,abuse,crush,damage,joyless,defeat,degrade,deject,demean,demoralize,demotivate,deplete,depress,deprive,desert,desolate,despair,devalu,devastate,dark,dead,chicken,consume,controll,corner,deflate,delicate,depend,deprave,disappoint,discourage,disempower,dishearten,dismay,disregard,disrespect,dissatisf,down,dump,downhearted,dispose,disposable,embarrass,emotional,emotions,drain,drear,dumb,discard,displease,doom,doubt,downtrodden,down,dread,bankrupt,encumber,exhaust,emotionless,emotion,flaw,fragile,grief,griev,guilt,heartbr,helpless,humiliate,hurt,insufficient,invisible,quiet,label,laugh,lie,lone,gloom,glum,lost,lousy,lousiness,loveless,low,mess,miser,mistreat,misunderst,mood,need,numb,pain,pessimist,powerless,pushed,sad,suffer,suppress,oppress,burise,burn,barren,sensitiv,shy,slow,small,bleak,poor,screw,pathetic,tire,worthless,worth,fail,empty,empti"\
sad = ("".join(sadString.lower()).split(","))\
\
anxiousString = "anxious,puzzle,queer,question,strange,blur,baffle,awkward,bizzare,annoy,avoid,apprehensive,box,irritate,panic,paranoid,petrif,nag,claustrophob,close,obsess,crowd,confine,scare,suspicious,afraid,stuck,cramp,suffocate,sother,distraught,distress,fear,freak,stress,fright,intimidate,hurried,harried,indecisive,inefficient,nervous,nerve,distant,pressure,distract,disturb,neurotic,neur,overwhelm,rattle,push,conflict,confront,shake,panic,nerv,jitter,afraid,worr,restless,tense,beat,rape,abuse,abusi"\
anxious = ("".join(anxiousString.lower()).split(","))\
\
suicidalString = "Cut,Commit,Harm,Suicid,dead,Die,Killing,Death,Dying,Gone,Notice,Attempt,bye,done,Save,Unbear,Disappear,last,Reliev,Relief,Forever,Razor,Blade,Hang,Jump"\
suicidal = ("".join(suicidalString.lower()).split(","))\
\
angerCount = 0\
sadCount = 0\
anxiousCount = 0\
suicidalCount = 0\
total = 0\
for emotion in range(0,len(inputStringList)):\
    for x in range(0,len(anger)):\
        total +=1\
        if anger[x] in inputStringList[emotion]:\
            angerCount +=1\
    for y in range(0,len(sad)):\
        if sad[y] in inputStringList[emotion]:\
            sadCount += 1\
        total += 1\
    for z in range(0,len(anxious)):\
        if anxious[z] in inputStringList[emotion]:\
            anxiousCount += 1\
        total +=1\
    for t in range(0,len(suicidal)):\
        if suicidal[t] in inputStringList[emotion]:\
            suicidalCount += 1\
        total += 1\
\
\
feels = ["anger", "depression", "anxiety", "suicidal ideation"]\
feelings = [angerCount,sadCount,anxiousCount,suicidalCount]\
currentFeeling = 0\
\
maxFeel = max(float(angerCount)/len(inputStringList),float(sadCount)/len(inputStringList),float(anxiousCount)/len(inputStringList))\
\
if maxFeel == angerCount:\
    currentFeeling = 0\
elif maxFeel == sadCount:\
    currentFeeling = 1\
elif maxFeel == anxiousCount:\
    currentFeeling = 2\
elif maxFeel == suicidalCount:\
    currentFeeling = 3\
normal = len(inputStringList) - (angerCount + sadCount + anxiousCount + suicidalCount)\
frequencies = [float(angerCount)/len(inputStringList),float(sadCount)/len(inputStringList),float(anxiousCount)/len(inputStringList), float(suicidalCount)/len(inputStringList),float(normal)/len(inputStringList)]\
if float(angerCount + sadCount + anxiousCount + suicidalCount)/len(inputStringList) >= 0.025:\
    print("You seem to be feeling " + feels[currentFeeling] + ". It is recommended you reach out to the following: (resources)")\
else:\
    print("You seem to be feeling okay! Keep up the great work!")\
\
# Data to plot\
sizes = [(angerCount+sadCount+anxiousCount+suicidalCount),normal]\
plt.figure(figsize=plt.figaspect(0.75))\
labels = ['Negative', 'Normal']\
\
colors = ['grey', 'lightgreen']\
explode = (0.1,0)\
\
\
\
p = plt.pie(sizes, explode = explode, colors = colors, labels=labels, shadow=True)\
plt.show()\
\
sizes = [angerCount,sadCount,anxiousCount,suicidalCount]\
plt.figure(figsize=plt.figaspect(0.75))\
labels = ['Anger', 'Depression','Anxiety',"Suicidal"]\
\
colors = ['lightcoral', 'c','gold','grey']\
explode = (0,0,0,0.1)\
\
\
\
p = plt.pie(sizes, explode = explode, colors = colors, labels=labels, shadow=True)\
plt.show()\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
}