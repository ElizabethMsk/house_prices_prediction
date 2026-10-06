import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("train.csv")
print(data.describe().T.sort_values(by="max", ascending=False))
