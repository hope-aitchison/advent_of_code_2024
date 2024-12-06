# identify the safe reports
# safe reports are either gradually increasing or decreasing
# gradual means levels are increasing by 1 or at most 3
# they must only be increasing or decreasing 
# how many reports are safe?

import pandas as pd # type: ignore
import numpy as np # type: ignore


reports_file = 'reports.csv'

# data = pd.read_csv(reports_file, header=None, sep='\s+')
data = pd.read_csv('input.csv', header=None)

#  validation function
def is_valid(report):

    #  drop the NaN values
    report = report.dropna()

    #  covnvert to a NumPy array for filters
    report = report.values

    #  calculate differences between elements (levels)
    differences = np.diff(report)

    #  check monotonicity
    is_increasing = np.all(differences > 0)
    is_decreasing = np.all(differences < 0)

    #  combine results
    is_monotonic = is_increasing or is_decreasing

    #  check differences between adjacent values
    valid_difference = np.all((abs(differences) >=1) & (abs(differences) <=3))
    # print(valid_difference)

    result = is_monotonic & valid_difference

    #  the report is valid only if both conditions are metß
    return result

# # filtered_reports = data[data.apply(is_valid, axis=1)]
filtered_reports = data.apply(is_valid, axis=1)
safe_reports = filtered_reports.sum()
print(f"The number of safe reports is: {safe_reports}")