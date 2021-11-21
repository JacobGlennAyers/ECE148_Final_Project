import numpy as np
import cv2
import time
import sys
import torch
from torchvision import transforms
from PIL import Image
import os

# argv[1] ==> model weights that will be used
# argv[2] ==> path to output text file


# Creating tthe predictions text file

if os.path.exists(sys.argv[2]):
	os.remove(sys.argv[2])


with open(sys.argv[2],'w') as f:
	f.write("start\n")


# Reading from the proper webcam
cap = cv2.VideoCapture(0)
# Reading in the pytorch model passed in by the user
model = torch.load(sys.argv[1])
data_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[.229,.224,.225])
])

class_list = ["JohnLennon","FrankSinatra","None","Beethoven"]
threshold = 0.99
class_prediction = "None"
# Infinite loop
while(True):
	# Reading in a webcam image
	ret, frame = cap.read()
	frame_altered = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	# convert to PIL image
	frame_altered = Image.fromarray(frame_altered)
	# Performing data transformations to tensor
	temp_tensor = data_transform(frame_altered)
	# altering to fit the input of the prediction pipeline (annoying artifict since it expects a batch of data
	# rather than a single datapoint)
	temp_tensor = temp_tensor.unsqueeze(0)
	# Making the prediction
	test_predicts = model(temp_tensor)
	# Finding the index of the highest prediction
	_, pred = torch.max(test_predicts,1)
	# if that prediction is above a threshold, then change the current prediction
	if test_predicts[0][int(pred[0])] >= threshold:
		class_prediction = class_list[int(pred[0])]
		# writing the class prediction to the file
		
		with open(sys.argv[2],'a') as f:
			f.write(class_prediction+'\n')
		
	
	# writing out the prediction to the screen
	cv2.putText(frame,class_prediction,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
        # Displaying the image as well as its prediction
	cv2.imshow('frame',frame)
	
	

	if cv2.waitKey(1) and 0xFF == ord('q'):
		break

	# Slowing down the frame rate to 3Hz
	time.sleep(.333)

cap.release()
cv2.destroyAllWindows()
