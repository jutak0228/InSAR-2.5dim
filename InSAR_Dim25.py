#-------------------------------------------------------------------------------
# Name:        InSAR_Dim25.py
# Purpose:     InSAR 2.5-dim Analysis Program
#
# Author:      006323
#
# Created:     08/06/2018
# Copyright:   (c) 006323 2018
# Licence:     <your licence>
# How to execute: > InSAR_Dim25.py [Ascending Displacement] [Ascending Local Incidence Angle] [Ascending Orientation Angle]
#                   [Descending Displacement] [Descending Local Incidence Angle] [Descending Orientation Angle]
#                   [Output Path] [Output Filename]
#-------------------------------------------------------------------------------

import arcpy
from arcpy import env
from arcpy.sa import *
import os
import sys  # ????
import arcpy.cartography as CA
import shutil

arcpy.CheckOutExtension("Spatial")

argvs = sys.argv    # ?????
argc = len(argvs)   # ?????

print(argvs)

if(argc < 9):
    print(argvs)
    print("Number of input=%d\n" % argc)
    print("InSAR 2.5-dim Analysis : set arguments as shown below. ----------------------------------------")
    print("[Ascending Displacement (Delta_A)] <char>")
    print("[Ascending Local Incidence Angle (Theta_A)] <char>")
    print("[Ascending Orientation Angle (Phi_A)] <char>")
    print("[Descending Displacement (Delta_D)] <char>")
    print("[Descending Local Incidence Angle (Theta_D)] <char>")
    print("[Descending Orientation Angle (Phi_D)] <char>")
    print("[Output Path] <char>")
    print("[Output Filename] <char>")
    quit()

in_Displacement_ASC = argvs[1]
in_IncidenceAngle_ASC = argvs[2]
in_OrientationAngle_ASC = argvs[3]
in_Displacement_DES = argvs[4]
in_IncidenceAngle_DES = argvs[5]
in_OrientationAngle_DES = argvs[6]
in_OutputPath = argvs[7]
in_OutputFile = argvs[8]

print("Check Parameters -----------------------------------")
print("Displacement_ASC=%s" % in_Displacement_ASC)
print("IncidenceAngle_ASC=%s" % in_IncidenceAngle_ASC)
print("OrientationAngle_ASC=%s" % in_OrientationAngle_ASC)
print("Displacement_DES=%s" % in_Displacement_DES)
print("IncidenceAngle_DES=%s" % in_IncidenceAngle_DES)
print("OrientationAngle_DES=%s" % in_OrientationAngle_DES)
print("OutputPath=%s" % in_OutputPath)
print("OutputFile=%s_X.tif, %s_Z.tif" % (in_OutputFile, in_OutputFile) )

# Process Start
print("##### PROCESS START. #####\n")

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = in_OutputPath

# Pre-Processing - delete output file
del_output = in_OutputPath + in_OutputFile
if os.path.exists(del_output):
    arcpy.Delete_management(del_output)

# Cast from input filepath to Raster
Delta_A = Raster(in_Displacement_ASC)
Theta_A = Raster(in_IncidenceAngle_ASC)
Phi_A = Raster(in_OrientationAngle_ASC)
Delta_D = Raster(in_Displacement_DES)
Theta_D = Raster(in_IncidenceAngle_DES)
Phi_D = Raster(in_OrientationAngle_DES)

# [2.5-dim Analysis with Raster Operation]
# format :
# delta_X = ( delta_A*cos(theta_D) - delta_D*cos(theta_A) ) / ( sin(theta_A)*cos(phi_A) - sin(theta_D)*cos(phi_D) )
# delta_Z = ( delta_A*sin(theta_D)*cos(phi_D) - delta_D*sin(theta_A)*cos(phi_A) ) / ( cos(theta_A)*sin(theta_D)*cos(phi_D) - cos(theta_D)*sin(theta_A)*cos(phi_A) )
print("[2.5-dim Analysis with raster operation] START... -----------------------------------")

upper_X = Delta_A*Cos(Theta_D) - Delta_D*Cos(Theta_A)
lower_X = Sin(Theta_A)*Cos(Phi_A) - Sin(Theta_D)*Cos(Phi_D)
upper_Z = Delta_A*Sin(Theta_D)*Cos(Phi_D) - Delta_D*Sin(Theta_A)*Cos(Phi_A)
lower_Z = Cos(Theta_A)*Sin(Theta_D)*Cos(Phi_D) - Cos(Theta_D)*Sin(Theta_A)*Cos(Phi_A)

ras_delta_X = upper_X / lower_X
ras_delta_Z = upper_Z / lower_Z

os.mkdir(in_OutputPath)
out_delta_X = in_OutputPath + "\\" + in_OutputFile + "_X.tif"
out_delta_Z = in_OutputPath + "\\" + in_OutputFile + "_Z.tif"

ras_delta_X.save(out_delta_X)
ras_delta_Z.save(out_delta_Z)


# Process End
print("##### PROCESS END. #####\n")
