import json
import requests
import csv

r = requests.post('http://jdih.cirebonkota.go.id/produk/browse')
jsonload = json.loads(r.content)
# now we will open a file for writing 
data_file = open('csv/cirebonkota.csv', 'w') 
count=0 
for row in range(len(jsonload)):
    if count==0:
        data_file.write('peraturan\n')
        count+=1
    data_file.write("{}\n".format(jsonload[row]['tentang']))
data_file.close()        