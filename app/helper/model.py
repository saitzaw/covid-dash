import numpy as np 

class DeathToll: 
    def __init__(self, daily_death, total_death, status): 
        self.status = status 
        self.daily_death = np.array(daily_death) 
        self.total_death = np.array(total_death) 

    def death_rate(self): 
        if self.status == 'log' :
            log_daily_death = np.log(self.daily_death)
            log_total_death = np.log(self.total_death)
            return (log_daily_death, log_total_death)
        return (self.daily_death, self.total_death)  
 
class InfectionCase: 
    def __init__(self, daily_case, total_case, status):
        self.status = status 
        self.daily_case = np.array(daily_case) 
        self.total_case = np.array(total_case)
        
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
        return (self.daily_death_per_case, self.total_death_per_case)

class RecoveryCase: 
    def __init__(self, daily_recovery, total_recovery, status): 
        self.status = status 
        self.daily_recovery = daily_recovery
        self.total_recovery = total_recovery

    def recovery_case(self): 
        if self.status == 'log':
            log_daily_recovery = np.log(self.daily_recovery) 
            log_total_recovery = np.log(self.total_recovery)
            return (log_daily_recovery, log_total_recovery)
        return (self.daily_recovery, self.total_recovery)

class ReportActiveInformation: 
    def __init__(self, active_infected_patient, active_mild_condition, active_critical):
        self.active_infected_patient = np.array(active_infected_patient)
        self.active_mild_condition = np.array(active_mild_condition) 
        self.active_critical = np.array(active_critical) 

    def percentage(self): 
        #active_total = self.active_infected_patient + self.active_mild_condition + self.active_critical
        return (
                self.active_infected_patient,
                self.active_mild_condition,
                self.active_critical
                )


class ReportInformation: 
    def __init__(self, total_covid_case, total_deaths, total_recovery):
        self.total_covid_case = np.array(total_covid_case) 
        self.total_deaths = np.array(total_deaths) 
        self.total_recovery = np.array(total_recovery) 

    def percentage(self): 
        total = self.total_recovery + self.total_deaths + self.total_covid_case
        return (
                self.total_covid_case/total,
                self.total_deaths/total, 
                self.total_recovery/total
                )



