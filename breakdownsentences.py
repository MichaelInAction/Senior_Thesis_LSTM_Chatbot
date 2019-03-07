#imports the re module to allow us to use regular expressions
import re

#open the formatted tweets file in to break each tweet down into sentences
trump_tweets_formatted = open('trumptweetsformatted.txt', 'r', encoding='latin-1')
#open the new file to store the sentences
trump_tweets_sentences = open('trumptweetssentences.txt', 'w', encoding='latin-1')

#read through each tweet one at a time
for line in trump_tweets_formatted:
    newline = "";
    newline += line;
    #remove period in signature
    newline = newline.replace('Donald J. Trump', 'Donald J Trump')
    #add in a newline after each . ? or !
    newline = newline.replace('. ', '.\n')
    newline = newline.replace('! ', '!\n')
    newline = newline.replace('? ', '?\n')
    newline = newline.replace('U.S.\n', 'U.S. ')
    #newline = newline.replace('\n#', ' #')
    #newline = newline.replace('\n #', ' #')
    print(newline, file=trump_tweets_sentences)

trump_tweets_formatted.close()
trump_tweets_sentences.close()
