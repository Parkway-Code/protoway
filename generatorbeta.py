import numpy as np
import pandas as pd
import sys

class garage:
    def __init__(self, ver, size=0, floor_count=0, size_per_floor=0):
        self.ver = ver
        self.per_fill = np.random.randint(0, 100, 1)
        self.size = size
        
        if(ver == 0):
            filler = []
            for i in range(0, floor_count):
                tmp = np.random.randint(0,2,size_per_floor)
                filler.append(tmp)
            self.model = pd.DataFrame(filler)
        elif(ver == 1):
            self.count = np.random.randint(0, size, 1)
            self.model = pd.DataFrame([self.count, self.size], columns = ["Occupancy", "Size"])
        elif(ver == 2):
            self.model = pd.Dataframe([self.per_fill, self.size], columns = ["Percentage", "Size"])
        elif(ver == 3):
            filler = []
            for i in range(0, floor_count):
                filler.append(np.random.randint(0, size_per_floor, 1))
            self.model = pd.DataFrame(filler)


mtype = sys.argv[1] 
d = {'one': np.random.randint(0, 2, 5), 'two': np.random.randint(0, 2, 5)}	
df = pd.DataFrame(d, index = ['a', 'b', 'c', 'd', 'e'])
a = garage(0, size_per_floor=40, floor_count=4)
print(a.model)
print (df.to_json(orient = 'split'))
