import numpy as np 

class DeathToll: 
    def __init__(self, daily_death, total_death, status): 
        self.status = status 
        self.daily_death = daily_death 
        self.total_death = total_death 

    def death_rate(self): 
        if self.status == 'log' :
            log_daily_death = np.log(self.daily_death)
            log_total_death = np.log(self.total_death)
            return (log_daily_death, log_total_death)
        return (self.daily_death, self.total_death)  
 
class InfectionCase: 
    def __init__(self, daily_case, total_case, status):
        self.status = status 
        self.daily_case = daily_case 
        self.total_case = total_case
        
    def case_rate(self): 
        if self.status == 'log': 
            log_daily_case = np.log(self.daily_case)
            log_total_case = np.log(self.total_case)
            return (log_daily_case, log_total_case)
        return (self.daily_case, self.total_case)

class DeathInfectionRatio: 
    def __init__(self, daily_death_per_case, total_death_per_case, status):  
        self.status = status         
        self.daily_death_per_case = daily_death_per_case
        self.total_death_per_case = total_death_per_case
    def death_per_infection(self):
        if self.status == 'log': 
            log_daily_death_per_infection = np.log(self.daily_death_per_case)
            log_total_death_per_infection = np.log(self.total_death_per_case)
            return (log_daily_death_per_infection, log_total_death_per_infection)
        return (self.total_death_per_case, self.total_death_per_case)

