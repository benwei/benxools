#!/usr/bin/env python
# this is sample script for play music using tools (aplay for wave file, mp321 for mp3)
# It retrieves files from music folder and play in turns.

import subprocess
import sys
import time
from glob import glob

SOURCE_MUSIC_DIR = "music"

def syntax():
    print "syntax: [music folder]\nplease put your music(wav, mp3) to %s" % SOURCE_MUSIC_DIR


def main():

    global SOURCE_MUSIC_DIR
    if len(sys.argv) > 1:
        SOURCE_MUSIC_DIR = sys.argv[1]

    waves=glob("%s/*.wav" % SOURCE_MUSIC_DIR)
    mp3s=glob("%s/*.mp3" % SOURCE_MUSIC_DIR)

    wavecount = len(waves)
    mp3count = len(mp3s) 


    if wavecount == 0 and mp3count == 0:
        syntax()
        sys.exit(1)

    curwave=0
    curmp3=0

    while True:
        if (mp3count > 0 and curmp3 < mp3count):
            p = subprocess.Popen(["mpg321", mp3s[curmp3]], stdout=subprocess.PIPE)
            curmp3 = curmp3 + 1
            print p.communicate()
        elif (wavecount > 0 and curwave < wavecount):
            p = subprocess.Popen(["aplay", waves[curwave]], stdout=subprocess.PIPE)
            curwave = curwave + 1
            print p.communicate()
        else:
            curmp3 = 0
            wavecount = 0

if __name__ == "__main__":
    main()
