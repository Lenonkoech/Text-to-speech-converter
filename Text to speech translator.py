# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:11:05 2023

@author: user
"""
#_*_import gTTs(google-text-to speech)_*_
from tkinter import*
import winsound
import gtts

root=Tk()
root.geometry('400x250')
root.configure(bg='#002')
root.resizable(False,False)
root.title('Text to Speech Translator.py')
Label(root,text="@Lenon's Project",font='chiller 13',foreground='gold',background='#002').pack(side='bottom')
Label(root,text="Text to speech Translator\nWith Python",font='castellar 14 ',fg='goldenrod',bg='#002').place(x=30,y=20)
Msg=StringVar()
Label(root,text='Enter your text BELOW:',bg='#002',fg='Olivedrab',font='forte 15').place(x=100,y=90)
entry_field=Entry(root,textvariable=Msg,width='60')
entry_field.place(x=20,y=130)
#_*_define play_*_
def Text_TO_Speech():
    Message=entry_field.get()
    speech=gtts.gTTS(text=Message)
    speech.save('Text_To_Speech.mp3')
    winsound.Playsound(sound='Text_To_Speech.mp3',flags=(0))
    #Default language is English
#_*_define reset_*_
def Reset():
    Msg.set("")
#define exit
def Exit():
    root.destroy()
Button(root,text='Play',width='6',font='chiller 11 bold',command=Text_TO_Speech).place(x=90,y=160)
Button(root,text='Reset',width='6',font='chiller 11 bold',command=Reset).place(x=175,y=160)
Button(root,text='Exit',width='6',font='chiller 11 bold',command=Exit).place(x=260,y=160)
root.mainloop()