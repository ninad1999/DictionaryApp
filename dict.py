from difflib import get_close_matches
import json
import tkinter as tk

window = tk.Tk()
data = json.load(open("data.json"))

def list_format(lst):
	i = 1
	for meaning in lst :
		t1.insert(tk.END, str(i) + ') ' + meaning + '\n')
		i += 1

def find_definition() :
	word = e1_value.get()	
	word = word.lower()

	if word in data:
		t1.delete("1.0", tk.END)
		list_format(data[word])
	elif word.title() in data:
		t1.delete("1.0", tk.END)
		list_format(data[word.title()])
	elif word.upper() in data:
		t1.delete("1.0", tk.END)
		list_format(data[word.upper()])
	elif len(get_close_matches(word, data.keys())) > 0 :
		t1.delete("1.0", tk.END)
		t1.insert(tk.END,  "The word doesn't exist in the dictionary. Did you mean one of these words?:\n {} ".format(get_close_matches(word, data.keys())))
	else:
		t1.delete("1.0", tk.END)
		t1.insert(tk.END,  "No entry found. Please enter another word.")

b1 = tk.Button(window, text="Enter", command=find_definition)
b1.grid(row = 0, column = 2, sticky="w")
b1.config(width=10)

e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)
e1.config(width=20)

t1 = tk.Text(window, height=10)
t1.grid(row=1, column=0, columnspan=3)

window.mainloop()

