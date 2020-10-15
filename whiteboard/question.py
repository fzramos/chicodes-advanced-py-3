"""
Length of Last word
Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “), return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.
Example Input: “Hello World”
Example Output: 5
Example Input 2: “The brown loud cow plowed”
Example Output 2: 6
"""

def lastWord(sentence):
    words = sentence.split()
    return len(words[-1])
    
print(lastWord('Hello World'))
print(lastWord('The brown loud cow plowed'))