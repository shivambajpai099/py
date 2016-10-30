#PROGRAM TO PLAY BLANKS
import random
names = ['MOUNTAIN','EXCELLENT','OUTRAGEOUS','OUTSTANDING','EXTRAORDINARY']
orig_word = random.choice(names)

#WORD CREATION
guess_word = orig_word
length = len(guess_word)       
tt = list(guess_word)
for i in range(1,length,2):
   tt[i] = "_"
    
guess_word = "".join(tt)

#PRINTED OUTPUT
print ("THE WORD YOU HAVE TO GUESS IS : ")
print guess_word
chances=0
while chances<5:
    alph = raw_input("GUESS A SUITABLE ALPHABET : ")
    

    orig = list(orig_word)

    for i in range(1,length,2):
        if orig[i] is alph:
            tt[i] = alph

    guess_word1 = "".join(tt)
    if guess_word1 == guess_word:
        chances = chances + 1
        
    guess_word = guess_word1    
    print guess_word

    if guess_word == orig_word:
        print "\nBravo!! You got it right!!"
        exit()
        
  
    print "You have " + str(5 - chances) + " chances left"  

print "Oops!! You lost the game. The word was " + orig_word
