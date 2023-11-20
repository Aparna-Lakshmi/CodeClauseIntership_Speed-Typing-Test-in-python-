from tkinter import *
import random
from timeit import default_timer as timer
import mysql.connector 
from tkinter import messagebox


connection=mysql.connector.connect(host="localhost", user="root",password="Bhavana@123",database="speedtypingtest")
cursor=connection.cursor()

register_window=Tk()
register_window.title("REGISTER FOR SPEED TYPING TEST ")
register_window.geometry("1500x1500")
rlabel=Label(register_window,text="Register For Speed Typing Test")
rlabel.pack()
rlabel.configure(font=("Helvetica",14))
registerend_mainframe=0
loginend_mainframe=0

def register():
    rusername=entry_username.get()
    rpassword=entry_password.get()
    rconfirm_password=entry_confirm_password.get()
   
    if(0):
        entry_password.delete(0,END(register_window))
        entry_confirm_password.delete(0,END(register_window))
    else:
        cursor.execute("INSERT INTO userdetails (username, password, confirm_password) VALUES (%s,%s,%s)",(rusername,rpassword,rconfirm_password))
        connection.commit()
        global registerend_mainframe
        if(registerend_mainframe==0):
            register_window.destroy()
            registerend_mainframe+=1
            
            def login():
                lusername=lentry_username.get()
                lpassword=lentry_password.get()
                    
                cursor.execute("SELECT * FROM userdetails WHERE username=%s AND password=%s",(lusername,lpassword))
                lresult=cursor.fetchone()
                    
                if(lresult):
                    global loginend_mainframe
                    if(loginend_mainframe==0):
                        login_window.destroy()
                        loginend_mainframe+=1
                        
                        def submit():
                            userinput=input.get()
                            user_name=name.get()
                            end_time=timer()
                            time_taken=round(end_time-start_time)
                            list1=list(userinput.split())
                            list2=list(text_taken.split())
                            count_mistakes=0
                                
                            for i in range(len(list1)):
                                    if(list1[i]!=list2[i]):
                                        count_mistakes+=1  
                            if(count_mistakes!=len(list1)):
                                typing_speed=len(list1)/time_taken
                                cursor.execute("SELECT id FROM userdetails WHERE username=%s",(user_name,))
                                user_id=cursor.fetchone()[0]
                                cursor.execute("INSERT INTO result(user_id,typing_speed,mistakes) VALUES(%s,%s,%s)",(user_id,typing_speed,count_mistakes))
                                connection.commit()
                                result.config(text=f"Typing speed: {typing_speed:.2f} words per seconds")
                                mistakes.config(text=f"mistakes : {count_mistakes}")
                            else:
                                result.config(text=f"Incorrect typing! Try again.")
                                    
                                    
                        tk=Tk()
                        tk.configure(bg="pink")
                        tk.title("Speed typing test")
                        label1=Label(tk,text="Speed Typing Test")
                        label1.pack()
                        label1.configure(font=("Helvetica",14),bg='pink')
                        tk.geometry("1500x1500")

                        list_content=["The major wild animals of India are elephant, tiger, lion, deer, bear etc. Wild animals are very important in balancing the environment.\nThey provide stability to different natural processes of nature. It can be found in all ecosystems, desert, rain forests, plains and other areas.",
                                            "The study of the diverse environments, places, and spaces of Earth's surface and their interactions. It seeks to answer the questions of why \nthings are as they are, where they are.",
                                            "The Grimm fairy tale gets a Technicolor treatment in Disney's first animated feature. Jealous of Snow White's beauty, the wicked queen orders \nthe murder of her innocent stepdaughter, but later discovers that Snow White is still alive and hiding in a cottage with seven friendly little miners.",
                                            "The system of private tuition has been in existence in India for a long time but in recent times it has grown in manifold affecting the core of the educational system.",
                                            "The live-action Snow White will star actress and singer Rachel Zegler as Snow White and Gal Gadot as the Evil Queen. Both castings were announced in 2021; \nthe full cast list has yet to be shared with the public."]
                        text_taken=random.choice(list_content)
                        expectedtext=Label(tk,text=text_taken,bg='pink')
                        expectedtext.pack()
                        expectedtext.place(relx=0.5,rely=0.3,anchor=CENTER)
                        expectedtext.configure(font=("Helvetica",13))
                                
                        lname=Label(tk,text="Name")
                        lname.pack()
                        lname.place(relx=0.4,rely=0.35,anchor=CENTER)
                            
                        name=Entry(tk)
                        name.pack()
                        name.place(relx=0.5,rely=0.35,anchor=CENTER)
                        name.configure(font=("Helvetica",12))

                        start_time=timer()
                        input=Entry(tk)
                        input.pack()
                        input.place(relx=0.5,rely=0.4,anchor=CENTER,height=50,width=600)
                        input.configure(font=("Helvetica",12))

                        submit1=Button(tk,text="Submit",command=submit)
                        submit1.pack()
                        submit1.place(relx=0.5,rely=0.5,anchor=CENTER)
                        submit1.configure(activebackground="blue",font=("Helvetica",12))

                        result=Label(tk,text="speed Typing test Result:",bg='pink',font=("Helvetica",13))
                        result.pack()
                        result.place(relx=0.5,rely=0.55,anchor=CENTER)

                        mistakes=Label(tk,text="",bg='pink',font=("Helvetica",13))
                        mistakes.pack()
                        mistakes.place(relx=0.5,rely=0.58,anchor=CENTER)
                        tk.mainloop()
                    
                    
                    
                else:
                    messagebox.showinfo("Login Error","Invalid username or password!")
                    lentry_password.delete(0,END(login_window))
                

                        
                
            login_window=Tk()
            login_window.title("LOGIN FOR SPEED TYPING TEST")
            login_window.geometry("1500x1500")
            llabel=Label(login_window,text="Login For Speed Typing Test")
            llabel.pack()
            llabel.configure(font=("Helvetica",14))
            
            lusername=Label(login_window,text="Username")
            lusername.pack()
            lusername.place(relx=0.4,rely=0.4,anchor=CENTER)

            lentry_username=Entry(login_window,)
            lentry_username.pack()
            lentry_username.place(relx=0.5,rely=0.4,anchor=CENTER)


            lpassword=Label(login_window,text="Password")
            lpassword.pack()
            lpassword.place(relx=0.4,rely=0.45,anchor=CENTER)

            lentry_password=Entry(login_window)
            lentry_password.pack()
            lentry_password.place(relx=0.5,rely=0.45,anchor=CENTER)
            
            loginl=Button(login_window,text="Login",command=login)
            loginl.pack()
            loginl.place(relx=0.45,rely=0.5,anchor=CENTER)
            loginl.configure(bg="blue")
            login_window.mainloop()
    
