import subprocess
import os
import shutil
import numpy as np
import re
from searchMedia import openFileToInto


def subprocessToList(command, returnError=False):
    p = subprocess.Popen(
        [command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    out, er = p.communicate()
    out_string = out.decode()
    files = out_string.replace("\t", ":").split("\n")
    if "" in files:
        files.remove("")

    if returnError:
        return files, er
    else:
        return files


def isFileEmpty(file):
    header = subprocessToList("head -5 " + file)
    return not bool(header)


def copyFilesInList(listIn, copyLocation):
    for element in listIn:
        destFileName = createNameRecursively(element, copyLocation)
        shutil.copy2(element, destFileName)


def doesFileExist(sourceFile, destination):
    baseName = os.path.basename(sourceFile)
    fullPath = os.path.join(destination, baseName)
    return os.path.exists(fullPath)


def checkForUnderScoreDigitExtension(stringIn):
    name, ext = os.path.splitext(stringIn)
    prevExt = name[-2:]  # get last 2 digits
    p = re.compile(r"_\d")  # match underscore and digit
    if bool(p.match(prevExt)):
        stripUnderscore = name.rsplit("_", 1)[0]  # split from right
        return stripUnderscore + ext
    else:
        return stringIn


def createNameRecursively(sourceFile, copyLocation, counter=1):
    baseName = os.path.basename(sourceFile)
    name, ext = os.path.splitext(baseName)
    noUnderScore = checkForUnderScoreDigitExtension(name)

    if not doesFileExist(sourceFile, copyLocation):
        return os.path.join(copyLocation, baseName)
    else:
        newName = noUnderScore + "_" + str(counter) + ext
        return createNameRecursively(newName, copyLocation, counter + 1)


def appendListToFile(file, listWrite):
    with open(file, "a") as appender:
        for newEntry in listWrite:
            appender.write("\n" + newEntry)


def fileDifference(file1, file2):
    file1Content = openFileToInto(file1, np.array)
    file2Content = openFileToInto(file2, np.array)

    diffResults = np.setdiff1d(file2Content, file1Content)

    if "" in diffResults:
        diffResults.remove("")

    return diffResults


def returnSuccessAndFailedCopies(destinationDir, sourceList):
    boolResults = []
    sourceList = np.array(sourceList)
    for i in sourceList:
        fullPath = os.path.join(destinationDir, os.path.basename(i))
        outcome = os.path.exists(fullPath)
        boolResults.append(outcome)

    successes = sourceList[boolResults]
    failures = sourceList[np.logical_not(boolResults)]

    return successes, failures
