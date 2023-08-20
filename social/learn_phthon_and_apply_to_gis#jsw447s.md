I always had trouble setting up PyQGIS environments and making scripts portable. Luckily, `qgis-process` works great. Just throwing that option out there. You can script using BASH, PowerShell, or Python subprocesses with `qgis-process` and it is often simpler than the QGIS Python API.

I also recommend `GeoPandas`. Reach for that first, but if you need something lower-level use `GDAL / OGR` instead of `rasterio / fiona`. It will take longer to get started but it will be usually much easier to work around weird edge cases.
