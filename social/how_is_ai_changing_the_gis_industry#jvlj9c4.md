I think there are two main impacts AI will have with GIS:

1. Tools like ChatGPT could be used as an interface to spatial data processing / analysis; but when it makes mistakes it won't be obvious that a mistake was made. For large datasets, batch spatial computation takes a while. So it will be expensive to rectify and reprocess data. Tools like ChatGPT lower the initial barrier to using low level libraries like GDAL/OGR to do custom geospatial processing but there is still a learning curve to be productive (eg. understanding why segmentation faults happen, how to fix them).

2. ML models allow working with a large number of datasets at the same time where a map with all the data overlaid would be difficult or impossible to interpret. It's not the solution for everything just a tool in the toolbox along with other spatial statistics and aggregating methods. Spatial ML models have been available for at least ten years but they are becoming more mainstream and product-ized.
