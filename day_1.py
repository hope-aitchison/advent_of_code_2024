import pandas as pd # type: ignore
import numpy as np # type: ignore

locations = 'locations_lists.csv'

data = pd.read_csv(locations, header=None, sep='\s+')

locations_array = data.values

list1 = locations_array[:, 0]
list2 = locations_array[:, 1]

list1_sorted = np.sort(list1)
list2_sorted = np.sort(list2)

difference = np.abs(list1_sorted - list2_sorted)

print(sum(difference))