def login_frame():
    global registerend_mainframe
    if(registerend_mainframe==0):
        register_window.destroy()
        registerend_mainframe+=1
   
    def login():
        lusername=lentry_username.get()
        lpassword=lentry_password.get()
            
        cursor.execute("SELECT * FROM userdetails WHERE username=%s AND password=%s",(lusername,lpassword))
        lresult=cursor.fetchone()
            
        if(lresult):
            global loginend_mainframe
            if(loginend_mainframe==0):
                login_window.destroy()
                loginend_mainframe+=1
                
                def submit():
                    userinput=input.get()
                    user_name=name.get()
                    end_time=timer()
                    time_taken=round(end_time-start_time)
                    list1=list(userinput.split())
                    list2=list(text_taken.split())
                    count_mistakes=0
                        
                    for i in range(len(list1)):
                            if(list1[i]!=list2[i]):
                                count_mistakes+=1  
                    if(count_mistakes!=len(list1)):
                        typing_speed=len(list1)/time_taken
                        cursor.execute("SELECT id FROM userdetails WHERE username=%s",(user_name,))
                        user_id=cursor.fetchone()[0]
                        cursor.execute("INSERT INTO result(user_id,typing_speed,mistakes) VALUES(%s,%s,%s)",(user_id,typing_speed,count_mistakes))
                        connection.commit()
                        result.config(text=f"Typing speed: {typing_speed:.2f} words per seconds")
                        mistakes.config(text=f"mistakes : {count_mistakes}")
                    else:
                        result.config(text=f"Incorrect typing! Try again.")
                            
                            
                tk=Tk()
                tk.configure(bg="pink")
                tk.title("Speed typing test")
                label1=Label(tk,text="Speed Typing Test")
                label1.pack()
                label1.configure(font=("Helvetica",14),bg='pink')
                tk.geometry("1500x1500")

                list_content=["The major wild animals of India are elephant, tiger, lion, deer, bear etc. Wild animals are very important in balancing the environment.\nThey provide stability to different natural processes of nature. It can be found in all ecosystems, desert, rain forests, plains and other areas.",
                                    "The study of the diverse environments, places, and spaces of Earth's surface and their interactions. It seeks to answer the questions of why \nthings are as they are, where they are.",
                                    "The Grimm fairy tale gets a Technicolor treatment in Disney's first animated feature. Jealous of Snow White's beauty, the wicked queen orders \nthe murder of her innocent stepdaughter, but later discovers that Snow White is still alive and hiding in a cottage with seven friendly little miners.",
                                    "The system of private tuition has been in existence in India for a long time but in recent times it has grown in manifold affecting the core of the educational system.",
                                    "The live-action Snow White will star actress and singer Rachel Zegler as Snow White and Gal Gadot as the Evil Queen. Both castings were announced in 2021; \nthe full cast list has yet to be shared with the public."]
                text_taken=random.choice(list_content)
                expectedtext=Label(tk,text=text_taken,bg='pink')
                expectedtext.pack()
                expectedtext.place(relx=0.5,rely=0.3,anchor=CENTER)
                expectedtext.configure(font=("Helvetica",13))
                        
                lname=Label(tk,text="Name")
                lname.pack()
                lname.place(relx=0.4,rely=0.35,anchor=CENTER)
                    
                name=Entry(tk)
                name.pack()
                name.place(relx=0.5,rely=0.35,anchor=CENTER)
                name.configure(font=("Helvetica",12))

                start_time=timer()
                input=Entry(tk)
                input.pack()
                input.place(relx=0.5,rely=0.4,anchor=CENTER,height=50,width=600)
                input.configure(font=("Helvetica",12))

                submit1=Button(tk,text="Submit",command=submit)
                submit1.pack()
                submit1.place(relx=0.5,rely=0.5,anchor=CENTER)
                submit1.configure(activebackground="blue",font=("Helvetica",12))

                result=Label(tk,text="speed Typing test Result:",bg='pink',font=("Helvetica",13))
                result.pack()
                result.place(relx=0.5,rely=0.55,anchor=CENTER)

                mistakes=Label(tk,text="",bg='pink',font=("Helvetica",13))
                mistakes.pack()
                mistakes.place(relx=0.5,rely=0.58,anchor=CENTER)
                tk.mainloop()
                 
        else:
            messagebox.showinfo("Login Error","Invalid username or password!")
            lentry_password.delete(0,END(login_window))
        
    login_window=Tk()
    login_window.title("LOGIN FOR SPEED TYPING TEST")
    login_window.geometry("1500x1500")
    llabel=Label(login_window,text="Login For Speed Typing Test")
    llabel.pack()
    llabel.configure(font=("Helvetica",14))
    
    lusername=Label(login_window,text="Username")
    lusername.pack()
    lusername.place(relx=0.4,rely=0.4,anchor=CENTER)

    lentry_username=Entry(login_window,)
    lentry_username.pack()
    lentry_username.place(relx=0.5,rely=0.4,anchor=CENTER)


    lpassword=Label(login_window,text="Password")
    lpassword.pack()
    lpassword.place(relx=0.4,rely=0.45,anchor=CENTER)

    lentry_password=Entry(login_window)
    lentry_password.pack()
    lentry_password.place(relx=0.5,rely=0.45,anchor=CENTER)
    
    loginl=Button(login_window,text="Login",command=login)
    loginl.pack()
    loginl.place(relx=0.45,rely=0.5,anchor=CENTER)
    loginl.configure(bg="blue")
    login_window.mainloop()
         
