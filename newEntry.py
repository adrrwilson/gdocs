#Adrian Wilson - Jan. 5th/2020. Sitting across from the one and only Linaaa.

#This Python script is used to quickly and efficiently update my personal list of German verbs/nouns/adjectives. It will be implemented by a Python script used to quiz me on each subject. Note that for each new entry, a '0' is appended, which will be incremented by the quiz.py app each time a translation is correctly answered.

#Which subject are we working on?
import sys 
subj = sys.argv[1]

#Where are the corresponding file and backup file located?
loc = '/home/adrian/gdocs/data/' + 'g' + subj + '.txt'
backuploc = '/home/adrian/gdocs/backups/' + 'g' + subj + 'backup.txt'
#lines list is used to lookup if a word has been added already.
with open(loc, 'r') as reader:
	lines = reader.readlines()

print("Hallo! ", end = '')
while True:
	ger = input("Please enter a German %s, or q to quit: " %subj)
	if ger == 'q':
		print("Auf wiedersehen!") ; break

	#Perform a check to see whether a word already exists in the file
	flag = False
	for line in lines:
		if line.split(", ")[0] == ger:
			print("That word has already been added!\n")
			flag = True ; break
	if flag: continue
		
	eng = input("Next, it's translation to English: ")
	
	#Only accept yes or no answers.
	ans = input("Add entry '%s, %s' to the list of German %ss? (y/n): " \
	%(ger, eng, subj) )
	
	while not (ans == 'y' or ans == 'n'): 
		ans = input("Excuse me, but that wasn't an answer to my question. Enter (y/n): ")
		
	if ans == 'y':
		with open(loc, 'a') as writer:
			writer.write("%s, %s, 0\n" %(ger, eng))
		with open(backuploc, 'a') as bwriter:
			bwriter.write("%s, %s, 0\n" %(ger, eng))
		print("Entry added successfully.\n")
	else: print("Entry not added.\n")


