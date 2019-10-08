import lomap
import os
import re
import time

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


# generate all directory paths (for all the different chunk sizes):

chunks_path = "input/druglike/chunks/"
paths = os.listdir(chunks_path)

whole_paths = []
for path in paths:
	whole_paths.append(chunks_path+path)

# sort them so we iterate over chunk sizes in the right order:
whole_paths.sort(key=natural_keys)

i = 2
for path in whole_paths:
	start = time.time()
	# run lomap on this chunk:
	db_mol = lomap.DBMolecules(path)
	db_mol.build_matrices()
	nx_graph = db_mol.build_graph() 

	end = time.time()
	elapsed = (end - start)
	print("Took", str(elapsed), "seconds to generate a graph for", str(i), "nodes.")
	row = str(i)+","+str(elapsed)+"\n"
	with open("output/lomap_druglikes_1.csv", "a") as myfile:
		myfile.write(row)
	i +=1