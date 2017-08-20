import os
from os.path import dirname as dname
import msgpack
from sys import argv, exit

DATA_DIR = dname(dname(dname(os.path.abspath(__file__)))) + '/data/'

def list_files(path):
	for (dirname, dirpath, filename) in os.walk(path):
		arr = [dirname + i for i in filename 
					if i.split('.')[-1] == 'jpg' 
					or i.split('.')[-1] == 'JPG'
				]
	return arr


def write_index(data):
	f = open(DATA_DIR + 'index.mp', 'wb')
	f.write(msgpack.packb(data))
	f.close()
	

def create_index(path):
	print '[Creating new index.]'
	files = list_files(path)
	write_index(files)
	print '[Total no. files added ==>', len(files)
	return files


def check(path):
	if os.path.isfile(DATA_DIR + 'index.mp'):
		f = open(DATA_DIR + 'index.mp', 'rb')
		data = f.read()
		f.close()
		data = msgpack.unpackb(data)
		files = list_files(path)
		new = [i for i in files if i not in data]
		print '[Total no. of new files ==> ]', len(new)
		if len(new) > 0:
			print '[Updating index]'
			data.extend(new)
			write_index(data)
			print '[Updated]'
		return data, new
	else:
		return create_index(path), []


if __name__ == '__main__':
	if len(argv) == 3:
		try:
			eval(argv[1] + '( "' + argv[2] + '")')
		except TypeError:
			raise ('No such function exists')
	else:
		raise Exception('No arguments passed! Exiting code :)')
		exit(0)