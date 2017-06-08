#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,os,json

MODELS = {}
FILE = ''

def ParseGeometry(file):
	print('\n=== Geometry ===')

	MODELS['vertices'] = []
	MODELS['indices'] = []
	MODELS['normals'] = []
	MODELS['normals_idx'] = []

	vertices = MODELS['vertices']
	indices = MODELS['indices']
	normals = MODELS['normals']
	normals_idx = MODELS['normals_idx']
	
	nLine = 0

	for line in open(file, 'r').readlines():
		nLine = nLine + 1
		try:
			if line.startswith('v '):
				for v in line[1:len(line)].split():
					MODELS['vertices'].append(float(v))

			elif line.startswith('vn '):
				for vn in line[3:len(line)].split():
					MODELS['normals'].append(float(vn))

			elif line.startswith('f '):
				f = line[1:len(line)].split()
				pl = len(f)
				if (pl == 3):
					fa = int(f[0][0:f[0].find('/')])
					fb = int(f[1][0:f[1].find('/')])
					fc = int(f[2][0:f[2].find('/')])
					MODELS['indices'].append(fa)
					MODELS['indices'].append(fb)
					MODELS['indices'].append(fc)
					na = int(f[0][f[0].rfind('/')+1:len(f[0])])
					nb = int(f[1][f[1].rfind('/')+1:len(f[1])])
					nc = int(f[2][f[2].rfind('/')+1:len(f[2])])
					MODELS['normals_idx'].append(na)
					MODELS['normals_idx'].append(nb)
					MODELS['normals_idx'].append(nc)
				else:
					print('faces need to be triangular')
					raise
		except:
			print ('Error while processing line %s' %str(nLine))
			print(line)
			raise

def CreateJsonModelFile():
	with open('cube.json', 'w') as f:
		f.write(json.dumps(MODELS))


if __name__ == '__main__':
	if(len(sys.argv) == 1):
		print ('Error -- Use like this: objparser.py objfile.obj')
		sys.exit(0)
	FILE = sys.argv[1]
	ParseGeometry(FILE)
	dir = os.path.dirname(os.path.realpath(FILE))
	os.chdir(dir)
	CreateJsonModelFile()
