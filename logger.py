import logging
import os
from datetime import datetime

# makeLogFile
def nameLogFile(logsPath, debug=False):
    datetimeNow = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    baseName = datetimeNow + ".log"

    if not debug:
        return os.path.join(logsPath, baseName)
    else:
        return os.path.join(logsPath, "debug.log")


def initiateLogging():

    logFile = nameLogFile("sandbox/logs/", True)

    logging.basicConfig(
        filename=logFile,
        filemode="a",
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )


def makeCopiedFileString(listCopiedFiles):
    logStringCopiedFiles = "copied files:\n"
    for copiedFile in listCopiedFiles:
        logStringCopiedFiles = logStringCopiedFiles + copiedFile + "\n"
    return logStringCopiedFiles


# initiateLogging()
# logging.info("I am some info")
# logging.warning("I am some warning")
# logging.error("I am some error")
# logging.critical("I am some critical")
