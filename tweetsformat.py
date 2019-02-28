#imports the csv module to allow us to read the input file as a csv
import csv
#imports the re module to allow us to use regular expressions, helpful for removing urls
import re

#open the formatted tweets file to allow us to write to it, using the latin-1 encoding
trump_tweets_formatted = open('trumptweetsformatted.txt', 'w', encoding='latin-1')

#open the input file using the latin-1 encoding
with open('trumptweets.csv', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='^')
    line_count = 0

    #look at each row in the input file, and if the row is not the header row, perform the following transformations
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            #We only want to look at tweets trump has tweeted, so if row 5 ('is_retweet') is true, he didn't tweet it and thus we don't want to look at it
            if row[5] != 'true':
                if '^' not in row[1]:
                    s = row[1]
                    #remove any urls from the string
                    s = re.sub(r'https?:\/\/.*[\r\n]*', '', s, flags=re.MULTILINE)
                    if len(s.strip()) > 0:
                        #replace all & characters with the word and
                        s = s.replace('&amp;', ' and ')
                        #replace all % with the word percent
                        s = s.replace('%', ' percent ')
                        #remove all commas and double quotes
                        s = s.replace(',', '')
                        s = s.replace('"', '')
                        s = s.replace('“', '')
                        s = s.replace('”', '')
                        #add spaces after ! and ?
                        s = s.replace('!', '! ')
                        s = s.replace('?', '? ')
                        #replace _ and / with spaces
                        s = s.replace('_', ' ')
                        s = s.replace('/', ' ')
                        #add a space before hashtags
                        s = s.replace('#', ' #')
                        #replace = with the word equals
                        s = s.replace('=', ' equals ')
                        #replace + with the word plus
                        s = s.replace('+', ' plus ')
                        print(s)
                        print(s, file=trump_tweets_formatted)
            line_count += 1
    print(f'Processed {line_count} lines.')

trump_tweets_formatted.close()
