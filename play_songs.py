import subprocess
import time
import os, random

#print(random.choice(os.listdir("../songs/JohnLennon/")))

song_dir = "../songs/"
text_file = "../predictions1.txt"
# function that runs a background process to play the relevant mp3
# returns the process so that you can shut it down at a designated time.
def play_mp3(path):
	return subprocess.Popen(['mpg123', '-q',path+random.choice(os.listdir(path))])
#f1 = open(text_file,"r")
#folder = f1.readlines()[-1]
#folder = folder[:-1] + '/'
#process1 = play_mp3(song_dir+folder)
#time.sleep(5)
#process1.terminate()
#f1.close()

# brainstorm how to kill the process in a while loop. 
# initializing the process in outer scope so that we can fail safe it
process = None

artist = ""
prev_artist = "start/"
while(artist != "end"):
	# reading the file the prediction script rights to
	f1 = open(text_file,"r")
	# Reading in the last line of the file, which is the most recent musician prediction
	artist = f1.readlines()[-1]
	# setting it up for an eventual path
	artist = artist[:-1]+'/'
	# closing the text file
	f1.close()
	# The case where a change has been detected
	if (prev_artist != artist):
		prev_artist = artist
		# Ending the prior song, while handling the case of the first song
		if process is not None:
			process.terminate()
		
		process = play_mp3(song_dir+artist)
		musician_change = False


# fail safe
process.terminate()




#process1 = play_mp3(path)
#time.sleep(5)
#process1.terminate()
#process2 = play_mp3(path)
#time.sleep(5)
#process2.terminate()

#path = "../songs/JohnLennon/JohnLennon0.mp3"
#time.sleep(10)
#process1.terminate()

#process2 = play_mp3(path)
#time.sleep(5)
#process2.terminate()
