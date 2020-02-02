from tkinter import*
import tkinter.messagebox

import picamera

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import RPi.GPIO as GPIO
import time


from time import sleep
from random import uniform


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#Blue LED
GPIO.setup(26, GPIO.OUT)

#Red LED
GPIO.setup(19, GPIO.OUT)

#Red Buzzer
GPIO.setup(17, GPIO.OUT)

#Yellow Buzzer
GPIO.setup(27, GPIO.OUT)


class MyGUI:
    def __init__(self):
        
        self.mw=Tk()

        self.mw.geometry("600x450+600+300")
        self.mw.title("Security")

        self.back = Frame(self.mw, width=600, height=450, bg="black")
        self.back.place(x=0, y=0)

##---------------------------------------------IN 1---------------------------------------------------------
        self.In1 = Frame(self.mw, width=580, height=430, bg="#458B74")
        self.In1.place(x=10, y=10)

        self.Entered1 = Label(self.In1, text="Welcome", font=("Arial",25, 'bold'), bg="#458B74", fg="black")
        self.Entered1.place(x=10, y=10)

        self.EnteredMessage11= Label(self.In1, text="Thank You For Signing Up!", font=("Arial",25), bg="#458B74", fg="black")
        self.EnteredMessage11.place(x=50, y=170)

        self.inLogOut1 = Button(self.In1, text="Log Out" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black",  command= self.LogOut)
        self.inLogOut1.place(x=30, y=350)

        self.InExit1 = Button(self.In1, text="Exit" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black",  command= self.mw.destroy)
        self.InExit1.place(x=380, y=350)
        
##---------------------------------------------IN 2---------------------------------------------------------
        self.In2 = Frame(self.mw, width=580, height=430, bg="#458B74")
        self.In2.place(x=10, y=10)

        self.Entered2 = Label(self.In2, text="Welcome", font=("Arial",25, 'bold'), bg="#458B74", fg="black")
        self.Entered2.place(x=10, y=10)

        self.EnteredMessage12= Label(self.In2, text="Please Give Me a Good Grade :)", font=("Arial",25), bg="#458B74", fg="black")
        self.EnteredMessage12.place(x=25, y=170)

        self.inLogOut2 = Button(self.In2, text="Log Out" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black",  command= self.LogOut)
        self.inLogOut2.place(x=30, y=350)

        self.InExit2 = Button(self.In2, text="Exit" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black",  command= self.mw.destroy)
        self.InExit2.place(x=380, y=350)

##---------------------------------------------Fail---------------------------------------------------------
        self.Fail = Frame(self.mw, width=580, height=430, bg="#458B74")
        self.Fail.place(x=10, y=10)

        self.Failed = Label(self.Fail, text="Notifying the User", font=("Arial",25, 'bold'), bg="#458B74", fg="black")
        self.Failed.place(x=10, y=10)

        self.FailedMessage1 = Label(self.Fail, text="Your image has been sent to the user to notify them of", font=("Arial",15), bg="#458B74", fg="black")
        self.FailedMessage1.place(x=10, y=100)

        self.FailedMessage2 = Label(self.Fail, text="your attempt to access of their account", font=("Arial",15), bg="#458B74", fg="black")
        self.FailedMessage2.place(x=10, y=130)

        self.failExit = Button(self.Fail, text="Exit" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black",  command= self.mw.destroy)
        self.failExit.place(x=30, y=350)



        
##----------------------------------------------Sign In--------------------------------------------------------------
        
        self.SIW = Frame(self.mw, width=580, height=430, bg="#458B74")
        self.SIW.place(x=10, y=10)

        self.siUserInVar = StringVar()
        self.siPassInVar = StringVar()

        self.triesVar = IntVar()
        self.triesVar.set(0)

        self.SignIn = Label(self.SIW, text="Sign In", font=("Arial",20, 'bold'), bg="#458B74", fg="black")
        self.SignIn.place(x=30, y=30)

        

        self.siUserName= Label(self.SIW, text="Username: ", font=("Arial", 15), bg="#458B74", fg="black")
        self.siUserName.place(x=30, y=100)

        self.siUserNameIn= Entry(self.SIW,width=25, font=("Arial", 13), textvariable=self.siUserInVar )
        self.siUserNameIn.place(x=250, y=100)


        
        self.siPass= Label(self.SIW, text="Password: ", font=("Arial", 15), bg="#458B74", fg="black")
        self.siPass.place(x=30, y=150)

        self.siPassIn= Entry(self.SIW,width=25, font=("Arial", 13), show="*", textvariable=self.siPassInVar )
        self.siPassIn.place(x=250, y=150)


        
        self.siSignUpButt = Button(self.SIW, text="Sign Up" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black",  command= self.SUWlift)
        self.siSignUpButt.place(x=30, y=350)

        self.siEnterButt = Button(self.SIW, text="Enter" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black", command=self.siEntered)
        self.siEnterButt.place(x=380, y=350)

##----------------------------------SIGN UP------------------------------------------------------
        
        self.SUW = Frame(self.mw, width=580, height=430, bg="#458B74")
        self.SUW.place(x=10, y=10)

        self.suUserInVar = StringVar()
        self.suPassInVar = StringVar()
        self.suPassreInVar = StringVar()
        self.suEmailInVar = StringVar()



        self.SignUp = Label(self.SUW, text="Sign Up", font=("Verdana",20, 'bold'), bg="#458B74", fg="black")
        self.SignUp.place(x=30, y=30)


        self.suUserName= Label(self.SUW, text="Username: ", font=("Arial", 15), bg="#458B74", fg="black")
        self.suUserName.place(x=30, y=100)

        self.suUserNameIn= Entry(self.SUW,width=25, font=("Arial", 13), textvariable=self.suUserInVar )
        self.suUserNameIn.place(x=250, y=100)



        self.suPass= Label(self.SUW, text="Password: ", font=("Arial", 15), bg="#458B74", fg="black")
        self.suPass.place(x=30, y=150)

        self.suPassIn= Entry(self.SUW,width=25, font=("Arial", 13), show="*", textvariable=self.suPassInVar )
        self.suPassIn.place(x=250, y=150)

           

        self.suPassRe= Label(self.SUW, text="Re-enter Password: ", font=("Arial", 15), bg="#458B74", fg="black")
        self.suPassRe.place(x=30, y=200)

        self.suPassreIn= Entry(self.SUW,width=25, font=("Arial", 13), show="*", textvariable=self.suPassreInVar )
        self.suPassreIn.place(x=250, y=200)

        
        self.suEmail= Label(self.SUW, text="E-mail: ", font=("Arial", 15), bg="#458B74", fg="black")
        self.suEmail.place(x=30, y=250)

        self.suEmailIn= Entry(self.SUW,width=25, font=("Arial", 13), textvariable=self.suEmailInVar )
        self.suEmailIn.place(x=250, y=250)    

        self.suSignInButt = Button(self.SUW, text="Sign In" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black", command= self.SIWlift)
        self.suSignInButt.place(x=30, y=350)

        self.suEnterButt = Button(self.SUW, text="Enter" , width=10, font=("Arial", 15, 'bold'), bg="#76EEC6", fg="black", command= self.suEntered)
        self.suEnterButt.place(x=380, y=350)     
        
        mainloop()
        
##-------------------------------------Sign Up-----------------------------------     
    
    def suEntered (self):
        
        suuser= self.suUserInVar.get()
        supass= self.suPassInVar.get()
        supassre=self.suPassreInVar.get()
        suemail= self.suEmailInVar.get()

        self.suEmailInVar.set(suemail)        

        if suuser =="" or supass=="" or supassre=="" or suemail=="":
            tkinter.messagebox.showinfo("!!!", "You are missing an information")
            
        elif supassre!=supass:
            tkinter.messagebox.showinfo("!!!", "Your password does not match")

        else:
            self.In1.lift()
            
##-------------------------------------Sign In-----------------------------------
            
    def siEntered (self):
        
        suuser= self.suUserInVar.get()
        supass= self.suPassInVar.get()
        
        fromaddr = 'final.proj.cmpt2200@gmail.com'
        toaddr = str(self.suEmailInVar.get())

        tries=self.triesVar.get()
        
        
        siuser= self.siUserInVar.get()
        sipass= self.siPassInVar.get()


        if siuser=="" or sipass=="":
            tkinter.messagebox.showinfo("!!!", "You are missing information")
            
        ##------------------------------------Tries-------------------------------
            
        elif siuser!=suuser or sipass!=supass:
            tries = self.triesVar.get()

            print(tries)
            
            if tries == 0:
                tkinter.messagebox.showinfo("!!!", "Your username or password is wrong" +'\n' + 'Attempts Left: 2')
                self.triesVar.set(+1)
               
             
                
            elif tries == 1:
                tkinter.messagebox.showinfo("!!!", "Your username or password is wrong" +'\n' + 'Attempts Left: 1'  )
                self.triesVar.set(+2)
                
                
            elif tries >= 2:
                tkinter.messagebox.showinfo("!!!", "You have no more attempts" )
               
                self.Fail.lift()

                #----------------------------taking picture----------------------------------

                with picamera.PiCamera() as camera:
                    camera.resolution = (1280, 720)
                    camera.capture("/home/pi/Desktop/FinalProj/intruder.jpg")
                    camera.close()

                #-----------------------------sending e-mail-----------------------------------
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = "Intruder"
                 

                body = "This person attempted to access your account."
                msg.attach(MIMEText(body, 'plain'))
                 

                filename = "intruder.jpg"
                attachment = open(filename, "rb")
                 

                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p) 
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                 
                msg.attach(p)


                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(fromaddr, "CMPT2200")
                text = msg.as_string()
                s.sendmail(fromaddr, toaddr, text)

                s.quit()

                ##--------------------------------------------------Alarm----------------------------------------------------------
                i=0
                while i <=5:
                    sleep(.5)
                    GPIO.output(17, True)
                    GPIO.output(27, True)
                    
                    GPIO.output(19, True)
                    GPIO.output(26, False)

                    sleep(.5)
                    GPIO.output(17, False)
                    GPIO.output(27, False)

                    GPIO.output(26, True)
                    GPIO.output(19, False)
                    i+=1

                GPIO.output(17, False)
                GPIO.output(27, False)
                GPIO.output(19, False)
                GPIO.output(26, False)

                GPIO.cleanup()

            
            
        elif siuser==suuser and sipass==supass:
                self.In2.lift()
                
##-----------------------------------------Frame Lifts---------------------------------------
    
    def SIWlift(self):
        self.SIW.lift()

    def SUWlift(self):
        self.SUW.lift()
        
    def LogOut (self):
        self.SIW.lift()

    def FailUp (self):
        self.Fail.lift()

    def Welcome1 (self):
        self.In1.lift()

    def Welcome2 (self):
        self.In2.lift()
        
my_gui=MyGUI()
    
