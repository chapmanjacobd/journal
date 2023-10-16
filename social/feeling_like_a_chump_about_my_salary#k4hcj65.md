If you can do shell scripting it is a lot easier to get started (and more portable; don't have to fiddle around with environments) if you call `qgis_process` instead of using PyQGIS. IMHO there isn't a huge benefit to learning PyQGIS. 

If you _are_ doing something really custom the learning curve is roughly the same to use Python GDAL/OGR bindings directly (rather than learning PyQGIS) and GDAL/OGR is generally more flexible.
