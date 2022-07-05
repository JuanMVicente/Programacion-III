from urllib import request
import csv

request.urlretrieve("https:\\datos.cultura.gob.ar\dataset\37305de4-3cce-4d4b-9d9a-fec3ca61d09f\resource\4207def0-2ff7-41d5-9095-d42ae8207a5d\download\museo.csv","verga.csv")

'''url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv"

myfile = urllib.request.urlretrieve(url,'verga.csv')'''

'''with open(url) as f:
    reader = csv.reader(f)
    for row in reader:
        print'''

        
'''r = request.get(url)
f = open("verga.csv", "wb")
f.write(r.read())
f.close()'''