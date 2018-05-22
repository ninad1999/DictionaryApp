from difflib import SequenceMatcher

SequenceMathcher(None,)  # first argument is for "isjunk" like while comparing 2 text lines, you want to ignore spaces or breaklines, then put that as first argument

import json

data = json.load(open("data.json"))

def find_definition(word) :
	word = word.lower()

	if word in data:
		return data[word]
	else:
		return "No entry found. Please enter another word."

while(True) :
	word = input("Enter the word: ")
	
	if (word == "exit") :
		break;
	else :
		print(find_definition(word))
	
