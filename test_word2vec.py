from os import getcwd as cwd
from os import chdir as chdir
import gensim

print("\n")
wd = cwd() + "/models"
chdir(wd)

models = ["corpus7_100on40_1_1", "corpus7_150on25_1_1"]
words_list = ["oasis", "australia", "thessaloniki", "washington", "masoala", "duisburg"]
words = ["gaza"]
numresults = 5
for modelname in models:
    model = gensim.models.Word2Vec.load(cwd()+"/"+modelname+".model")
    print("Results from model: " + modelname)
    for word in words:
        print("\nTop 5 most similar words to " + word)
        print(model.most_similar(positive=word, topn=numresults))
    print("\n")

# print(model.most_similar(positive=["california", "arizona"], negative=["congo"], topn=10))

