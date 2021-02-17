# Photo & Video Sync

SynThing used to sync phone photos with computer.

**Problem**: if photos are moved from the new sync dir (i.e. it is being organised), another will replace it 
**Solution**: copy photos into a new dir, and have an "already copied list"
**Notes**: 2 stages to allow for ease of searching, as SyncThing folder structure is hard to find photos

## To Do
* date of copy in excludeCopy
    * or another file - json?
* logs
* when switching to a new destination dir, if the same exclude file is present it will copy all the old files

* DIR1 = SyncThing folder
* DIR2 = _TO_ORGANISE_PHONE


1. Walk through DIR1 and gather photos
    1.1. list of accepted file types in ".gitignore" style file
    1.2. Make list of files to copy
2. Copy file to _TO_ORGANISE_PHONE
    2.1. Having checked if file was in an already copied list
        2.1.1. Name match and path match checks
3. Check if move was successful 
    4.1. TRUE: add file to already copied list
    4.2. FALSE: error/resync


Permanent files
* `info/excludeCopy`
* `info/includeExtensions` - update to include more file types

Temporary files
* `info/filesCopy`