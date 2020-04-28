import os
from datetime import datetime

#start Device Backend
os.system("source /opt/rosenimbus-backend/bin/activate")

print("=========================================================\n"
      "Red Meters Cartridge Trainer ~ Temperature and Pressure\n"
      "This application WILL SHUT DOWN the device back end while running. Please allow it to completely finish.\n"
      "If you do not get the 'All done!' message at the end, the back end most likely WAS NOT RESTARTED.\n"
      "In this case, reboot the Red Meter to get the back end working again or DATA WILL NOT BE STORED.\n"
      "=========================================================\n")

cartName = input("Enter a name for the cartridge")
dir = "/var/lib/rosenimbus/csv/" + cartName

#this logic probably doesn't work
if os.path.isfile(dir):
    print("A cartridge with this name/serial has already been tested. Re-using cartridge specifications")

#TEST
os.system("./cartridge.sh " + dir)
timestamp = datetime.now()
testDir = dir + 'temp_pressure_' + timestamp
os.system("sudo mkdir " + testDir)
os.system("source /opt/rosenimbus-backend/bin/activate")
os.system("systemctl stop rosenimbus-backend.service")

print("ALL done!")
