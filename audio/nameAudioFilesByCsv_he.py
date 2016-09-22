# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys

wordsCsvPath = '/Users/yairshefi/temp/cut_avishag_wav_files/avishag_little.csv'
if len(sys.argv) > 1 and (sys.argv[1] != None or sys.argv[1].strip() != ''):
	wordsCsvPath = sys.argv[1]

wordsCsvFile = open(wordsCsvPath, 'r')

startLine = 1
if len(sys.argv) > 2 and (sys.argv[2] != None or sys.argv[2].strip() != ''):
	startLine = sys.argv[2]

audioPath = '/Users/yairshefi/temp/cut_avishag_wav_files/AP_avishag_little_result_-52d_with_names/'
if len(sys.argv) > 3 and (sys.argv[3] != None or sys.argv[3].strip() != ''):
	audioPath = sys.argv[3]

os.chdir( audioPath )
wordIndex = 1
currLine = -1
for line in wordsCsvFile:
	currLine += 1
	if currLine < startLine:
		continue
	line = line.split(',')
	newFileName = line[1]
	if newFileName.strip() == '':
		break
	newFileName = newFileName.replace( '(', '_' ).replace( ')', '_' ).replace( 'S', '_s_' ).replace( 'X', '_x_' )
	newFileName += '.wav'
	oldFileName = 'word' + str( wordIndex ).zfill(3) + '.wav'
	os.rename( oldFileName, newFileName )
	print 'renamed file ' + oldFileName + ' to ' + newFileName
	wordIndex += 1

print str( wordIndex - 1 ) + ' files were renamed.'