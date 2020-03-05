import json
import requests
import re

urls=['https://web.pangandarankab.go.id/public/jdih/dokumen/list/1/peraturan-daerah?_=1583154735707',
      'https://web.pangandarankab.go.id/public/jdih/dokumen/list/4/keputusan-bupati?_=1583154402551',
      'https://web.pangandarankab.go.id/public/jdih/dokumen/list/3/peraturan-bupati?_=1583153982973']
peraturan=[]
for url in urls:
    r = requests.get(url)
    jsondata = json.loads(r.content)
    peraturan += jsondata['data'] 

data_file = open('csv/pangandarankab.csv', 'w') 
count=0 
for perda in peraturan:
    if count==0:
        data_file.write('peraturan\n')
        count+=1
    if perda[3]:
        data_file.write("{}\n".format(perda[3]))
    else:
        data_file.write("{}\n".format(re.findall(r"[^\s*].*[^\s*]",perda[4])))
data_file.close()        

    