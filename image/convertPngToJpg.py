# -*- coding: utf-8 -*-
#!/usr/bin/python

import glob, os, re, shutil
import Image

output_dir = os.path.abspath("")

# def convertToPng():
os.chdir('/Users/yairshefi/Google Drive/SLPlay Shared/מוצר/חומרים מסודרים סוף סוף/Images/sep-14')
for file_name in glob.glob("*.png"):
	png = Image.open(file_name).convert("RGBA")
	jpg = Image.new("RGB", png.size, (255, 255, 255))
	jpg.paste(png, mask=png.split()[3]) # 3 is the alpha channel

	(name, ext) = re.split('\.', file_name)
	out_file = os.path.join(output_dir, name + ".jpg")
	jpg.save(out_file, "JPEG")

	print file_name

# convertToPng()

# exit()

