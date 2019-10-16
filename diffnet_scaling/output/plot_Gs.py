import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("GsMatrix.csv", names=["cdim", "n"])
df_rt = pd.read_csv("diffnet_runtime.csv", names=["Nodes", "Runtime (minutes)"])

df = pd.concat([df, df_rt], axis=1)

print(df)

f, axes = plt.subplots(1, 3)

sns.lineplot(x= "Nodes", y= "Runtime (minutes)", data=df, ax=axes[0])
sns.lineplot(x= "Nodes", y= "cdim", data=df, ax=axes[1])
sns.lineplot(x= "Nodes", y= "n", data=df, ax=axes[2])

plt.tight_layout()
plt.savefig("GsMatrix_plot.png", dpi=300)
plt.show()