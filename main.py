import random
from tkinter import *
from PIL import Image, ImageTk

from canara_bank import canra_bank
from iob import iob
from sbi import sbi

class Struct(object):
    pass
class iris_banking_multiple:

    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Iris Banking'
        self.titlec = 'IRIS BANKING'
        self.backround_color = '#2F4F4F'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd.jpg'

    def get_title(self):
        return self.title

    def get_titlec(self):
        return self.titlec

    def get_backround_color(self):
        return self.backround_color

    def get_text_color(self):
        return self.text_color

    def get_backround_image(self):
        return self.backround_image

    def set_window_design(self):
        root = Tk()

        w = 550
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        root.title(self.title)
        root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(280, 30, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)
        ################################################

        # def init(data):
        #     for _ in range(1000):
        #         x = random.randint(0, data.width)
        #         y = random.randint(0, data.height)
        #         data.data.append(canvas.create_line(x, y, x + 10, y + 10, fill='#202020'))
        # def mousePressedWrapper(event, canvas, data):
        #     pass
        # def keyPressedWrapper(event, canvas, data):
        #     pass
        # def timerFiredWrapper(canvas, data):
        #     for rect_id in data.data:
        #         x = random.randint(-10, 10)
        #         y = random.randint(-10, 10)
        #         canvas.move(rect_id, x, y)
        #     canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        # data = Struct()
        # data.width = 550
        # data.height = 600
        # data.timerDelay = 10  # milliseconds
        # data.data = []  # place for small red rectangles
        # for _ in range(100):
        #     x = random.randint(0, data.width)
        #     y = random.randint(0, data.height)
        #     data.data.append(canvas.create_line(x, y, x+10, y+10, fill='#404040'))
        # timerFiredWrapper(canvas, data)




        def clickHandler1(event):
            tt = canra_bank()
            tt.canara_login()
        image1 = Image.open('images/canara.png')
        img1 = image1.resize((100, 100))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(280, 110, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", clickHandler1)
        admin_id1 = canvas.create_text(280, 190, text="CANARA BANK", font=("Times New Roman", 18), fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", clickHandler1)
        def clickHandler2(event):
            tt = sbi()
            tt.sbi_login()
        image2 = Image.open('images/sbi.png')
        img2 = image2.resize((100, 100))
        my_img2 = ImageTk.PhotoImage(img2)
        image_id2 = canvas.create_image(280, 290, image=my_img2)
        canvas.tag_bind(image_id2, "<1>", clickHandler2)
        admin_id2 = canvas.create_text(280, 360, text="SBI", font=("Times New Roman", 18), fill=self.text_color)
        canvas.tag_bind(admin_id2, "<1>", clickHandler2)
        def clickHandler3(event):
            tt = iob()
            tt.iob_login()
        image3 = Image.open('images/iob.png')
        img3 = image3.resize((100, 100))
        my_img3 = ImageTk.PhotoImage(img3)
        image_id3 = canvas.create_image(280, 450, image=my_img3)
        canvas.tag_bind(image_id3, "<1>", clickHandler3)
        admin_id3 = canvas.create_text(280, 530, text="IOB", font=("Times New Roman", 18), fill=self.text_color)
        canvas.tag_bind(admin_id3, "<1>", clickHandler3)
        root.mainloop()




ar = iris_banking_multiple()
root = ar.set_window_design()
