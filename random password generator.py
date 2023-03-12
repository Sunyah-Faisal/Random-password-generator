from tkinter import *
import random
import string

                                    ## button functions
def suggest():
    specChar = ['!', '$', '#', '%', '&', '*', '(', ')', '[', ']', '{', '}', '?']

    pwd = ""

    for i in range(100):
        if len(pwd) > 10:
            break
        else:
            num = str(random.randint(0, 9))
            alpha = random.choice(string.ascii_uppercase)
            char = random.choice(specChar)
            
            comb = [num+alpha+char, num+char+alpha, alpha+num+char, alpha+char+num, char+alpha+num, char+num+alpha]
            select = random.choice(comb)
            pwd = pwd + select

    pswrd.delete(0, END)
    pswrd.insert(0,pwd)

users = []
def save():
    ListName = name.get()
    ListPwd = pswrd.get()

    if ListName != '' and ListPwd != '':
        users.append([ListName, ListPwd])
        print(users)

                                    ## gui window
window = Tk()
window.title('Random password generator')
window.geometry('500x400')

inputs = LabelFrame(window, borderwidth = 0, highlightthickness  = 0)
inputs.pack(side='top')

nameLabel = Label(inputs, text = 'Name: ', font= ("Times New Roman",20,"bold"))
nameLabel.grid(row = 1 , column = 1 ,padx = 30, pady = 40)
name = Entry(inputs, font = ("Times New Roman",16))
name.grid(row = 1 , column = 2)

pwdLabel = Label(inputs, text = 'Password: ', font= ("Times New Roman",20,"bold"))
pwdLabel.grid(row = 2 , column = 1)
pswrd = Entry(inputs, font = ("Times New Roman",16))
pswrd.grid(row = 2 , column = 2)

buttons = LabelFrame(window , borderwidth = 0, highlightthickness  = 0)
buttons.pack(side='bottom')

btn1 = Button(buttons, text = 'suggest strong password', font= ("Times New Roman",16), command = suggest)
btn1.grid(row = 1, column = 1, padx = 50, pady = 10)

btn2 = Button(buttons, text = 'save', font= ("Times New Roman",16), command = save)
btn2.grid(row = 2, column = 1, pady = 30)

window.mainloop()
