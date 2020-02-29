import json
import re

with open('cianjurkab_perda.json') as json_file: 
    data = json.load(json_file) 

with open('cianjurkab_perbup.json') as json_fil: 
    data2 = json.load(json_fil) 
  
perdas = data['data'] 
perbups = data2['data']
peraturan = perdas+perbups

data_file = open('cianjurkab.csv', 'w') 
count=0 
for perda in peraturan:
    if count==0:
        data_file.write('peraturan\n')
        count+=1
    data_file.write("{}\n".format(re.findall(r'\w+.+?(?=<)',perda[2])[0]))
data_file.close()        

    