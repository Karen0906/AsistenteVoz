import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import re
from gensim.models import Word2Vec
import spacy
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans, SpectralClustering

with open('DB.csv', 'r', encoding='UTF-8', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

l = [re.sub('[\\n]','',value[0]) for value in data]

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

pca = PCA().fit(avgwvt)

plt.rcParams["figure.figsize"] = (12,6)

fig, ax = plt.subplots()
xi = np.arange(1, avgwvt.shape[0]+1, step=1)
y = np.cumsum(pca.explained_variance_ratio_)

plt.ylim(0.0,1.1)
plt.plot(xi, y, marker='o', linestyle='--', color='b')

plt.xlabel('Número de componentes')
plt.xticks(np.arange(1, avgwvt.shape[0]+1, step=1)) #change from 0-based array index to 1-based human-readable label
plt.ylabel('Varianza cumulativa (%)')
plt.title('El número de componentes necesarios para explicar la varianza.')

plt.axhline(y=0.95, color='r', linestyle='-')
plt.text(0.5, 0.85, '95% umbral de corte', color = 'red', fontsize=16)

plt.axvline(x=np.argwhere(y>0.95)[0]+1, color='g', linestyle='-')
plt.text((np.argwhere(y>0.95)[0]+2), 0.5, 'Cantidad óptima: '+str(np.argwhere(y>0.95)[0,0]+1), color = 'green', fontsize=16)

ax.grid(axis='x')
plt.savefig('VarianzaPCA.png')
plt.clf()

pca = PCA(n_components=0.95).fit(avgwvt)
reduced = pca.transform(avgwvt)


kmmodel = SpectralClustering()
visualizer = KElbowVisualizer(
    kmmodel, k=(2,20)
)

visualizer.fit(reduced)
visualizer.show(outpath="OptimalK.png")

kmmodel = SpectralClustering(visualizer.elbow_value_).fit(reduced)

with open('DBN.csv', 'w', newline='') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows([list(i) for i in zip(kmmodel.labels_.tolist(),l)])