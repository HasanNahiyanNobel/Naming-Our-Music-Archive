# Naming-Our-Music-Archive
This is a combination of two simple python scripts:

## 1. `RenameFiles.py`
1. Read lines from `input.txt` file. This input text is a direct copy-paste from a Wikipedia *track listing* table, like [this](https://en.wikipedia.org/wiki/Rubber_Soul#Track_listing). According to general Wikipedia convention, the second column of the table holds song name, so is our assumption of this input.
1. Given a path and an index *n*, all the files in that path are renamed from the *n*th row of the track listing table, having "n. " as its prefix, with a leading zero for *n*<10.

## 2. `EditMetadata.py`
1. Given a path, clears the existing metadata from all the mp3 files in that path. We did not test it for other formats.
1. Adds metadata from the following variables:
	- `title`
	- `album`
	- `artist`
	- `albumartist`
	- `genre`
	- `date`
	- `originaldate`
	- `tracknumber`