from os import walk
from sys import getsizeof
import json

for (dirname, dirpath, filename) in walk('thumbnails/'):
	files = [{'name':i, 'link':'http://localhost:8000/static/thumbnails/' + i} for i in filename]

f = open('data/list.json', 'w')
f.write(json.dumps(files))
f.close()
