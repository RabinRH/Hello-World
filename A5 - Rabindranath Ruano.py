# Title:  	A5 - Rabindranth Ruano Hafferan
# Author: 	Rabindranath Ruano Hafferan
# Purpose:	Creates a story based on verbs, adjectives and nouns that the user inputs
# Usage:	Practice python functions and reusability

# Notes:	Create Mad Libs style game where user inputs certain types of words
#			Story doesn't have to be too long but should have some sort of story line.

# Subgoals:
#			If user puts in a name, change first letter to capital letter
#			Change the word "a" to "an" when next word in sentence begins with a vowel



'''

To wash clothes, you first need to REMOVE the clothes. Then you need to TURN ON the WASHER. Take your time so you don't STAIN any clothes that might be dirty. 
Separate the COLORED CLOTHES from the WHITE CLOTHES and then load the WASHER. Make sure you don't mix the WHITE CLOTHES with the RED CLOTHES. 
Set the temperature to 100 and start the cycle. Once it's finished, PICK UP the clothes and THROW them into the dryer.
Set the temperature and TURN ON the dryer. After about 60 minutes, it should be complete! Now all you have to do is PUT ON the clothes and voila! Clean clothes!

'''

'''
To wash _(noun you wear)_, you first need to _(verb)_. Then you need to _(verb 2)_ the _(adjective)_ washer. Take your time so you don't _(adjective describing clothes)_ that might be dirty. 
Separate the _(color plural)_ from the _(color plural 2)_ and then load the _(adjective)_ washer. Make sure you don't mix the _(color plural)_ _(noun you wear)_ with the _(color plural 2)_ _(noun you wear)_.
Set the temperature to _(number)_ and _(verb that means go)_ the cycle. Once it's finished, _(verb 3)_ the _(noun you wear)_ and _(adverb with ly ending)_ _(verb 4)_ them into the dryer.
After about _(number referring to time)_ minutes, it should be complete! Now all you have to do is _(verb 5)_ and Voila! _(adjective 2)_ _(noun you wear)_!

'''

from time import sleep
import datetime

def madlibs():
	now = datetime.datetime.now()
	print("Madlibs starting, please enter the words below: ")
	print("______________________________________")
	wearablenoun = input("A noun you can wear: ")
	verb1 = input("A verb: ")
	verb2 = input("A second verb: ")
	machineadj = input("An adjective to describe a machine: ")
	clothesadj = input("An adjective describing clothes: ")
	colorplural1 = input("plural color: ")
	colorplural2 = input("another color plural: ")
	number = input("a number: ")
	goverb = input("a go verb: ")
	verb3 = input("third verb: ")
	adverbly = input("an adverb with ly at the end: ")
	verb4 = input("fourth verb: ")
	numbertime = input("number from 1-120: ")
	verb5 = input("the final verb: ")
	clothesadj2 = input("A second adjective to describe clothes: ")
	print("\n ____________________________________")
	print("All words have been gathered, completing story now.")
	sleep(10)
	print("To wash " + wearablenoun + ", you first need to " + verb1 + ".")
	sleep(5)
	print("Then you need to " + verb2 +  " the " + machineadj + " washer.")
	sleep(5)
	print("Take your time so you don't " + clothesadj + " clothes that might be dirty.")
	sleep(5)
	print("Separate the " + colorplural1 + " from the " + colorplural2 + " and then load the " + machineadj + " washer.")
	sleep(5)
	print("Make sure you don't mix the " + colorplural1 + " " + wearablenoun + " with the " + colorplural2 + " " + wearablenoun)
	sleep(5)
	print("Set the temperature to " + number +  " and " + goverb + " the cycle.")
	sleep(5)
	print("Once it's finished, " + verb3 + " the " + wearablenoun + " and " + adverbly + " " + verb4 + " them into the dryer.")
	sleep(5)
	print("After about " + numbertime + " minutes, it should be complete! Now all you have to do is " + verb5 + " and Voila! " + clothesadj2 + "  " + wearablenoun + "!")
	sleep(2)

	print("\n time to generate the story: " + str(datetime.datetime.now() - now))
	print("\n The End \n\n")


madlibs()



