import hashlib
import random
import csv
from tkinter import messagebox
import logging
import pandas as pd


logging.basicConfig(level=logging.INFO, filename='loging.log', filemode='a')
class User:
    count = 1
    def __init__(self,username=None, password=None):
        self.username = username
        if password != None:
            self.password = hashlib.sha256(password.encode()).hexdigest()
        
      
   
    

    def add_to_file(self,code):
        fields = ['username','password','code','subjects']
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
                    
        data = [{'username':self.username,'password':self.password,'code':code,'subjects':''}]
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
                else:
                    messagebox.showerror(title='error',message='the password or username does not match')
                    logging.info(f'{username} is failed to log in.')
                    
                    
            
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
    
    def choose_sub(self):
        list_data = []
        try:
            with open('subjects-data.csv','r') as data:
                reader = csv.DictReader(data)
                for row in reader:
                    subject = row['subject']
                    unit = row['unit']
                    teacher = row['teacher']
                    if teacher == '':
                        list_data.append(subject) 
                return tuple(list_data)
            
                
        except FileNotFoundError:
            messagebox.showerror(title='error',message='the current data is not availble!')
            
    def update_file(self, subject_name ,teacher_name):
        all_unit = 0
        flag = 0
        df = pd.read_csv('subjects-data.csv')
        with open('subjects-data.csv','r') as data:
                reader = csv.DictReader(data)
                sub_data = list(reader)
                for dic in sub_data:
                    if dic['teacher'] == teacher_name:
                        all_unit += int(dic['unit'])
                    for subject in subject_name:
                        if dic['subject'] == subject:
                            all_unit += int(dic['unit'])
                            
                for dic2 in sub_data:
                    for subject2 in subject_name:
                        if dic2['subject'] == subject2:
                            if 10 <= all_unit <= 15:
                                df.loc[sub_data.index(dic2),'teacher'] = teacher_name
                                df.to_csv("subjects-data.csv", index=False)
                                messagebox.showinfo(title='successful',message='subject added successfully!!')
                            else:
                                messagebox.showerror(title='error',message='you choos more than 15 units or less than 10 units!!')
                                flag = 1
                                break
                    if flag == 1:
                        break
    
    def choose_sub12(self,subjects,student_name,s_code=None):
        #student get subjects and data add to file
        all_unit = 0
        df = pd.read_csv('subjects-data.csv')
        with open('subjects-data.csv','r') as data:
                reader = csv.DictReader(data)
                sub_data = list(reader)
                for dic in sub_data:
                    for sub in subjects:
                        if dic['subject'] == sub:
                            all_unit += int(dic['unit'])
                            capacity = int(dic['capacity']) - 1
                            df.loc[sub_data.index(dic),'capacity'] = capacity
                            df.to_csv("subjects-data.csv", index=False)
                            
        
        self.s_code = s_code
        fields = ['student_name','code','subjects']
        try:
            with open('university-data.csv','r') as file:
                reader = csv.DictReader(file)
                data_list = list(reader)
                for dic in data_list:
                    if dic['username'] == student_name:
                        self.s_code = dic['code'] 
            
        except FileNotFoundError:
            messagebox.showerror(title='error',message='no such data exist yet!')
        
        data = [{'student_name':student_name,'code':self.s_code,'subjects':subjects}]
        if 10 <= all_unit <= 20:
            with open('studentsub-data.csv','a') as f:
                writer = csv.DictWriter(f, fieldnames =fields,lineterminator='\n')
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerows(data)
                messagebox.showinfo(title='successful',message='subject added successfully!!')
        else:
            messagebox.showerror(title='error',message='you choos more than 20 units or less than 10 units!!')
            
    def choose_sub13(self):
        list_data = []
        try:
            with open('subjects-data.csv','r') as data:
                reader = csv.DictReader(data)
                for row in reader:
                    subject = row['subject']
                    unit = row['unit']
                    teacher = row['teacher']
                    list_data.append(subject) 
                return tuple(list_data)
        
        except FileNotFoundError:
            messagebox.showerror(title='error',message='no such data exist yet!')
    def get_tree_data14(self):
        list_data = []
        try:
            with open('studentsub-data.csv','r') as data:
                reader = csv.DictReader(data,delimiter=',')
                for row in reader:
                    subjects = row['subjects']
                    name = row['student_name']
                    
                    list_data.append([name,subjects]) 
                return list_data
                
        except FileNotFoundError:
            messagebox.showerror(title='error',message='the current data is not availble!')
            
    def search_num_name(self,inputs):
        list_data = []
        with open('university-data.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (row['username'] == inputs) or (row['code']== inputs):
                    name = row['username']
                    code = row['code']
                    subject = row['subjects']
                    
                    list_data.append([name,code,subject])
                    
                return list_data
    def show_student(self):
        list_data = []
        with open('university-data.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if  (row['code'][0]== 'S'):
                    name = row['username']
                    code = row['code']
                    
                    
                    list_data.append([name,code])
                    
            return list_data
    
        
                    
            
            
            
        
                        
                    
        
            
            
        
    
                
                    
        
class Admin:
    counter = 1
    def __init__(self,subject=None,teacher=None,unit=None,capacity=None):
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
            logging.info(f'{self.subject} is added.')
            
    def accept(self,name):
        df = pd.read_csv('university-data.csv')
        with open('studentsub-data.csv','r') as f:
           reader1 = csv.DictReader(f)
           sub_data1 = list(reader1)
           for dic in sub_data1:
                if dic['student_name'] == name:
                    with open('university-data.csv','r') as file:
                        reader2 = csv.DictReader(file)
                        sub_data2 = list(reader2)
                        for dic2 in sub_data2:
                            if dic2['username'] == name:
                                df.loc[sub_data2.index(dic2),'subjects'] = dic['subjects']
                                df.to_csv("university-data.csv", index=False)
                             
                                messagebox.showinfo(title='successful',message='subject added successfully!!')
                                logging.info(f'{name} subject is accept.')
                                
                            
    def deny(self,name):
        df = pd.read_csv('subjects-data.csv')
        with open('studentsub-data.csv','r') as data:
            reader = csv.DictReader(data)
            sub_data = list(reader)
            for dic in sub_data:
                s = dic['subjects']
                name_dic = dic['student_name']
                convert_list = s.strip('][').split(', ')
                
                with open('subjects-data.csv','r') as file:
                    reader2 = csv.DictReader(file)
                    sub_data2 = list(reader2)
                    for dic2 in sub_data2:
                        for sub in convert_list:
                            sub2 = sub.split("'")
                            if dic2['subject'] == sub2[1] and name_dic == name :
                                capacity = int(dic2['capacity']) + 1
                                df.loc[sub_data2.index(dic2),'capacity'] = capacity
                                df.to_csv("subjects-data.csv", index=False)
                                
                    messagebox.showinfo(title='successful',message='deny successfully!!')
                    logging.info(f'{name} subject is denyed.')
                    break
                
                                        
                                        
    def search_by_sub(self,sub_name):
        list_data = []
        sub_data = []
        with open('university-data.csv','r') as file:
            reader = csv.DictReader(file)
            list_reader = list(reader)
            for dic in list_reader:
                a = dic['subjects']
                if a:
                    convert_list = a.strip('][').split(', ')
                    for sub in convert_list:
                        sub2 = sub.split("'")
                        if sub2[1] == sub_name:
                           name = dic['username']
                           code = dic['code']
                           list_data.append([name,code])
                    
                     
            return list_data
        
class Teacher:
    @staticmethod
    def search_by_sub2(sub_name):
        list_data = []
        sub_data = []
        with open('university-data.csv','r') as file:
            reader = csv.DictReader(file)
            list_reader = list(reader)
            for dic in list_reader:
                a = dic['subjects']
                if a:
                    convert_list = a.strip('][').split(', ')
                    for sub in convert_list:
                        sub2 = sub.split("'")
                        if sub2[1] == sub_name:
                           name = dic['username']
                           code = dic['code']
                           list_data.append([name,code])
                    
                     
            return list_data
            
        
                                        
                                            
                                   
                                
        
                                
                                
                                
                                
            
            
        
        
        
          
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

def len_file():
    with open('studentsub-data.csv','r') as f:
        reader = csv.DictReader(f)
        data_list = list(reader)
        len_data = len(data_list)
        return len_data
def get_name():
    names = []
    with open('studentsub-data.csv','r') as f:
        reader = csv.DictReader(f)
        data_list = list(reader)
        for dic in data_list:
            names.append(dic['student_name'])
        return names
def get_sub():
    subjects = []
    with open('studentsub-data.csv','r') as f:
        reader = csv.DictReader(f)
        data_list = list(reader)
        for dic in data_list:
            subjects.append(dic['subjects'])
        return subjects
            
    




#obj = Admin()
#print(obj.search_by_sub('math'))
#print(a[1][0])