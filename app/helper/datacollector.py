import os 
import numpy as np 
import pandas as pd 
from .model import DeathToll, InfectionCase, DeathInfectionRatio, ReportActiveInformation,  ReportInformation

file_path = os.path.dirname(__file__)
data_file = os.path.join(file_path,'covid19_data.csv')
report_file = os.path.join(file_path,'covid19_report.csv')
countries_file = os.path.join(file_path,'covid19_country.csv')
virus_data = pd.read_csv(data_file) 
report_data = pd.read_csv(report_file)
countries_data = pd.read_csv(countries_file)

class Table: 
    table_data = virus_data.sort_index(ascending=0)
    table_report = report_data.sort_index(ascending=0)
    table_countries = countries_data
        
class Date: 
    date_list = virus_data['Date']

class Death:
    @staticmethod
    def death(status): 
        daily_death = virus_data['daily death']
        total_death = virus_data['total death']
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
        daily_case = virus_data['daily case']
        total_case = virus_data['total case']
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
        death_per_case = None
        try: 
            death_per_case = DeathInfectionRatio(daily_death_per_case,total_death_per_case, status).death_per_infection()
        except ValueError: 
            print ("Something go wrong!...")
        return death_per_case

class Report: 
    #status may be total and active case 
    @staticmethod
    def report(status): 
        if status == 'active': 
            active_infected_patient = report_data['active infected patient']
            active_mild_condition = report_data['active mild condition']
            active_critical = report_data['active critical']
            report_active = None
            try: 
                report_active = ReportActiveInformation(active_infected_patient,active_mild_condition,active_critical).percentage()
            except ValueError: 
                print("Something go wrong!...")
            return report_active 
        
        total_covid_case = report_data['total covid case']
        total_deaths = report_data['total deaths']
        total_recovery = report_data['total recovery']
        report_total = None
        try: 
            report_total = ReportInformation(total_covid_case,total_deaths,total_recovery).percentage()
        except ValueError: 
            print("Something go wrong!...")
        return report_total 
