import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




print(df.describe())


print(df.corr())


colormap = plt.cm.gist_heat
plt.figure(figsize=(12, 12))
plt.hist(x=[df.plasma[df.diabetes == 0], df.plasma[df.diabetes == 1]], bins=30, histtype='barstacked', label=['nomal', 'dia'] )