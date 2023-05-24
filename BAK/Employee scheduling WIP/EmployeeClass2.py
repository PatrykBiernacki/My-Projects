import datetime
import os

import openpyxl

class Employee:
    
    employee_list = []
   
    def __init__(self, employee_id:int, first_name:str, last_name:str, middle_name:str, born_date:datetime, employee_gender:str,
                 home_address:str, sick_leave:bool, on_vacation:bool, last_shift:datetime  ) -> None:
        
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.born_date = born_date
        self.employee_gender = employee_gender
        self.home_address = home_address 
        self.sick_leave = sick_leave
        self.on_vacation = on_vacation
        self.last_shift = last_shift


    @classmethod
    def read_employee_from_xlsx(cls) -> list:                  
        """Reads employees from excel file and add them to employee_list."""
        try:            
            employee_list_file = openpyxl.load_workbook('employees_data.xlsx')
            sheet_active = employee_list_file.active

            for row in sheet_active.iter_rows(min_row = 2, values_only = True):
                employee = cls(*row)
                cls.employee_list.append(employee)
            return cls.employee_list
        except Exception as e:
            print('Employees data file not found or improper format.', e)
            

    def employee_info(self) -> None:
        true_tuple = (True, 'True', 'true', 'Yes', 'yes', 'Y', 'y')
        print(f"""{'Mr.' if self.employee_gender == 'male' else 'Ms.'} {self.first_name} {self.middle_name} {self.last_name},
        was born on {self.born_date.strftime('%d-%m-%Y')}. Lives in {self.home_address}.""")
        print(f"{'He' if self.employee_gender == 'male' else 'She'} is currently \
              {'on sick leave' if self.sick_leave in true_tuple else 'on vacation' if self.on_vacation in true_tuple else 'available for work.'}")

"""
    @property
    def employee_id(self) -> int:
        return self.employee_id


    @employee_id.setter
    def employee_id(self, employee_id:int) -> None:
        self.employee_id = employee_id
       

    @property
    def employee_name(self) -> tuple:
        return (self.first_name, self.middle_name, self.last_name)


    @employee_name.setter
    def employee_name(self, first_name:str, last_name:str, middle_name:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name


    @property
    def born_date(self) -> datetime:
        return self.born_date


    @born_date.setter
    def born_date(self, born_date:str) -> None:
          self.born_date = datetime.datetime.strptime(born_date)


    @property
    def employee_gender(self) -> str:
        return self.employee_gender
    

    @employee_gender.setter
    def employee_gender(self, employee_gender:str) -> None:
        if employee_gender.lower() in ('male', 'female'):
            self.employee_gender = employee_gender.lower()
        else:
            self.employee_gender = 'female' 


    @property
    def home_address(self) -> dict:
        return self.home_address


    @home_address.setter
    def home_address(self, city:str, postal_code:str, street:str, building:str, apartment:str) ->dict:
        self.home_address = {'city': city, 'postal code' : postal_code, 'street': street, 'building': building, 'apartment': apartment}


    def show_home_address(self) -> None:
        print(f"{self.home_address.get('city', '')} {self.home_address.get('postal code', '')}  ")
        print(f"{self.home_address.get('street', '')} {self.home_address.get('building', '')}/{self.home_address.get('apartment', '')}")
        

    @property
    def sick_leave(self) -> str:
        return self.sick_leave
    
    
    @sick_leave.setter
    def sick_leave(self, sick_leave:str) -> None:
          self.sick_leave = sick_leave


    @property
    def on_vacation(self) -> str:
        return self.on_vacation
    
    
    @on_vacation.setter
    def on_vacation(self, on_vacation:str) -> None:
          self.on_vacation = on_vacation


    @property
    def last_shift(self) -> str:
        return self.last_shift
    
    
    @last_shift.setter
    def last_shift(self, last_shift:int) -> None:
        if last_shift in (1, 2, 3):
            self.last_shift = last_shift
        else:
            self.last_shift = 1
"""

if __name__ == '__main__':
    Employee.read_employee_from_xlsx()
    for employee in Employee.employee_list:
        Employee.employee_info(employee)