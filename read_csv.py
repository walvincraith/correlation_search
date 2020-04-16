import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns

path = r'/Users/calvinwraith/Jupyter/Data/NFL/player_passing' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

correlations = frame.corr(method='pearson')

frame.to_csv(path + "/combined.csv", index = False)
correlations.to_csv(path + "/correlation.csv")

sns.heatmap(correlations)
plt.savefig(path + "/correlation.png")
plt.show()