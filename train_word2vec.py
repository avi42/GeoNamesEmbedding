# Just a bunch of imports
# The following packages are used:
# --> os
# --> glob
# --> random
# --> gensim
# --> nltk
# If you do not have a package use pip3 install (package name) in ur command line
# Before using pip3 make sure you set up ur python enviornment in here
from os import getcwd as cwd
from os import chdir as chdir
from os import path as path
from glob import glob as glob
from random import shuffle as shuffle
import gensim
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")

# Gets each line from each file in the res folder
lines = []
wd = cwd() + "/res"
chdir(wd)
for file in glob("*.txt"):
    reader = open(file)
    str = reader.read()
    thislines = str.split("\n")
    for idx, line in enumerate(thislines):
        lines.append(line)

# Switches current working directory to the models folder
wd = path.dirname(cwd())
chdir(wd + "/models")

# Sanitizes the data (tokenizes it into words, makes it lowercase, removes punctuation and stopwords, etc.)
processedlines = []
for line in lines:
    processedline = gensim.utils.simple_preprocess(line, True)
    filteredwords = [word for word in processedline if word not in stopwords.words('english')]
    processedlines.append(filteredwords)

# Randomizes the order of the lines in the data to ensure a better sample
shuffle(processedlines)

# Creates, trains, and saves the model
model = gensim.models.Word2Vec(processedlines, min_count=2, size=150)
model.train(processedlines, total_examples=len(processedlines), epochs=25)
model.save(cwd()+"/corpus7_150on25_1_1.model")

# Tests the model for the first time
words = ["texas", "aden", "canyon", "congo", "hanoi", "tangier", "izmir", "dunedin"]
numresults = 5
for word in words:
    print("\nTop 5 most similar words to " + word)
    print(model.wv.most_similar(positive=word, topn=numresults))

