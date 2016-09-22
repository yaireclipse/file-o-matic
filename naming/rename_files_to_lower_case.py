# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys, re

imagesPath = '/Users/Nissi_000/Git/slplay/mobile/corona/texture_packer/exercise_screen/buttons/original/en'
if len(sys.argv) > 1 and (sys.argv[1] != None or sys.argv[1].strip() != ''):
	imagesPath = sys.argv[1]

deleteNotFound = False
if len(sys.argv) > 3 and (sys.argv[3] != None or sys.argv[3].strip() != ''):
	dictCsvPath = sys.argv[3]

destLang = 'en'
if len(sys.argv) > 2 and (sys.argv[2] != None or sys.argv[2].strip() != ''):
	dictCsvPath = sys.argv[2]

# dictCsvFile = open(dictCsvPath, 'r')

wordNum = 0
for line in dictCsvFile:
	wordNum += 1
	wordFileName = 'word' + str(wordNum) + '.wav'
	newName = line.lower + '.wav'
	os.rename(imagesPath + '/' + wordFileName, imagesPath + '/result/' + newName)
	print (wordFileName + ' renamed to ' + newName)