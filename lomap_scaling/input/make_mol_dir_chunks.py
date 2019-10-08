import os
from random import sample 
import shutil



druglikes = []
for file in os.listdir("druglike/mol2"):
    if file.endswith(".mol2"):
    	druglikes.append(file)

for i in range(len(druglikes)+1):
	# make the directories:
	path = "druglike/chunks/c"
	os.makedirs(path+str(i), exist_ok=True)
	
	# randomly sample from the available sdf files:
	selected = sample(druglikes, i)

	# copy the sampled files to each chunk folder:
	for file in selected:
		destination_path = path+str(i)+"/"+file
		shutil.copyfile("druglike/mol2/"+file, destination_path)




fragments = []
for file in os.listdir("fragments/mol2"):
    if file.endswith(".mol2"):
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
		shutil.copyfile("fragments/mol2/"+file, destination_path)