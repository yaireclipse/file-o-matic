# -*- coding: utf-8 -*-
#!/usr/bin/python

import glob, os, re, shutil
from subprocess import call

output_dir = os.path.abspath("")

os.chdir('/Users/yairshefi/git/SLPlay/mobile/corona/Talkie/Audio/Words')
# os.chdir('/Users/yairshefi/temp/cut')
trimmedCount = 0
for file_name in glob.glob("*.wav"):
	(name, ext) = re.split('\.', file_name)
	outFileName = name + '_trimmed.' + ext
	call(['/Users/yairshefi/temp/cut/sox-14.4.1/sox', file_name, outFileName, 'reverse', 'silence', '1', '0.1', '-52d', 'reverse'])
	os.remove(file_name)
	os.rename(outFileName, file_name)
	print file_name + ' was trimmed.'
	trimmedCount += 1

print 'total trimmed: ' + str(trimmedCount)