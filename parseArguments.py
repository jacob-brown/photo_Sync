import argparse
import os


def parseSetUpArguments():
    parser = argparse.ArgumentParser(description="Description of program")

    parser.add_argument(
        "-l",
        "--log-dir",
        dest="logDir",
        type=str,
        required=True,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-f",
        "--info-dir",
        dest="infoDir",
        type=str,
        required=True,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-c",
        "--copy-history",
        dest="copyHistory",
        type=str,
        default="copyHistory",
        required=False,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-v",
        "--valid-extensions",
        dest="validExtensions",
        type=str,
        default="validExtensions",
        required=False,
        help="",
        metavar="",
    )

    args = parser.parse_args()
    return args


def parseRunArguments():
    parser = argparse.ArgumentParser(description="Description of program")

    parser.add_argument(
        "-i",
        "--input-dir",
        dest="inDir",
        type=str,
        required=True,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-o",
        "--output-dir",
        dest="outDir",
        type=str,
        required=True,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-l",
        "--log-dir",
        dest="logDir",
        type=str,
        required=False,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-f",
        "--info-dir",
        dest="infoDir",
        type=str,
        required=False,
        help="point to where are the misc. info files stored. Only works if defaults naming convention was used",
        metavar="",
    )

    parser.add_argument(
        "-v",
        "--valid-extensions",
        dest="validExtensions",
        type=str,
        default="validExtensions",
        required=False,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-c",
        "--copy-history",
        dest="copyHistory",
        type=str,
        default="copyHistory",
        required=False,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-t",
        "--temp-file",
        dest="tempFile",
        type=str,
        default="tempFile",
        required=False,
        help="",
        metavar="",
    )

    args = parser.parse_args()
    addInfoPathToMiscArgsIfGiven(args)

    return args


def addInfoPathToMiscArgsIfGiven(args):
    if args.infoDir:
        args.tempFile = os.path.join(args.infoDir, args.tempFile)
        args.copyHistory = os.path.join(args.infoDir, args.copyHistory)
        args.validExtensions = os.path.join(args.infoDir, args.validExtensions)
