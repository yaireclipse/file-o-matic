# -*- coding: utf-8 -*-
#!/usr/bin/python

# import glob, os, re, shutil
# from subprocess import call

#
# what's actually done here is:
# 1. delete silence from the beginning until the first sound (greater than -52 d)
# 2. cut the following 1.8 seconds
# 3. reverse the cut part
# 4. delete silence from the beginning of the reversed cut part
# 5. reverse the cut part back
# 6. save the cut part to a new file
# 7. restart the process on the remainder of the original file

# "/Users/yairshefi/temp/cut/sox-14.4.1/sox a-p.wav word.wav silence 1 0.1 -52d trim 0 1.8 reverse silence 1 0.1 -52d reverse : newfile : restart"

import glob, os, re, shutil
from subprocess import call
from nameAudioFilesByCsv_en import renameAudioFiles
from convertWavToMp3 import convert

pathToSox = '/Users/yairshefi/temp/cut/sox-14.4.1/sox'
inputDir = '/Users/yairshefi/git/SLPlay/mobile/corona/original/audio/words/en/17apr15/'
# inputDir = '/Users/yairshefi/temp/'
inpuFileName = 'Jenna2'
audioExtension = '.wav'
inputAudioPath = inputDir + inpuFileName + audioExtension
slicedDuration = '1.5'
silenceDecibels = '-82d'

(inputName, ext) = re.split('\.', inputAudioPath)
outputDirBaseName = inputName + '_sliced' + silenceDecibels
wavOutputDir = outputDirBaseName + '_wav'
audioOutputPrefix = 'word'
wavOutputFileNameTemplate = wavOutputDir + '/' + audioOutputPrefix + audioExtension

if not os.path.exists(wavOutputDir):
	os.makedirs( wavOutputDir )

call( [ pathToSox, inputAudioPath, wavOutputFileNameTemplate, 'silence', '1', '0.1', silenceDecibels, 'trim', '0', slicedDuration, 'reverse', 'silence', '1', '0.1', silenceDecibels, 'reverse', ':', 'newfile', ':', 'restart' ] )

inputCsvPath = inputDir + inpuFileName + '.csv'
startLine = 0
renameAudioFiles( inputCsvPath, wavOutputDir, audioOutputPrefix, startLine )

mp3OutputPath = outputDirBaseName + '_mp3'
convert( wavOutputDir, mp3OutputPath )