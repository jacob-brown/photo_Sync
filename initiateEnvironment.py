import os
import brownfunk as bf


def makeFolder(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def makeFileWithContent(filename, path, content=[]):
    fullPath = os.path.join(path, filename)
    if not os.path.exists(fullPath):
        bf.saveTxt(fullPath, content)


def photoVideoExt():
    return ["jpeg", "jpg", "png", "mp4", "wmv", "mov"]