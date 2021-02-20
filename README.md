# Photo & Video Sync

SynThing used to sync phone photos with computer.

**Problem**: if photos are moved from the a sync dir (i.e. it is being organised), another will replace it 
**Solution**: copy photos into a new dir, and have an "already copied list"

## To Do
* add different extensions depending on file types
## General Notes
* when a file fails to run, it is left for the next run to try again

# Examples
## Partial Control - recommended 
Default naming criteria has been used for the miscellaneous files (`--valid-extensions` and `--copy-history`).
**Establish the environment**
```
python3 newEnv.py \
        --log-dir "sandbox/flattenSyncTest/logs"\
        --info-dir "sandbox/flattenSyncTest/info"
```

**Run the program**
Only the location of the `--info-dir` is required, the program will use the default names.

```
python3 main.py \
    --input-dir "sandbox/flattenSyncTest/A" \
    --output-dir "sandbox/flattenSyncTest/B" \
    --log-dir "sandbox/flattenSyncTest/logs"\
    --info-dir "sandbox/flattenSyncTest/info"
```
## Full Control
i.e. no default naming criteria
If the names of `--valid-extensions` and `--copy-history`  were specified in the set-up, they also need ot be specified here

**Establish the environment**
```
python3 newEnv.py \
        --log-dir "sandbox/flattenSyncTest/logs" \
        --info-dir "sandbox/flattenSyncTest/info" \
        --copy-history "historyFile" \
        --valid-extensions "extensionsToUse"
```

**Run the program**

```
python3 main.py \
    --input-dir "sandbox/flattenSyncTest/A" \
    --output-dir "sandbox/flattenSyncTest/B" \
    --log-dir "sandbox/flattenSyncTest/logs"\
    --valid-extensions "sandbox/flattenSyncTest/info/extensionsToUse" \
    --copy-history "sandbox/flattenSyncTest/info/historyFile" \
    --temp-file "sandbox/flattenSyncTest/info/tmpCopyFile" 
```