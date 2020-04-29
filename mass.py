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
dir = "/var/lib/rosenimbus/csv/" + cartName
if os.path.isfile(dir):
      print("A cartridge with this name/serial has already been tested. Re-using cartridge specifications.")

#     else: ????
#     ./cartridge.sh $cname
else:
      exec(open('cartridge.py').read())


timestamp = datetime.now()
testDir = str(dir + "/mass_" + timestamp)
diameter = os.system("jq .inner_diameter_in $dir/cartridge.json")
ballsRolled = 0
balls = [67, 1046, 130, 8164, 3, 1807, 28, 226, 4273, 8, 93, 536]
numOfBalls = len(balls)


#REFACTOR
print("Making new test directory...")
os.system("sudo mkdir " + testDir)

os.system("systemctl stop rosenimbus-backend.service")


# How are we to evaluate mass?
# NEED: Testing code cleaned up and insight, please advise
# Lines with mass in for loop need revision and elaboration

for numOfBalls in balls:
      ballDiameter = 1
      ballsRolled = ballsRolled + 1

      if ballDiameter >= diameter:
            print("==============================================\n",
                  ballsRolled + " / " + numOfBalls +  "Skipping the" + mass +  "gram ball as it will not fit in cartridge")
            touchFile = testDir + ' / ' + massSizeSkipped
            os.system("touch $touchFile")
print("=========================================================\n")
print(ballsRolled / numOfBalls + "Please use " + mass + "gram ball next...")
print("Roll the ball through the training cartridge three times in the same direction within 30 seconds\n")
print("Press 'Escape' to skip this ball or 'Enter' when you're ready to begin")
while True:
      try:
            if keyboard.is_pressed('esc'):
                  print("Skipping " + balls + " gram ball by user command")
                  break

            if keyboard.is_pressed('enter'):
                  testfile = testDir / mass-g.csv #Need: Help Here
                  os.system("python /root/DeviceBackend/example/totalreader/totalreader_csv.py -c" + testfile + " 0.01 30 " + mass)
                  numOfBalls = numOfBalls - 1
                  break
      except:
            break

print("Restarting Device Backend service...")
os.system("systemctl start rosenimbus-backend.service")



