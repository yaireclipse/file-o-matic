# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys

def renameAudioFiles( wordsCsvPath, audioDir, audioPrefix, startLine ):

	audioExtension = '.wav'

	wordsCsvFile = open(wordsCsvPath, 'r')

	# os.chdir( audioDir )
	wordIndex = 1
	currLine = -1
	for line in wordsCsvFile:
		currLine += 1
		if currLine < startLine:
			continue
		if line.strip() == '':
			continue
		line = line.split(',')
		newFileName = audioDir + '/' + line[0]
		newFileName = newFileName.strip()
		if newFileName == '':
			break
		newFileName = newFileName.replace( ' ', '_' )
		newFileName += audioExtension
		oldFileName = audioDir + '/' + audioPrefix + str( wordIndex ).zfill(3) + audioExtension
		os.rename( oldFileName, newFileName )
		print 'renamed file ' + oldFileName + ' to ' + newFileName
		wordIndex += 1

	print str( wordIndex - 1 ) + ' files were renamed.'