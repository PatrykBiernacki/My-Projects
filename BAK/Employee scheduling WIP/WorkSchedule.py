import datetime
from collections import defaultdict 

from EmployeeClass import Employee
from WorkLocatons import WorkLocations



class EmployeeSchedule(Employee, WorkLocations):
         
    def __init__(self, employee_list:list, locations:list, start_date:datetime, finish_date:datetime):
        self.employee_list = employee_list
        self.locations = locations
        self.schedule = defaultdict()
        self.start_date = start_date
        self.finish_date = finish_date

    def create_schedule(self):
        for employee in Employee.employee_list:
            if not employee.on_vacation and not employee.sick_leave:
                available_employees.append(employee)
        
        days_to_schedule = self.finish_date - self.start_date
        for day_to_schedule in range(days_to_schedule.days + 1):
            for shift in range(1, 4):  # Assuming 3 shifts per location
                self.schedule = 
                
                
                
        
        for location in self.locations:
            location_schedule = {}
            for shift in range(1, 4):  # Assuming 3 shifts per location
                min_employees = getattr(location, f'shift_{shift}_min_employees')
                nom_employees = getattr(location, f'shift_{shift}_nom_employees')
                employees_assigned = []
                available_employees = [employee for employee in self.employee_list if not employee.on_vacation and not employee.sick_leave]

                if len(available_employees) < min_employees:
                    print(f"Not enough available employees for {location.location_name}, shift {shift}!")
                    break

                if len(available_employees) >= nom_employees:
                    employees_assigned = available_employees[:nom_employees]
                else:
                    employees_assigned = available_employees

                location_schedule[f"Shift {shift}"] = employees_assigned

            self.schedule[location.location_name] = location_schedule

    def display_schedule(self):
        for location, schedule in self.schedule.items():
            print(f"Location: {location}")
            for shift, employees in schedule.items():
                print(f"Shift {shift}:")
                if employees:
                    for employee in employees:
                        print(f" - {employee.first_name} {employee.last_name}")
                else:
                    print("No employees assigned.")
            print()


if __name__ == '__main__':
    employee_list = Employee.read_employee_from_xlsx()
    locations = WorkLocations.read_locations_from_xlsx()

    schedule = EmployeeSchedule(employee_list, locations)
    schedule.create_schedule()
    schedule.display_schedule()