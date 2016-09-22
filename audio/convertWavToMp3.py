# -*- coding: utf-8 -*-
#!/usr/bin/python

# Example of command to run in order to convert wav file to mp3 with great quality.
# Actually, 9 is the worst quality lame provides (0 is the best) but after hearing
# both outputs, the difference is un-noticed and isn't worth the few more bytes...
# The -V option referes to VBR - Variable Bit Rate.

# "lame -V 9 author.wav author.mp3"

import glob, os, re, shutil
from subprocess import call

def convert( inputDir, outputDir ):

	waveExtension = '.wav'
	mp3Extension = '.mp3'

	if not os.path.exists( outputDir ):
		os.makedirs( outputDir )

	convertedCount = 0
	for file_name in glob.glob( inputDir + '/*' + waveExtension ):
		fileNameWitoutPath = os.path.basename( file_name )
		(name, ext) = re.split('\.', fileNameWitoutPath)
		outFileName = outputDir + '/' + name + mp3Extension
		call( [ 'lame', '-V', '9', file_name, outFileName ] )
		print file_name + ' was converted to ' + outFileName
		convertedCount += 1

	print 'total converted: ' + str(convertedCount)