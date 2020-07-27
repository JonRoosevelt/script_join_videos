# Script Join Videos

About
---
This a simple Python script to merge video files.

Instalation
---

As any Python code, you should do this inside a virtual environment. 
Though it doesn't require any external python lib, you need ffmpeg installed in your machine.

**Linux**
```  
$ (sudo) apt install ffmpeg
```

**Mac**
```
$ brew install ffmpeg
```

Usage
---

From the installed folder, run
```
$ python join_videos.py ~/path/to/videos

```

It will generate the output file in the same folder where the input videos are.

Ps.:
---
* Currently works only with webm files.
* To a better result, you should rename your files to be merged in the order you want.
* It generates the output file with a UUID hash, so it won't ~~ever~~ repeat names.