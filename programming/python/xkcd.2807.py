import argparse
from pathlib import Path

from osgeo import ogr


def abs_coordinates(geometry):
    if isinstance(geometry, ogr.Geometry):
        for ring in geometry:
            if not ring.IsRing():
                ring.AddPoint(ring.GetX(0), ring.GetY(0))

            for point in ring:
                x, y = point.GetX(), point.GetY()
                point.SetPoint(0, abs(x), abs(y))


def process_geometry_file(input_file, output_file):
    ds = ogr.OpenShared(input_file)

    in_layer = ds.GetLayer()

    out_ds_driver = ogr.GetDriverByName('FlatGeobuf')
    out_ds = out_ds_driver.CreateDataSource(output_file)
    out_layer = out_ds.CreateLayer("abs_geometries", geom_type=ogr.wkbMultiPolygon)

    in_layer_defn = in_layer.GetLayerDefn()
    for i in range(in_layer_defn.GetFieldCount()):
        field_defn = in_layer_defn.GetFieldDefn(i)
        out_layer.CreateField(field_defn)

    for input_feature in in_layer:
        geometry = input_feature.GetGeometryRef().Clone()
        abs_coordinates(geometry)

        out_feature = ogr.Feature(out_layer.GetLayerDefn())
        out_feature.SetGeometry(geometry)
        for i in range(input_feature.GetFieldCount()):
            out_feature.SetField(i, input_feature.GetField(i))

        out_layer.CreateFeature(out_feature)
        del out_feature

    del ds
    del out_ds

    print("RADICAL LONGITUDINAL DUDE:", output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process geometry file to abs(longitude)")
    parser.add_argument("input_file", help="Path to the input geometry file")
    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_path = input_path.parent / f"{input_path.stem}.xkcd2807{input_path.suffix}"
    output_path.unlink(missing_ok=True)

    process_geometry_file(str(input_path), str(output_path))
