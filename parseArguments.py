import argparse


def parseArguments():
    parser = argparse.ArgumentParser(description="Description of program")

    parser.add_argument(
        "-i",
        "--input-file",
        dest="inFile",
        type=str,
        required=True,
        help="bam IN_BAM to have snps sampled from",
        metavar="IN_BAM",
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
        "-s",
        "--supported-types-from",
        dest="supportedFileTypes",
        type=str,
        default="info/includeExtensions",
        required=False,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-e",
        "--exclude-from",
        dest="excludeFrom",
        type=str,
        default="info/excludeCopy",
        required=False,
        help="",
        metavar="",
    )

    parser.add_argument(
        "-t",
        "--temp-file",
        dest="tempFile",
        type=str,
        default="info/filesCopy",
        required=False,
        help="",
        metavar="",
    )

    # define args
    args = parser.parse_args()

    return args