import sys
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def read_file(file_name):
    with open(file_name, encoding="utf-16", errors="ignore") as text_file:
        content = text_file.read().replace('\n', '')
    return content

def write_file(word_count):
    fh = open("output.txt","w")
    fh.write("Number of unique words: " + str(len(word_count)) + "\n\n")
    for word in word_count:
        fh.write(str(word) + "\n")
    fh.close()

def process_text(text_input):

    #Make all words lowercase and use nltk
    text_input = str.lower(text_input)
    words = word_tokenize(text_input)
    
    #filter out common words and punctuation
    filtered_words = []
    stops = set(stopwords.words("russian"))
    for word in words:
        if (word not in stops) and (len(word) > 1):
            filtered_words.append(word)

    #create a dictionary with words as keys, and number of occurences as values
    word_count = {}
    for word in filtered_words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    #sorts dictionary by values (big to small)
    import operator
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

    #print dictionary
    print(sorted_word_count)
    print("Number of unique words: " + str(len(sorted_word_count)))
    write_file(sorted_word_count)


#start program
if(len(sys.argv) < 2):
    sys.exit("missing file name")

text_input = read_file(sys.argv[1])

process_text(text_input)