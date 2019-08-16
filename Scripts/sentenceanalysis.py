#For visualizing special words
import numpy as np
import matplotlib.pyplot as plt

#open the file containing trumps tweet sentences
trump_tweets_sentences = open('../Dataset/trumptweetssentences.txt', 'r', encoding='latin-1')
sentences_analysis = open('../Dataset/sentencesanalysis.txt', 'w', encoding='latin-1')

num_of_sentences = 0
word_count = 0

#initialize an array of length 54, since the longest sentence has 54 words
length_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

#Create a dictionary of all hashtags and twitter handles, tied to their counts
specialWords = {};

#read through each sentence one at a time
for line in trump_tweets_sentences:
    newline = line.strip()
    words = newline.split()
    #if the sentence is not length 0, add 1 to the corresponding index
    if len(words) > 0:
        length_arr[len(words) - 1] += 1

    #Now loop through each sentence looking for hashtags and handles
    for word in words:
        if (word[0] == '#' or word[0] == '@'):
            if word in specialWords:
                specialWords[word] = specialWords[word] + 1
            else:
                specialWords[word] = 1

i = 1
#generate the statistics from the constructed array
for length in length_arr:
    num_of_sentences += length
    word_count += length * i
    print(str(i) + ': ' + str(length))
    print(str(length), file=sentences_analysis)
    i += 1

print('Total number of sentences: ' + str(num_of_sentences))
print('Total number of sentences: ' + str(num_of_sentences), file=sentences_analysis)
print('Total number of words: ' + str(word_count))
print('Total number of words: ' + str(word_count), file=sentences_analysis)
print('Average sentence length: ' + str(word_count / num_of_sentences))
print('Average sentence length: ' + str(word_count / num_of_sentences), file=sentences_analysis)

#Visualize counts for special words
def sortFirst(val):
    return val[0]

def sortSecond(val):
    return val[1]

specialWordsSorted = list(specialWords.items())
specialWordsSorted.sort(key=sortSecond)
print(specialWordsSorted);

#find the counts of the counts

specialWordsCounts = {}

for pair in specialWordsSorted:
    if pair[1] in specialWordsCounts:
        specialWordsCounts[pair[1]] = specialWordsCounts[pair[1]] + 1
    else:
        specialWordsCounts[pair[1]] = 1

print(specialWordsCounts)

specialWordsCountsSorted = list(specialWordsCounts.items())
specialWordsCountsSorted.sort(key=sortSecond)

x = [];
y = [];
for pair in specialWordsCountsSorted:
    x.append(pair[1])
    y.append(pair[0])

plt.bar(x=range(0, len(x)),height=x, align='edge')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.show()

trump_tweets_sentences.close()
