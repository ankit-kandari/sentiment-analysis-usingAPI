from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API


class NLPapp:
    def __init__(self):

        #create database class object
        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title("nlpapp")
        #self.root.iconbitmap("resource/")
        self.root.geometry("300x600")
        self.root.configure(bg = "red")
        self.login_gui()
        self.root.mainloop() #holds gui in screen

    def login_gui(self):

        self.clear()

        heading = Label(self.root,text = "NLPapp",bg ="#3776ab",fg = "white")
        #no self because only this def will use this
        heading.pack(pady = (30,30))  #pady for gap
        heading.configure(font = ("verdana",24,"bold"))

        label1 = Label(self.root,text = "enter email")
        label1.pack(pady = (30,30))

        self.email_input = Entry(self.root,width = 30)  #entry class
        self.email_input.pack(pady = (5,10),ipady = 10)  #for increase in y direction or length

        label2 = Label(self.root,text = "enter password")
        label2.pack(pady = (30,30))

        self.pswd_input = Entry(self.root,width = 30,show = "*")  #entry class
        self.pswd_input.pack(pady = (5,10),ipady = 10)

        login_btn = Button(self.root,text = "login",command = self.perform_login)  #can give height to button not to entry box
        login_btn.pack(pady = (10,10))

        label3 = Label(self.root, text="not a member")
        label3.pack(pady=(30, 30))

        redirect_btn = Button(self.root,text = "register now",command =self.register_gui)
        redirect_btn.pack(pady = (10,10))

    def register_gui(self):
        #clear eisting gui
        self.clear()
        heading = Label(self.root,text = "NLPapp",bg ="#3776ab",fg = "white")
        #no self because only this def will use this
        heading.pack(pady = (30,30))  #pady for gap
        heading.configure(font = ("verdana",24,"bold"))

        label0 = Label(self.root, text="enter name")
        label0.pack(pady=(30, 30))

        self.name_input = Entry(self.root,width = 30)  #entry class
        self.name_input.pack(pady = (5,10),ipady = 10)

        label1 = Label(self.root,text = "enter email")
        label1.pack(pady = (30,30))

        self.email_input = Entry(self.root,width = 30)  #entry class
        self.email_input.pack(pady = (5,10),ipady = 10)  #for increase in y direction or length

        label2 = Label(self.root,text = "enter password")
        label2.pack(pady = (30,30))

        self.pswd_input = Entry(self.root,width = 30,show = "*")  #entry class
        self.pswd_input.pack(pady = (5,10),ipady = 10)

        register_btn = Button(self.root,text = "register",
        command = self.perform_registration)  #can give height to button not to entry box
        register_btn.pack(pady = (10,10))

        label3 = Label(self.root, text="already a member")
        label3.pack(pady=(30, 30))

        redirect_btn = Button(self.root,text = "login now",command =self.login_gui)
        redirect_btn.pack(pady = (10,10))


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        pswd= self.pswd_input.get()


        response = self.dbo.add_data(name,email,pswd)

        if response:
            messagebox.showinfo("success","reg successful.you can login now")
        else:
            messagebox.showerror("error","email exists")


    def perform_login(self):

        email = self.email_input.get()
        pswd = self.pswd_input.get()

        response = self.dbo.search(email,pswd)

        if response:
            messagebox.showinfo("success","login successful")
            self.home_gui()
        else:
            messagebox.showerror("error","incorrect email/password")

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPapp", bg="#3776ab", fg="white")

        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, "bold"))

        sentiment_btn = Button(self.root,text = "sentiment analysis",width = 30,height= 4,
        command = self.sentiment_gui)  #can give height to button not to entry box
        sentiment_btn.pack(pady = (10,10))

        ner_btn = Button(self.root, text="named entity revognition", width=30, height=4,
        command=self.perform_registration)  # can give height to button not to entry box
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text="emotion detection", width=30, height=4,
        command=self.perform_registration)  # can give height to button not to entry box
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="logout", command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPapp", bg="#3776ab", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, "bold"))

        heading = Label(self.root, text="NLPapp", bg="#3776ab", fg="white")
        heading.pack(pady=(10, 30))
        heading.configure(font=("verdana", 24, "bold"))

        label1 = Label(self.root, text="enter text")
        label1.pack(pady=(10, 30))

        self.sentiment_input = Entry(self.root, width=30)  # entry class
        self.sentiment_input.pack(pady=(5, 10), ipady=10)

        sentiment_btn = Button(self.root, text="analyze",
        command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text="",bg="#34495E",fg = "white")
        self.sentiment_result.pack(pady=(10, 30))
        self.sentiment_result.configure(font = ("verdana",16))


        goback_btn = Button(self.root, text="go back", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        print(result)

        txt = " "

        for i in result["sentiment"]:

            txt = txt + i+"->"+ str(result["sentiment"][i]) + "\n"
            print(i,result["sentiment"][i])

        self.sentiment_result["text"] = txt




nlp = NLPapp()



