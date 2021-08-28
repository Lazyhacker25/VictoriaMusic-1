from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from Victoria.services.converter.converter import convert
