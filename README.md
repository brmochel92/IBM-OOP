# IBM-OOP

___

![](https://img.shields.io/badge/BackEnd-Python-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=5F7FF6)

___

## Intro

Custom classes are an important feature of Python and necessary for OOP.  In this file, we are creating two custom objects necessary for further operations. 

# SSR Class (IBM job role)

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
        
```
Here you can see the SSR object is being initialized with several attributes, such as first name, last name, etc.  There is a counter method within the class object that we can call upon anytime to calculate the total number of SSR's working at IBM at any given time.  

# Division Class (IBM Divisions)

```
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

The basic idea behind this object is to be able to use some business logic to determine max amount of employees/SSR allowed in each division and to add SSR to the Division object.  After the initialization, we can call the add_employee_division method, which will allow us to add employees to whichever Division Object we want.  

# Dataframes with Pandas

## SSR Object
```
First Name Last Name Employee_Serial Specialization  Band Level    Pay  Employment Length
0    Brandon    Mochel          4J4122  Power Systems           4  45000                 23
1     Melisa    Mochel          4J4123       System X           2  38000                 12
2      Blake     Birch          4J4358     Lenovo PCD           1  35000                  4
```
## Division Object
### Notice the object being printed out within each Division Instance (GTS/TSS) - Success!
```
  Division                                          Employees  Max Employees
0      GTS  [<__main__.SSR object at 0x000001406FBD0610>, ...            500
1      TSS      [<__main__.SSR object at 0x000001406FBD05B0>]            300
```
