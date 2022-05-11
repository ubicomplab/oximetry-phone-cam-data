from unittest import skip
from matplotlib import path
import pandas as pd
from pathlib import Path
import numpy as np
import torch

procLoc = './/data//ppg-csv' # processed data location
procDir = Path.home().joinpath(Path.cwd().parent,procLoc)
patientNums = np.arange(100001,100007,1)

# Function to add header to the processed data
# Load the original csv, add RGB header, and write back to the original csv file
def add_Header():
    for i in ['Left/', 'Right/']:
        for j in patientNums:
            path_to_file = Path.joinpath(procDir, i, str(j) + '.csv')
            print(path_to_file)

            data_without_label = np.loadtxt(path_to_file)
            df = pd.DataFrame(data_without_label, columns = ['R', 'G', 'B'])
            df.to_csv(path_to_file, index=False)

# some demo to load tensor from the csv file
path_to_file = Path.joinpath(procDir, 'Left/' + str(patientNums[0]) + '.csv')
data = torch.tensor(np.genfromtxt(path_to_file, delimiter=',',skip_header=1).transpose())