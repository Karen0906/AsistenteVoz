import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import re
from gensim.models import Word2Vec
import spacy
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd

with open('DBN.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

classes = [i for i, j in data]

l = [j for i, j in data]

l = [re.sub('[\\n]','',value[0]) for value in l]

nlp = spacy.load('es_core_news_sm')

tokensl = []
for corpus in l:
  doc = nlp(corpus)
  tokensl.append([t.lemma_.lower().split(' ')[0] for t in doc if t.orth_.isalpha() and not t.is_punct | t.is_stop])

path = '/'.join(os.path.dirname(__file__).split('\\')[:-1])

model = Word2Vec.load(path+'/modelo/complete.model')

def avg_word2vec(doc):
  #remove out-of-vocabulary words
  return np.mean([model.wv[word] for word in doc if word in model.wv.index2word], axis = 0)

avgwv = []
for tokens in tokensl:
  avgwv.append(avg_word2vec(tokens))
avgwv = np.array(avgwv)
scaler = MinMaxScaler().fit(avgwv)
avgwvt = scaler.transform(avgwv)

pca = PCA(n_components=2).fit(avgwvt)
reduced = pca.transform(avgwvt)

df = pd.DataFrame(data = np.concatenate([reduced,np.array(classes,dtype=int).reshape(-1,1)],axis=1),columns=['c1','c2','target'])

df.plot.scatter(x = 'c1',y ='c2',c = 'target')
plt.show()