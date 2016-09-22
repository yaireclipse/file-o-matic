# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys, re

imagesPath = '/Users/yairshefi/temp/aaa/result/'
if len(sys.argv) > 1 and (sys.argv[1] != None or sys.argv[1].strip() != ''):
	imagesPath = sys.argv[1]

deleteNotFound = False
if len(sys.argv) > 3 and (sys.argv[3] != None or sys.argv[3].strip() != ''):
	dictCsvPath = sys.argv[3]

destLang = 'en'
if len(sys.argv) > 2 and (sys.argv[2] != None or sys.argv[2].strip() != ''):
	dictCsvPath = sys.argv[2]

for filename in os.listdir(imagesPath):
	if not os.path.isfile(imagesPath + filename) :
		continue
	if not filename.endswith('.wav') :
		continue
	newName = filename.replace(' ', '_')
	if newName != filename :
		os.rename(imagesPath + '/' + filename, imagesPath + '/' + newName)
	print filename + ' renamed to ' + newName