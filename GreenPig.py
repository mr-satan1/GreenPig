import exifread
import os, os.path
from PIL import Image
from PIL.ExifTags import TAGS
import argparse
parser = argparse.ArgumentParser(
    description ='[!] GreenPig - Bulk Forensic EXIF Tag Extractor',
)
parser.add_argument('-d', required = True, help = "Directory containing photos for EXIF tag extraction")
args = parser.parse_args()

path = args.d
validExtensions = [".jpg", ".gif", ".png", ".jpeg"]
for photo in os.listdir(path):
    extension = os.path.splitext(photo)[1]
    if extension.lower() not in validExtensions:
        print("File extension on '{}' not valid photo".format(photo))
        continue
    print('='*60)
    print("    Valid photo file: '{}'. EXIF Dump => :".format(photo))
    print('='*60)
    img = Image.open(photo)
    try:
        exif = img._getexif()
    except AttributeError as error:
        print(error)
        continue
    except ExceptionError as error:
        print(error)
        continue
    for tag in exif:
        tagName = TAGS.get(tag,tag)
        value = exif[tag]
        print('[*] ' + str(tagName) + " =>  " + str(value))
    print('\n\n')
