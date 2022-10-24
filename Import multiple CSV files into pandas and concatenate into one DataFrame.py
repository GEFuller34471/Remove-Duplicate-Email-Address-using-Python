import pandas as pd
import glob
import os

# Get data file names
path = r'Datafiles' # use your path
all_files = glob.glob(os.path.join(path , "/*.csv"))

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)