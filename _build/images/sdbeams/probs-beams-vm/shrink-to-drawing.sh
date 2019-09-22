for f in *-prob.svg; do echo $f; inkscape -z --file=$f --export-dpi=96 --export-area-drawing --export-margin=0.2 --export-plain-svg=x/$f; done
