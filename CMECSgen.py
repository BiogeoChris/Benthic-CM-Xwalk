#run this script in ArcGIS python window
#execfile(r'C:\Users\chris.clement\CMECS\CMECSgen.py')

import arcpy
import os
import sys
import csv

arcpy.env.workspace = 'C:/Users/chris.clement/CMECS'

# Make a feature layer to work on
arcpy.MakeFeatureLayer_management("Guam_2005test","Guam_2005_CM")

# Add Fields
arcpy.AddField_management("Guam_2005_CM",
                          "MSTR_CM",
                          "TEXT",
                          "",
                          "",
                          "250",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")
arcpy.AddField_management("Guam_2005_CM",
                          "MSTR_CMCD",
                          "TEXT",
                          "",
                          "",
                          "25",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")

arcpy.AddField_management("Guam_2005_CM",
                          "DSTR_CM",
                          "TEXT",
                          "",
                          "",
                          "250",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")
arcpy.AddField_management("Guam_2005_CM",
                          "DSTR_CMCD",
                          "TEXT",
                          "",
                          "",
                          "25",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")

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

arcpy.AddField_management("Guam_2005_CM",
                          "PCOV_CM",
                          "TEXT",
                          "",
                          "",
                          "250",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")
arcpy.AddField_management("Guam_2005_CM",
                          "PCOV_CMCD",
                          "TEXT",
                          "",
                          "",
                          "25",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")

arcpy.AddField_management("Guam_2005_CM",
                          "ZONE_CM",
                          "TEXT",
                          "",
                          "",
                          "250",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")
arcpy.AddField_management("Guam_2005_CM",
                          "ZONE_CMCD",
                          "TEXT",
                          "",
                          "",
                          "25",
                          "",
                          "NULLABLE",
                          "NON_REQUIRED",
                          "")


# Create dictionaries
dictMSTR= {'AField1':('AField2','AField3'),
           'Coral Reef and Hardbottom':('Rock Substrate - Substrate Class (SC) AND Coral Reef Substrate - Substrate Subclass (SC)','Gg2.5, Gg1.50'),
           'Unconsolidated sediment':('Unconsolidated Mineral Substrate - Substrate Class (SC)','S1.2'),
           'Other Delineations':('No Equivalent','no code'),
           'Unknown':('Unknown (Mapping Convention)','0')}

dictDSTR= {'AField1':('AField2','AField3'),
           'Aggregate Reef':('Aggregate Coral Reef- Level 1 and Level 2 Geoform Type (GC)',
           'Gg2.5.1'),'Aggregated Patch Reefs':('Patch Coral Reef - Level 1 and Level 2 Geoform Type (GC) Patchiness (Modifier)','Gg2.5.9(PC##)'),
           'Artificial':('Anthropogenic - Geoform Origin (GC)','Gg3'),'Individual Patch Reef':('Patch Coral Reef - Level 1 and Level 2 Geoform Type (GC)','Gg2.5.9'),
           'Land':('No Equivalent','no code'),'Mud':('Mud - Substrate Group AND Carbonate - Substrate Descriptor (Modifier)','S1.2.2.5'),
           'Pavement':('Pavement Area - Level 1 and 2 Geoform (GC) AND Carbonate - Substrate Descriptor (Modifier)','Gg1.44(SD01)'),
           'Pavement with Sand Channels':('Pavement Area - Level 1 and 2 Geoform (GC) AND Carbonate - Substrate Descriptor (Modifier) WITH Co-Occurring Element Sand Channel - Level 2 Geoform (GC)','Gg1.44(SD01), Gg1.9.2'),
           'Reef Rubble':('Rubble Area- Level 1 Geoform (GC) AND Coral Rubble- Substrate Subclass (SC)','S2.2.2'),'Rhodoliths':('Rhodolith Substrate - Substrate Subclass (SC)','S2.1.2'),
           'Rhodoliths with Scattered Coral and Rock':('Rhodolith Substrate - Substrate Subclass (SC) WITH Co-Occurring Element Coral Head - Level 2 Geogorm Type (GC) WITH Co-Occurring Element Boulder - Subgroup (SC)','S2.1.2, S2.2.2, S1.1'),
           'Rock/Boulder':('Rock Outcrop - Level 1 Geoform (GC)','Gg1.7'),
           'Sand':('Sand - Substrate Group (SC)','S1.2.2.2'),
           'Sand with Scattered Coral and Rock':('Sand - Substrate Group (SC) WITH Co-Occurring Element Coral Head - Level 2 Geoform Type (GC) AND/OR Co-Occurring Element Boulder - Subgroup (SC)','S1.2.2.2, S2.2.2, S1.1'),
           'Spur and Groove':('Spur and Groove Coral Reef- Level 1 and Level 2 Geoform Type (GC)','Gg2.5.11'),
           'Unknown':('Unknown (Mapping Convention)','0')}

dictMCOV= {'AField1':('AField2','AField3'),
           'Live Coral':('Shallow/Mesophotic Coral Reef Biota - Biotic Subclass (BC)','B2.1.2'),
           'Coralline Algae':('Coralline/Crustose Algal Bed - Biotic Group (BC)','B2.5.1.3'),
           'Mangrove':('Tidal Mangrove Shrubland- Biotic Group (BC) OR Tidal Mangrove Forest - Biotic Group (BC)','B2.7.1.4, B2.8.1.4'),
           'Macroalgae':('Benthic Macroalgae - Biotic Subclass (BC)','B2.5.1'),
           'Seagrass':('Seagrass Bed- Biotic Group (BC)','B2.5.2.1'),
           'Turf':('Turf Algal Bed - Biotic Group (BC)','B2.5.1.8'),
           'No Cover':('No Cover','0'), 'Unclassified':('N/A','0'),
           'Emergent Vegetation':('Emergent Vegetation ???','0'),
           'Unknown':('Unknown (Mapping Convention)','0')}

dictPCOV= {'AField1':('AField2','AField3'),
           'Patchy (10% - <50%)':('Patchy 1 (10% - <50%) - Percent Cover (Modifier)','(PC10 - <50)'),
           'Patchy (50% - <90%)':('Patchy 2 (50% - <90%) - Percent Cover (Modifier)','(PC50 - <90)'),
           'Continuous (90% - 100%)':('Continuous (90% - 100%) - Percent Cover (Modifier)','(PC90 - 100)'),
           'N/A':('NA','na')}

dictZONE= {'AField1':('AField2','AField3'),
           'Back Reef':('Back Reef - Coral Reef Zone (Modifier)','(CRZ01)'),
           'Bank/Shelf':('Bank/Shelf - Coral Reef Zone (Modifier)','(CRZ02)'),
           'Bank/Shelf Escarpment':('Bank/Shelf Escarpment - Coral Reef Zone (Modifier)','(CRZ03)'),
           'Channel':('Pass/Lagoon Channel - Level 2 Geoform Type (GC)','Gg1.9.1'),
           'Dredged':('Dredged - Anthropogenic Impact (Modifier)','(AI04)'),
           'Fore Reef':('Fore Reef - Coral Reef Zone (Modifier)','(CRZ04)'),
           'Lagoon':('Lagoon - Coral Reef Zone (Modifier)','(CRZ05)'),
           'Reef Crest':('Reef Crest - Coral Reef Zone (Modifier)','(CRZ06)'),
           'Reef Flat':('Reef Flat - Coral Reef Zone (Modifier)','(CRZ07)'),
           'Reef Hole':('Hole/Pit - Level 1 Geoform (GC)','GG1.25'),
           'Reef Ridge Complex':('Reef Ridge Complex - Coral Reef Zone (Modifier)','(CRZ08)?'),
           'Salt Pond':('Salt Pond - Level 1 or 2 Geoform (GC)','Gg3.32'),
           'Shoreline Intertidal':('Shore Complex - Level 1 Geoform (GC)','Gp7'),
           'Land':('No Equivalent','no code')}


#Get key value pairs, optional just to make sure the dictionary is working
#for key, val in dictMCOV.items():
#...     print key, " => ", val


# Write the dictionaries to csv files
with open("dmstr7.csv", "wb") as f:
    csv.writer(f).writerows ((k,) + v for k, v in sorted(dictMSTR.iteritems()))

with open("ddstr7.csv", "wb") as f:
    csv.writer(f).writerows((k,) + v for k, v in sorted(dictDSTR.iteritems()))    

with open("dmcov7.csv", "wb") as f:
    csv.writer(f).writerows((k,) + v for k, v in sorted(dictMCOV.iteritems()))

with open("dpcov7.csv", "wb") as f:
    csv.writer(f).writerows((k,) + v for k, v in sorted(dictPCOV.iteritems()))

with open("dzone7.csv", "wb") as f:
    csv.writer(f).writerows((k,) + v for k, v in sorted(dictZONE.iteritems()))


# Import csv into geodatabase
arcpy.TableToTable_conversion("C:/Users/chris.clement/CMECS/dmstr7.csv","C:/Users/chris.clement/CMECS/testpython.gdb","dmstr77")
arcpy.TableToTable_conversion("C:/Users/chris.clement/CMECS/ddstr7.csv","C:/Users/chris.clement/CMECS/testpython.gdb","ddstr77")
arcpy.TableToTable_conversion("C:/Users/chris.clement/CMECS/dmcov7.csv","C:/Users/chris.clement/CMECS/testpython.gdb","dmcov77")
arcpy.TableToTable_conversion("C:/Users/chris.clement/CMECS/dpcov7.csv","C:/Users/chris.clement/CMECS/testpython.gdb","dpcov77")
arcpy.TableToTable_conversion("C:/Users/chris.clement/CMECS/dzone7.csv","C:/Users/chris.clement/CMECS/testpython.gdb","dzone77")

# Join the dictionary table
arcpy.AddJoin_management("Guam_2005_CM","M_STRUCT","dmstr77","AField1")
arcpy.AddJoin_management("Guam_2005_CM","D_STRUCT","ddstr77","AField1")
arcpy.AddJoin_management("Guam_2005_CM","M_COVER","dmcov77","AField1")
arcpy.AddJoin_management("Guam_2005_CM","P_COVER","dpcov77","AField1")
arcpy.AddJoin_management("Guam_2005_CM","ZONE","dzone77","AField1")


# Calculate CM and CMCD fields
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.MSTR_CM","!dmstr77.AField2!","PYTHON")
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.MSTR_CMCD","!dmstr77.AField3!","PYTHON")

arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.DSTR_CM","!ddstr77.AField2!","PYTHON")
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.DSTR_CMCD","!ddstr77.AField3!","PYTHON")

arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.MCOV_CM","!dmcov77.AField2!","PYTHON")
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.MCOV_CMCD","!dmcov77.AField3!","PYTHON")

arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.PCOV_CM","!dpcov77.AField2!","PYTHON")
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.PCOV_CMCD","!dpcov77.AField3!","PYTHON")

arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.ZONE_CM","!dzone77.AField2!","PYTHON")
arcpy.CalculateField_management("Guam_2005_CM","Guam_2005test.ZONE_CMCD","!dzone77.AField3!","PYTHON")
       
