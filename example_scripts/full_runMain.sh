#!/bin/sh

python3 main.py \
    --input-dir "sandbox/flattenSyncTest/A" \
    --output-dir "sandbox/flattenSyncTest/B" \
    --log-dir "sandbox/flattenSyncTest/logs"\
    --valid-extensions "sandbox/flattenSyncTest/info/extensionsToUse" \
    --copy-history "sandbox/flattenSyncTest/info/historyFile" \
    --temp-file "sandbox/flattenSyncTest/info/tmpCopyFile" 
