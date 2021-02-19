import os
import logging


def writeFoundContent(rawMediaDir, extensions, fileToWrite):
    extensions = tuple(extensions)
    writer = open(fileToWrite, "w")
    for root, dirs, files in os.walk(rawMediaDir):
        dirs[:] = [d for d in dirs if not d[0] == "."]  # removes hidden dirs
        findContent(files, extensions, root, writer)
    writer.close()


def findContent(files, extensions, root, writer):
    for f in files:
        if f.endswith(extensions):
            fullPath = os.path.join(root, f)
            writer.write(fullPath + "\n")


def openFileToInto(file, type=list):
    tmp = []
    with open(file, "r") as reader:
        for row in reader.readlines():
            row = row.replace("\n", "")
            tmp.append(row)  # add row to list
    return type(tmp)


def searchController(supportedFileTypes, rawMediaDir, fileToWrite):
    acceptedExtensions = openFileToInto(supportedFileTypes, tuple)
    writeFoundContent(rawMediaDir, acceptedExtensions, fileToWrite)


def checkFilesWereFound(tmpFileWithFilesToMove):
    foundFiles = openFileToInto(tmpFileWithFilesToMove)

    if len(foundFiles) != 0:
        return True
    else:
        return False
