import subprocess
import os
import shutil
from searchMedia import openFileToTuple


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
    file1Tuple = openFileToTuple(file1)
    file2Tuple = openFileToTuple(file2)

    diffResults = list(set(file1Tuple) ^ set(file2Tuple))

    if "" in diffResults:
        diffResults.remove("")

    return diffResults


# def copyController(copyList, excludeList, dirOut):
#
#    newMoves = fileDifference(excludeList, copyList)
#
#    if len(newMoves) != 0:
#        print("Moving files\n")
#        copyFilesInList(newMoves, dirOut)
#        print("Updating excludes list\n")
#        appendListToFile(excludeList, newMoves)
#        print("Finished\n")
#    else:
#        print("Up to date, no moves.")
#