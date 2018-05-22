from difflib import SequenceMatcher, get_close_matches

import json

data = json.load(open("data.json"))

def find_definition(word) :	
	word = word.lower()

	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0 :
		return "The word doesn't exist in the dictionary. Did you mean one of these words?: {}".format(get_close_matches(word,data.keys()))
	else:
		return "No entry found. Please enter another word."

while(True) :
	word = input("Enter the word: ")
	
	if (word == "exit") :
		break;
	else :
		print(find_definition(word))
	
