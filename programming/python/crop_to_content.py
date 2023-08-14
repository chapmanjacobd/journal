#!/usr/bin/python

import argparse
import numpy as np
from osgeo import gdal


def clip_to_content(input_path, output_path):
    ds = gdal.Open(input_path)

    # Find the minimal and maximal rows and columns across all bands
    min_row = ds.RasterYSize
    max_row = 0
    min_col = ds.RasterXSize
    max_col = 0
    for band_gid in range(1, ds.RasterCount + 1):
        band = ds.GetRasterBand(band_gid)
        data = band.ReadAsArray()
        nodata = band.GetNoDataValue()
        row_idxs, col_idxs = np.where(data != nodata)
        if len(row_idxs) > 0:
            min_row = min(min_row, int(np.min(row_idxs)))
            max_row = max(max_row, int(np.max(row_idxs)))
        if len(col_idxs) > 0:
            min_col = min(min_col, int(np.min(col_idxs)))
            max_col = max(max_col, int(np.max(col_idxs)))

    # Clip the raster to its content
    clip_width = max_col - min_col + 1
    clip_height = max_row - min_row + 1
    driver = gdal.GetDriverByName("GTiff")
    clipped_ds = driver.Create(
        output_path,
        xsize=clip_width,
        ysize=clip_height,
        bands=ds.RasterCount,
        eType=ds.GetRasterBand(1).DataType,
        options=["TILED=YES", "COMPRESS=DEFLATE"],
    )
    for band_gid in range(1, ds.RasterCount + 1):
        band = ds.GetRasterBand(band_gid)
        nodata = band.GetNoDataValue()
        data = band.ReadAsArray(min_col, min_row, clip_width, clip_height)
        clipped_ds.GetRasterBand(band_gid).WriteArray(data)
        clipped_ds.GetRasterBand(band_gid).SetNoDataValue(nodata)

    # Set the affine transformation matrix for the clipped raster
    xoff, xres, _, yoff, _, yres = ds.GetGeoTransform()
    new_xoff = xoff + min_col * xres
    new_yoff = yoff + min_row * yres
    clipped_ds.SetGeoTransform((new_xoff, xres, 0, new_yoff, 0, yres))

    # Copy over the projection from the original raster
    clipped_ds.SetProjection(ds.GetProjection())

    del ds

    # Compute Stats of each band
    for band_gid in range(1, clipped_ds.RasterCount + 1):
        clipped_ds.GetRasterBand(band_gid).ComputeStatistics(approx_ok=False)

    del clipped_ds


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clip a multi-band raster to its content.")
    parser.add_argument("input_path", help="Path to the input raster.")
    parser.add_argument("output_path", help="Path to the output raster.")
    args = parser.parse_args()

    clip_to_content(args.input_path, args.output_path)
