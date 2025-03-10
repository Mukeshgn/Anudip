"""1. Write a Python program to count the occurrences of each word in a given sentence 

string = “To change the overall look of your document.
To change the look available in the gallery”
"""

# Given Input sentence
input_sentence="To change the overall look of your document. To change the look available in the gallery"

# Split the sentence into individual words with space(" ")
words=input_sentence.split(" ")

# Iterate through each word in the set
for word in set(words):
    # Print the word counts
    print(word,input_sentence.count(word))


"""
OUTPUT:

change 2
overall 1
document. 1
To 2
your 1
available 1
look 2
in 1
the 3
of 1
gallery 1
"""
    
