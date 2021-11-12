from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry('400x400')
root.title('Roll the Dice')

l0 = Label(root)
l0.pack()

l1 = Label(root, fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
l1.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = Label(root, image=image1)
label1.image = image1

label1.pack( expand=True)

my_btn = Button(root, text = "Exit", command = root.quit).pack()
# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1


# exit button
button = Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)


button.pack( expand=True)

root.mainloop()
