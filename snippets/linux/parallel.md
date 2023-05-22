ls \*tif | parallel --sshloginfile nodefile \
 --dry-run \
 --transfer \
 --return {.}\_b1.tif \
 --cleanup \
 gdal_translate -of GTiff -b 1 {} {.}\_b1.tif
