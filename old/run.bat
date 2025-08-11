@echo off
copy "periodic_table.svg" "run/temp/0.svg"
echo preparation DONE

python "run/embed_font.py"	"run/temp/0.svg"	"run/temp/1.svg"	"run/font/Roboto-Bold.woff2.b64.embed"
echo font embed DONE

python "run/translate.py"	"run/temp/1.svg"	"run/temp/2.svg"	"run/translations/en-pl.json"
echo translation DONE

copy "run/temp/2.svg" "export.svg"
echo svg export DONE

"C:\Program Files\Inkscape\bin\inkscape.exe" "run/temp/2.svg" --export-type=png --export-filename=output.png --export-dpi=500
echo png export DONE

echo all DONE