#!/bin/bash

for f in P-2*.svg; do
    echo $f
    inkscape -z --export-area-drawing --export-margin=0.2 --export-plain-svg=../$f $f
done

