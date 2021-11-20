import numpy as np
from cv2 import *
import sys
from datetime import datetime
# initial user input comes in the form of a command line
# where the user enters in a path to the directory of interest.


while(True):
	# take in user input
	user_input = input("Press <Enter> key to take a photo. Press <Ctrl> + <c> to end!")
	if user_input == "":
		cam = VideoCapture(1)
		result, image = cam.read()
		if result:
			cur_time = datetime.now().strftime("%H%M%S")
			imwrite(str(sys.argv[1])+cur_time+".jpg", image)
		else:
			print("something went wrong")

