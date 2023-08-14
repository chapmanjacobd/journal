#!/usr/bin/python
import argparse

from osgeo import gdal

parser = argparse.ArgumentParser(description='Print the bounding box of a GeoTIFF file')
parser.add_argument('path')

args = parser.parse_args()

gdalinfo = gdal.Info(args.path, format='json')

xmin = ulx = gdalinfo['cornerCoordinates']['upperLeft'][0]
ymin = lry = gdalinfo['cornerCoordinates']['lowerRight'][1]
ymax = uly = gdalinfo['cornerCoordinates']['upperLeft'][1]
xmax = lrx = gdalinfo['cornerCoordinates']['lowerRight'][0]

print(f"gdalwarp -co COMPRESS=DEFLATE -te {xmin} {ymin} {xmax} {ymax} ")
