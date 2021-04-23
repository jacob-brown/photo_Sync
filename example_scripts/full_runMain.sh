#!/bin/sh

python3 main.py \
    --input-dir "sandbox/A" \
    --output-dir "sandbox/B" \
    --log-dir "sandbox/logs"\
    --valid-extensions "sandbox/info/extensionsToUse" \
    --copy-history "sandbox/info/historyFile" \
    --temp-file "sandbox/info/tmpCopyFile" 
