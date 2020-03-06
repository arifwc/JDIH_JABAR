import os
import re


basepath = "csv/"
filtered = re.compile(r'\b(ELEKTRONIK|TEKNOLOGI|KOMUNIKASI|KOMPUTER|APLIKASI|KOMPUTER|DIGITAL|DATA|INFORMASI|SISTEM INFORMASI|INTEGRASI|JARINGAN|KEAMANAN SISTEM|KEAMANAN INFORMASI|WEBSITE|INTERNET|E-GOVERNMENT|SOFTWARE|ONLINE|INFORMATIKA)\b')
for file in os.listdir(basepath):
    count_peraturan=0
    with open(os.path.join(basepath,file),encoding="utf8") as f:
        datas = f.read().split('\n')
    for data in datas:
        if filtered.search(data):
            # print(filtered.findall(data))
            count_peraturan += 1

    print(file+" "+str(count_peraturan)) 