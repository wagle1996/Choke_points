import arcpy
from arcpy.sa import *

# Set the workspace and enable Spatial Analyst extension
arcpy.env.workspace = r'C:\Path\to\Your\Workspace'  # Change to your workspace directory
arcpy.CheckOutExtension("Spatial")

# Input pour point feature class
pour_point_shapefile = r'C:\Path\to\Your\PourPointShapefile.shp'

# Input flow direction raster (you need to have this precomputed)
flow_direction_raster = r'C:\Path\to\Your\FlowDirectionRaster.tif'

# Output watershed feature class
output_watershed_shapefile = r'C:\Path\to\Your\WatershedShapefile.shp'

try:
    # Convert the pour point feature class to a raster
    pour_point_raster = arcpy.PourPoint(pour_point_shapefile)

    # Create the watershed using the Watershed tool
    watershed_raster = Watershed(flow_direction_raster, pour_point_raster)

    # Convert the watershed raster to a feature class
    arcpy.RasterToPolygon_conversion(watershed_raster, output_watershed_shapefile, "Simplify")

    print('Watersheds created and saved to', output_watershed_shapefile)

except Exception as e:
    print('An error occurred:', str(e))

# Release Spatial Analyst extension
arcpy.CheckInExtension("Spatial")
