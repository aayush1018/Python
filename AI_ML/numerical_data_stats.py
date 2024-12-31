# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:22:39 2024

@author: Aayush
"""

"Numerical Data Stats"

import pandas as pd

pd.options.display.max_rows=10
pd.options.display.float_format = "{:.1f}".format

training_df = pd.read_csv(filepath_or_buffer="https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")

print(training_df.describe())

"""Based on the output
The following columns might contain outliers:

  * total_rooms
  * total_bedrooms
  * population
  * households
  * possibly, median_income

In all of those columns:

  * the standard deviation is almost as high as the mean
  * the delta between 75% and max is much higher than the delta between min and 25%."""