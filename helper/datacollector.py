import os 
import numpy as np 
import pandas as pd 

file_path = os.path.dirname(__file__)
data_file = os.path.join(file_path,'covid19_data.csv')
virus_data = pd.read_csv(data_file) 
day_list = virus_data['Date'] 

class DeathToll: 
    daily_death = virus_data['daily death']
    total_death = virus_data['total death']
    num_of_death = np.array(daily_death)
    num_of_total_death = np.array(total_death)

class InfectionCase: 
    daily_case = virus_data['dialy case']
    total_case = virus_data['total case']
    num_of_case = np.array(daily_case)
    num_of_total_case = np.array(total_case)
 

