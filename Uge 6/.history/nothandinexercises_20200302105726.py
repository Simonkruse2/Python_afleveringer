import pandas as pd

# Create a generator function that can 
# take a list of names as parameter 
# and return each name. 
# Get approved unisex names here:

# data = pd.read_csv('https://ast.dk/_namesdb/export/names?format=csv&gendermask=4')
data = pd.read_csv('befkbhalderstatkode.csv')

def whatever():
    generator = data.iterrows()
    for idx,row in generator:
        if idx < 5: #Gets 5 first rows
            print(row,'\n')
        else:
            break
            # raise StopIteration

# whatever()

deezNames = ['Kim', 'Jonna', 'Jim', 'George']

def iterateNames(names):
    for name in names:
        print(name)


def iterateNamesAgain(names):
    num = 0
    while num < len(names):
        yield names
        num += 1

# iterateNames(deezNames)
iterateNamesAgain(deezNames)
    