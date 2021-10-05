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
                        break
                    
                    if (dic['username'] == input_username) and (dic['code'][0] == 'A'):
                        #print(dic,'admin')
                        return 'admin'
                        break
                    
                    if (dic['username'] == input_username) and (dic['code'][0] == 'T'):
                        #print(dic,'teacher')
                        return 'teacher'
                        break
                
                    
        
class Admin:
    def __init__(self,subject,teacher,unit):
        self.subject = subject
        self.teacher = teacher
        self.unit = unit
        
    def add_subject_data(self):
        fields = ['subject','teacher','unit']
        
        data = [{'subject':self.subject,'teacher':self.teacher,'unit':self.unit}]
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
    

#obj = User()
#print(obj.check_login('sara','123'))