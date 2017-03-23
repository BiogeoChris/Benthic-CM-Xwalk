#run this script in ArcGIS python window
#execfile(r'C:\Users\chris.clement\CMECS\CMECSgen.py')

import arcpy
import os
import sys

arcpy.env.workspace = 'C:/Users/chris.clement/CMECS'

#Make a feature layer to work on
arcpy.MakeFeatureLayer_management("Guam_2005test","Guam_2005_CM")

# Add Fields (will be adding many more fields for the cross walk but just getting this part to work for now).
arcpy.AddField_management("Guam_2005_CM",
                          "MCOV_CM",
                          "TEXT",
                          "",
                          "",
                          "250",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")
arcpy.AddField_management("Guam_2005_CM",
                          "MCOV_CMCD",
                          "TEXT",
                          "",
                          "",
                          "25",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")



#Create dictionaries
dictMCOV= {'Live Coral':('Shallow/Mesophotic Coral Reef Biota - Biotic Subclass (BC)','B2.1.2'),
           'Coralline Algae':('Coralline/Crustose Algal Bed - Biotic Group (BC)','B2.5.1.3'),
           'Mangrove':('Tidal Mangrove Shrubland- Biotic Group (BC) OR Tidal Mangrove Forest - Biotic Group (BC)','B2.7.1.4, B2.8.1.4'),
           'Macroalgae':('Benthic Macroalgae - Biotic Subclass (BC)','B2.5.1'),
           'Seagrass':('Seagrass Bed- Biotic Group (BC)','B2.5.2.1'),
           'Turf':('Turf Algal Bed - Biotic Group (BC)','B2.5.1.8'),
           'No Cover':('No Cover','0'), 'Unclassified':('N/A','0'),
           'Emergent Vegetation':('Emergent Vegetation ???','0'),
           'Unknown':('Unknown (Mapping Convention)','0')}


#Get key value pairs, optional just to make sure the dictionary is working
#>>> for key, val in dictMCOV.items():
#...     print key, " => ", val


#Write the dictionaries to a csv file
import csv
with open("dmcov.csv", "wb") as f:
    csv.writer(f).writerows((k,) + v for k, v in dictMCOV.iteritems())

# Import csv into geodatabase
arcpy.TableToTable_conversion("C:/Users/chris.clement/CMECS/dmcov.csv","C:/Users/chris.clement/CMECS/testpython.gdb","dmcov4")

# Join the dictionary table
arcpy.AddJoin_management("Guam_2005_CM","M_COVER","dmcov4","Field1")

#Calculate MCOV_CM and MCOV_CMCD fields
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.MCOV_CM","!dmcov4.Field2!","PYTHON")
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.MCOV_CMCD","!dmcov4.Field3!","PYTHON")


       
