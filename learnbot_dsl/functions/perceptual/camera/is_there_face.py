from __future__ import print_function, absolute_import
import sys, os

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
import visual_auxiliary as va

def is_there_face(lbot):
    frame = lbot.getImage()
    mat = va.detect_face(frame)
    for row in mat:
        for cell in row:
            if cell == 1:
                return True
    return False