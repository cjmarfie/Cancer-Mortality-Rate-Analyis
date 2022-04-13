# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\cjmar\Downloads\IHME_USA_COUNTY_CANCER_MORTALITY_RATES_1980_2014_ALABAMA_Y2017M01D24.CSV'

df = pd.read_csv(file_path)

print(df)

df2 = df[df["location_name"]=="Alabama"]

print(df2)

for i in df2["location_name"]:
    print(i)
    
   
    
    
plt.figure()
plt.bar(df2["year_id"], df2["mx"])

plt.ylim([250,400])


plt.xlabel("year")
plt.ylabel("mortality rate")
plt.title("Alabama Cancer Mortality Rate 1980-2015")

plt.show()


