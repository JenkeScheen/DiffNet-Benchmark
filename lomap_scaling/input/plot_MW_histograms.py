import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolAlign, rdDepictor, rdmolfiles, rdmolops
import csv 
import numpy as np 
import matplotlib.image as mpimg


def distplot_with_hue(data=None, x=None, hue=None, row=None, col=None, legend=True, **kwargs):
    _, bins = np.histogram(data[x].dropna())
    g = sns.FacetGrid(data, hue=hue, row=row, col=col, height=2, aspect=5)
    g.map(sns.distplot, x, **kwargs)
    if legend and (hue is not None) and (hue not in [x, row, col]):
        g.add_legend(title=hue) 


files = [
		["drug-like_light.smi", "druglike_light"],
		["drug-like_heavy.smi", "druglike_heavy"],
		["bulky.smi", "bulky"],
		["fragments.smi", "fragments"]
		]

MW_compiled_df = pd.DataFrame()

for moltype in files:
	weights = []


	with open(moltype[0], "r") as file:
		reader = csv.reader(file)
		for row in reader:
			try:
				mol = Chem.rdmolfiles.MolFromSmiles(row[0])
				weight = Descriptors.ExactMolWt(mol)
				weights.append(weight)
			# some smi lines are incorrect, skip them:
			except:
				pass

	weights_df = pd.DataFrame(weights, columns=["MW"])
	weights_df["collection"] = moltype[1]
	MW_compiled_df = pd.concat([MW_compiled_df, weights_df])

distplot_with_hue(
				data=MW_compiled_df,
				x="MW",
				hue="collection",
				hist=False,
				legend=False,
				)

# # remove left y axis:
cur_axes = plt.gca()
cur_axes.axes.get_yaxis().set_visible(False)
sns.despine(left=True)

# annotate:

plt.annotate(ha="center", s="Fragments", xy=(150, 0.0045))
plt.annotate(ha="center", s="Druglike - light", xy=(330, 0.01))
plt.annotate(ha="center", s="Druglike - heavy", xy=(550, 0.005))
plt.annotate(ha="center", s="Bulky", xy=(800, 0.005))

plt.xlabel(r"Molecular mass [g$\cdot$mol$^{-1}$]")



plt.ylim(0, 0.01)
plt.xlim(0, 1000)
plt.savefig("input_molecules_mass_histogram.png", dpi=300)
plt.show()