#!/usr/bin/env python
# this is sample script for play music using tools (aplay for wave file, mp321 for mp3)
# It retrieves files from music and play in turns.

import subprocess
import time
from glob import glob

waves=glob("music/*.wav")
mp3s=glob("music/*.mp3")

wavecount = len(waves)
mp3count = len(mp3s) 

curwave=0
curmp3=0

while True:
    if (mp3count > 0 and curmp3 < mp3count):
        p = subprocess.Popen(["mpg321", mp3s[curmp3]], stdout=subprocess.PIPE)
        curmp3 = curmp3 + 1
        print p.communicate()
    elif (wavecount > 0 and curwav < wavecount):
        p = subprocess.Popen(["aplay", waves[curwav]], stdout=subprocess.PIPE)
        curwav = curwav + 1
        print p.communicate()
    else:
        curmp3 = 0
        wavecount = 0
