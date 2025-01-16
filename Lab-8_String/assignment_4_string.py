"""Q4. 4. Write a Python program to count and display the vowels of a given text 

String=”Welcome to python Training”
"""

input_str="Welcome to python Training"
vowels="aeiou"
vowel_cnt={}
for i in input_str.lower():
    if i in vowel_cnt:
        vowel_cnt[i]=vowel_cnt[i]+1
    elif i in vowels:
        vowel_cnt[i]=1

print(vowel_cnt)
#output without dictonary
print("the vowels of a given text are: ")
for i,j in vowel_cnt.items():
    print(i,"=",j)

    
