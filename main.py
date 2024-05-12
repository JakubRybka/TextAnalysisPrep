f = open("Hamlet.txt",encoding="utf8")
k=0
content = f.read()# I read hamlet from gutenberg
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
stop_words = stopwords.words('english')
words = word_tokenize(content)#I word tokenize text
NewWords = [word for word in words if word not in stop_words and word not in punctuation]#I remove stopwords and punctuation from list of words
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in NewWords]#I stem words (get rid of inflection)
dictionaryOfWords = {}
for w in stemmed:
    if w in dictionaryOfWords.keys():
        dictionaryOfWords[w] += 1
    else:
        dictionaryOfWords[w] = 1#I make dictionary to pair words with numbers of occurrences
commonWords = [word for word in dictionaryOfWords.keys() if dictionaryOfWords[word]>=100]#I peak all words that occurred atleast 100 times
print(sorted(commonWords))