#!/usr/bin/python

import argparse
from pathlib import Path

from osgeo import gdal, gdalconst


def parse_args():
    parser = argparse.ArgumentParser(description='Apply various GDAL warp resample algorithms to a raster file.')
    parser.add_argument('input_path', help='the input raster file')
    parser.add_argument('output_folder')
    parser.add_argument('--multiply', type=float, default=2)
    return parser.parse_args()


resample_modes = [
    'near',
    'bilinear',
    'cubic',
    'cubicspline',
    'lanczos',
    'average',
    'rms',
    'mode',
    'max',
    'min',
    'med',
    'q1',
    'q3',
    'sum',
]


def main():
    args = parse_args()

    ds: gdal.Dataset = gdal.Open(args.input_path, gdalconst.GA_ReadOnly)

    geotransform = ds.GetGeoTransform()
    origin_x = geotransform[0]
    pixel_width = geotransform[1]
    rotation_0 = geotransform[2]
    origin_y = geotransform[3]
    rotation_1 = geotransform[4]
    pixel_height = geotransform[5]

    Path(args.output_folder).mkdir(parents=True, exist_ok=True)
    for mode in resample_modes:
        output_path = Path(args.output_folder) / Path(Path(args.input_path).stem + '_' + mode + '.tif')
        warp_options = gdal.WarpOptions(
            resampleAlg=mode,
            xRes=args.multiply * pixel_width,
            yRes=args.multiply * pixel_height,
        )
        gdal.Warp(str(output_path), ds, options=warp_options)


if __name__ == '__main__':
    main()
