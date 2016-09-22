#!/usr/bin/python

import glob, os, re, shutil
import Image

input_dir = os.path.abspath("../Talkie/Resources/Images")
output_dir = os.path.abspath("../Talkie/Resources/Images")

renew = False

def do_resize():

	os.chdir(input_dir)
	for file_name in glob.glob("*.png") + glob.glob("*.jpg"):
		(name, ext) = re.split('\.', file_name)

		in_file = os.path.join(input_dir, file_name)
		out_file = os.path.join(output_dir, name + ".jpg")

		im = Image.open(file_name).convert("RGBA")
		width = im.size[0]
		height = im.size[1]
		
		max_size = 0
		new_width = width
		new_height = height
		
		if name.startswith("bg_"):
		    max_size = 2048
		else:
		    max_size = 1024
		    
		if width > height:
		    if width > max_size:
			new_width = max_size
			new_height = height * new_width / width
		else:
		    if height > max_size:
			new_height = max_size
			new_width = width * new_height / height
		
		#print file_name
		
		#im.convert("RGB")
		
		if new_width != width or new_height != height:
		    im.thumbnail((new_width, new_height), Image.ANTIALIAS)
		    
		    ch = im.split()
		    
		    #if len(im) > 3:
	    	    bg = Image.new("RGB", im.size, (255, 255, 255))
		    bg.paste(im, mask=im.split()[3]) # 3 is the alpha channel
		    
		    bg.save(out_file, "JPEG", quality=80)
		    #else:
		#	im.save(out_file, "JPEG", quality=80)
			
		    print file_name + "(%d, %d) -> (%d, %d)" % (width, height, new_width, new_height)
		elif ext != "jpg":
		    #im.convert("RGB").save(out_file, "JPEG", quality=80)
		    
		    bg = Image.new("RGB", im.size, (255, 255, 255))
		    bg.paste(im, mask=im.split()[3]) # 3 is the alpha channel
		    
		    bg.save(out_file, "JPEG", quality=80)
		    
		    print file_name + " - (%d, %d)" % (width, height)

		if ext != "jpg":
		    os.remove(in_file)
		    print "Deleted " + file_name


	print "Done"

do_resize()

exit()

