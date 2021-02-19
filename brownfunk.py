def saveTxt(dirfile, listToSave, sep="\n"):
    with open(dirfile, "w") as f:
        for num, val in enumerate(listToSave):
            if num == len(listToSave) - 1:
                f.write(val)
            else:
                f.write(val + sep)