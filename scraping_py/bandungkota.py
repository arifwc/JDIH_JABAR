import requests

r = requests.post('https://jdih.bandung.go.id/home/produk-hukum/daerah/datasource',
                  headers={"Host":"jdih.bandung.go.id",
                            "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0",
                            "Content-Type":"application/json",
                            "X-CSRF-TOKEN":"4R4VvCnEVzEVBrGNOCa5RX54mzf8w9Zj6iweQ64d",
                            "X-Requested-With":"XMLHttpRequest",
                            "Content-Length":"0",
                            "Origin":"https://jdih.bandung.go.id",
                            "Connection":"keep-alive",
                            "Referer":"https://jdih.bandung.go.id/home/produk-hukum/daerah",
                            "Cookie":"jdih_cookie=eyJpdiI6ImZLYzZDUTA2dUphRVdkQjNVSjZnRUE9PSIsInZhbHVlIjoid2lIYjZ5UGRcL29WM2xxU0JnNHZqcXcrQ284cThMenVcL0Q2aHYyKzJKd3ZHcjRnWDJUZFhcL0ljZFIrbk5BTU95XC9GbGJqRnFQNFoxZFJ2Z0g0UVhiaEl1VFp2QVU1aHJpZGtSOXZtSnNPRjZrMG40dFNuNVBnVWlEcytWdUtaSTl1IiwibWFjIjoiYWRiNjU0NWZkOTNmN2NhYTkxMjNmZmU4YWRmNDRjZTU2ZDg1OTA2OWExODM4MTM2YzFmYWM5Y2IwZTZkZmFhMyJ9; _ga=GA1.3.791521472.1582813254; _gid=GA1.3.1553587332.1582813254; XSRF-TOKEN=eyJpdiI6InJQTE1BcFg1K3BpTFUrcktKbnVVeUE9PSIsInZhbHVlIjoia3p1NjU5RDczSHUrbFBSU09cL09TS1wvbEw5cnhwVFU4VUsyd1VjbDN2dnRJM09QXC9WWTA0MlJqNzlaQmtiRUp5ciIsIm1hYyI6ImNkMmM3MDg4NTMxYTJjN2Q3NTMyNTVkN2RjMWIyMzI3N2JhYzkzYTBlNDJiMDVkZGZlODIyNjViZGI2NWFjMzQifQ%3D%3D; jdih_kota_bandung_session=eyJpdiI6IjRIdlpycGlsS1YyR3pHaFwvNDlIaUJ3PT0iLCJ2YWx1ZSI6IkpXOTBPXC8rZXZzQzVcL0tSOStWWDd4SUNSTG5nR3dmV3BjVHNVK0lHdGdPcEx5OFo5UHJ4RkxacG1jTXNVZXJJdSIsIm1hYyI6IjFiYmExNDc0Mjc0YzM4ZDNkZDJhNTNmY2E5MTEyYmZjMjA4OGM2MjYwYzE4YjNjNzE3ZWIzNTkzODFjYjczOTcifQ%3D%3D",
                            "Cache-Control":"max-age=0, no-cache",
                            "Upgrade-Insecure-Requests":"1",
                            "Pragma":"no-cache"})
data = r.json()
jsonload = data['data']
# now we will open a file for writing 
data_file = open('csv/bandungkota.csv', 'w') 
count=0 
for row in range(len(jsonload)):
    if count==0:
        data_file.write('peraturan\n')
        count+=1
    data_file.write("{}\n".format(jsonload[row]['dokumen_judul']))
data_file.close()   