from tkinter import Tk, Label, Button, Entry, Frame ,ttk  ,END,StringVar,NO,CENTER
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import backend as bc
import random
import csv



#==============================MainMenu======================================
class ProgramGui:
    def __init__(self):
        #main screen
        self.main_win = Tk()
        self.main_win.title('select unit')
        self.main_win.minsize(800, 500)
        
        #backgrond iamges
        self.image2=tk.PhotoImage(file='main-bg.png')
        w = self.image2.width()
        h = self.image2.height()
        self.main_win.geometry('%dx%d+0+0'%(w,h))
        lab1=Label(self.main_win, image=self.image2)
        lab1.place(x=0,y=0,relwidth=1,relheight=1)
    
        #buttons images
        self.register_img=tk.PhotoImage(file='register.png')
        self.login_img=tk.PhotoImage(file='login.png')
        self.exit_img=tk.PhotoImage(file='exit.png')
        
    
        #buttons
        b1 = tk.Button(self.main_win, image=self.register_img,bd=0,highlightthickness=0, command = self.register)
        b1.image = self.register_img
        b2 = tk.Button(self.main_win, image=self.login_img , command = self.login_menu)
        b2.image = self.login_img
        b3 = tk.Button(self.main_win, image=self.exit_img,command=self.exit_program)
        b3.image=self.exit_img
        
        #place them in bg
        b1.place(x=130,y=160)
        b2.place(x=130,y=250)
        b3.place(x=200,y=420)
        
    def mainloop(self):
        #to show the gui window
        self.main_win.mainloop()
        
    def exit_program(self):
        self.main_win.destroy()
        
        
    def back_to_main(self):
        #back to the main menu
        self.register_win.destroy()
        obj2=ProgramGui()
        obj2.mainloop()
       
    def back_to_main2(self):
        #back to the main menu
        self.login_win1.destroy()
        obj2=ProgramGui()
        obj2.mainloop()
        
    def back_to_win1(self):
        #back to the main menu
        self.register_win.destroy()
        obj3 = ProgramGui()
        obj3.mainloop()
       
   
    def register(self):
        self.main_win.destroy()
        self.register_win=register_win=Tk()
        register_win.geometry("500x500")
        register_win.title("Login")
        register_win.configure(bg="royalblue3")
        
        #labels
        l_title=Label(register_win,text="Register",relief="raised",fg="white",bg="black", width=20)
        l_title.config(font=("Courier","30","bold"))
        l_title.place(x=10, y=0)
        l1=Label(register_win,text="Enter Name:",bg='white', font=('',10, 'bold'))
        l1.place(x=200,y=80)
        l2=Label(register_win,text="Enter your password:",bg='white', font=('',10, 'bold'))
        l2.place(x=175,y=160)
        l3=Label(register_win,text="Enter your password again:",bg='white', font=('',10, 'bold'))
        l3.place(x=150,y=240)
        
        
        #combobox
        # label
        combo_lab = ttk.Label(register_win, text = "Select your position :",font = ("Times New Roman", 10))
        combo_lab.place(x=70,y=320)
        
          
        # Combobox creation
        self.position = tk.StringVar()
        positionchoosen = ttk.Combobox(register_win, width = 27, textvariable = self.position)
          
        # Adding combobox drop down list
        positionchoosen['values'] = ('teacher','admin','student')
        
        positionchoosen.place(x=220,y=320)
        positionchoosen.current()
                
        #set user input in a varieble
        self.username = StringVar()
        self.password = StringVar()
        self.repit_pass = StringVar()
        
    
            
        #Entry name
        self.ad_e1= ad_e1 = Entry(register_win,width = 40,textvariable=self.username)
        ad_e1.place(x=120, y=120)
        
        #Entry password
        self.ad_e2 = ad_e2= Entry(register_win,show="*",width = 40,textvariable=self.password)
        ad_e2.place(x=120,y=200)
        
        #Entry password
        self.ad_e3 = ad_e3= Entry(register_win,show="*",width = 40,textvariable=self.repit_pass)
        ad_e3.place(x=120,y=280)
    
        #button to get users input and add it to file
        b=Button(register_win,text="Submit", bg='black', fg='white',command=lambda:[self.get_var(),bc.code_generator(self.username1,self.password1,self.repit_pass1,self.position1)],width=15)
        b.place(x=170, y=380)
        
        #back button
        back_butt = Button(register_win, text='back',bg='black' ,fg='white',command=self.back_to_win1,width=15)
        back_butt.place(x=170,y=420)
        
                      
    def get_var(self):
        self.position1 = self.position.get()
        self.username1 = self.username.get()
        self.password1 = self.password.get()
        self.repit_pass1 = self.repit_pass.get()
        
                
              
    def login_menu(self):
        self.main_win.destroy()
        self.login_win1=login_win1=Tk()
        login_win1.geometry("500x500")
        login_win1.title("Login")
        login_win1.configure(bg="royalblue3")
        
        #set username and password
        self.input_username = StringVar()
        self.input_password = StringVar()
        
        #labels
        l_title=Label(login_win1,text="Login",relief="raised",fg="white",bg="black", width=20)
        l_title.config(font=("Courier","30","bold"))
        l_title.place(x=10, y=0)
        l1=Label(login_win1,text="Enter UserName:",bg='white', font=('',10, 'bold'))
        l1.place(x=200,y=80)
        l2=Label(login_win1,text="Enter your password:",bg='white', font=('',10, 'bold'))
        l2.place(x=175,y=160)
    
        #Entry
        self.ad_e1= ad_e1 = Entry(login_win1,width = 30,textvariable=self.input_username)
        ad_e1.place(x=150, y=120)
        self.ad_e2 = ad_e2= Entry(login_win1,show="*",width = 30,textvariable=self.input_password)
        ad_e2.place(x=150,y=200)
    
        #button
        b=Button(login_win1,text="login", bg='black', fg='white',width=15,command=self.login)
        b.place(x=180, y=250)
        
        #back button
        back_butt = Button(login_win1, text='back',bg='black' ,fg='white',command=self.back_to_main2,width=15)
        back_butt.place(x=180,y=300)
    
    def login(self):
         self.input_username2 = self.input_username.get()
         input_password = self.input_password.get()
         obj2 = bc.User()
         if obj2.check_login(self.input_username2,input_password) == True:
             if obj2.check_position(self.input_username2) == 'student':
                       
