# Script Join Videos

About
---
This a simple Python script to merge video files.

Instalation
---

As any Python code, you should do this inside a virtual environment. 
Though it doesn't require any external python lib, you need mkvtoolnix installed in your machine.

**Linux**
```  
$ (sudo) apt install mkvtoolnix
```

**Mac**
```
$ brew install mkvtoolnix
```

Usage
---

From the installed folder, run
```
$ python join_videos.py ~/path/to/videos

```

It will generate the output file in a folder called 'output' in the same folder where the input videos are.

Ps.:
---
* Currently works only with webm files.
* To a better result, you should rename your files to be merged in the order you want. I had better results with non-ambiguous ordering names. Depending on the OS, only by renaming files starting with ordered numbers, like 
```shell=
video0.webm
video1.webm
video2.webm
...
```
' won't work. In MacOS for instance I had to rename the files as '
```shell=
video001.webm
video002.webm
video003.webm
...
``` 
so it wouldn't order like 
```shell=
video1.webm
video10.webm
video11.webm
...
``` 
* It generates the output file with a UUID hash, so it won't ~~ever~~ repeat names.