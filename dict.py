from difflib import SequenceMatcher, get_close_matches

import json

data = json.load(open("data.json"))

def find_definition(word) :	
	word = word.lower()

	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0 :
		yon = input( "The word doesn't exist in the dictionary. Did you mean one of these words?: {}. Enter Y for Yes and N for No: ".format(get_close_matches(word,data.keys())))

		if yon == 'Y' :
			new_word = input("Enter the word from the given choices: ")
			new_word = new_word.lower()
			return data[new_word]
		elif yon == 'N' :
			return "No entry found. Please enter another word."
		else :
			return "Invalid Entry."
	else:
		return "No entry found. Please enter another word."

while(True) :
	word = input("Enter the word: ")
	
	if (word == "exit") :
		break;
	else :
		print(find_definition(word))
	
