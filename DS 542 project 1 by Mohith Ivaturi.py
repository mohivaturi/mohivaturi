#!/usr/bin/env python
# coding: utf-8

# # # DS-542 Summer 2023
# 
# # Project 1
# 
# # Mohith Ivaturi
# 

# In[2]:


#Importing pandas Libraries
import pandas as pd


# In[3]:


#Loading the data set
waterplant_data = pd.read_csv(r"https://data.cityofnewyork.us/api/views/ia2d-e54m/rows.csv?accessType=DOWNLOAD")


# In[4]:


#Importing numpy libraties for mathematical functions
import numpy as np


# In[5]:


#Assigning coloums lo a variable
years = waterplant_data['Year']
water_consumption = waterplant_data['NYC Consumption(Million gallons per day)']
population = waterplant_data['New York City Population']
per_capita = waterplant_data['Per Capita(Gallons per person per day)']


# In[6]:


#Years to Decades converstion
decade_consumption = {}

for i in range(len(years)):
    year = years[i]
    value = water_consumption[i]
    decade = int(year // 10) * 10
    
#Loading the values in the comsumption by decade dictionary     
    if decade in decade_consumption:
        decade_consumption[decade].append(value)
    else:
        decade_consumption[decade] = [value]


# In[7]:


# 1. Mean water consumption by decade
decade_mean_consumptions = {}

for decade in range(1970,2030,10):    
    decade_mean_consumptions[f'{decade}s'] = np.mean(decade_consumption[decade])

print("Mean :",decade_mean_consumptions)


# In[9]:


#2. Median water consumption in the 1990s
decade_median_consumptions = {}

for decade in range(1990, 2000):
     decade_median_consumptions[decade] = np.median(decade_consumption[1990])
    
print("Median:",decade_median_consumptions)


# In[37]:


#3.Analyzing water consumption per capita trends
previous_year_per_capita = per_capita[0]

#Taking index value of 1 for the current year
for i in range(1, len(years)):
    current_year_per_capita = per_capita[i]
    
    if current_year_per_capita > previous_year_per_capita:
        print(f"{years[i-1]} to {years[i]} increased")
    elif current_year_per_capita < previous_year_per_capita:
        print(f"{years[i-1]} to {years[i]} decreased")
    else:
        print(f"{years[i-1]} to {years[i]} is same")

    previous_year_per_capita = current_year_per_capita


# In[12]:


#4.The total cost per of water processing per decade
#As my first name starts with M 
cost_per_decade_A_M = {
    '1970s': 7.1,
    '1980s': 3.2,
    '1990s': 5.4,
    '2000s': 6.7,
    '2010s': 9.6,
    '2020s': 4.5
}

total_cost_per_decade = {}

for decade in cost_per_decade_A_M:
    total_cost_per_decade[decade] = decade_mean_consumptions[decade] * cost_per_decade_A_M[decade]

print(total_cost_per_decade)


# In[42]:


#5a. Plotting the population over each year

import matplotlib.pyplot as plt
plt.plot(years, population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population over Each Year')
plt.grid(True, color='black', linestyle='-', linewidth=0.8)
plt.show()



# In[41]:


#5b. Plotting the total water consumption over each year
plt.plot(years,water_consumption)
plt.xlabel('Year')
plt.ylabel('water_consumption')
plt.title('Total Water Consumption over Each Year')
plt.grid(True,color = 'black', linestyle = '-',linewidth=0.8)
plt.show()


# In[ ]:




