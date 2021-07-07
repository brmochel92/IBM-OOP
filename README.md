# IBM-OOP

___

![](https://img.shields.io/badge/BackEnd-Python-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=5F7FF6)

___

## Intro

Custom classes are an important feature of Python and necessary for OOP.  In this file, we are creating two custom objects

```
class  SSR(object):
    # counter for total number of SSR instances
    ssr_counter = 0
    def __init__(self, first, last, employee_serial, specialization, band_level, pay, employment_length):
        self.first = first
        self.last = last
        self.employee_serial = employee_serial 
        self.specialization = specialization
        self.band_level = band_level
        self.pay = pay
        self.employment_length = employment_length  
        # Adds 1 to the counter for every instance of the object     
        SSR.ssr_counter +=1

    def ssr_dataframe(self):
        return {'First Name': self.first, 'Last Name': self.last, 'Employee_Serial': self.employee_serial, 'Specialization': self.specialization, 'Band Level': self.band_level, 'Pay': self.pay, 'Employment Length': self.employment_length}
        
class Division:
    
    def __init__(self, division, max_employees):
        self.division = division
        self.max_employees = max_employees
        self.employees = []
    division_counter = 0   

    # A class method to add new employees to division per rules business logic
    def add_employee_division(self, employee):
        if len(self.employees) <  self.max_employees:
            self.employees.append(employee)
            return True 
        return False
        # Adds 1 to the counter for every instance of the object 
        Division.division_counter +=1

    def division_dataframe(self):
        return {'Division': self.division, 'Employees': self.employees, 'Max Employees': self.max_employees}
```
