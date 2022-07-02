import ImageProcessing
import serialCommunication
import os
import sys

path = sys.argv[1]

ImageProcessing.process_image(path)
serialCommunication.printImage()