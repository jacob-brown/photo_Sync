import initiateEnvironment as ie
from parseArguments import parseSetUpArguments


def main(args):

    ie.makeFolder(args.logDir)
    ie.makeFolder(args.infoDir)
    extensionList = ie.photoVideoExt()
    ie.makeFileWithContent(args.copyHistory, args.infoDir)
    ie.makeFileWithContent(args.validExtensions, args.infoDir, extensionList)

    return 0


if __name__ == "__main__":
    main(parseSetUpArguments())
