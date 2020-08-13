import sys #for terminating the program if the frequencies are invalid
import matplotlib.pyplot as plot, random

def motifChecker(motif): #Motif Checker for combinations of ACTG
    for i in motif:
        if i != 'A' and i != 'T' and i != 'C' and i != 'G':
            return False #i ended up changing this from a cascading if struct, it seems more efficient
    return True

def SequenceGenerator(BaseFrequency, N):# Generates Sequence form all four frequencies
    sequence = ""
    for i in range(0, N):
        rand = random.random()
        if rand < BaseFrequency[0]:#bc th indices 0 - 3 are all the frequences of the Bases ACTG respectively,
            sequence += 'A'
        elif BaseFrequency[0] <= rand < BaseFrequency[0] + BaseFrequency[1]:
            sequence += 'T'
        elif  BaseFrequency[0] + BaseFrequency[1] <= rand < BaseFrequency[0] + BaseFrequency[1] + BaseFrequency[2]:
            sequence += 'C'
        else:
            sequence += 'G'
    return sequence

def sequenceCounter(sequence, motif): #counts for the motifs in the sequence string
    return sequence.count(motif) #the documentation shows a .count method, and
    # apparently it works for strings other than a char and orders the indiex searching in
    # accordance to the stirng length

def Trials(BaseFrequency, motif, lengths): #this is essentially a glorified for loop, <- Just kidding
    # runs the simulation of the sequence generator and motif counter 100 times for each length
    expectedNumber = []
    for i in lengths: #iterates through all of the possible values
        counter = 0
        for x in range(0, 100):
            sequence = SequenceGenerator(BaseFrequency, i)
            counter += sequenceCounter(sequence, motif)
        expectedNumber.append(counter/100)
    return expectedNumber





 # PART 1 <---------------------------------------------------------->
print("Hello, please enter a string combination of only As,Ts,Cs, or Gs\n")

checker = False #checker, try to figure out a way to do this recursively

while checker is False:
    motif = str(input("\nString:\t"))
    checker = motifChecker(motif) #checks if the bool value is false ro true regarding the combination of motif


BaseFrequency, motifFrequency = [], 1 #indexes 0 - 3, inclusive are for the frequencies of the DNA Bases

for i in 'ATCG':
    Base = float(input("Enter Frequency for Base {}:\t".format(i)))
    Base /= 100
    BaseFrequency.append(Base)
    motifFrequency *= (Base)

sum = 0

print(motif)

for i in range(0, len(BaseFrequency)):
    sum += BaseFrequency[i]
    if sum > 1.0:
        print("Frequencies are Invalid")
        sys.exit()



# PART 2 <---------------------------------------------------------->
motifFinder, probability = [], 0
for i in range(len(motif), 5001):
    probability = 1 - (1 - motifFrequency) ** i
    motifFinder.append(probability)


#the probability plot is in part3 of the code for the othe rouput to execute before the plots get plotted on the loop


#part 3 <---------------------------------------------------------->
print("Motif:\t", motif)
#for i in 'ACTG':
#    print("{}'s Frequency:\t{}".format(i, BaseFrequency[x]))
#    x+=1
print("Probability of appearing in a sequence N = 4 is {} or {} %".format(motifFrequency, motifFrequency * 100))


lengths = (100,1000, 2000, 5000, 10000) # essentially the x axis,
# this is what he average motifs found value corresponds to, the length N is each fo these indices

plot.figure(1)
plot.xlabel('Sequence Length')
plot.ylabel('Probability of Finding At Least One Motif Once')
plot.title('Probability of Finding At Least One Motif Once vs. Sequence Length')
plot.plot(motifFinder)


expectedNumber = Trials(BaseFrequency, motif, lengths)
plot.figure(2)
plot.ylabel('Average Number of Motifs')
plot.xlabel('Sequence Length')
plot.title('Average Number of Motifs vs. Sequence Length')
plot.scatter(lengths, expectedNumber, s = 200)
plot.show()

print("Motif:\t", motif)

#for i in 'ACTG' and x in '0123':
#    print("{}'s Frequency:\t{}".format(i, BaseFrequency[int(x)]))

#print("Probability of appearing in a sequence N = 4 is {} or {} %".format(motifFrequency, motifFrequency * 100))

