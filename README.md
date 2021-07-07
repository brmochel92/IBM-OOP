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
