import os
from random import sample 
import shutil



druglike_light = []
for file in os.listdir("druglike_light/"):
    if file.endswith(".sdf"):
    	druglike_light.append(file)

for i in range(len(druglike_light)+1):
	# make the directories:
	path = "druglike_light/chunks/c"
	os.makedirs(path+str(i), exist_ok=True)
	
	# randomly sample from the available sdf files:
	selected = sample(druglike_light, i)

	# copy the sampled files to each chunk folder:
	for file in selected:
		destination_path = path+str(i)+"/"+file
		shutil.copyfile("druglike_light/"+file, destination_path)

druglike_heavy = []
for file in os.listdir("druglike_heavy/"):
    if file.endswith(".sdf"):
    	druglike_heavy.append(file)

for i in range(len(druglike_heavy)+1):
	# make the directories:
	path = "druglike_heavy/chunks/c"
	os.makedirs(path+str(i), exist_ok=True)
	
	# randomly sample from the available sdf files:
	selected = sample(druglike_heavy, i)

	# copy the sampled files to each chunk folder:
	for file in selected:
		destination_path = path+str(i)+"/"+file
		shutil.copyfile("druglike_heavy/"+file, destination_path)

bulky = []
for file in os.listdir("bulky/"):
    if file.endswith(".sdf"):
    	bulky.append(file)


for i in range(len(bulky)+1):
	# make the directories:
	path = "bulky/chunks/c"
	os.makedirs(path+str(i), exist_ok=True)
	
	# randomly sample from the available sdf files:
	selected = sample(bulky, i)

	# copy the sampled files to each chunk folder:
	for file in selected:
		destination_path = path+str(i)+"/"+file
		shutil.copyfile("bulky/"+file, destination_path)



fragments = []
for file in os.listdir("fragments/"):
    if file.endswith(".sdf"):
    	fragments.append(file)

for i in range(len(fragments)+1):
	# make the directories:
	path = "fragments/chunks/c"
	os.makedirs(path+str(i), exist_ok=True)
	
	# randomly sample from the available sdf files:
	selected = sample(fragments, i)

	# copy the sampled files to each chunk folder:
	for file in selected:
		destination_path = path+str(i)+"/"+file
		shutil.copyfile("fragments/"+file, destination_path)