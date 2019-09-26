#!/bin/bash
./svg-hide-border *.svg
for f in *.svg; do
    echo $f;
    inkscape -z --file=$f --export-dpi=96 --export-area-drawing --export-margin=20 --export-plain-svg=../$f;
done
