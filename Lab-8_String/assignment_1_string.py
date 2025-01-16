"""1. Write a Python program to count the occurrences of each word in a given sentence 

string = “To change the overall look of your document.
To change the look available in the gallery”
"""

input_str="To change the overall look of your document. To change the look available in the gallery"
words=input_str.split(" ")
for word in set(words):
    print(word,input_str.count(word))
    
