from mass import cartName
import os

cartName = cartName
diameter = input("ENTER:  Inner-Diameter of the cartridge (inches): ")
length = input("ENTER:  Length of the cartridge (inches): ")
wraps = input("IF: carbon fiber, enter the number of ply/wraps. For Rubber, Enter: 0 ... : ")

dir = "/var/lib/rosenimbus/csv/" + cartName
checkDir = os.path.isdir(dir)

if os.path.isfile(dir):
      print("A cartridge with this name has already been tested... Re-using cartridge specs")

#IF: carbon fiber...
if wraps != 0:
      print("This is a Carbon Fiber Cartridge...Entering Carbon Fiber Selection...\n")
      cureAmbient = input("ENTER: Cure time at ambient temperature in minutes: ")
      cureBaked = input("ENTER: Post-cure time at 160°F in minutes: ")
      linerType = input("ENTER: Liner Type --> 1 for Gum Rubber, 2 for Neoprene, 3 for Nitrile")
      if linerType == "1":
            print("Liner Type: Gum Rubber")
            #linerType = gumRubber
      if linerType == "2":
            print("Liner Type: Neoprene")
            #linerType = neoprene
      if linerType == "3":
            print("Liner Type: Nitrile")
            #linerType = nitrile

if wraps == 0:
    cureAmbient = 0
    cureBaked = 0
    linerType = 0

# echo "Writing calibration and cartridge data..."
print("Writing calibration and cartridge data...")
#
#
# mkdir $dir
os.system("mkdir " + dir)
#
# echo ""
#
# echo "========================================================="
# echo " *** DV ***"
# curl -s http://127.0.0.1:5000/calibration/sensor_linear/active/data/dv/meter | \jq '.'
os.system("curl -s http://127.0.0.1:5000/calibration/sensor_linear/active/data/dv/meter | \jq '.'")
# echo "========================================================="
# echo " *** Pressure ***"
# curl -s http://127.0.0.1:5000/calibration/sensor_linear/active/data/pressure/psi | \jq '.'
os.system("curl -s http://127.0.0.1:5000/calibration/sensor_linear/active/data/pressure/psi | \jq '.'")
# echo "========================================================="

# HOW TO : Write this....
# cartridge="{\"inner_diameter_in\": $iDiameter, \"length_in\": $iLength, \"ply\": $iPly, \"cure_time_ambient_min\": $iCureAmbient, \"post_cure_time_min\": $iCureBaked, \"resin_type\": $iRType,
# \"liner_type\": $iLType, \"recorded_at\": $tstamp }"