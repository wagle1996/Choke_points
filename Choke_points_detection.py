import arcpy

# Set the environment workspace
arcpy.env.workspace = r'C:\Path\to\Your\Workspace'  # Change to your workspace directory

# Input shapefile paths
polygon_shapefile = r'C:\Path\to\Your\0.6m_watershed_boundary.shp' #Intersection between boundary of 0.6m and 2m river lines are choke points"
line_shapefile = r'C:\Path\to\Your\2m_river_lines.shp'
basin_shapefile = r'C:\Path\to\Your\Basin.shp'  #Remove all the choke points which are closer to basins

# Output shapefile path
output_shapefile = r'C:\Path\to\Your\OutputShapefile.shp'

# Buffer distance
buffer_distance = '500 Units'

try:
    # Create feature layers for the shapefiles
    arcpy.MakeFeatureLayer_management(polygon_shapefile, 'polygon_lyr')
    arcpy.MakeFeatureLayer_management(line_shapefile, 'line_lyr')
    arcpy.MakeFeatureLayer_management(basin_shapefile, 'basin_lyr')

    # Intersect the line with the polygon to find intersection points
    arcpy.Intersect_analysis(['polygon_lyr', 'line_lyr'], 'in_memory/intersect_points')

    # Buffer the basin points
    arcpy.Buffer_analysis('basin_lyr', 'in_memory/buffered_basin', 50)

    # Create a feature layer for the buffered basin
    arcpy.MakeFeatureLayer_management('in_memory/buffered_basin', 'buffered_basin_lyr')

    # Select the intersection points that are outside of the buffered basin
    arcpy.SelectLayerByLocation_management('in_memory/intersect_points', 'WITHIN', 'buffered_basin_lyr', invert_spatial_relationship=True)

    # Copy the selected points to the output shapefile
    arcpy.CopyFeatures_management('in_memory/intersect_points', output_shapefile)

    print('Intersection points outside of the buffered basin have been saved to', output_shapefile)

except Exception as e:
    print('An error occurred:', str(e))

# Clean up intermediate data
arcpy.Delete_management('in_memory/intersect_points')
arcpy.Delete_management('in_memory/buffered_basin')
