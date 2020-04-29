from mainPage import cartName
import os
from datetime import datetime
import json

cartName = cartName
diameter = input("ENTER:  Inner-Diameter of the cartridge (inches): ")
length = input("ENTER:  Length of the cartridge (inches): ")
wraps = input("IF: carbon fiber, enter the number of ply/wraps. For Rubber, Enter: 0 ... : ")

dir = "/var/lib/rosenimbus/csv/" + cartName
checkDir = os.path.isdir(dir)

if os.path.isfile(dir):
    print("A cartridge with this name has already been tested... Re-using cartridge specs")

# IF: carbon fiber...
if wraps != 0:
    print("This is a Carbon Fiber Cartridge...Entering Carbon Fiber Selection...\n")
    cureAmbient = input("ENTER: Cure time at ambient temperature in minutes: ")
    cureBaked = input("ENTER: Post-cure time at 160°F in minutes: ")
    linerType = input("ENTER: Liner Type --> 1 for Gum Rubber, 2 for Neoprene, 3 for Nitrile")
    if linerType == "1":
        print("Liner Type: Gum Rubber")
        # linerType = gumRubber
    if linerType == "2":
        print("Liner Type: Neoprene")
        # linerType = neoprene
    if linerType == "3":
        print("Liner Type: Nitrile")
        # linerType = nitrile

    #IF: pipe is carbon fiber, THEN: Resin type is LAM-135
    resinType = 'LAM-135'

# Rubber Cartridge
if wraps == 0:
    cureAmbient = 0
    cureBaked = 0
    linerType = 0

# echo "Writing calibration and cartridge data..."
print("Writing calibration and cartridge data...")

# mkdir $dir
os.system("mkdir " + dir)

#Call API for pressure and DV
print("\n=========================================================\n"
      "*** DV ***\n")
os.system("curl -s http://127.0.0.1:5000/calibration/sensor_linear/active/data/dv/meter | \jq '.'")

print("\n=========================================================\n"
      "*** Pressure ***\n")
os.system("curl -s http://127.0.0.1:5000/calibration/sensor_linear/active/data/pressure/psi | \jq '.'")

# HOW TO : Write this....
# iCureAmbient=$(expr $cureAmbient + 0)
# iCureBaked=$(expr $cureBaked + 0)
# iDiameter=$(expr $diameter + 0)
# iLength=$(expr $length + 0)
# iPly=$(expr $wraps + 0)
# iRType=$(expr $resinType + 0)
# iLType=$(expr $liner_type + 0)

iTimestamp = datetime.now()
iCureAmbient = cureAmbient + 0
iCureBaked = cureBaked + 0
iDiameter = diameter + 0
iLength = length + 0
iPly = wraps + 0
iRtype = resinType + 0
iLType = linerType + 0

# cartridge='{\"inner_diameter_in\": $iDiameter, \"length_in\": $iLength, \"ply\": $iPly, \"cure_time_ambient_min\": $iCureAmbient, \"post_cure_time_min\": $iCureBaked, \"resin_type\": $iRType,
#  \"liner_type\": $iLType, \"recorded_at\": $tstamp }'

cartridge = '{ "inner_diameter_in" : "iDiameter", "length_in" : "iLength", "ply" : "iPly", ' \
            '"cure_time_ambient" : "iCureAmbient", ' \
            '"post_cure_time_min" : "iCureBaked", "resin_type" : "iRType",' \
            '"liner_type" : "iLType", "recorded_at" : "iTimestamp"}'
