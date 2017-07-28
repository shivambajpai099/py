import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

fil = open("ter.txt","r")
ne = fil.read()
print "Original Paragraph:"
print ne
print '\n'
new_s = ne.lower()

ne = ne.replace('\n',' ')
ne = ne.split('.')





delim = [',','?','/','//','!','\\','[',']','&','-',':',';','@','...','>','<','\n','\r']

for i in delim:
	new_s = new_s.replace(i,'')					#Text Cleaning 

re = new_s.split(".")

start = nltk.word_tokenize(re[0])
sent = []

stop_words = set(stopwords.words('english'))

for i in range(1,len(re)):
	filtered_sentence = []
	temp = nltk.word_tokenize(re[i])	
	for w in temp:
    		if w not in stop_words:
        		filtered_sentence.append(w)
	sent.append(filtered_sentence)
	
tokens = []

for i in range(1,len(sent)):
	te = nltk.word_tokenize(' '.join(sent[i]))
	tokens = tokens + te

score = []

for i in range(len(sent)):
	score.append([])

#1 Sentence Location
score[0].append(1)
score[1].append(0.8)
score[2].append(0.6)
score[3].append(0.4)
score[4].append(0.2)

for i in range(5,len(sent)-1):
	score[i].append(0)


#2Sentence length

maxi = 0
for i in range(len(sent)-1):
	if len(sent[i]) > maxi:
		maxi = len(sent[i])


for i in range(len(sent)-1):
	score[i].append(float(len(sent[i]))/maxi)


#3 TERM FREQUENCY
maxi = 0
for i in set(tokens):
	le = tokens.count(i)
	if le>maxi:
		maxi = le

for i in range(len(sent)-1):
	sumi = 0	
	for j in range(len(sent[i])):
		le = tokens.count(sent[i][j])
                av = float(le)/maxi
		sumi = sumi + av 
        avg = float(sumi)/len(sent[i])
	score[i].append(avg)

#4 SENTENCE RESEMBELENCE TO TITLE RESEMEBELENCE
count = 0
for i in range(len(sent)-1):
	count = 0
	for word in start:
		if word in sent[i]:
			count = count + 1
        myset = set(start)
	myset.update(sent[i])
	val = float(count)/len(myset)
        score[i].append(val)


#5 SENTENCE CENTRALITY

size = len(tokens)
for i in range(len(sent)-1):
        count = 0
	for j in range(len(sent)-1):
		flag = 0
		if i!=j:
			for k in range(len(sent[i])):
				for l in range(len(sent[j])):
					if k ==l:
						count = count + 1
						flag = 1
						break
				if flag ==1:
					break
					
	score[i].append(float(count)/size)



#6 EMPHASIZE WORDS

emp = ["very" , "amazingly" , "remarkably" , "especially", "certainly", "crucially", "truly", "really", "exceptionally", "particularly", "specifically", "seriously", "importantly", "surely", "extremely", "incredibly", "absolutely", "quite", "highly", "indeed" ]

for i in range(len(sent)-1):
	count = 0
	for j in range(len(sent[i])):
		for k in emp:
			if k == sent[i][j]:
				count = count + 1
	score[i].append(float(count)/len(sent[i]))


#7 SENTENCE INCLUSION OF NAME ENTITIES

for i in range(len(sent) - 1):
	count = 0
	seta = nltk.pos_tag(sent[i])
	for a,b in seta:
		if b == "NNP":
			count = count + 1;
	score[i].append(float(count)/len(sent[i]))



#8 SENTENCE INCLUSION OF NUMERICAL DATA

for i in range(len(sent)-1):
	count = 0
	for j in range(len(sent[i])):
		if sent[i][j].isdigit() == True:
			count = count + 1
	score[i].append(float(count)/len(sent[i]))


#9 Number of collocation
for i in range(len(sent)):
	re[i] = ' '.join(sent[i])
bigrams = [b for l in re for b in zip(l.split()[:-1], l.split()[1:])]
freq = nltk.FreqDist(bigrams)

for i in freq.hapaxes():
	bigrams.remove(i)

bigrams = set(bigrams)

print '\n'

for i in range(len(sent)-1):
	count =0
	for j in range(len(sent)-1):
		flag = 0
		if i!=j :
			for k in range(len(sent[i])):
				if flag == 0:
					for l in range(len(sent[j])):
						if flag == 0:
							for a,b in bigrams:
								if( a == sent[i][k] and b == sent[j][l]):
									count = count + 1
									flag = 1
									break
						else:
							break
				else:
					break
	score[i].append(float(count)/len(sent))

tot = []


wt = [14,3,1,4,13,12,11,2,12]

for i in range(len(score)):
	su = 0
	for j in range(len(score[i])):
		su = su + wt[j]*score[i][j]
	tot.append(su)

fin = []
for i in range(len(tot)):
	fin.append([])
        fin[i].append(float(tot[i])/9)
	fin[i].append(i)



fin.sort(key=lambda x: x[0],reverse=True)

print ("How many lines of summary you want:")
a = raw_input()
for i in range(0,int(a)):
	print ne[fin[i][1]+1] + '.'


