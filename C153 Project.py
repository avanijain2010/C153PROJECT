from tkinter import *
import random
root = Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(bg="light blue")

entry = Entry(root)
entry.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root)
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label2 = Label(root)
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

array_3d = [[['1','2'],['king','queen'],['!','@']]]

def password_generator():
    label["text"] = "The Guessed Password : " + entry.get()
    random_no_1 = random.randint(0,1)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,1)
    
    letter1 =str(array_3d[0][0][random_no_1])
    letter2 =(array_3d[0][1][random_no_2])
    letter3 =(array_3d[0][2][random_no_3])
    label2["text"] = letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text="New Password", command = password_generator, bg = "light green")
btn.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()