#==============================StudentMenu======================================
                            self.login_win1.destroy()
                            self.student_win = student_win= Tk()
                            self.student_win.minsize(1000, 1000)
                            student_win.title('login menu')
                            student_win.config(background='orange')
                            
                            #labels
                            header = Label(student_win, text=['hello',self.input_username2,'welcome to student panel'], bg='black',fg='white', font=("Courier","30","bold"))
                            header.grid(row=0, column=0)
                            
                            
                            #buttons
                            show_butt = Button(student_win, text='see subjects',bg='lightyellow2', fg='black',font ='20',width =30,command=self.show_sub_stu3)
                            search_butt = Button(student_win,text ='search subjects',bg ='lightyellow2', fg ='black',font ='20',width =30,command=self.search2)
                            num_subject_butt = Button(student_win, text='show number of units',bg ='lightyellow2', fg ='black',font ='20',width =30,command=self.all_unit1)
                            get_subject = Button(student_win,text='get subject',bg ='lightyellow2', fg ='black',font ='10',width =30,command=self.choose_sub12)
                            logout = Button(student_win,text='logout',bg ='black', fg ='white',font ='10',width =30,command=self.logout)
                            
                            show_butt.place(x=100,y=100)
                            search_butt.place(x=100,y=150)
                            num_subject_butt.place(x=100,y=200)
                            get_subject.place(x=100,y=250)
                            logout.place(x=100,y=300)
                            
                        
#==============================AdminMenu======================================
                        
             elif obj2.check_position(self.input_username2) == 'admin':
                 
                 self.login_win1.destroy()
                 self.admin_win = admin_win = Tk()
                 self.admin_win.minsize(1800, 1800)
                 admin_win.title('login menu2')
                 admin_win.config(background='orange')
                            
                 #labels
                 header = Label(admin_win, text=f"hello {self.input_username2}  welcome to Admins's panel", bg='black',fg='white', font=("Courier","30","bold"))
                 header.grid(row=0, column=0)
                            
                 #buttons
                 show_butt = Button(admin_win, text='see subjects',bg='lightyellow2', fg='black',font ='20',width =30,command=self.show_sub5)
                 search_butt = Button(admin_win,text ='search subjects',bg ='lightyellow2', fg ='black',font ='20',width =30,command=self.search_4)
                 num_subject_butt = Button(admin_win, text='show number of units',bg ='lightyellow2', fg ='black',font ='20',width =30,command=self.all_unit6)
                 logout = Button(admin_win,text='logout',bg ='black', fg ='white',font ='10',width =30,command=self.logout2)
                 search_stu = Button(admin_win,text='search Students',bg ='lightyellow2', fg ='black',font ='10',width =30,command=self.search_student_frame)
                 search_sub = Button(admin_win,text='search student of subject',bg ='lightyellow2', fg ='black',font ='10',width =30,command=self.search_by_sub)
                 show_stu = Button(admin_win,text='show all Students',bg ='lightyellow2', fg ='black',font ='10',width =30,command=self.show_all_student)
                 req_stu = Button(admin_win,text='Students Requests',bg ='lightyellow2', fg ='black',font ='10',width =30,command=self.send_sub12)
                 add_subject = Button(admin_win,text='add subject',bg ='black', fg ='white',font ='10',width =30,command=self.add_subject7)
                            
                 show_butt.place(x=100,y=100)
                 search_butt.place(x=100,y=150)
                 num_subject_butt.place(x=100,y=200)
                 add_subject.place(x=100,y=250)
                 search_stu.place(x=100,y=300)
                 search_sub.place(x=100,y=350)
                 show_stu.place(x=100,y=400)
                 req_stu.place(x=100,y=450)
                 logout.place(x=100,y=500)
