import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolAlign, rdDepictor, rdmolfiles, rdmolops

import csv

files = [["drug-like.smi", "druglike"],["fragments.smi", "fragments"]]


for moltype in files:
	mols = []
	with open(moltype[0], "r") as file:
		reader = csv.reader(file)
		for row in reader:
			try:

				mol = Chem.rdmolfiles.MolFromSmiles(row[0])

				# remove fragments, make 2d coords:
				molecules = rdmolops.GetMolFrags(mol, asMols = True)
				mol = max(molecules, default=mol, key=lambda m: m.GetNumAtoms())
				AllChem.Compute2DCoords(mol)

				num_atoms = mol.GetNumAtoms()
				mols.append([mol, num_atoms])
			except:
				pass

	largest_mol = sorted(mols, key = lambda x: x[1])[-1][0]
	Chem.rdmolfiles.MolToMolFile(largest_mol, moltype[1]+"/largest_mol")

	i=1
	for mol in mols:
		#molblock = Chem.MolToMolBlock(mol[0])
		path = moltype[1]+"/"+str(i)+".sdf"

		Chem.rdmolfiles.MolToMolFile(mol[0], path)
		i+=1
		