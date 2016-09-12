#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer

if __name__ == '__main__':
        config = {
                #Replace "xxxxxxxx" below with your project's host, access_key and access_secret.
                'host':'eu-west-1.api.acrcloud.com',
                'access_key':'ab296940c747bdb8cecd75a471271d68',
                'access_secret':'pFIwbmXEDfx2Tljds91xiHFRPc8789Qvbiej2Igv',
                'timeout':10 # seconds
        }

        '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
        re = ACRCloudRecognizer(config)

        #recognize by file path, and skip 180 seconds from from the beginning of sys.argv[1].
        print re.recognize_by_file(sys.argv[1], 180)
        
        buf = open(sys.argv[1], 'rb').read()
        #recognize by file_audio_buffer that read from file path, and skip 180 seconds from from the beginning of sys.argv[1].
        print re.recognize_by_filebuffer(buf, 180)
