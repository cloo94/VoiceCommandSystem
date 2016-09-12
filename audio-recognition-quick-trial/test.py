#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python test.py test.mp3
'''

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer

if __name__ == '__main__':
    config = {
        'host':'eu-west-1.api.acrcloud.com',
        'access_key':'ab296940c747bdb8cecd75a471271d68',
        'access_secret':'pFIwbmXEDfx2Tljds91xiHFRPc8789Qvbiej2Igv',
        'debug':False,
        'timeout':10 # seconds
    }
    
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)
    print "recognizing by file ..."
    inputFile = sys.argv[1]
    #recognize by file path, and skip X seconds from from the beginning of inputFile.
    X = 0
    print re.recognize_by_file( inputFile, X)

    '''
    # Another way that recognize by buffer
    # inputFile must be in format: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
    inputFile = sys.argv[1]
    buf = open( inputFile, 'rb').read()
    print "recognizing by buffer ..."
    #recognize by file_audio_buffer that read from file path, and skip X seconds from from the beginning of sys.argv[1].
    X = 0
    print re.recognize_by_filebuffer(buf, X)
    '''

