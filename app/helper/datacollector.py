import os 
import numpy as np 
import pandas as pd 
from .model import DeathToll, InfectionCase, DeathInfectionRatio

file_path = os.path.dirname(__file__)
data_file = os.path.join(file_path,'covid19_data.csv')
virus_data = pd.read_csv(data_file) 

class Date: 
    date_list = virus_data['Date']

class Death:
    @staticmethod
    def death(status): 
        daily_death = np.array(virus_data['daily death'])
        total_death = np.array(virus_data['total death'])  
        death_toll = None 
        try:   
            death_toll = DeathToll(daily_death, total_death,status).death_rate()
            print(list(death_toll))
        except ValueError: 
            print("Something go wrong!...")
        return death_toll 
    
class Case: 
    @staticmethod
    def case(status): 
        daily_case = np.array(virus_data['daily case'])
        total_case = np.array(virus_data['total case'])
        infection_case = None 
        try:
            infection_case = InfectionCase(daily_case, total_case, status).case_rate()
        except ValueError: 
            print("Something go wrong!...")
        return infection_case

class Rate:
    @staticmethod 
    def rate(status):
        daily_death = np.array(virus_data['daily death'])
        total_death = np.array(virus_data['total death']) 
        daily_case = np.array(virus_data['daily case'])
        total_case = np.array(virus_data['total case'])
        daily_death_per_case = daily_death/daily_case * 100 
        total_death_per_case = total_death/total_case * 100 
        try: 
            death_per_case = DeathInfectionRatio(daily_death_per_case,total_death_per_case, status)
        except ValueError: 
            print ("Something go wrong!...")
        return death_per_case
