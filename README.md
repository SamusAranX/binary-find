# binary-find
or `bfind` for short

## What?

I needed a way to find files based on their binary headers.

## Usage

```
$ ./bfind.py -h
usage: bfind.py [-h] [-r] [-x] header input [input ...]

find files based on their headers

positional arguments:
  header           the header to look for (must be ascii)
  input            the files or folders to scan

options:
  -h, --help       show this help message and exit
  -r, --recursive  scan folders recursively
  -x, --hex        parse header as hex string (see https://docs.python.org/3/library/stdtypes.html#bytes.fromhex)
```

### Examples:

```
$ bfind "KB2" textures/videos/static/
Looking for 3 bytes: b'KB2'
<path>/textures/videos/static/static_alice_documentary.tex
```

```
$ bfind -r "KB2" textures/videos/
Recursively looking for 3 bytes: b'KB2'
<path>/textures/videos/blended_videos/bv_darkness.tex
<path>/textures/videos/blended_videos/bv_placeholder.tex
<path>/textures/videos/blended_videos/cine/bv_cine_tor_01.tex
<path>/textures/videos/blended_videos/echoes/bv_echo_alex_casey_face_01.tex
<path>/textures/videos/blended_videos/echoes/bv_echo_alex_casey_face_02.tex
```

```
$ bfind -x "44 44 53" textures/weapons/
Looking for 3 bytes: b'DDS'
<path>/textures/weapons/casey_pistol/casey_pistol_d.tex
<path>/textures/weapons/casey_pistol/casey_pistol_n.tex
<path>/textures/weapons/casey_pistol/casey_pistol_s.tex
<path>/textures/weapons/casey_pistol/casey_pistol_sa.tex
```