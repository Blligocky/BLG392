# Import ArcPy 
import arcpy



### Create File geodatabase 
# Set folder path
fp = r"C:\\Users\\Bendi\\OneDrive\\Documents\\G392\\Labs\\BLG392\\Lab4"

# Set GDB name and path 
gdb_name = "G392_Lab04.gdb"
gdb_path = fp + "\\" + gdb_name
arcpy.CreateFileGDB_management(fp, gdb_name)



### Read CSV and make layer from it
# Retrieve data 
csv_path = r"C:\\Users\\Bendi\\OneDrive\\Documents\\G392\\Labs\\BLG392\\Lab4\\Lab04_Data\\garages.csv"
garage_layer_name = "Garage_Points"
garages = arcpy.MakeXYEventLayer_management(csv_path, "X", "Y", garage_layer_name)

# Add garages to GDB
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)

# Get points layer
garage_points = gdb_path + "\\" + garage_layer_name



### Copy buildings to Lab GDB from Campus GDB
# Open campus GDB
campus = r"C:\\Users\\Bendi\\OneDrive\\Documents\\G392\\Labs\\BLG392\\Lab4\\Lab04_Data\\Campus.gdb"
buildings_campus = campus + "\\Structures"
buildings = gdb_path + "\\" + "Buildings"

# Copy 
arcpy.Copy_management(buildings_campus, buildings)



### Make sure the projections match 
# Buildings layer projection
spatial_ref = arcpy.Describe(buildings).spatialReference 

# Project garage points 
arcpy.Project_management(garage_points, gdb_path +  "\Garage_Points_reprojected", spatial_ref)



# Spatial analysis based on buildings and points layers
# Buffer garages 
garage_buffered = arcpy.Buffer_analysis(gdb_path + "\Garage_Points_reprojected", gdb_path + "\Garage_Points_buffered", 150)

# Intersect the layers
arcpy.Intersect_analysis([garage_buffered, buildings], gdb_path + "\Garage_Building_Intersection", "ALL")

# Output the information of buildings to csv
arcpy.TableToTable_conversion(gdb_path + "\Garage_Building_Intersection.dbf", r"C:\\Users\\Bendi\\OneDrive\\Documents\\G392\\Labs\\BLG392\\Lab4\\Lab04_Data", "nearbyBuildings.csv")