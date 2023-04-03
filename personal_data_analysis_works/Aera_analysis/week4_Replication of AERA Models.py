# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:05:29 2023

@author: nicho
"""

# Import the libraries we'll need
import pandas as pd
import numpy as np

"""never name a gender variable gender, because if we generate dummy, it needs to be 0 or 1, which is female or male."""
# Import data
data = pd.read_csv(r"C:\Users\DanielS\Desktop\Modern Data Structure_MDS\GitHub_Clone\QMSS-GR5072_Spring2023_HWs\Class Activities\Week 4\els_extracted_data_v4.csv")
data

# Filter data
data = data[data.F3ERN2011 > 0]
data = data[data.F3ERN2011 < 200000]
data = data[data.F3C02 >= 0]
data = data[data.F3JUNEDSTAT >= 3]
data = data[data.BYS14 >= 0]
data = data[data.BYRACE >= 0]
data = data[data.BYTXCSTD >= 0]
data = data[data.F3REGION >= 0]
data = data[data.BYP61 >= -0.25]
data = data[data.BYMOTHED >= 0]
data = data[data.BYTXCSTD >= 0]
data = data[data.F3B35 >= 0]

# Explore soe of data here if you need to
data.BYTXCSTD.hist()

# look at modified data
data

# Create dummies for BYSEX
data["female"] = (data["BYS14"] ==2).astype(int)

# Check that this method is working by crosstabing the results
pd.crosstab(index=data['BYS14'], columns=data['female'])
"""
# Now that we have verified the code above works for greating dichotomus dummy variables, 
# we can use this same method to safely create the remaining variables.

# For variables which have more than 2 categories, we can use pd.get_dummies()

# Create dummies for BYP61


# Create dummies for BYMOTHED

# Create dummies for F3REGION

# Create dummies for high_school_grad

# Create dummies for F3EVRGED

# Create dummies for BYRACE2, which uses the same coding scheme used for race/ethnicity in the paper

# Check your work!


# Once you've check your work, now make dummies


# note that this produces prettier print! But it does take up more space


# Since the dummies are good, we need to add them to our dataset


# Recode highest education into years of education 

# See final dataset
data

# Model 1
import statsmodels.api as sm  # library for estimating regression models

# Define the formula for the model1
formula = 'np.log(F3ERN2011) ~ ged + high_school_grad + female + Black + Hispanic + Asian + Other + BYSES1 + no_parent + BYTXCSTD'

# Fit the multilevel model using the formula
model = sm.MixedLM.from_formula(formula, data, groups=data["SCH_ID"])
result = model.fit()

# Print the summary of the model
print(result.summary())

# model 2
# Define the formula for the model 2
formula = 'np.log(F3ERN2011) ~ ged + high_school_grad + female + Black + Hispanic + Asian + Other + BYSES1 + no_parent + BYTXCSTD  + F3B35 + post_sec_edu'

# Fit the multilevel model using the formula
model = sm.MixedLM.from_formula(formula, data, groups=data["SCH_ID"])
result = model.fit()

# Print the summary of the model
print(result.summary())

# Create dummies for F3EVRGED
data["GEDT"] = (data["F3EVRGED"]*data["BYTXCSTD"]).astype(int)

# model 3
# Define the formula for the model 3
formula = 'np.log(F3ERN2011) ~ ged + high_school_grad + female + Black + Hispanic + Asian + Other + BYSES1 + no_parent + BYTXCSTD  + GEDT'

# Fit the multilevel model using the formula
model = sm.MixedLM.from_formula(formula, data, groups=data["SCH_ID"])
result = model.fit()

# Print the summary of the model
print(result.summary())
"""