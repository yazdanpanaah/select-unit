import hashlib
import random
import csv
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.INFO, filename='loging.log', filemode='a')
class Register:
    count = 1
    def __init__(self,username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
      
    
    def add_to_file(self,code):
        fields = ['username','password','code']
        try:
            with open('university-data.csv','r') as file:
                reader = csv.DictReader(file)
                data_list = list(reader)
                for dic in data_list:
                    if dic['username'] == self.username:
                        self.username = self.username + str(Register.count) 
            Register.count +=1
        except FileNotFoundError:
            messagebox.showerror(title='error',message='no such data exist yet so add your info anyway!')
                    
        data = [{'username':self.username,'password':self.password,'code':code}]
        with open('university-data.csv','a') as f:
            writer = csv.DictWriter(f, fieldnames =fields ,lineterminator='\n')
            if f.tell() == 0:
                writer.writeheader()
           
            writer.writerows(data)
            logging.info(f'{self.username} is registered.')
    def check_login(self,username,password):
        try:
            with open('university-data.csv','r') as file:
                reader = csv.DictReader(file)
                data_list = list(reader)
                for dic in data_list:
                    if dic['username'] == username and dic['password'] == hashlib.sha256(password.encode()).hexdigest():
                        return True
                    else:
                        return False
            
        except FileNotFoundError:
            messagebox.showerror(title='error',message='no such data exist yet!')
        
class Admin:
    def __init__(self,subject,teacher,unit):
        self.subject = subject
        self.teacher = teacher
        self.unit = unit
    def add_data(self):
        fields = ['subject','teacher','unit']
        
        data = [{'subject':self.subject,'teacher':self.teacher,'unit':self.unit}]
        with open('subjects-data.csv','a') as f:
            writer = csv.DictWriter(f, fieldnames =fields ,lineterminator='\n')
            if f.tell() == 0:
                writer.writeheader()
           
            writer.writerows(data) 
        
        
          

    

