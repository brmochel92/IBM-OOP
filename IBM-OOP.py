import pandas as pd;

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

# Instances of Custom SSR object 
ssr1 = SSR("Brandon", "Mochel", "4J4122", "Power Systems", 4, 45000, 23)
ssr2 = SSR("Melisa", "Mochel", "4J4123", "System X", 2, 38000, 12)
ssr3 = SSR ("Blake", "Birch", "4J4358", "Lenovo PCD", 1, 35000, 4)

# Print Total number of SSR at IBM 
print("There are", SSR.ssr_counter, "SSRs working at IBM.")

# Print out dictionary of each SSR instance 
print(ssr1.__dict__)
print(ssr2.__dict__)
print(ssr3.__dict__)

# add instances to list
ssr_list = [ssr1, ssr2, ssr3]

# Convert SSR Object to Dataframe (DF) using Pandas Library 
df = pd.DataFrame([x.ssr_dataframe() for x in ssr_list])
print(df)

print(df.tail(1))

# Instance of Division Object 
division1 = Division("GTS", 500)
division2 = Division("TSS", 300)

# Adding SSR instances to Division Object
division1.add_employee_division(ssr1)
division1.add_employee_division(ssr2)
division2.add_employee_division(ssr3)

# add instances to list
division_list = [division1, division2]

# Convert Division Object to Dataframe (DF) using Pandas Library 
df2 = pd.DataFrame([x.division_dataframe() for x in division_list])
print(df2)

print(df2.tail(1))