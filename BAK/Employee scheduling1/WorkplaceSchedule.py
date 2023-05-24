from collections import defaultdict 

from EmployeeClass import Employee
from WorkLocatons import WorkLocations


class WorkplaceSchedule():
    
    def __init__(self, location_name:str, location_address:str, shift1_schedule:list, shift2_schedule:list, shift3_schedule:list) -> None:
        self.location_name = location_name
        self.location_address = location_address
        
        self.shift_schedule = {'shift1': shift1_schedule, 'shift2': shift2_schedule, 'shift3': shift3_schedule}

    @classmethod
    def create_schedules(cls) ->list:
        """Creates schedules for WorkLocations for shift1, shift2 and shift3 populated with Employees. 
        Reads WorkLocations from 'locations.xlsx' and Employees from 'employees_data.xlsx'."""
        cls.defined_schedules = []
        cls.defined_employees = cls.define_available_employees()
        for work_location in WorkLocations.read_locations_from_xlsx():
            cls.defined_schedules.append(cls.schedule_min_for_one_location(cls, work_location, cls.defined_employees))
        for work_location in WorkLocations.read_locations_from_xlsx():
            cls.defined_schedules.append(cls.schedule_nom_for_one_location(cls, work_location, cls.defined_employees))
                      
        return cls.defined_schedules


    def schedule_min_for_one_location(self, work_location:list, available_employees:list) -> isinstance:
        """Creates instance of work schedule for WorkLocation and populates with minimal number of Emploees"""
        self.work_schedule = WorkplaceSchedule(work_location.location_name, work_location.location_address, shift1_schedule = [], shift2_schedule = [], shift3_schedule = [])
          
        for shift_no, min_employees_in_shift in enumerate((work_location.shift_1_min_employees, work_location.shift_2_min_employees, work_location.shift_3_min_employees,), start = 1):
            shift_employees = []
            while len(shift_employees) < min_employees_in_shift and len(available_employees) > 0:
                print('before!!', work_location.location_name, 'shift employees:', len(shift_employees), 'available employees:', len(available_employees))
                shift_employees.append(available_employees.pop())
                print('after!!', work_location.location_name, 'shift employees:', len(shift_employees), 'available employees:', len(available_employees))
            self.work_schedule.shift_schedule[f'shift{shift_no}'] = shift_employees.copy()
            if len(available_employees) == 0:
                return self.work_schedule
        
        return self.work_schedule    
            
    def schedule_nom_for_one_location(self, work_location:list, available_employees:list) -> isinstance:  
        """Populates already existing work schedules with nominal number of Emploees"""      
        for shift_no, nom_employees_in_shift in enumerate((work_location.shift_1_nom_employees, work_location.shift_2_nom_employees, work_location.shift_3_nom_employees,), start = 1):
            shift_employees = []
            while len(shift_employees) < nom_employees_in_shift and len(available_employees) > 0:
                shift_employees.append(available_employees.pop())

            self.work_schedule.shift_schedule[f'shift{shift_no}'].extend(shift_employees.copy())
            if len(available_employees) == 0:
                return self.work_schedule
            
        return self.work_schedule
            
    """Pytanie do Marcina. Nieważne czy dam work_schedule czy self.work_schedule - wynik jest ten sam. Po co dawać self?            <---------------------------------"""
    
                    
    def show_work_schedule(self) :
        "Displays work schedule"
        print(f'\nAssigned employees to {self.location_name} at {self.location_address}.')
        print ('\nFor shift 1:')
        for employee in self.shift_schedule['shift1']:
            employee.employee_info()
        print ('\nFor shift 2:')
        for employee in self.shift_schedule['shift2']:
            employee.employee_info()
        print ('\nFor shift 3:')
        for employee in self.shift_schedule['shift3']:
            employee.employee_info()
  
    @classmethod
    def define_available_employees(cls) ->list:
        """Returns list of employees that are available for shifts, by removing employees on sick leave and on vacation."""
        cls.available_employees = []
        for employee in Employee.read_employee_from_xlsx():
            if not employee.on_vacation and not employee.sick_leave:
                cls.available_employees.append(employee)
        return cls.available_employees
          
if __name__ == '__main__':
    WorkplaceSchedule.create_schedules()
    for schedule in WorkplaceSchedule.defined_schedules:
        print(f'Schedule for {schedule.location_name}, at {schedule.location_address}')
        schedule.show_work_schedule()



