import hashlib
import random
import csv
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.INFO, filename='loging.log', filemode='a')
class User:
    count = 1
    def __init__(self,username=None, password=None):
        self.username = username
        if password != None:
            self.password = hashlib.sha256(password.encode()).hexdigest()
        
      
   
    

    def add_to_file(self,code):
        fields = ['username','password','code']
        try:
            with open('university-data.csv','r') as file:
                reader = csv.DictReader(file)
                data_list = list(reader)
                for dic in data_list:
                    if dic['username'] == self.username:
                        self.username = self.username + str(User.count) 
            User.count +=1
        except FileNotFoundError:
            messagebox.showerror(title='error',message='no such data exist yet so add your info anyway!')
                    
        data = [{'username':self.username,'password':self.password,'code':code}]
        with open('university-data.csv','a') as f:
            writer = csv.DictWriter(f, fieldnames =fields,lineterminator='\n')
            if f.tell() == 0:
                writer.writeheader()
           
            writer.writerows(data)
            logging.info(f'{self.username} is registered.')
            
    def check_login(self,username,password):
        try:
            with open('university-data.csv','r') as file:
                reader2 = csv.DictReader(file)
                data_list2 = list(reader2)
                idx2 = 0 #index
                lines_Data2 = {}
                list_dic2 = []
                for dic2 in data_list2:
                    lines_Data2[str(idx2)] = dic2   # syntax to assign key value to dict
                    idx2 = idx2 + 1  
                
                for key2 in lines_Data2:
                    list_dic2.append(lines_Data2[key2])
                    
                for dic3 in data_list2:
                    if (dic3['username'] == username) and (dic3['password'] == hashlib.sha256(password.encode()).hexdigest()):
                        return True
                    
            
        except FileNotFoundError:
            messagebox.showerror(title='error',message='no such data exist yet!')
            
            
            
    def check_position(self,input_username):
         with open('university-data.csv','r') as file:
                reader = csv.DictReader(file)
                data_list = list(reader)
                idx = 0 #index
                lines_Data = {}
                list_dic = []
                for dic in data_list:
                    lines_Data[str(idx)] = dic   # syntax to assign key value to dict
                    idx = idx + 1  
                
                for key in lines_Data:
                    list_dic.append(lines_Data[key])
        
                for dic in list_dic:
                    if (dic['username'] == input_username) and (dic['code'][0] == 'S'):
                        #print(dic,'student')
                        return 'student'
                        
                        
                    if (dic['username'] == input_username) and (dic['code'][0] == 'A'):
                        #print(dic,'admin')
                        return 'admin'
                        
                    if (dic['username'] == input_username) and (dic['code'][0] == 'T'):
                        #print(dic,'teacher')
                        return 'teacher'
                        
                        
                        
    def get_tree_data(self):
        list_data = []
        try:
            with open('subjects-data.csv','r') as data:
                reader = csv.DictReader(data,delimiter=',')
                for row in reader:
                    subject = row['subject']
                    unit = row['unit']
                    teacher = row['teacher']
                    capacity = row['capacity']
                    list_data.append([subject,unit,teacher,capacity]) 
                return list_data
                
        except FileNotFoundError:
            messagebox.showerror(title='error',message='the current data is not availble!')
            
        
    
                
                    
        
class Admin:
    counter = 1
    def __init__(self,subject,teacher,unit,capacity):
        self.subject = subject
        self.teacher = teacher
        self.unit = unit
        self.capacity = capacity
        
    def add_subject_data(self):
        fields = ['subject','teacher','unit','capacity']
        try:
            with open('subjects-data.csv','r') as file:
                reader = csv.DictReader(file)
                data_list = list(reader)
                for dic in data_list:
                    if dic['subject'] == self.subject:
                        self.subject = self.subject + str(Admin.counter) 
            Admin.counter +=1
        except FileNotFoundError:
            messagebox.showinfo(title='file error',message='no such data exist yet so add your info anyway!')
            
       
        
        data = [{'subject':self.subject,'teacher':self.teacher,'unit':self.unit,'capacity':self.capacity}]
        with open('subjects-data.csv','a') as f:
            writer = csv.DictWriter(f, fieldnames =fields ,lineterminator='\n')
            if f.tell() == 0:
                writer.writeheader()
           
            writer.writerows(data) 
        
        
          
#==============================Functions======================================
def code_generator(username,password,repit_pass,position):
    
    code_generator = random.randint(10000000, 99999999)
    if (username and password and repit_pass and position):
            if password == repit_pass:
                if position == 'teacher':
                    code = 'T'+str(code_generator)
                elif position == 'admin':
                    code = 'A'+str(code_generator)
                else:
                    code = 'S'+str(code_generator)
                    
                    
                obj = User(username,password)
                obj.add_to_file(code)
                messagebox.showinfo(title='successful',message = [code,obj.username])
                
            else:
                 messagebox.showerror(title='Not match', message='the repited password is not match')
    else:
          messagebox.showerror(title='empty', message='no data to add')
    
def num_subject_data():
    number_1 = 0
    number_2 = 0
    number_3 = 0
    number_4 = 0
    all_unit = 0
    
    
    try:
        with open('subjects-data.csv','r') as data:
            reader = csv.DictReader(data)
            data = list(reader)
            for unit in data:
                if unit['unit'] == '1':
                    number_1 += 1
                    all_unit += 1
                    
                elif unit['unit'] == '2':
                    number_2 += 1
                    all_unit +=2
              
                elif unit['unit'] == '3':
                    number_3 += 1
                    all_unit +=3
                    
                else:
                    number_4 += 1
                    all_unit += 4
                   
                    
                    
    except FileNotFoundError:
        messagebox.showerror(title='error',message='the current data is not availble!') 
        
        
    all_sub = number_1 + number_2 + number_3 + number_4  
    return [number_1,number_2,number_3,number_4,all_unit,all_sub] 




#obj = User()
#a = obj.get_tree_data()
#print(a[0])