#==============================TeacherMenu======================================
             else:
                 self.login_win1.destroy()
                 self.teacher_win = teacher_win = Tk()
                 self.teacher_win.minsize(1000, 1000)
                 teacher_win.title('login menu2')
                 teacher_win.config(background='orange')
                            
                 #labels
                 header = Label(teacher_win, text=f"hello {self.input_username2}  welcome to teacher's panel", bg='black',fg='white', font=("Courier","30","bold"))
                 header.grid(row=0, column=0)
                            
                            
                 #buttons
                 show_butt = Button(teacher_win, text='see subjects',bg='lightyellow2', fg='black',font ='20',width =30,command=self.show_sub9)
                 search_butt = Button(teacher_win,text ='search subjects',bg ='lightyellow2', fg ='black',font ='20',width =30,command=self.search_8)
                 logout = Button(teacher_win,text='logout',bg ='black', fg ='white',font ='10',width =30,command=self.logout4)
                 get_subject = Button(teacher_win,text='add subject',bg ='black', fg ='white',font ='10',width =30,command=self.choose_sub10)
                 search_stu_sub = Button(teacher_win,text='search student by subject',bg ='black', fg ='white',font ='10',width =30,command=self.search_by_sub2)
                            
                 show_butt.place(x=100,y=100)
                 search_butt.place(x=100,y=150)
                 get_subject.place(x=100,y=200)
                 search_stu_sub.place(x=100,y=250)
                 logout.place(x=100,y=300)
                 
#==============================teacherchoosesubject======================================
    def rm16(self):
        self.f16.destroy()


    def serch16(self):
        input_search16 =self.sid16.get()
        if input_search16 !="" :
            self.list16=("NAME","CODE")
            self.trees16=self.create_tree(self.f16,self.list16)
            self.trees16.place(x=25,y=150)
            
            obj16 = bc.Teacher()
            subject_info16 = obj16.search_by_sub2(input_search16)
            for data16 in subject_info16:
                self.trees16.insert('',END,values=(data16[0],data16[1]))
                
            
            
        else:
            messagebox.showinfo("Error","Data not found")




    def search_by_sub2(self):
        self.sid16 = StringVar()
        self.f16 = Frame(self.teacher_win,height=600,width=600,bg='black')
        self.f16.place(x=450,y=100)
        l1=Label(self.f16,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        e1=Entry(self.f16,width=25,bd=5,bg='orange',fg='black',textvariable=self.sid16).place(x=180,y=40)
        b1=Button(self.f16,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=self.serch16).place(x=400,y=37)
        b2=Button(self.f16,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm16).place(x=250,y=450)               
#==============================teacherchoosesubject====================================== 
    def rm10(self):
         self.f10.destroy()
    def choose_sub10(self):
        self.f10=Frame(self.teacher_win,height=500,width=500,bg='black')
        self.f10.place(x = 470,y = 100)
        # Combobox creation
        self.subject1 = tk.StringVar()
        self.subject2 = tk.StringVar()
        self.subject3 = tk.StringVar()
        self.subject4 = tk.StringVar()
        self.subject5 = tk.StringVar()
        self.subject6 = tk.StringVar()
        self.subject7 = tk.StringVar()
        
        
        subjectchoosen1 = ttk.Combobox(self.f10, width = 27, textvariable = self.subject1)
        subjectchoosen2 = ttk.Combobox(self.f10, width = 27, textvariable = self.subject2)
        subjectchoosen3 = ttk.Combobox(self.f10, width = 27, textvariable = self.subject3)
        subjectchoosen4 = ttk.Combobox(self.f10, width = 27, textvariable = self.subject4)
        subjectchoosen5 = ttk.Combobox(self.f10, width = 27, textvariable = self.subject5)
        subjectchoosen6 = ttk.Combobox(self.f10, width = 27, textvariable = self.subject6)
        subjectchoosen7 = ttk.Combobox(self.f10, width = 27, textvariable = self.subject7)
        
        
        #get the lessons with no teacher
        obj10 = bc.User()
        sub_data10 =  obj10.choose_sub()
       
       
        subjectchoosen1['values'] = sub_data10
        subjectchoosen1['state'] = 'readonly'
        subjectchoosen1.place(x=20,y=10)
        subjectchoosen1.current()
        
        subjectchoosen2['values'] = sub_data10
        subjectchoosen2['state'] = 'readonly'
        subjectchoosen2.place(x=20,y=40)
        subjectchoosen2.current()
        
        subjectchoosen3['values'] = sub_data10
        subjectchoosen3['state'] = 'readonly'
        subjectchoosen3.place(x=20,y=70)
        subjectchoosen3.current()
        
        subjectchoosen4['values'] = sub_data10
        subjectchoosen4['state'] = 'readonly'
        subjectchoosen4.place(x=20,y=100)
        subjectchoosen4.current()
        
        subjectchoosen5['values'] = sub_data10
        subjectchoosen5['state'] = 'readonly'
        subjectchoosen5.place(x=20,y=130)
        subjectchoosen5.current()
        
        subjectchoosen6['values'] = sub_data10
        subjectchoosen6['state'] = 'readonly'
        subjectchoosen6.place(x=20,y=160)
        subjectchoosen6.current()
        
        subjectchoosen7['values'] = sub_data10
        subjectchoosen7['state'] = 'readonly'
        subjectchoosen7.place(x=20,y=190)
        subjectchoosen7.current()
        
        
        
        
        
        
        self.subjects1 = tk.StringVar()
        self.subjects2 = tk.StringVar()
        self.subjects3 = tk.StringVar()
        self.subjects4 = tk.StringVar()
        self.subjects5 = tk.StringVar()
        self.subjects6 = tk.StringVar()
        self.subjects7 = tk.StringVar()
        self.subjects8 = tk.StringVar()
        
        
        
        subjectschoosen1 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects1)
        subjectschoosen2 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects2)
        subjectschoosen3 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects3)
        subjectschoosen4 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects4)
        subjectschoosen5 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects5)
        subjectschoosen6 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects6)
        subjectschoosen7 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects7)
        subjectschoosen8 = ttk.Combobox(self.f10, width = 27, textvariable = self.subjects8)
        
        
        #get the lessons with no teacher
        obj10 = bc.User()
        sub_data10 =  obj10.choose_sub()
       
       
        subjectschoosen1['values'] = sub_data10
        subjectschoosen1['state'] = 'readonly'
        subjectschoosen1.place(x=250,y=10)
        subjectschoosen1.current()
        
        subjectschoosen2['values'] = sub_data10
        subjectschoosen2['state'] = 'readonly'
        subjectschoosen2.place(x=250,y=40)
        subjectschoosen2.current()
        
        subjectschoosen3['values'] = sub_data10
        subjectschoosen3['state'] = 'readonly'
        subjectschoosen3.place(x=250,y=70)
        subjectschoosen3.current()
        
        subjectschoosen4['values'] = sub_data10
        subjectschoosen4['state'] = 'readonly'
        subjectschoosen4.place(x=250,y=100)
        subjectschoosen4.current()
        
        subjectschoosen5['values'] = sub_data10
        subjectschoosen5['state'] = 'readonly'
        subjectschoosen5.place(x=250,y=130)
        subjectschoosen5.current()
        
        subjectschoosen6['values'] = sub_data10
        subjectschoosen6['state'] = 'readonly'
        subjectschoosen6.place(x=250,y=160)
        subjectschoosen6.current()
        
        subjectschoosen7['values'] = sub_data10
        subjectschoosen7['state'] = 'readonly'
        subjectschoosen7.place(x=250,y=190)
        subjectschoosen7.current()
        
        subjectschoosen8['values'] = sub_data10
        subjectschoosen8['state'] = 'readonly'
        subjectschoosen8.place(x=250,y=220)
        subjectschoosen8.current()
        
        
    
            
        
      #buttons
        obj10 = bc.User()
        b10=Button(self.f10,text='get',bg='orange' ,fg='black',width=10,bd=3,command=lambda:[self.get_var10(),obj10.update_file([self.sub1,self.sub2,self.sub3,self.sub4,self.sub5,self.sub6,self.sub7,self.sub8,self.sub9,self.sub10,self.sub11,self.sub12,self.sub13,self.sub14,self.sub15],self.input_username2)]).place(x=130,y=430)
        b_10=Button(self.f10,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=self.rm10).place(x=250,y=430)
        
    def get_var10(self):
        self.sub1 = self.subject1.get()
        self.sub2 = self.subject2.get()
        self.sub3 = self.subject3.get()
        self.sub4 = self.subject4.get()
        self.sub5 = self.subject5.get()
        self.sub6 = self.subject6.get()
        self.sub7 = self.subject7.get()
        
        
        self.sub8 = self.subjects1.get()
        self.sub9 = self.subjects2.get()
        self.sub10 = self.subjects3.get()
        self.sub11 = self.subjects4.get()
        self.sub12 = self.subjects5.get() 
        self.sub13 = self.subjects6.get() 
        self.sub14 = self.subjects7.get()
        self.sub15 = self.subjects8.get()
        
        
            

