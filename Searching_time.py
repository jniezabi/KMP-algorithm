from Searching import nfind, kmpfind
import sys
from numpy import random
import timeit

text = sys.argv[len(sys.argv) - 1]

with open(text, "r") as txt:
    txt_content = []
    txt_content1 = []
    for letter in txt.read().strip("\n"):
        txt_content.append(letter)
        txt_content1.append(letter)

txt_content1.append("test")

# empty string or text
print("Empty string:")
print("naive", nfind("", txt_content))
print("KMP", kmpfind("", txt_content))

print("\nEmpty text:")
print("naive", nfind("AISDI", ""))
print("KMP", kmpfind("AISDI", ""))

# empty string and text
print("\nEmpty string and text:")
print("naive", nfind("", ""))
print("KMP", kmpfind("", ""))

# string = text
print("\nString = text:")
print("naive", nfind(txt_content, txt_content))
print("KMP", kmpfind(txt_content, txt_content))

# string > text
print("\nString > text:")
print("naive", nfind(txt_content1, txt_content))
print("KMP", kmpfind(txt_content1, txt_content))

# string not in text
print("\nString not in text:")
print("naive", nfind("AISDI", txt_content))
print("KMP", kmpfind("AISDI", txt_content))

# predefined string-text pairs
pairs = [("AABA", "AABAACAADAABAABA"), ("AAAAA", "AAAAAAAAAAAAAAAAAA"),
         ("AAAAB", "AAAAAAAAAAAAAAAAAB"), ("FAA", "AABCCAADDEE")]

print("\nPredefined string-text pairs:")
for pair in pairs:
    print(pair[0], pair[1], nfind(pair[0], pair[1]))

# randomly generated words and patterns:
letters = ["a", "b"]
print("\nRandomly generated words and patterns:")
for example in range(4):
    text = [letters[n] for n in random.randint(low=0, high=2, size=11)]
    word = [letters[n] for n in random.randint(low=0, high=2, size=4)]
    text_string = "".join(text)
    word_string = "".join(word)
    print("naive", word_string, text_string, nfind(word, text))
    print("KMP", word_string, text_string, kmpfind(word, text))
    print("\n")
