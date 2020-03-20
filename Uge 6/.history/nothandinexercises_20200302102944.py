import pandas as pd

# Create a generator function that can 
# take a list of names as parameter 
# and return each name. 
# Get approved unisex names here:

data = pd.read_csv(https://ast.dk/_namesdb/export/names?format=xls&gendermask=4')

def whatever():
    generator = data.iterrows()
    for idx,row in generator:
        if idx < 4:
            print(row,'\n')

whatever()