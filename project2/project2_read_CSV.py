import arcpy
arcpy.env.workspace = r"C:\arcGISpro\SSCI586\project2" # r"C:\arcGISpro\project2\MyProject2" 

# Set the local variables
interesting_locations_table = "target_locations.csv"
out_place_to_visit_shape_class = "place_to_visit.shp"
x_coords = "LONGITUDE"
y_coords = "LATITUDE"
z_coords = "ELEVATION(ft)"

# SpatialReference ==> https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/pdf/projected_coordinate_systems.pdf
# Geographic Coordinate System ==> https://spatialreference.org/ref/epsg/nad83/
arcpy.management.XYTableToPoint(interesting_locations_table, out_place_to_visit_shape_class,
                                x_coords, y_coords, z_coords,
                                arcpy.SpatialReference(4269))

# Print the total rows
print(arcpy.GetCount_management(out_place_to_visit_shape_class))
