import pyautogui
from tkinter import Tk, Entry, Label, Button
# import pygame
from pyautogui import click, moveTo
from time import sleep

root = Tk()
# вырубаем защиту левого верхнего угла экрана
pyautogui.FAILSAFE = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
#пароль к данному приложению password

def checkpassword():
    if entry.get() == "password":
        root.destroy()
        root.quit()
    else:
        # pygame.init()
        # pygame.mixer.init()
        # pygame.mixer.music.load('music.mp3')
        # pygame.mixer.music.play()
        pass

root.title("Это недорой локер")
root.attributes("-fullscreen", True)
entry = Entry(root, font=10)
entry.place(width=500, height=70, x=width / 2 - 250, y=height / 2 - 75)

label0 = Label(root, text = "Таинственный хакер", font =("Arial", 15))
label0.place(width = 200, height = 100, x = width/2 - 50, y = height/3 - 50, )

button1 = Button(root, text = "Пиши пароль и нажми сюда", font = ("Arial", 15), command=checkpassword)
button1.place(width = 300, height = 100, x =width/2 - 50, y = height/5 )



root.configure(bg="black")
root.update()
root.mainloop()










