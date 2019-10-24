import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

diffnet_run1 = pd.read_csv("diffnet_scaling/output/diffnet_runtime.csv", names=["nodes", "time"])
diffnet_run1["Method"] = "DiffNet"

diffnet_run2 = pd.read_csv("diffnet_scaling/output/diffnet_sparse_runtime.csv", names=["nodes", "time"])
diffnet_run2["Method"] = "DiffNet - Sparse"

# lomap_druglike_light = pd.read_csv("lomap_scaling/output_cluster/lomap_druglike_light_1.csv", names=["nodes", "time"])
# lomap_druglike_light["Method"] = "LOMAP - Druglike light"

# lomap_druglike_heavy = pd.read_csv("lomap_scaling/output_cluster/lomap_druglike_heavy_1.csv", names=["nodes", "time"])
# lomap_druglike_heavy["Method"] = "LOMAP - Druglike heavy"

# lomap_bulky = pd.read_csv("lomap_scaling/output_cluster/lomap_bulky_1.csv", names=["nodes", "time"])
# lomap_bulky["Method"] = "LOMAP - bulky"

# lomap_fragments = pd.read_csv("lomap_scaling/output_cluster/lomap_fragment_1.csv", names=["nodes", "time"])
# lomap_fragments["Method"] = "LOMAP - fragments"


df = pd.concat([
				diffnet_run1,
				diffnet_run2,
				# lomap_druglike_light,
				# lomap_druglike_heavy,
				# lomap_bulky,
				# lomap_fragments
				])


df["time_mins"] = df["time"] / 60
print(df)



ax = sns.lineplot(x="nodes", y="time_mins", hue="Method", data=df)
ax.set_xlabel("Total nodes in network")
ax.set_ylabel("Unit test runtime (minutes)")

successful_nodes = df["nodes"].values.tolist()
all_treated_nodes = np.arange(2, max(successful_nodes), 1)



plt.savefig("diffnet_types.png", dpi=300)
#plt.savefig("lomap_vs_diffnet.png", dpi=300)

plt.show()