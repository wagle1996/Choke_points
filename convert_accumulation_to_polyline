import rasterio
from shapely.geometry import mapping, shape
import geopandas as gpd
import fiona

# Input raster accumulation file (TIFF)
input_raster_file = 'accumulation.tif'

# Output vector file (GeoJSON) for the thresholded polylines
output_vector_file = 'thresholded_accumulation.geojson'

# Accumulation threshold
threshold = 100

# Open the input raster file
with rasterio.open(input_raster_file) as src:
    # Read the raster as a NumPy array
    accumulation_array = src.read(1)

    # Apply the threshold to the accumulation array
    thresholded_array = accumulation_array >= threshold

    # Create a new shapefile and write the thresholded features to it
    schema = {
        'geometry': 'LineString',
        'properties': {'id': 'int'},
    }

    with fiona.open(output_vector_file, 'w', 'GeoJSON', schema) as dst:
        for geom, value in rasterio.features.shapes(thresholded_array, transform=src.transform):
            if value:
                line = shape(geom)
                line = line.simplify(0.1)  # Simplify the line for cleaner output
                if line.is_empty:
                    continue
                geom = mapping(line)
                dst.write({'geometry': geom, 'properties': {'id': 1}})

# Load the thresholded polylines as a GeoDataFrame
gdf = gpd.read_file(output_vector_file)

# Print the GeoDataFrame
print(gdf)
