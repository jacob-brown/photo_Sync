import os


def findContent(rawMediaDir, extensions, fileToWrite):

    writer = open(fileToWrite, "w")

    for root, dirs, files in os.walk(rawMediaDir):

        dirs[:] = [d for d in dirs if not d[0] == "."]  # removes hidden dirs

        for f in files:
            if f.endswith(extensions):
                fullPath = os.path.join(root, f)
                writer.write(fullPath + "\n")

    writer.close()


def openFileToTuple(file):
    tmp = []
    with open(file, "r") as reader:
        for row in reader.readlines():
            row = row.replace("\n", "")
            tmp.append(row)  # add row to list
    return tuple(tmp)
