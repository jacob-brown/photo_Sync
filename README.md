# Photo & Video Sync
Program used to sync a `source` dir with `destination` dir, when files are removed from `destination` the `source` does not re-add them. 


**Problem being solved**: if files are moved from a `destination` dir (i.e. it is being organised) but are still present in a `source` dir another copy will replace it. This is an issue if files have been organised. 
**Solution**: copy files into the `destination` dir and log them in a "already copied" list

Currently (my) usage is for organising photos and videos:
1. SynThing on phone dumps all photos to a nested `SynThing` dir on computer
2. This program syncs `SynThing` dir with a `To_Organise`
3. Periodically I sort photos, removing them from `To_Organise` and categorising them where they need to go


*Currently only for *nix systems - sorry*

## Dependencies
* `Python 3`

Python modules

* `logging==0.4.9.6`
* `numpy==1.20.0`
* `argparse==1.4.0`

## To Do
* add different extensions depending on file types
* Add an auto log deleter - eg. delete logs older than 30 days
* Windows version
* Continuously run script (i.e. not having to add to task manager)
## General Notes
* when a file fails to run, it is left for the next run to try again

# Tutorial
* Create dummy environment
* Copy files from Folder A (nested) to folder B (flat).
* If the photos in folder B are removed, they will not be copied again. 

## Create a dummy environment
```
mkdir -p sandbox/A/subdir1
mkdir -p sandbox/B
cd sandbox/A
touch file1.jpg file2.jpg file3.jpg subdir1/file4.jpg subdir1/file5.jpg
cd ../../ 
```

## Partial Control - recommended 
Default naming criteria has been used for the miscellaneous files (`--valid-extensions` and `--copy-history`).
**Establish the environment**
```
python3 newEnv.py \
        --log-dir "sandbox/logs"\
        --info-dir "sandbox/info"
```

**Run the program**
Only the location of the `--info-dir` is required, the program will use the default names.

```
python3 main.py \
    --input-dir "sandbox/A" \
    --output-dir "sandbox/B" \
    --log-dir "sandbox/logs"\
    --info-dir "sandbox/info"
```
## Full Control
i.e. no default naming criteria
If the names of `--valid-extensions` and `--copy-history`  were specified in the set-up, they also need ot be specified here

**Establish the environment**
```
python3 newEnv.py \
        --log-dir "sandbox/logs" \
        --info-dir "sandbox/info" \
        --copy-history "historyFile" \
        --valid-extensions "extensionsToUse"
```

**Run the program**

```
python3 main.py \
    --input-dir "sandbox/A" \
    --output-dir "sandbox/B" \
    --log-dir "sandbox/logs"\
    --valid-extensions "sandbox/info/extensionsToUse" \
    --copy-history "sandbox/info/historyFile" \
    --temp-file "sandbox/info/tmpCopyFile" 
```