rusername=Label(register_window,text="Username")
rusername.pack()
rusername.place(relx=0.4,rely=0.4,anchor=CENTER)

entry_username=Entry(register_window,)
entry_username.pack()
entry_username.place(relx=0.5,rely=0.4,anchor=CENTER)


rpassword=Label(register_window,text="Password")
rpassword.pack()
rpassword.place(relx=0.4,rely=0.45,anchor=CENTER)

entry_password=Entry(register_window)
entry_password.pack()
entry_password.place(relx=0.5,rely=0.45,anchor=CENTER)

rconfirm_password=Label(register_window,text="Confirm password")
rconfirm_password.pack()
rconfirm_password.place(relx=0.4,rely=0.5,anchor=CENTER)

entry_confirm_password=Entry(register_window)
entry_confirm_password.pack()
entry_confirm_password.place(relx=0.5,rely=0.5,anchor=CENTER)


bregister=Button(register_window,text="Register",command=register)
bregister.pack()
bregister.place(relx=0.45,rely=0.6,anchor=CENTER)
bregister.configure(bg="blue")

rlabel_login=Label(register_window,text="If Already Registered")
rlabel_login.pack()
rlabel_login.place(relx=0.45,rely=0.65,anchor=CENTER)

blogin=Button(register_window,text="Login",command=login_frame)
blogin.pack()
blogin.place(relx=0.5,rely=0.65,anchor=CENTER)
blogin.configure(bg="blue")


register_window.mainloop()
cursor.close()
connection.close()