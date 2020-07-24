import smtplib
import tkinter as tk
from tkinter import *


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adithyahm7@gmail.com', 'gmailadi24')
    server.sendmail('adithyahm7@gmail.com', to, content)
    server.close()


class email(Tk):
    def __init__(self):
        super().__init__()
        self._frame = Frame(self)
        self._frame.pack()
        self.SEmail = StringVar()
        self.SPass = StringVar()
        self.msg = ''
        self.semail = Entry(self._frame, textvariable=self.SEmail, width=40)
        self.eLabel = Label(self._frame, text='Email : ')
        self.spass = Entry(self._frame, textvariable=self.SPass, width=30)
        self.pLabel = Label(self._frame, text='Password : ')
        self.lbtn = Button(self._frame,
                           text="Login",
                           width=20,
                           command=self.Login)
        self.semail.grid(row=2, column=1)
        self.eLabel.grid(row=2, column=0)
        self.spass.grid(row=4, column=1)
        self.pLabel.grid(row=4, column=0)
        self.lbtn.grid(row=6, column=1)
        self.sendframe = Frame(self)
        self.REmail = StringVar()

        self.remail = Entry(self.sendframe, textvariable=self.REmail, width=30)
        self.rLabel = Label(self.sendframe, text='Email : ')
        self.bLabel = Label(self.sendframe, text='Body : ')
        self.body = Text(self.sendframe, height=10, width=100)
        self.sbtn = Button(self.sendframe,
                           text="SEND",
                           width=20,
                           command=self.sendf)
        self.qbtn = Button(self.sendframe,
                           text='Quit',
                           command=quit)

        self.remail.grid(row=2, column=1)
        self.rLabel.grid(row=2, column=0)
        self.bLabel.grid(row=4, column=0)
        self.body.grid(row=4, column=1)
        self.sbtn.grid(row=6, column=1)
        self.qbtn.grid(row=6, column=0)
        if self.msg:
            Label(self.sendframe, text=self.msg).grid(row=5)

    def Login(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.semail.get(), self.spass.get())
        print("LOGGED IN")
        self.switch_frame(self.sendframe)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def sendf(self):
        self.server.sendmail(self.SEmail.get(), self.REmail.get(), self.body.get(1.0, 'end'))
        self.msg = f'Message Sent : [{self.REmail.get()}] : {self.body.get(1.0)}'
        print(self.msg)


if __name__ == "__main__":
    app = email()
    app.mainloop()
