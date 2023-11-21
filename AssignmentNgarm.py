'''
Name:Sanket CHandrabhan Shelke
Batch:B3
Roll no:52
Pract no 3: Generating the n gram model using nltk
'''

from nltk import ngrams

from nltk.util import ngrams
#unigram model
n = 1
sentence = 'My name is sanket chandrabhan shelke. Currently i am pursuing B.Tech degree in sanjivani college of engineering. '
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'My name is sanket chandrabhan shelke. Currently i am pursuing B.Tech degree in sanjivani college of engineering. '
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
#trigram model
n = 3
sentence = 'My name is sanket chandrabhan shelke. Currently i am pursuing B.Tech degree in sanjivani college of engineering. '
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)

#using text file input
from nltk import ngrams
#file = open("C:\Users\Sanket\OneDrive\Desktop\NLP-LAB\sanket.txt")
file = open("/home/exam/Desktop/NLP_LAB75/al.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()
        