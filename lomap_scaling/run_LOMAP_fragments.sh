#!/bin/bash

echo "Starting loop on fragments.."
i=1
until python lomap_fragments.py 
do
	# run the script until it crashes:
	echo "LOMAP crashed with exit code $?."

	# if we don't have 5 replicates yet, rerun:
	if [ "$i" -lt 6 ]
	then
		let i=i+1
		sleep 1

	# if we do have 5 replicates, exit the loop:
	elif [ "$i" == 6 ]
	then
		echo "Finished the final replicate for these molecules, moving on.."
		break
	fi
done

