import sys
import json

if len(sys.argv) != 4:
	print("usage: python translate.py input.svg output.svg translation.json")
	sys.exit(1)


# read file
file = open(sys.argv[1], "r")
file_contents = file.read()
file.close()


# translate
trans_dict = json.load(open(sys.argv[3], 'r', encoding='utf-8'))
asd = file_contents
for old, new in trans_dict.items():
	asd = asd.replace(old, new)
file_contents = asd


# write file
file = open(sys.argv[2], "w", encoding="utf-8")
file.write(file_contents)
file.close()
