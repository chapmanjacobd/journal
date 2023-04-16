#!/usr/bin/python

# This does not quite work

import argparse
import math
import os
from pathlib import Path
import sys

import numpy as np
from osgeo import gdal
from PIL import Image, ImageDraw,ImageFont


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compare a list of rasters and output an 8-bit RGB image"
    )
    parser.add_argument(
        "input_folder",
        help="Path to folder containing input rasters"
    )
    parser.add_argument(
        "output_file",
        help="Path to output file (should end in .jpg)"
    )
    parser.add_argument(
        "--image-size",
        type=int,
        default=256,
        help="Size (in pixels) of output image (default: 512)",
    )
    parser.add_argument(
        "--font",
        default="/usr/share/fonts/dejavu-sans-fonts/DejaVuSansCondensed-Bold.ttf",
    )
    args = parser.parse_args()

    num_rasters = len([
        entry.name for entry in os.scandir(args.input_folder)
        if entry.is_file() and entry.name.endswith((".tif", ".tiff"))
    ])
    min_image_size = int(math.ceil(math.sqrt(num_rasters))) * 128
    args.image_size = max(args.image_size, min_image_size)

    return args


def read_raster(raster_path):
    raster = gdal.Open(raster_path)
    if raster is None:
        print(f"Error: Could not open {raster_path}", file=sys.stderr)
        sys.exit(1)
    return np.array(raster.GetRasterBand(1).ReadAsArray())

def main():
    args = parse_args()
    input_folder = args.input_folder
    output_file = args.output_file
    image_size = args.image_size

    raster_paths = [
        entry.path
        for entry in os.scandir(input_folder)
        if entry.is_file() and entry.name.endswith((".tif", ".tiff"))
    ]

    # Get information about all rasters
    rasters = []
    max_width = 0
    max_height = 0
    for raster_path in raster_paths:
        raster = gdal.Open(raster_path)
        if raster is None:
            print(f"Error: Could not open {raster_path}", file=sys.stderr)
            sys.exit(1)
        rasters.append(raster)
        width = raster.RasterXSize
        height = raster.RasterYSize
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height

    # Compute the number of rows and columns of rasters in the output image
    num_rasters = len(rasters)
    num_cols = math.ceil(math.sqrt(num_rasters))
    num_rows = math.ceil(num_rasters / num_cols)

    # Create a blank output image
    output_image = Image.new("RGB", (num_cols * image_size, num_rows * image_size), color="white")

    # Draw the title on the output image
    title_font = ImageFont.truetype(args.font, 24)
    draw = ImageDraw.Draw(output_image)
    title_text = "GDAL ResampleAlg Comparison"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = (output_image.width - title_bbox[2]) // 2
    draw.text((title_x, 10), title_text, fill="black", font=title_font)

    # Iterate over the rasters and paste them into the output image
    for i, raster in enumerate(rasters):
        # Compute the coordinates where this raster should be pasted
        row = i // num_cols
        col = i % num_cols
        x = col * image_size
        y = row * image_size

        # Get the raster data and rescale it to 8-bit
        band = raster.GetRasterBand(1)
        nodata_value = band.GetNoDataValue()
        data = band.ReadAsArray()
        data[data == nodata_value] = 0

        global_min = np.min(data)
        global_max = np.max(data)
        data = (data - global_min) / (global_max - global_min) * 255
        data = data.astype(np.uint8)

        # Get the label text for this raster
        label_text = Path(raster.GetDescription()).stem

        # Draw the label on the output image
        label_font = ImageFont.truetype(args.font, 16)
        label_bbox = draw.textbbox((0, 0), label_text, font=label_font)
        label_width = label_bbox[2] - label_bbox[0]
        label_height = label_bbox[3] - label_bbox[1]
        label_x = x + (image_size - label_width) // 2
        label_y = y + image_size + label_height
        draw.text((label_x, label_y), label_text, fill="black", font=label_font)

        # Paste the RGB data into the output image
        output_image.paste(
            Image.fromarray(data),
            box=(x, y, x + data.shape[1], y + data.shape[0]),
        )

    # Save the output image
    output_image.save(output_file)


if __name__ == "__main__":
    main()
