I do spatial data engineering and, depending what analysis or transformation you need to do, it is often easier to use system calls to SAGA or QGIS (via the qgis_process CLI) than it is to setup an environment to interface with the python libraries like pyQGIS, etc. And it's easier to parallelize that way as well.

gdal_translate/warp and ogr2ogr are immensely helpful and easy to use as well after an hour or two of getting used to some syntax.

For vector libraries in python there is geopandas and ogr from osgeo (same as ogr2ogr, it's part of GDAL).

For raster you can try rasterio but I think some of the interface choices they made make it confusing to use. Might be better to use the python bindings of GDAL directly! If you are just converting formats then use gdal_translate because that will be easier and faster

System call example:
    
    from subprocess import PIPE, run
    
    
    def cmd(command, **kwargs):
        log = logging.getLogger()
        r = run(
            command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True, **kwargs
        )
        log.debug(r.args)
        if r.returncode != 0:
            log.error(f"process exited with returncode {r.returncode}")
        log.info(r.stdout.strip())
        log.error(r.stderr.strip())
        return r
    
    cmd('saga_cmd -f=q grid_calculus "Grid Calculator" blah blah')
    
    or 
    
    cmd(f'env QT_QPA_PLATFORM=offscreen qgis_process run native:pixelstopolygons -- FIELD_NAME=value INPUT_RASTER="${{1%.tif}}.sdat" OUTPUT="./out/${{1%.tif}}.shp" RASTER_BAND=1')