#==============================teacherlogout======================================
    def logout4(self):
        self.teacher_win.destroy()
        obj5=ProgramGui()
        obj5.mainloop()                             
                            
                            
#==============================teacherShowButt======================================
    def rm9(self):
         self.f9.destroy()
         
         
    def show_sub9(self):  
        
        self.f9=Frame(self.teacher_win,height=500,width=500,bg='black')
        self.f9.place(x = 470,y = 100)
        b9=Button(self.f9,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=self.rm9).place(x=250,y=400)
        self.list9 = ("SUBJECT","TEACHER","UNIT")
        self.treess9 = self.create_tree(self.f9,self.list9)
        self.treess9.place(x=25,y=50)
        obj9 = bc.User()
        subject_info9 = obj9.get_tree_data()
        for data9 in subject_info9:
            self.treess9.insert('',END,values=(data9[0],data9[2],data9[1],data9[3]))
                    
                                
                            
#==============================TeacherSearchButt======================================
    def rm8(self):
         self.f8.destroy()
         
         
    def serch8(self):
        input_search8 =self.sid8.get()
        if input_search8 !="" :
            self.list8=("SUBJECT","TEACHER","UNIT","CAPACITY")
            self.trees8=self.create_tree(self.f8,self.list8)
            self.trees8.place(x=25,y=150)
            
            obj8 = bc.User()
            subject_info8 = obj8.get_tree_data()
            for data8 in subject_info8:
                if input_search8 == data8[0]:
                    self.trees8.insert('',END,values=(data8[0],data8[2],data8[1],data8[3]))
                
            
            
        else:
            messagebox.showinfo("Error","Data not found")
         
    def search_8(self):
        self.sid8 =StringVar()
        self.f8=Frame(self.teacher_win,height=500,width=500,bg='black')
        self.f8.place(x=450,y=100)
        l1=Label(self.f8,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        e1=Entry(self.f8,width=25,bd=5,bg='orange',fg='black',textvariable=self.sid8).place(x=180,y=40)
        b1=Button(self.f8,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=self.serch8).place(x=400,y=37)
        b1=Button(self.f8,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm8).place(x=250,y=450)  

                        
                            
#==============================Adminaddsubject======================================
    def rm7(self):
        self.f7.destroy()
        
    def add_data7(self):
        subject = self.subject.get()
        teacher = self.teacher.get()
        unit = self.unit.get()
        capacity = self.capacity.get()
        if (subject and unit and capacity):
            obj7 = bc.Admin(subject,teacher,unit,capacity)
            obj7.add_subject_data()
            messagebox.showinfo(title='successful',message='data added successfuly!')
        else:
            messagebox.showerror(title='empty',message='no data to add')
        
        
    def add_subject7(self):
        
        self.subject=StringVar()
        self.teacher=StringVar()
        self.unit=StringVar()
        self.capacity =StringVar()
        
        self.f7=Frame(self.admin_win,height=500,width=650,bg='black')
        self.f7.place(x=500,y=100)
        l1=Label(self.f7,text='subject name : ',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f7,width=45,bg='orange',fg='black',textvariable=self.subject).place(x=150,y=50)
        
        l2=Label(self.f7,text='Teacher : ',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=100)
        e2=Entry(self.f7,width=45,bg='orange',fg='black',textvariable=self.teacher).place(x=150,y=100)
        
        l3=Label(self.f7,text='Unit : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=150)
        e3=Entry(self.f7,width=45,bg='orange',fg='black',textvariable=self.unit).place(x=150,y=150)
        
        l4=Label(self.f7,text='capacity : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=200)
        e4=Entry(self.f7,width=45,bg='orange',fg='black',textvariable=self.capacity).place(x=150,y=200)
        
        self.f7.grid_propagate(0)
        b1=Button(self.f7,text='Add',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=self.add_data7)
        b2=Button(self.f7,text='Back',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=self.rm7)
        
        b1.place(x=150,y=250)
        b2.place(x=150,y=300)
                            
                            
#==============================AdminnumberOfSubject======================================
    def rm6(self):
        self.f6.destroy()
                   
    def show_all6(self):
        self.list6 = ("UNITS","NUMBER")
        self.treess6 = self.create_tree(self.f6,self.list6)
        self.treess6.place(x=40,y=100)
        
        num_data = bc.num_subject_data()
        
        
        self.treess6.insert('',END,values=('1',str(num_data[0])))
        
        self.treess6.insert('',END,values=('2',str(num_data[1])))
       
              
        self.treess6.insert('',END,values=('3',str(num_data[2])))
            
               
        self.treess6.insert('',END,values=('4',str(num_data[3])))
        
        #last line of treeviwe contain number of subjects and sum of their units
        self.treess6.insert('',END,values=(f'all_units = {num_data[4]}',f'all_subjects = {num_data[5]}'))
        
        
            
        
        
    def all_unit6(self):
        self.f6=Frame(self.admin_win,height=500,width=500,bg='black')
        self.f6.place(x=450,y=100)
        l1=Label(self.f6,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        b1=Button(self.f6,text='Go',bg='orange',font='Papyrus 10 bold',width=20,bd=2,command=self.show_all6).place(x=200,y=37)
        b1=Button(self.f6,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm6).place(x=250,y=450)
                            
                            
                            
#==============================adminlogout======================================
    def logout2(self):
        self.admin_win.destroy()
        obj5=ProgramGui()
        obj5.mainloop()                             
                            
                            
#==============================adminShowButt======================================
    def rm5(self):
         self.f5.destroy()
         
         
    def show_sub5(self):    
        self.f5=Frame(self.admin_win,height=500,width=500,bg='black')
        self.f5.place(x=470,y=100)
        b1=Button(self.f5,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=self.rm5).place(x=250,y=400)
        self.list5=("SUBJECT","TEACHER","UNIT","CAPACITY")
        self.treess5 = self.create_tree(self.f5,self.list5)
        self.treess5.place(x=25,y=50)
        
        obj5 = bc.User()
        subject_info5 = obj5.get_tree_data()
        for data5 in subject_info5:
            self.treess5.insert('',END,values=(data5[0],data5[2],data5[1],data5[3]))
                
        
        
                         
                            
#==============================adminSearchButt======================================
    def rm4(self):
         self.f8.destroy()
         
         
    def serch4(self):
        input_search4 =self.sid4.get()
        if input_search4 !="" :
            self.list4=("SUBJECT","TEACHER","UNIT","CAPACITY")
            self.trees4=self.create_tree(self.f4,self.list4)
            self.trees4.place(x=25,y=150)
            
            obj4 = bc.User()
            subject_info4 = obj4.get_tree_data()
            for data4 in subject_info4:
                if input_search4 == data4[0]:
                    self.trees.insert('',END,values=(data4[0],data4[2],data4[1],data4[3]))
                
            
            
        else:
            messagebox.showinfo("Error","Data not found")
         
    def search_4(self):
        self.sid4 = StringVar()
        self.f4 = Frame(self.admin_win,height=500,width=500,bg='black')
        self.f4.place(x=450,y=100)
        l1=Label(self.f4,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        e1=Entry(self.f4,width=25,bd=5,bg='orange',fg='black',textvariable=self.sid4).place(x=180,y=40)
        b1=Button(self.f4,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=self.serch4).place(x=400,y=37)
        b2=Button(self.f4,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm4).place(x=250,y=450)                              
                            
#==============================adminSearchStudent====================================== 
    def rm13(self):
        self.f13.destroy()


    def serch13(self):
        input_search13 =self.sid13.get()
        if input_search13 !="" :
            self.list13=("NAME","CODE","SUBJECT")
            self.trees13=self.create_tree2(self.f13,self.list13)
            self.trees13.place(x=25,y=150)
            
            obj13 = bc.User()
            subject_info13 = obj13.search_num_name(input_search13)
            for data13 in subject_info13:
                if (input_search13 == data13[0]) or (input_search13 == data13[1]):
                    self.trees13.insert('',END,values=(data13[0],data13[1],data13[2]))
                
            
            
        else:
            messagebox.showinfo("Error","Data not found")




    def search_student_frame(self):
        self.sid13 = StringVar()
        self.f13 = Frame(self.admin_win,height=1300,width=1300,bg='black')
        self.f13.place(x=450,y=100)
        l1=Label(self.f13,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        e1=Entry(self.f13,width=25,bd=5,bg='orange',fg='black',textvariable=self.sid13).place(x=180,y=40)
        b1=Button(self.f13,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=self.serch13).place(x=400,y=37)
        b2=Button(self.f13,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm13).place(x=250,y=450)  
                               
#==============================adminShowStudent======================================
    def rm14(self):
        self.f14.destroy()


    def show14(self):
            self.list14=("NAME","CODE")
            self.trees14=self.create_tree(self.f14,self.list14)
            self.trees14.place(x=25,y=150)
            
            obj14 = bc.User()
            subject_info14 = obj14.show_student()
            for data14 in subject_info14:
                self.trees14.insert('',END,values=(data14[0],data14[1]))
                
            
            
       




    def show_all_student(self):
        self.sid14 = StringVar()
        self.f14 = Frame(self.admin_win,height=500,width=500,bg='black')
        self.f14.place(x=450,y=100)
        l1=Label(self.f14,text='Students: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        b1=Button(self.f14,text='go',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=self.show14).place(x=400,y=37)
        b2=Button(self.f14,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm14).place(x=250,y=450)                        
                            
#==============================AdminSearchStudentbysubject======================================
    def rm15(self):
        self.f15.destroy()


    def serch15(self):
        input_search15 =self.sid15.get()
        if input_search15 !="" :
            self.list15=("NAME","CODE")
            self.trees15=self.create_tree(self.f15,self.list15)
            self.trees15.place(x=25,y=150)
            
            obj15 = bc.Admin()
            subject_info15 = obj15.search_by_sub(input_search15)
            for data15 in subject_info15:
                self.trees15.insert('',END,values=(data15[0],data15[1]))
                
            
            
        else:
            messagebox.showinfo("Error","Data not found")




    def search_by_sub(self):
        self.sid15 = StringVar()
        self.f15 = Frame(self.admin_win,height=600,width=600,bg='black')
        self.f15.place(x=450,y=100)
        l1=Label(self.f15,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        e1=Entry(self.f15,width=25,bd=5,bg='orange',fg='black',textvariable=self.sid15).place(x=180,y=40)
        b1=Button(self.f15,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=self.serch15).place(x=400,y=37)
        b2=Button(self.f15,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm15).place(x=250,y=450)
                            
                            
#==============================StudentGETSubject======================================
    def rm12(self):
         self.f12.destroy()
         
    def choose_sub12(self):
        self.f12=Frame(self.student_win,height=500,width=500,bg='black')
        self.f12.place(x = 470,y = 100)
        # Combobox creation
        self.subject_1 = tk.StringVar()
        self.subject_2 = tk.StringVar()
        self.subject_3 = tk.StringVar()
        self.subject_4 = tk.StringVar()
        self.subject_5 = tk.StringVar()
        self.subject_6 = tk.StringVar()
        self.subject_7 = tk.StringVar()
        
        
        subject_choosen1 = ttk.Combobox(self.f12, width = 27, textvariable = self.subject_1)
        subject_choosen2 = ttk.Combobox(self.f12, width = 27, textvariable = self.subject_2)
        subject_choosen3 = ttk.Combobox(self.f12, width = 27, textvariable = self.subject_3)
        subject_choosen4 = ttk.Combobox(self.f12, width = 27, textvariable = self.subject_4)
        subject_choosen5 = ttk.Combobox(self.f12, width = 27, textvariable = self.subject_5)
        subject_choosen6 = ttk.Combobox(self.f12, width = 27, textvariable = self.subject_6)
        subject_choosen7 = ttk.Combobox(self.f12, width = 27, textvariable = self.subject_7)
        
        
        #get the lessons with no teacher
        obj12 = bc.User()
        sub_data12 =  obj12.choose_sub13()
       
       
        subject_choosen1['values'] = sub_data12
        subject_choosen1['state'] = 'readonly'
        subject_choosen1.place(x=20,y=10)
        subject_choosen1.current()
        
        subject_choosen2['values'] = sub_data12
        subject_choosen2['state'] = 'readonly'
        subject_choosen2.place(x=20,y=40)
        subject_choosen2.current()
        
        subject_choosen3['values'] = sub_data12
        subject_choosen3['state'] = 'readonly'
        subject_choosen3.place(x=20,y=70)
        subject_choosen3.current()
        
        subject_choosen4['values'] = sub_data12
        subject_choosen4['state'] = 'readonly'
        subject_choosen4.place(x=20,y=100)
        subject_choosen4.current()
        
        subject_choosen5['values'] = sub_data12
        subject_choosen5['state'] = 'readonly'
        subject_choosen5.place(x=20,y=130)
        subject_choosen5.current()
        
        subject_choosen6['values'] = sub_data12
        subject_choosen6['state'] = 'readonly'
        subject_choosen6.place(x=20,y=160)
        subject_choosen6.current()
        
        subject_choosen7['values'] = sub_data12
        subject_choosen7['state'] = 'readonly'
        subject_choosen7.place(x=20,y=190)
        subject_choosen7.current()
        
        
        
        
        
        
        self.subjects_1 = tk.StringVar()
        self.subjects_2 = tk.StringVar()
        self.subjects_3 = tk.StringVar()
        self.subjects_4 = tk.StringVar()
        self.subjects_5 = tk.StringVar()
        self.subjects_6 = tk.StringVar()
        self.subjects_7 = tk.StringVar()
        self.subjects_8 = tk.StringVar()
        
        
        
        subjects_choosen1 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_1)
        subjects_choosen2 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_2)
        subjects_choosen3 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_3)
        subjects_choosen4 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_4)
        subjects_choosen5 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_5)
        subjects_choosen6 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_6)
        subjects_choosen7 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_7)
        subjects_choosen8 = ttk.Combobox(self.f12, width = 27, textvariable = self.subjects_8)
        
        
        #get the lessons with no teacher
        obj12 = bc.User()
        sub_data12 =  obj12.choose_sub13()
       
       
        subjects_choosen1['values'] = sub_data12
        subjects_choosen1['state'] = 'readonly'
        subjects_choosen1.place(x=250,y=10)
        subjects_choosen1.current()
        
        subjects_choosen2['values'] = sub_data12
        subjects_choosen2['state'] = 'readonly'
        subjects_choosen2.place(x=250,y=40)
        subjects_choosen2.current()
        
        subjects_choosen3['values'] = sub_data12
        subjects_choosen3['state'] = 'readonly'
        subjects_choosen3.place(x=250,y=70)
        subjects_choosen3.current()
        
        subjects_choosen4['values'] = sub_data12
        subjects_choosen4['state'] = 'readonly'
        subjects_choosen4.place(x=250,y=100)
        subjects_choosen4.current()
        
        subjects_choosen5['values'] = sub_data12
        subjects_choosen5['state'] = 'readonly'
        subjects_choosen5.place(x=250,y=130)
        subjects_choosen5.current()
        
        subjects_choosen6['values'] = sub_data12
        subjects_choosen6['state'] = 'readonly'
        subjects_choosen6.place(x=250,y=160)
        subjects_choosen6.current()
        
        subjects_choosen7['values'] = sub_data12
        subjects_choosen7['state'] = 'readonly'
        subjects_choosen7.place(x=250,y=190)
        subjects_choosen7.current()
        
        subjects_choosen8['values'] = sub_data12
        subjects_choosen8['state'] = 'readonly'
        subjects_choosen8.place(x=250,y=220)
        subjects_choosen8.current()
        
        
    
            
        
      #buttons
        obj12 = bc.User()
        b12=Button(self.f12,text='get',bg='orange' ,fg='black',width=10,bd=3,command=lambda:[self.get_var12(),obj12.choose_sub12([self.sub_1,self.sub_2,self.sub_3,self.sub_4,self.sub_5,self.sub_6,self.sub_7,self.sub_8,self.sub_9,self.sub_10,self.sub_11,self.sub_12,self.sub_13,self.sub_14,self.sub_15],self.input_username2)]).place(x=130,y=430)
        b_12=Button(self.f12,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=self.rm12).place(x=250,y=430)
        self.student_name = self.input_username2
        
    def get_var12(self):
        self.sub_1 = self.subject_1.get()
        self.sub_2 = self.subject_2.get()
        self.sub_3 = self.subject_3.get()
        self.sub_4 = self.subject_4.get()
        self.sub_5 = self.subject_5.get()
        self.sub_6 = self.subject_6.get()
        self.sub_7 = self.subject_7.get()
        
        
        self.sub_8 = self.subjects_1.get()
        self.sub_9 = self.subjects_2.get()
        self.sub_10 = self.subjects_3.get()
        self.sub_11 = self.subjects_4.get()
        self.sub_12 = self.subjects_5.get() 
        self.sub_13 = self.subjects_6.get() 
        self.sub_14 = self.subjects_7.get()
        self.sub_15 = self.subjects_8.get()
        
        self.sub_list = [self.sub_1,self.sub_2,self.sub_3,self.sub_4,self.sub_5,self.sub_6,self.sub_7,self.sub_8,self.sub_9,self.sub_10,self.sub_11,self.sub_12,self.sub_13,self.sub_14,self.sub_15]
        
                         
#==============================StudentSendsubToAdmin======================================
    def rm12(self):
        self.f12.destroy()

    def send_sub12(self):
        self.sid12 = StringVar()
        self.f12=Frame(self.admin_win,height=1000,width=1000,bg='black')
        self.f12.place(x=470,y=100)
        self.list12 = ("NAME","SUBJECTS")
        self.treess12=self.create_tree2(self.f12,self.list12)
        self.treess12.place(x=40,y=100)
        
        obj12 = bc.User()
        obj_12 = bc.Admin()
        subject_info12 = obj12.get_tree_data14()
        for data12 in subject_info12:
            self.treess12.insert('',END,values=(data12[0],data12[1]))
            
            
        l2=Label(self.f12,text='enter name of student: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=500)
        e2=Entry(self.f12,width=25,bd=5,bg='orange',fg='black',textvariable=self.sid12).place(x=200,y=500)
        b2=Button(self.f12,text='accept',bg='green',fg= 'white',font='Papyrus 10 bold',width=9,bd=2,command = lambda:[self.get_var13(),obj_12.accept(self.input_search12)]).place(x=150,y=600)
        b3=Button(self.f12,text='deny',bg='red',fg='white',font='Papyrus 10 bold',width=10,bd=2,command = lambda:[self.get_var14(),obj_12.deny(self.input_search12)]).place(x=300,y=600)
        b4=Button(self.f12,text='back',bg='orange',fg='black',font='Papyrus 10 bold',width=10,bd=2,command = self.rm12).place(x=450,y=600)
    
    def get_var13(self):
         self.input_search12 = self.sid12.get()
    def get_var14(self):
         self.input_search12 = self.sid12.get()
        
        
        
        

    
                           
                    
#==============================studentlogout======================================
    def logout(self):
        self.student_win.destroy()
        obj5=ProgramGui()
        obj5.mainloop()
        
                    
                    
#==============================StudentShowButt======================================
    def rm3(self):
         self.f3.destroy()
         
         
    def show_sub_stu3(self):    
        self.f3=Frame(self.student_win,height=500,width=500,bg='black')
        self.f3.place(x=470,y=100)
        b1=Button(self.f3,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=self.rm3).place(x=250,y=400)
        self.list3 = ("SUBJECT","TEACHER","UNIT","CAPACITY")
        self.treess3 = self.create_tree(self.f3,self.list3)
        self.treess3.place(x=25,y=50)
        
        
        obj3 = bc.User()
        subject_info3 = obj3.get_tree_data()
        for data3 in subject_info3:
            self.treess3.insert('',END,values=(data3[0],data3[2],data3[1],data3[3]))


#==============================StudentSearchButt======================================
    def rm2(self):
         self.f2.destroy()
         
         
    def serch2(self):
        input_search2 =self.sid2.get()
        if input_search2 !="" :
            self.list2 = ("SUBJECT","TEACHER","UNIT","CAPACITY")
            self.trees2 = self.create_tree(self.f2,self.list2)
            self.trees2.place(x=25,y=150)
            
            obj2 = bc.User()
            subject_info2 = obj2.get_tree_data()
            for data2 in subject_info2:
                if input_search2 == data2[0]:
                    self.trees2.insert('',END,values=(data2[0],data2[2],data2[1],data2[3]))
                    
            
        else:
            messagebox.showinfo("Error","Data not found")
         
    def search2(self):
        self.sid2 = StringVar()
        self.f2 = Frame(self.student_win,height=500,width=500,bg='black')
        self.f2.place(x=450,y=100)
        l2=Label(self.f2,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        e2=Entry(self.f2,width=25,bd=5,bg='orange',fg='black',textvariable=self.sid2).place(x=180,y=40)
        b2=Button(self.f2,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=self.serch2).place(x=400,y=37)
        b2=Button(self.f2,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm2).place(x=250,y=450)  
             
#==============================StudentnumberOfSubject======================================
    def rm1(self):
        self.f1.destroy()
                   
    def show_all_1(self):
        self.list1=("UNITS","NUMBER")
        self.treess1=self.create_tree(self.f1,self.list1)
        self.treess1.place(x=40,y=100)
        
        num_data = bc.num_subject_data()
        
        
        self.treess1.insert('',END,values=('1',str(num_data[0])))
        
        self.treess1.insert('',END,values=('2',str(num_data[1])))
       
              
        self.treess1.insert('',END,values=('3',str(num_data[2])))
            
               
        self.treess1.insert('',END,values=('4',str(num_data[3])))
        
        #last line of treeviwe contain number of subjects and sum of their units
        self.treess1.insert('',END,values=(f'all_units = {num_data[4]}',f'all_subjects = {num_data[5]}'))
        
    def all_unit1(self):
        self.f1=Frame(self.student_win,height=500,width=500,bg='black')
        self.f1.place(x=450,y=100)
        l1=Label(self.f1,text='Subject: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        b1=Button(self.f1,text='Go',bg='orange',font='Papyrus 10 bold',width=20,bd=2,command=self.show_all_1).place(x=200,y=37)
        b1=Button(self.f1,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=self.rm1).place(x=250,y=450)
        
   
        
        
    
         
    
        
        
    
    
    
    
            
    
        
    
    def create_tree(self,plc,lists):
        self.tree=ttk.Treeview(plc,height=13,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=100)
            n=n+1
        return self.tree
    
    def create_tree2(self,plc,lists):
        self.tree=ttk.Treeview(plc,height=13,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=400)
            n=n+1
        return self.tree
    
    
    
         
        
















    
