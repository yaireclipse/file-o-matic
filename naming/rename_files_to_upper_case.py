# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys, re

imagesPath = 'C:/Users/Nissi_000/Git/slplay/mobile/corona/texture_packer/exercise_screen/buttons/original/en/'
# if len(sys.argv) > 1 and (sys.argv[1] != None or sys.argv[1].strip() != ''):
# 	imagesPath = sys.argv[1]

print (' check! ')

for filename in os.listdir(imagesPath):
	print (imagesPath + filename)

	if not os.path.isfile(imagesPath + filename) :
		continue
	if not filename.endswith('jpg') and not filename.endswith('png'):
		continue
	(name, ext) = re.split('\.', filename)
	newName = name.lower() + '.' + ext
	if newName != filename :
		os.rename(imagesPath + '/' + filename, imagesPath + '/' + newName)
	print (filename + ' renamed to ' + newName)

print (imagesPath + filename)