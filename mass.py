import os
import keyboard
from datetime import datetime

print("========================================================= \n",
      "Red Meters Cartridge Trainer ~ Mass 4.0\n",
      "This application WILL SHUT DOWN the device back end while running. Please allow it to completely finish.\n ",
      "If you do not get the 'All done!' message at the end, the back end most likely WAS NOT RESTARTED. \n",
      " In this case, reboot the Red Meter to get the back end working again or DATA WILL NOT BE STORED.\n",
      "========================================================= \n"
      )

cartName = input("ENTER:  Cartridge name: ")



# REWRITE :
#
# dir="/var/lib/rosenimbus/csv/$cname"
#
# if [[ -d $dir ]]
# then
#     echo "A cartridge with this name/serial has already been tested. Re-using cartridge specifications."
#
#     echo ""
# else
#     ./cartridge.sh $cname
# fi

timestamp = datetime.now()
testDir = "$dir/mass_(timestamp)"
diameter = os.system("jq .inner_diameter_in $dir/cartridge.json")
ballsRolled = 0
balls = [67, 1046, 130, 8164, 3, 1807, 28, 226, 4273, 8, 93, 536]
numOfBalls = len(balls)

#REFACTOR
print("Making new test directory...")
os.system("sudo mkdir testDir")

os.system("systemctl stop rosenimbus-backend.service")

for numOfBalls in balls:
      ballDiameter = 1
      ballsRolled = ballsRolled + 1

      if ballDiameter >= diameter:
            print("==============================================\n"
                  "%s / %s Skipping the %s gram ball as it will not fit in cartridge")
            touchFile = testDir / massSizeSkipped
            os.system("touch $touchFile")
print("=========================================================\n")
print(ballsRolled / numOfBalls + "Please use " + mass + "gram ball next...")
print("Roll the ball through the training cartridge three times in the same direction within 30 seconds\n")
print("Press 'Escape' to skip this ball or 'Enter' when you're ready to begin")
while True:
      try:
            if keyboard.is_pressed('esc'):
                  print("Skipping " + mass +"gram ball by user command")
                  break

            if keyboard.is_pressed('enter'):
                  testfile = testDir / mass-g.csv
                  os.system("python /root/DeviceBackend/example/totalreader/totalreader_csv.py -c $testfile 0.01 30 $mass")
                  break
      except:
            break

print("Restarting Device Backend service...")
os.system("systemctl start rosenimbus-backend.service")



