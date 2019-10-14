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


echo "Starting loop on druglikes, light.."
i=1
until python lomap_druglikes_light.py 
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

echo "Starting loop on druglikes, heavy.."
i=1
until python lomap_druglikes_heavy.py 
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


echo "Starting loop on bulky.."
i=1
until python lomap_bulky.py 
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