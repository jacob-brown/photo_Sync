import subprocess
import os
import shutil
from searchMedia import openFileToInto
import numpy as np


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
        shutil.copy2(element, copyLocation)


def appendListToFile(file, listWrite):
    with open(file, "a") as appender:
        for newEntry in listWrite:
            appender.write("\n" + newEntry)


def fileDifference(file1, file2):
    file1Tuple = openFileToInto(file1, tuple)
    file2Tuple = openFileToInto(file2, tuple)

    diffResults = list(set(file1Tuple) ^ set(file2Tuple))

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
