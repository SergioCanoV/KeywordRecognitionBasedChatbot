from lib2to3.pgen2 import token
from os import remove
from shutil import unregister_archive_format
import numpy as np
import nltk
from nltk.corpus import stopwords
import string
import random
import sklearn
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

f = open('lotr_chars.txt','r', errors = 'ignore')
raw_doc = f.read()
stopwords = stopwords.words('english')

sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    filtered_tokens = [lemmer.lemmatize(token) for token in tokens]
    # exclude stopwords from stemmed words
    return [t for t in filtered_tokens if t not in stopwords]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#define a greeting function
GREET_INPUTS = ("hello","hi","greetings","sup","what's up","hey")
GREET_RESPONSES = ["hi","hey","*nods*","hi there","hello","I am glad! You are talking to me"]
def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo1_response = ''
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize,
                              # stop_words='english'
                              )
    tfidf = TfidVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        robo1_response = robo1_response+"I am sorry! I don't understand you, try again"
        return robo1_response
    else:
        robo1_response = robo1_response+sent_tokens[idx]
        return robo1_response
