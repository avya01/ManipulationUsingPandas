import pandas as pd
import numpy as np
data = {
    "Name" : ["Pankaj", "Meghna", "David", "Lisa"],
    "Role" : ["CEO", np.nan, np.nan, np.nan],
    "Salary" : ["100", "200", np.nan, np.nan]
}

dataframe = pd.DataFrame(data, index = ["Employee1", "Employee2", "Employee3","Employee4"])

print(dataframe)

no_of_nulls = (dataframe.isnull().sum()).sum()

print(no_of_nulls)

data2 = {}

dataframe2 = pd.DataFrame(data2)

dataframe2 = dataframe.dropna()

print(dataframe2)

print(dataframe.fillna(300))