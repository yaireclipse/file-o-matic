# -*- coding: utf-8 -*-
#!/usr/bin/python

import glob, os, re, shutil
import Image

output_dir = os.path.abspath("")

# def convertToPng():
os.chdir('/Users/yairshefi/Google Drive/SLPlay Shared/מוצר/חומרים מסודרים סוף סוף/Images/vector')
for file_name in glob.glob("*.eps"):
	from subprocess import call
	(name, ext) = re.split('\.', file_name)
	call(['convert', file_name, name + '.jpg'])
	print file_name

# convertToPng()

# exit()