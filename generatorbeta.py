import numpy as np
import pandas as pd

d = {'one': np.random.randint(0, 2, 5), 'two': np.random.randint(0, 2, 5)}	
df = pd.DataFrame(d, index = ['a', 'b', 'c', 'd', 'e'])
print df.to_json(orient = 'split')
