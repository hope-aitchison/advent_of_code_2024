#  Similarity score
#  take the number in the first list x
#  count the number of times it appears in the second list y, and then do xy, where xy is the similarity score
#  take the sum of xy

import pandas as pd # type: ignore
import numpy as np # type: ignore

locations = 'locations_lists.csv'

data = pd.read_csv(locations, header=None, sep='\s+')

locations_array = data.values

list1 = locations_array[:, 0]
list2 = locations_array[:, 1]

# initialise the sum of the similarity score, starting point is 0
sum_score = 0

for item in list1:
    #  count the number of times item appears in list2
    count = np.sum(list2 == item)

    #  multiply item by the count and add to the total sum
    sum_score += item * count

print(sum_score)