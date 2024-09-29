# AI init p4
import numpy as np
import pylab

class Animal(object):
    def __init__(self, name, features):
        self.name = name
        self.features = np.array(features)

    def getName(self):
        return self.name
    
    def getFeatures(self):
        return self.features
    
    def distance(self, other_animal):
        dist=0.0
        if isinstance(other_animal, Animal):
            return np.linalg.norm(self.features - other_animal.features)
        else:
            raise ValueError("Input is not an instance of Animal")


# Creating instances of the Animal class
rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
boa = Animal('boa', [0, 1, 0, 1, 0])
frog = Animal('frog', [1, 0, 1, 0, 1])

def compareAnimals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
       Builds a table of Euclidean distance between each animal"""
    #Get labels for columns and rows
    columnLabels = [animal.getName() for animal in animals]

    rowLabels = columnLabels[:]
    tableVals = []

    #Get distances between pairs of animals
    #For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
        
    pylab.figure(figsize=(15,5))
    #Produce table
    table = pylab.table(rowLabels=rowLabels,
                        colLabels=columnLabels,
                        cellText=tableVals,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.2]*len(animals))
    
    # your code to set table scale (any one appropriate)
    
    # Set the table scale
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.5, 1.5)

    pylab.title('Euclidean Distance Between Animals')
    pylab.show()

# Call the compareAnimals function with the provided animals and precision
compareAnimals([rattlesnake, boa, frog], 2)