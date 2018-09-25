# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:05:34 2018

@author: Michael
"""

class Employee:
    
    employee_count = 0
    bonus = 1.05
    
    def __init__(self, first_name, last_name, tenure, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.tenure = tenure
        self.salary = salary
        self.email = first_name[0] + '.' + last_name + '@dundermifflin.com'
        
        Employee.employee_count += 1
        
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def bonus_pay(self):
        self.new_salary = int(self.salary * self.bonus) 
        return self.new_salary
    
    def tenure_bonus(self):
        if self.tenure >= 5:
            self.bonus = self.bonus + 0.01
            
    @classmethod
    def adjust_bonus(cls, amount):
        cls.bonus = amount 
    
    @classmethod
    def from_string(cls, empSTR):
        first_name, last_name, tenure, salary = empSTR.split('-')
        return cls(first_name, last_name, int(tenure), int(salary))
    
    @staticmethod
    def is_TacoTuesday(day):
        if day.weekday() == 1:
            return True
        else:
            return False

class Manager(Employee):
    bonus = 1.125
        
empA = Employee('Jim', 'Halpert', 3, 25000)
empB = Employee('Dwight', 'Schrute', 7, 28000)
empC = Manager('Michael', 'Scott', 11, 45000)

print empA.fullname()
print empA.email    
print empA.tenure
print empA.salary
print empA.bonus_pay()
print 'Dunder Mifflin has ' + str(Employee.employee_count) + ' employees'

Employee.adjust_bonus(1.075)
print empA.bonus_pay()

empSTR_A = 'Pam-Beesly-2-21000'
empD = Employee.from_string(empSTR_A)
print empD.fullname()
print empD.email
print empD.bonus_pay()

import datetime
random_date = datetime.date(2018, 11, 20)

print Employee.is_TacoTuesday(random_date)

print empC.email
print empC.salary
print empC.bonus_pay()

print empB.salary
print empB.bonus_pay()
empB.tenure_bonus()
print empB.bonus_pay()





