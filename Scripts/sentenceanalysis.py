#open the file containing trumps tweet sentences
trump_tweets_sentences = open('../Dataset/trumptweetssentences.txt', 'r', encoding='latin-1')
sentences_analysis = open('../Dataset/sentencesanalysis.txt', 'w', encoding='latin-1')

num_of_sentences = 0
word_count = 0

#initialize an array of length 54, since the longest sentence has 54 words
length_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

#read through each sentence one at a time
for line in trump_tweets_sentences:
    newline = line.strip()
    words = newline.split()
    #if the sentence is not length 0, add 1 to the corresponding index
    if len(words) > 0:
        length_arr[len(words) - 1] += 1

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

trump_tweets_sentences.close()
