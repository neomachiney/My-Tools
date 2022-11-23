# PROJECT UNMAINTAINED AND MAY CONTAIN BUGS. CURRENTLY TAKING BREAKEXIF is metadata of image files. So, to uploading image with malicious EXIF metadata will cause either XSS or Code Injection or sometimes other parsing bugs. You need to have exiftool installed
* Use exiftool to view exif metadata before and after injecting payloads. Eg: `exiftool awk.png`

# EXIF-RCE
* Description: The tool has set of exif metadata list where malicious codes are injected in values of exif metadata. 
* Usage: Use --help to know its usage. 
 - If server is php based, use php reverse shell code in --payload. Escaping of payload maybe needed.
 - In EXIF-RCE.py, change `argv.payload` to one with `argv.server` (second payload) by commenting the last and removing `#` of second payload. Then you are free to use --server and --port otherwise those options are additional.
 - If --payload isn't specified, it will use the last one
 - Use any png or jpeg in --input. Might work with other images types	

# EXIF-XSS
* Description: The tool has set of exif metadata list where malicious xss payloads are injected in values of exif metadata. 
* Usage: Use --help to know its usage. 
 - If --payload isn't specified it will use default payload.
 - Use any png or jpeg in --input. Might work with other images types	

