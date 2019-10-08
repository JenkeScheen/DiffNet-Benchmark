import pandas as pd 
import pubchempy as pcp 
import csv

# read pre-imported pubchem file to retrieve cids:
druglike = pd.read_csv("drug-like.csv")
drug_cids = druglike["cid"].values

# use pubchempy to retrieve canonical smiles per cid:
druglike_smiles = []
for cid in drug_cids:
	mol = pcp.Compound.from_cid(str(cid))
	mol_dict = mol.to_dict(properties=["canonical_smiles"])
	for k, v in mol_dict.items():
		druglike_smiles.append(v)
		print(v)

# save to smiles file:
with open("drug-like.smi", "w") as file:
	writer = csv.writer(file)
	for row in druglike_smiles:
		writer.writerow([row])

##############
## repeat for fragments:

# read pre-imported pubchem file to retrieve cids:
druglike = pd.read_csv("fragments.csv")
drug_cids = druglike["cid"].values

# use pubchempy to retrieve canonical smiles per cid:
druglike_smiles = []
for cid in drug_cids:
	mol = pcp.Compound.from_cid(str(cid))
	mol_dict = mol.to_dict(properties=["canonical_smiles"])
	for k, v in mol_dict.items():
		druglike_smiles.append(v)
		print(v)

# save to smiles file:
with open("fragments.smi", "w") as file:
	writer = csv.writer(file)
	for row in druglike_smiles:
		writer.writerow([row])