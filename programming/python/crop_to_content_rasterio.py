#!/usr/bin/python

import argparse
import os

import numpy as np
import rasterio


def clip_edges(src_path, dst_path):
    with rasterio.open(src_path) as src:
        # Read the nodata value from the metadata
        nodata = src.nodata

        # Read the image data as a numpy array
        data = src.read(1)

        # Find the indices of the first and last rows and columns that contain valid data
        rows = np.where(np.any(data != nodata, axis=1))[0]
        cols = np.where(np.any(data != nodata, axis=0))[0]

        # Clip the data array to the valid rows and columns
        clipped_data = data[rows.min() : rows.max() + 1, cols.min() : cols.max() + 1]

        # Compute the new affine transformation matrix for the clipped data
        transform = src.transform
        xoff = transform[2] + cols.min() * transform[0]
        yoff = transform[5] + rows.min() * transform[4]
        new_transform = rasterio.Affine(transform[0], transform[1], xoff, transform[3], transform[4], yoff)

        # Write the clipped data to a new raster file
        kwargs = src.meta
        kwargs.update({'width': clipped_data.shape[1], 'height': clipped_data.shape[0], 'transform': new_transform})
        with rasterio.open(dst_path, 'w', **kwargs) as dst:
            dst.write(clipped_data, 1)


def main():
    parser = argparse.ArgumentParser(description='Clip raster images by removing edges with no valid data')
    parser.add_argument('input_files', nargs='+', help='Input files to clip')
    parser.add_argument('-o', '--output-dir', default='clipped', help='Output directory for clipped files')
    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Clip each input file and write the clipped version to the output directory
    for src_path in args.input_files:
        dst_path = os.path.join(args.output_dir, os.path.basename(src_path))
        clip_edges(src_path, dst_path)


if __name__ == '__main__':
    main()
