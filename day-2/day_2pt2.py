#  Test if a report satifies the original rule
#  If not, iterate through each element of the report, remove it
#  Check if after the removal, the report then satisfies the filters

import pandas as pd # type: ignore
import numpy as np # type: ignore


reports_file = 'reports.csv'

# data = pd.read_csv(reports_file, header=None, sep='\s+')
data = pd.read_csv('input.csv', header=None)
print(data)

#  validation function
def original_filters(report):

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

    return is_monotonic & valid_difference

#  removing one level (element)
def is_safe_with_removal(report):

    #  iterate over each index in the report array
    for level in range(len(report)):
        
        # temporarily remove each level
        reduced_report = np.delete(report, level)
        if original_filters(reduced_report):
            return True
    return False

# combined function to determine if a report is safe
def is_a_report_safe(report):

    #  drop the NaN values & convert to NumPy array
    report = report.dropna().values

    # check if full report is safe
    if original_filters(report):
        return True
    
    #  check if removing an element makes it safe
    return is_safe_with_removal(report)


#  apply the function across all rows (reports) in the dataframe
safe_reports = data.apply(is_a_report_safe, axis=1)

# sum the number of safe reports
number_of_safe_reports = safe_reports.sum()

print(f"The number of safe reports is: {number_of_safe_reports}")