import os


def findContent(rawMediaDir, extensions, fileToWrite):

    writer = open(fileToWrite, "w")

    for root, dirs, files in os.walk(rawMediaDir):

        dirs[:] = [d for d in dirs if not d[0] == "."]  # removes hidden dirs

        for f in files:
            if f.endswith(extensions):
                fullPath = os.path.join(root, f)
                writer.write(fullPath + "\n")
                print(fullPath)

    writer.close()


pathMedia = "sandbox/flattenSyncTest/A/"
# "sandbox/raw_photos"
acceptedExtensions = (".mp4", ".jpeg", ".jpg", "png", "mp4", "wmv", "mov")

findContent(pathMedia, acceptedExtensions, "info/filesCopy")
