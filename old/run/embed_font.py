import sys
import json

if len(sys.argv) != 4:
	print("usage: python embed_font.py input.svg output.svg font.woff2.b64.embed")
	sys.exit(1)


# read file
file = open(sys.argv[1], "r")
file_contents = file.read()
file.close()


# embed font
asd = file_contents.split("\n")
asd.insert(1, open(sys.argv[3]).read())
file_contents = "\n".join(asd)


# write file
file = open(sys.argv[2], "w")
file.write(file_contents)
file.close()
