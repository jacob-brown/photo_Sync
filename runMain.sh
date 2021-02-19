#!/bin/sh

# Full
#python3 main.py \
#    --input-dir "sandbox/flattenSyncTest/A" \
#    --output-dir "sandbox/flattenSyncTest/B" \
#    --log-dir "sandbox/flattenSyncTest/logs"\
#    --valid-extensions "sandbox/flattenSyncTest/info/extensionsToUse" \
#    --copy-history "sandbox/flattenSyncTest/info/historyFile" \
#    --temp-file "sandbox/flattenSyncTest/info/tmpCopyFile" 

# Partial
#python3 main.py \
#    --input-dir "sandbox/flattenSyncTest/A" \
#    --output-dir "sandbox/flattenSyncTest/B" \
#    --log-dir "sandbox/flattenSyncTest/logs"\
#    --info-dir "sandbox/flattenSyncTest/info"

# Partial
python3 main.py \
    --input-dir "sandbox/raw_photos" \
    --output-dir "sandbox/ALL_PHOTOS" \
    --log-dir "sandbox/logs"\
    --info-dir "sandbox/info"