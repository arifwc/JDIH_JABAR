# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import re
import string
import random

random_state = 0 

jdih = open('all_jdihkabkota_jabar.txt')
read_jdih = jdih.read()
all_text = read_jdih.split("\n")[1:-1]
# filtered = re.compile(r'\b(ELEKTRONIK|TEKNOLOGI|KOMUNIKASI|KOMPUTER|APLIKASI|KOMPUTER|SISTEM|DATA|INFORMASI|SISTEM INFORMASI|INTEGRASI|JARINGAN|KEAMANAN SISTEM|KEAMANAN INFORMASI|WEBSITE|INTERNET)\b')
# filtered_text = []
# for text in all_text:
#     text=text.upper()
#     filtered_text.append(filtered.findall(text))
# print(filtered_text)

# stopword = ['PERUBAHAN', 'PERATURAN','DAERAH','TENTANG', 'NOMOR', 'TAHUN', 'KOTA', 'DAN', 'PADA', 'WALIKOTA', 'KABUPATEN', 'BUPATI', 'TIM', 'ATAS', 'UMUM', 'PERDA', 'GUBERNUR','KEPULAUAN', 'KAB' , 'NO', '2018', '2016', '2015']


def preprocessing(line):
    line = line.upper()
    filtered = re.compile(r'(ELEKTRONIK|TEKNOLOGI|KOMUNIKASI|KOMPUTER|APLIKASI|KOMPUTER|SISTEM|DATA|INFORMASI|SISTEM INFORMASI|INTEGRASI|JARINGAN|KEAMANAN SISTEM|KEAMANAN INFORMASI|WEBSITE|INTERNET)')
    line = str(filtered.findall(line))
    # line = line.upper()
    # line = re.sub(r"[{}]".format(string.punctuation), " ", line)
    # for stop_word in stopword:
	# line = line.replace(stop_word, '') 
    # line =  re.sub(r'\b[0-9(.,)+]*\b', '', line)
    print(line)
    return line




tfidf_vectorizer = TfidfVectorizer(preprocessor=preprocessing)
tfidf = tfidf_vectorizer.fit_transform(all_text)

distorsions = []
for k in range(2, 5):
	cls = MiniBatchKMeans(n_clusters=k, random_state=random_state)
	print(cls.fit(tfidf))
	print("Top terms per cluster:")
	order_centroids = cls.cluster_centers_.argsort()[:, ::-1]
	terms = tfidf_vectorizer.get_feature_names()
	for i in range(k):
    		print ("Cluster %d:" % i),
    		for ind in order_centroids[i, :10]:
        		print (' %s' % terms[ind]),
    		print
	print(cls.labels_)
	print(cls.inertia_)
	distorsions.append(cls.inertia_)

fig = plt.figure(figsize=(15, 5))
plt.plot(range(2, 5), distorsions)
plt.grid(True)
plt.title('Elbow curve')
plt.show()

# reduce the features to 2D
pca = PCA(n_components=2, random_state=random_state)
reduced_features = pca.fit_transform(tfidf.toarray())

# reduce the cluster centers to 2D
reduced_cluster_centers = pca.transform(cls.cluster_centers_)

plt.scatter(reduced_features[:,0], reduced_features[:,1], c=cls.predict(tfidf))
plt.show()

plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:,1], marker='x', s=150, c='b')

plt.show()






