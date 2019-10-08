import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

diffnet_run1 = pd.read_csv("output/diffnet_1.csv", names=["nodes", "time"])
diffnet_run1["Method"] = "DiffNet"
diffnet_run2 = pd.read_csv("output/diffnet_2.csv", names=["nodes", "time"])
diffnet_run2["Method"] = "DiffNet"
diffnet_run3 = pd.read_csv("output/diffnet_3.csv", names=["nodes", "time"])
diffnet_run3["Method"] = "DiffNet"

lomap_druglike_run1 = pd.read_csv("lomap_scaling/output/lomap_druglikes_1.csv", names=["nodes", "time"])
lomap_druglike_run1["Method"] = "LOMAP - Drug-like"
# lomap_druglike_run2 = pd.read_csv("lomap_scaling/output/lomap_druglikes_2.csv", names=["nodes", "time"])
# lomap_druglike_run2["Method"] = "LOMAP - Drug-like"
# lomap_druglike_run3 = pd.read_csv("lomap_scaling/output/lomap_druglikes_3.csv", names=["nodes", "time"])
# lomap_druglike_run3["Method"] = "LOMAP - Drug-like"

lomap_fragment_run1 = pd.read_csv("lomap_scaling/output/lomap_fragment_1.csv", names=["nodes", "time"])
lomap_fragment_run1["Method"] = "LOMAP - Fragments"
# lomap_fragment_run2 = pd.read_csv("lomap_scaling/output/lomap_fragment_2.csv", names=["nodes", "time"])
# lomap_fragment_run2["Method"] = "LOMAP - Fragments"
# lomap_fragment_run3 = pd.read_csv("lomap_scaling/output/lomap_fragment_3.csv", names=["nodes", "time"])
# lomap_fragment_run3["Method"] = "LOMAP - Fragments"

#tmp for unfinished runs:
df = pd.concat([diffnet_run1, diffnet_run2, diffnet_run3, 
				lomap_druglike_run1,
				lomap_fragment_run1, 
				])



# df = pd.concat([diffnet_run1, diffnet_run2, diffnet_run3, 
# 				lomap_druglike_run1, lomap_druglike_run2, lomap_druglike_run3,
# 				lomap_fragment_run1, lomap_fragment_run2, lomap_fragment_run3
# 				])


df["time_mins"] = df["time"] / 60
print(df)



ax = sns.lineplot(x="nodes", y="time_mins", hue="Method", data=df)
ax.set_xlabel("Total nodes in network")
ax.set_ylabel("Unit test runtime (minutes)")

successful_nodes = df["nodes"].values.tolist()
all_treated_nodes = np.arange(2, max(successful_nodes), 1)



plt.savefig("lomap_vs_diffnet.png", dpi=300)

plt.show()