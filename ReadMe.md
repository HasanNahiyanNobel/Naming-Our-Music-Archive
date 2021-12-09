# Naming Our Music Archive
This is a combination of four simple python scripts:


## 1. `starter.py`
The starting point of execution. This script:
1. Formats all the files using `yapf`, with the Google style.
2. Invokes `rename_files.py`.
3. And then, invokes `edit_metadata.py`.
4. Stores output in an output directory.


## 2. `rename_files.py`
1. Reads lines from an input file. This input text is a direct copy-paste from a Wikipedia *track listing* table, like [this](https://en.wikipedia.org/wiki/Rubber_Soul#Track_listing).
1. The variables `SPLIT_CHAR` and `COL_INDEX_IN_INPUT` are set according to the table, to retrieve the song names.
1. Given a path and an index *n*, all the files in that path are renamed from the *n*th row of the track listing table, having "n. " as its prefix, with a leading zero for *n*<10.


## 3. `edit_metadata.py`
1. Given a path, clears the existing metadata from all the `.mp3` files in that path. We did not test it for other formats.
1. Adds metadata of the following:
  - `title`
  - `album`
  - `artist`
  - `albumartist`
  - `genre`
  - `date`
  - `originaldate`
  - `tracknumber`


## 4. `utilities.py`
Stores shared constants, variables and functions used by the other scripts.
