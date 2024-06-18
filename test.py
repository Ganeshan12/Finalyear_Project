from tkinter import *
from PIL import Image, ImageTk
import random

IMAGE_PATH = 'images/background_hd.jpg'

class Struct(object):
    pass

def run(width=300, height=300):

    def init(data):
        # create 1000 rectangles in random position
        for _ in range(1000):
            x = random.randint(0, data.width)
            y = random.randint(0, data.height)
            data.data.append(canvas.create_oval(x, y, x+10, y+10, fill='red'))

    def mousePressedWrapper(event, canvas, data):
        #mousePressed(event, data)
        pass

    def keyPressedWrapper(event, canvas, data):
        #keyPressed(event, data)
        pass

    def timerFiredWrapper(canvas, data):
        # move objects
        for rect_id in data.data:
            x = random.randint(-2, 2)
            y = random.randint(-2, 2)
            canvas.move(rect_id, x, y)

        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    data.data = [] # place for small red rectangles

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()

    #canvas.create_rectangle(0, 0, data.width, data.height, fill='white', width=0)
    img = Image.open(IMAGE_PATH)
    img = img.resize((data.width, data.height))
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=photo, anchor='nw')

    init(data) # init after creating canvas because it create rectangles on canvas

    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)

    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 700)