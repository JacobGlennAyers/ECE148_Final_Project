import numpy as np
import cv2
import sys
from datetime import datetime
# initial user input comes in the form of a command line
# where the user enters in a path to the directory of interest.


while(True):
	# take in user input
	user_input = input("Press <Enter> key to take a photo. Press <Ctrl> + <c> to end!")
	if user_input == "":
		cam = cv2.VideoCapture(2)
		result, image = cam.read()
		if result:
			cur_time = datetime.now().strftime("%H%M%S")
			cv2.imwrite(str(sys.argv[1])+cur_time+".jpg", image)
		else:
			print("something went wrong")

