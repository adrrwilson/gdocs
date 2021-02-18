#Adrian Wilson - Jan 5th/2020 - Sitting at the chair of the one and only Lina as she studies upstairs.

#This Python script interprets the verb, noun, adjective and phrase files as 2D lists, each entry corresponding to an instance of 'german, english, score'.

#subj dictionary is used to convert single letter user input to the corresponding subject.
subj = {'v' : 'verb', 'n' : 'noun', 'a' : 'adjective'}

import random #Used to switch between ger - eng and eng - ger, and to randomly select questions.
foop = {0 : "German", 1 : "English"}
newscores = {} #Logs scores during execution, and is used to update text files after quit() is called.
minscore = 4 #minimum score before word stops being tested

#Before ending the quiz, quit() updates the scores.
def quit():
	open('/home/adrian/gdocs/data/' + 'g' + subj[sub] + '.txt', 'w').close()
	with open('/home/adrian/gdocs/data/' + 'g' + subj[sub] + '.txt', 'w') as update:
		for q in qcopy:
			if not q[0] in newscores.keys():
				update.write("%s, %s, %s\n" %(q[0], q[1], q[2]))
				continue
			#print("%s, %s" %(q[2], newscores[q[0]]))
			if not q[2] == newscores[q[0]]:
				update.write("%s, %s, %s\n" %(q[0], q[1], newscores[q[0]]))
	print("Scores updated successfully. Gute Arbeit! Bis zum nächsten mal!")

#Feedback! Generously provided (mostly) by Lina.
with open('/home/adrian/gdocs/feedback/negative.txt', 'r') as reader:
	nfeedback = reader.read().splitlines()
with open('/home/adrian/gdocs/feedback/positive.txt', 'r') as reader:
	pfeedback = reader.read().splitlines()

sub = input("Quiz time! Would you like to test nouns, verbs or adjectives? (n/v/a): ")
while not (sub == 'n' or sub == 'v' or sub == 'a'):
	sub = input("Please select a valid option. (n/v/aq): ")
	
print("Alrighty, %ss it is! Enter 'q' when you'd like to quit." %subj[sub])

#Import entries from corresponding subject's text file.
with open('/home/adrian/gdocs/data/' + 'g' + subj[sub] + '.txt') as doc:
	qlist = doc.readlines()

#Skim away newlines from document, and ignore end them at the end of each line.
qlist = [x[:-1] for x in qlist if not x == '\n']
#This copy will be used rewrite the subject's text file.
qcopy = [x.split(", ") for x in qlist]
#Skim entries from qlist with score greater than minscore.
qlist = [x.split(", ") for x in qlist if int(x[-1]) < minscore]

#This is where the fun begins!
while(True):
	if not len(qlist): 
		print("No questions available! (With scores less than %s)." %minscore) 
		quit() ; break
		
	q = random.choice(qlist)
	#foo determines whether the translation will be ger to eng or vice versa.
	foo = random.choice([0,1])
	ans = input("What is the %s translation of: %s? " %(foop[foo], q[(foo + 1) % 2]) )
	#Quit option
	if ans == 'q':
		quit() ; break
		
	#Incorrect guess
	if not ans == q[foo]:
		print("%s The correct answer was: %s." %(random.choice(nfeedback), q[foo]))
		
	#Correct guess
	else:
		print("%s" %random.choice(pfeedback))
		if not q[0] in newscores.keys():
			newscores[q[0]] = int(q[2])
		newscores[q[0]] = newscores[q[0]] + 1
		if newscores[q[0]] > minscore:
			print("You've mastered this translation! Gute Arbeit!")
			qlist.remove(q[:])
		

