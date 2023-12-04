# Lab 07

import arcpy

# Use satellite imagery to create a composite raster image
dataPath = r"C:\\Users\\Bendi\\OneDrive\\Documents\\G392\\Labs\\BLG392\\Lab7\\Lab07_Data\\"
resultsPath = r"C:\\Users\\Bendi\\OneDrive\\Documents\\G392\\Labs\\BLG392\\Lab7\\Lab07_Results\\"
# Image file paths for each band
blue = arcpy.sa.Raster(dataPath + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF") 
green = arcpy.sa.Raster(dataPath + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF") 
red = arcpy.sa.Raster(dataPath + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF") 
nir = arcpy.sa.Raster(dataPath + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF") 
# Composite all together
# comp = arcpy.CompositeBands_management([blue, green, red, nir], resultsPath + "combined.tif")


# Use DEM to create hillshade
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(dataPath + r"\\n30_w097_1arc_v3.tif", resultsPath + r"\\hillshade.tif", azimuth, altitude, shadows, z_factor)


# Use DEM to create slope image
outputMeasurements = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(dataPath + r"\\n30_w097_1arc_v3.tif", resultsPath + r"\\slopes.tif", outputMeasurements, z_factor)