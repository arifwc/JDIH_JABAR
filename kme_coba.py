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

all_text = """
TIM ASISTENSI E-BUDGETING RENCANA KERJA SATUAN KERJA PERANGKAT DAERAH TINGKAT KOTA BANDUNG TAHUN ANGGARAN 2017
PERUBAHAN ATAS PERATURAN WALIKOTA BANDUNG NOMOR 548 TAHUN 2016 TENTANG TATA CARA PENERAPAN SANKSI ADMINISTRATIF DALAM PENYELENGGARAAN BANGUNAN GEDUNG
PERUBAHAN KEDUA ATAS PERATURAN WALIKOTA BANDUNG NOMOR 495 TAHUN 2015 TENTANG STANDAR OPERASIONAL PROSEDUR PELAYANAN PERIZINAN TERPADU
TIM AHLI BANGUNAN GEDUNG KOTA BANDUNG MASA BAKTI 2015-2016
PEMBENTUKAN FORUM KOMUNIKASI ANAK KOTA BANDUNG PERIODE TAHUN 2015 2017
MASTERPLAN SMART CITY KABUPATEN BATANG
PERUBAHAN KEDUA ATAS PERATURAN BUPATI BATANG NOMOR 62 TAHUN 2018 TENTANG PENJABARAN ANGGARAN PENDAPATAN DAN BELANJA DAERAH KABUPATEN BATANG TAHUN ANGGARAN 2019
JASA PELAYANAN PADA BADAN LAYANAN UMUM DAERAH RUMAH SAKIT UMUM DAERAH LIMPUNG
PERATURAN WALIKOTA NOMOR 18 TAHUN 2018 TENTANG PEDOMAN PERHITUNGAN PENETAPAN DAN PEMBAYARAN TARIF AIR MINUM PADA PERUSAHAAN DAERAH AIR MINUM
PERATURAN WALIKOTA NOMOR 30 TAHUN 2018 TENTANG PENGEMBANGAN SENTRA USAHA MIKRO DAN KECIL
PERATURAN DAERAH NOMOR 30 TAHUN 2018 TENTANG PENGELOLAAN TANGGUNG JAWAB SOSIAL DAN LINGKUNGAN PERUSAHAAN
BATAS AKHIR PENERBITAN SURAT PERINTAH PENCAIRAN DANA (SP2D) KABUPATEN BATANG
HAK KEUANGAN ADMINISTRATIF PIMPINAN DAN ANGGOTA DPRD
PERUBAHAN ATAS PERATURAN GUBERNUR KEPULAUAN BANGKA BELITUNG NOMOR 54 TAHUN 2008 TENTANG URAIAN TUGAS DINAS TENAGA KERJA DAN TRANSMIGRASI PROVINSI KEPULAUAN BANGKA BELITUNG
PERUBAHAN ATAS PERATURAN BUPATI TEGAL NOMOR 88 TAHUN 2017 TENTANG PEDOMAN PELAKSANAAN ANGGARAN PENDAPATAN DAN BELANJA DAERAH KABUPATEN TEGAL
PERDA NO. 4 TAHUN 2015 TENTANG PERUBAHAN APBD TAHUN ANGGARAN 2015
PENAMBAHAN PENYERTAAN MODAL PEMERINTAH KABUPATEN BELITUNG PADA PERUSAHAAN DAERAH AIR MINUM KABUPATEN BELITUNG PADA TAHUN ANGGARAN 2014
PENETAPAN LOKASI BANTUAN LANGSUNG MASYARAKAT (BLM) FASILITATOR DESA DAN BIAYA OPERASIONAL PROYEK (BOP) KECAMATAN/DESA PROYEK PEMBERDAYAAN DALAM MENGATASI DAMPAK KRISIS EKONOMI (PDM-DKE) KAB. LUWU UTARA T.A. 1999/2000
PENCABUTAN KEPUTUSAN BUPATI LUWU UTARA NOMOR 533 TAHUN 2001 TENTANG PEMBERHENTIAN DAN PENGANGKATAN PEJABAT SEMENTARA KEPALA DESA LINGKUP KECAMATAN BAEBUNTA KAB. LUWU UTARA
PERATURAN DAERAH NOMOR 29 TAHUN 2018 TENTANG PERLINDUNGAN LAHAN PERTANIAN PANGAN BERKELANJUTAN
""".split("\n")[1:-1]


stopword = ['PERUBAHAN', 'PERATURAN','DAERAH','TENTANG', 'NOMOR', 'TAHUN', 'KOTA', 'DAN', 'PADA', 'WALIKOTA', 'KABUPATEN', 'BUPATI', 'TIM', 'ATAS', 'UMUM', 'PERDA', 'GUBERNUR','KEPULAUAN', 'KAB' , 'NO', '2018', '2016', '2015']


def preprocessing(line):
    line = line.upper()
    line = re.sub(r"[{}]".format(string.punctuation), " ", line)
    for stop_word in stopword:
        line = line.replace(stop_word, '')
        line =  re.sub(r'\b[0-9(.,)+]*\b', '', line)
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






