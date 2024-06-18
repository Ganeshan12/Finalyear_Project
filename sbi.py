import time
from random import randint
from tkinter import Tk, messagebox, ttk
from tkinter import *
from tkinter.messagebox import askyesno
# import imagehash
from tkinter.ttk import Treeview

import cv2
import sys
import os
import datetime

import ar_master_iob
import ar_master_sbi
import sample
import ar_master_canara
from PIL import Image, ImageTk
mm= ar_master_sbi.master_flask_code()
class sbi:
    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Sbi Bank'
        self.titlec = 'SBI BANK'
        self.backround_color = '#2F4F4F'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd2.jpg'

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

    def sbi_login(self):
        care_taker_login_root = Toplevel()
        care_taker_login_root.attributes('-topmost', 'true')
        get_data = sbi()
        w = 780
        h = 500
        ws = care_taker_login_root.winfo_screenwidth()
        hs = care_taker_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        care_taker_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd2.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        care_taker_login_root.resizable(False, False)
        canvas1 = Canvas(care_taker_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="USER LOGIN", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Account No", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        def clickHandler1(event):
            tt = sbi()
            tt.user_registration()

        new_register_id = canvas1.create_text(440, 450, text="New Registration Here...", font=("Times New Roman", 24),
                                              fill=get_data.get_text_color())
        canvas1.tag_bind(new_register_id, "<1>", clickHandler1)
        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(490, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '), show="*")
        canvas1.create_window(490, 300, window=e2)

        def exit_program():
            a = e1.get()
            b = e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Account No", parent=care_taker_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=care_taker_login_root)
            else:
                qry = "SELECT * from user_details where account_no='" + str(a) + "' and password='" + str(b) + "'"
                result = mm.select_login(qry)
                if result == "no":
                    messagebox.showinfo("Result", "Login Failed", parent=care_taker_login_root)
                else:
                    def image_matching(a, b):
                        i1 = Image.open(a)
                        i2 = Image.open(b)
                        assert i1.mode == i2.mode, "Different kinds of images."
                        assert i1.size == i2.size, "Different sizes."

                        pairs = zip(i1.getdata(), i2.getdata())
                        if len(i1.getbands()) == 1:
                            # for gray-scale jpegs
                            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
                        else:
                            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

                        ncomponents = i1.size[0] * i1.size[1] * 3
                        xx = (dif / 255.0 * 100) / ncomponents
                        return xx

                    def match_templates(in_image):
                        name = []
                        values = []
                        entries = os.listdir('train/')
                        folder_lenght = len(entries)
                        i = 0
                        for x in entries:
                            val = 100
                            directory = x
                            name.append(x)
                            x1 = "train/" + x
                            arr = os.listdir(x1)
                            for x2 in arr:
                                path = x1 + "/" + str(x2)
                                find = image_matching(path, in_image)
                                if (find < val):
                                    val = find
                            values.append(val)
                        values_lenght = len(values)
                        pos = 0;
                        pos_val = 100
                        for x in range(0, values_lenght):
                            if values[x] < pos_val:
                                pos = x
                                pos_val = values[x]
                        if (pos_val < 15):
                            print(pos,pos_val,name[pos])
                            return name[pos]
                        else:
                            return "unknown"
                    messagebox.showinfo("Result", "Login Success", parent=care_taker_login_root)
                    cascPath = "haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(cascPath)
                    train = True
                    video_capture = cv2.VideoCapture(0)
                    name = "testing"
                    if os.path.exists(name):
                        h = 0;
                    else:
                        os.mkdir(name)
                    e_mail = 0
                    eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
                    status = True
                    while status:
                        ret, frame = video_capture.read()
                        frame1 = frame
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        ######
                        if (frame is None):
                            print("Can't open image file")
                        face_cascade = cv2.CascadeClassifier(cascPath)
                        faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
                        if (faces is None):
                            print('Failed to detect face')
                        else:
                            for (x, y, w, h) in faces:
                                ddd = 0
                            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
                            #############################################################################
                            i = 0
                            for (x, y, w, h) in eyes:
                                i = (len(eyes))
                                w1 = x
                                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                                img1 = frame[y:y + h, x:x + w]
                            #############################################################
                            height, width = frame1.shape[:2]
                            for (x, y, w, h) in faces:
                                r = max(w, h) / 2
                                centerx = x + w / 2
                                centery = y + h / 2
                                nx = int(centerx - r)
                                ny = int(centery - r)
                                nr = int(r * 2)
                                faceimg = frame1[ny:ny + nr, nx:nx + nr]
                                lastimg = cv2.resize(faceimg, (100, 100))
                                i += 1
                                str1 = name + '\\tt.jpg'
                                # kk=kk+1
                                cv2.imwrite(str1, lastimg)

                                ar = match_templates(str1)
                                if ar == "unknown":
                                    e_mail = 0
                                else:
                                    e_mail = e_mail + 1
                                if e_mail >= 1:
                                    dddd = 0

                                    dd = str(a)
                                    ar = str(ar)
                                    cv2.putText(frame, ar, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2,
                                                cv2.LINE_AA)

                                    if ar == dd:
                                        status = False
                                        video_capture.release()
                                        cv2.destroyAllWindows()
                                        care_taker_login_root.destroy()
                                        tt = sbi()
                                        tt.user_home(a)

                        cv2.imshow('Video', frame)

                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    video_capture.release()
                    cv2.destroyAllWindows()


        b1 = Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(490, 400, window=b1)
        care_taker_login_root.mainloop()
    def user_registration(self):
        user_registration_root = Toplevel()
        user_registration_root.attributes('-topmost', 'true')
        get_data = sbi()
        w = 780
        h = 500
        ws = user_registration_root.winfo_screenwidth()
        hs = user_registration_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_registration_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd2.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_registration_root.resizable(False, False)
        canvas1 = Canvas(user_registration_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
        #                     fill=get_data.get_text_color())
        ##
        maxin1 = mm.find_max_id("user_details")
        acc_no=randint(10000000, 100000000)
        acc="s"+str(acc_no)+""+str(maxin1)
        admin_id2 = canvas1.create_text(390, 20, text="USER REGISTRATION", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 70, text="Name", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 120, text="Contact", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 170, text="Email", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 220, text="Address", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 270, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 320, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 370, text="Account No", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 70, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 120, window=e2)
        e3 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 170, window=e3)
        e4 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 220, window=e4)
        e5 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 270, window=e5)
        e6 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 320, window=e6)
        e7 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 370, window=e7)
        e7.insert(0,str(acc))

        def exit_program():
            name = e1.get()
            contact = e2.get()

            email = e3.get()
            address = e4.get()
            username = e5.get()
            password = e6.get()
            account_no = e7.get()




            if (name == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=user_registration_root)
            elif (contact == ""):
                messagebox.showinfo(title="Alert", message="Enter Contact", parent=user_registration_root)
            elif (email == ""):
                messagebox.showinfo(title="Alert", message="Enter Email", parent=user_registration_root)
            elif (address == ""):
                messagebox.showinfo(title="Alert", message="Enter Address", parent=user_registration_root)
            elif (username == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=user_registration_root)
            elif (password == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=user_registration_root)
            else:
                maxin = mm.find_max_id("user_details")
                # print(account_no)
                qry="insert into user_details(id,name,contact,email,address,username,password,account_no,balance,report) values('"+str(maxin)+"','"+str(name)+"','"+str(contact)+"','"+str(email)+"','"+str(address)+"','"+str(username)+"','"+str(password)+"','"+str(account_no)+"','0','0')"

                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Registration Success", parent=user_registration_root)


                cascPath = "haarcascade_frontalface_default.xml"
                eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
                faceCascade = cv2.CascadeClassifier(cascPath)
                train = True
                video_capture = cv2.VideoCapture(0)
                name = "train"
                if os.path.exists(name):
                    h = 0;
                else:
                    os.mkdir(name)
                s1 = str(account_no)
                name1 = "train\\" + str(s1)
                if os.path.exists(name1):
                    j = 0;
                else:
                    os.mkdir(name1)
                k = 0
                while True:
                    ret, frame = video_capture.read()
                    frame1 = frame
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    if (frame is None):
                        print("Can't open image file")
                    face_cascade = cv2.CascadeClassifier(cascPath)
                    faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
                    if (faces is None):
                        print('Failed to detect face')
                    else:
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
                        i = 0
                        for (x, y, w, h) in eyes:
                            i = (len(eyes))
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        for (x, y, w, h) in faces:
                            r = max(w, h) / 2
                            centerx = x + w / 2
                            centery = y + h / 2
                            nx = int(centerx - r)
                            ny = int(centery - r)
                            nr = int(r * 2)
                            faceimg = frame1[ny:ny + nr, nx:nx + nr]
                            lastimg = cv2.resize(faceimg, (100, 100))
                            i += 1
                            k += 1
                            if ((k <= 20) & (k >= 5)):
                                str1 = name1 + '\\%d.jpg' % k
                                cv2.imwrite(str1, lastimg)

                    cv2.imshow('Video', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                video_capture.release()
                cv2.destroyAllWindows()

                user_registration_root.destroy()

        b1 = Button(canvas1, text="Register", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 420, window=b1)
        user_registration_root.mainloop()

    def user_home(self, account_no):
        user_home_root = Toplevel()
        w = 950
        h = 600
        ws = user_home_root.winfo_screenwidth()
        hs = user_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        user_home_root.title(self.title)
        user_home_root.resizable(False, False)
        # bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(user_home_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(470, 40, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)

        def deposit(event):
            tt = sbi
            tt.user_deposit(event, account_no)

        image = Image.open('images/deposit.png')
        img = image.resize((100, 100))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(350, 170, image=my_img)
        canvas.tag_bind(image_id, "<1>", deposit)
        admin_id = canvas.create_text(520, 170, text="DEPOSIT", font=("Times New Roman", 15), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", deposit)

        def withdraw(event):
            tt = sbi
            tt.user_withdraw(event, account_no)

        image2 = Image.open('images/withdrw.png')
        img2 = image2.resize((100, 100))
        my_img2 = ImageTk.PhotoImage(img2)
        image_id2 = canvas.create_image(350, 270, image=my_img2)
        canvas.tag_bind(image_id2, "<1>", withdraw)

        admin_id1 = canvas.create_text(520, 270, text="WITHDRAW", font=("Times New Roman", 15), fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", withdraw)

        ###########################
        def transaction(event):
            tt = sbi
            tt.user_transaction(event, account_no)

        image1 = Image.open('images/transaction.png')
        img1 = image1.resize((100, 100))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(350, 370, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", transaction)
        admin_id = canvas.create_text(520, 370, text="TRANSACTION", font=("Times New Roman", 15), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", transaction)

        # ################################
        def mini(event):
            tt = sbi
            tt.user_ministatement(event, account_no)

        admin_id1 = canvas.create_text(520, 470, text="MINI STATEMENT", font=("Times New Roman", 15),
                                       fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", mini)
        image3 = Image.open('images/mini.png')
        img3 = image3.resize((100, 100))
        my_img3 = ImageTk.PhotoImage(img3)
        image_id3 = canvas.create_image(350, 480, image=my_img3)
        canvas.tag_bind(image_id3, "<1>", mini)
        user_home_root.mainloop()
    def user_deposit(self,account_no):
        user_deposit_root = Toplevel()
        get_data = sbi()
        user_deposit_root.attributes('-topmost', 'true')
        w = 550
        h = 350
        ws = user_deposit_root.winfo_screenwidth()
        hs = user_deposit_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_deposit_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        user_deposit_root.title(get_data.get_title())
        user_deposit_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        canvas = Canvas(user_deposit_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(280, 70, text="DEPOSIT", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 140, text="Amount", font=("Times New Roman", 24),fill=get_data.get_text_color())
        e1 = Entry(user_deposit_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 140, window=e1)
        def select_image():
            amount=int(e1.get())
            qry="select balance from user_details where account_no='" + str(account_no) + "'"
            data=mm.select_direct_query(qry)
            bal = int(data[0][0]) + int(amount)
            mm.insert_query("update user_details set balance='" + str(bal) + "' where account_no='" + str(account_no) + "'")
            process = "Deposit"
            date = datetime.datetime.today()
            time = date.strftime("%I:%M %p")
            date=datetime.datetime.now().date()

            mm.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','-','" + str(date) + "','" + str(time) + "','" + str(account_no) + "')")
            messagebox.showinfo(title='message', message='success',parent=user_deposit_root)
            user_deposit_root.destroy()
        b1 = Button(user_deposit_root, text='Deposit', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 230, window=b1)
        user_deposit_root.mainloop()
    def user_withdraw(self,account_no):
        user_withdraw_root = Toplevel()
        get_data = sbi()
        user_withdraw_root.attributes('-topmost', 'true')
        w = 550
        h = 350
        ws = user_withdraw_root.winfo_screenwidth()
        hs = user_withdraw_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_withdraw_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        user_withdraw_root.title(get_data.get_title())
        user_withdraw_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        canvas = Canvas(user_withdraw_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(280, 70, text="WITHDRAW", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 140, text="Amount", font=("Times New Roman", 24),fill=get_data.get_text_color())
        e1 = Entry(user_withdraw_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 140, window=e1)
        def select_image():
            amount=int(e1.get())
            qry="select balance from user_details where account_no='" + str(account_no) + "'"
            data=mm.select_direct_query(qry)
            xx=int(data[0][0])
            if amount<=xx:
                bal = int(data[0][0]) - int(amount)
                mm.insert_query(
                    "update user_details set balance='" + str(bal) + "' where account_no='" + str(account_no) + "'")
                process = "Withdraw"
                date = datetime.datetime.today()
                time = date.strftime("%I:%M %p")
                mm.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','-','" + str(date) + "','" + str(time) + "','" + str(account_no) + "')")
                messagebox.showinfo(title='message', message='success', parent=user_withdraw_root)
                user_withdraw_root.destroy()
            else:
                messagebox.showinfo(title='message', message='Low Balance', parent=user_withdraw_root)
        b1 = Button(user_withdraw_root, text='Withdraw', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 230, window=b1)
        user_withdraw_root.mainloop()
    def user_transaction(self,account_no):
        user_transaction_root = Toplevel()
        get_data = sbi()
        user_transaction_root.attributes('-topmost', 'true')
        w = 550
        h = 350
        ws = user_transaction_root.winfo_screenwidth()
        hs = user_transaction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_transaction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        user_transaction_root.title(get_data.get_title())
        user_transaction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        canvas = Canvas(user_transaction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(280, 70, text="TRANSACTION", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 140, text="Amount", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 180, text="Account No", font=("Times New Roman", 24),fill=get_data.get_text_color())
        e1 = Entry(user_transaction_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 140, window=e1)
        e2 = Entry(user_transaction_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 180, window=e2)
        def canara_bank(sender,receiver,amount):


            qry = "select balance from user_details where account_no='" + str(account_no) + "'"
            data = mm.select_direct_query(qry)

        def select_image():
            amount=int(e1.get())
            receiver=str(e2.get())
            if amount=="":
                messagebox.showinfo("Alert","Enter Amount")
            elif receiver=="":
                messagebox.showinfo("","Enter Account No")
            else:
                qry = "select balance from user_details where account_no='" + str(account_no) + "'"
                data = mm.select_direct_query(qry)
                xx = int(data[0][0])
                if amount <= xx:
                    bal = int(data[0][0]) - int(amount)
                    mm.insert_query("update user_details set balance='" + str(bal) + "' where account_no='" + str(account_no) + "'")
                    process = "Debit"
                    date = datetime.datetime.today()
                    time = date.strftime("%I:%M %p")
                    mm.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','" + str(receiver) + "','" + str(date) + "','" + str(time) + "','" + str(account_no) + "')")

                    mm_canara = ar_master_canara.master_flask_code()
                    mm_iob = ar_master_iob.master_flask_code()
                    mm_sbi = ar_master_sbi.master_flask_code()
                    qry = "select balance from user_details where account_no='" + str(receiver) + "'"

                    canara = mm_canara.select_direct_query(qry)
                    iob = mm_iob.select_direct_query(qry)
                    sbi = mm_sbi.select_direct_query(qry)
                    if canara:
                        qry = "select balance from user_details where account_no='" + str(receiver) + "'"
                        data = mm_canara.select_direct_query(qry)
                        if len(data) > 0:
                            bal = int(data[0][0]) + int(amount)
                            mm_canara.insert_query("update user_details set balance='" + str(bal) + "' where account_no='" + str(receiver) + "'")
                            process = "Credit"
                            date = datetime.datetime.today()
                            time = date.strftime("%I:%M %p")
                            mm_canara.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','" + str(account_no) + "','" + str(date) + "','" + str(time) + "','" + str(receiver) + "')")
                            messagebox.showinfo(title='message', message='success', parent=user_transaction_root)
                            user_transaction_root.destroy()
                    elif iob:
                        qry = "select balance from user_details where account_no='" + str(receiver) + "'"
                        data = mm_iob.select_direct_query(qry)
                        if len(data) > 0:
                            bal = int(data[0][0]) + int(amount)
                            mm_iob.insert_query("update user_details set balance='" + str(bal) + "' where account_no='" + str(receiver) + "'")
                            process = "Credit"
                            date = datetime.datetime.today()
                            time = date.strftime("%I:%M %p")
                            mm_iob.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','" + str(account_no) + "','" + str(date) + "','" + str(time) + "','" + str(receiver) + "')")
                            messagebox.showinfo(title='message', message='success', parent=user_transaction_root)
                            user_transaction_root.destroy()
                    elif sbi:
                        qry = "select balance from user_details where account_no='" + str(receiver) + "'"
                        data = mm_sbi.select_direct_query(qry)
                        if len(data) > 0:
                            bal = int(data[0][0]) + int(amount)
                            mm_sbi.insert_query("update user_details set balance='" + str(bal) + "' where account_no='" + str(receiver) + "'")
                            process = "Credit"
                            date = datetime.datetime.today()
                            time = date.strftime("%I:%M %p")
                            mm_sbi.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','" + str(account_no) + "','" + str(date) + "','" + str(time) + "','" + str(receiver) + "')")
                            messagebox.showinfo(title='message', message='success', parent=user_transaction_root)
                            user_transaction_root.destroy()
                    else:
                        messagebox.showinfo(title='message', message='Check Accont No', parent=user_transaction_root)
                else:
                    messagebox.showinfo(title='message', message='Low Balance', parent=user_transaction_root)

        b1 = Button(user_transaction_root, text='Transfer', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 230, window=b1)
        user_transaction_root.mainloop()
    def user_ministatement(self,account_no):
        user_transaction_root = Toplevel()
        get_data = sbi()
        user_transaction_root.attributes('-topmost', 'true')
        w = 650
        h = 350
        ws = user_transaction_root.winfo_screenwidth()
        hs = user_transaction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_transaction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        user_transaction_root.title(get_data.get_title())
        user_transaction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd2.jpg')
        canvas = Canvas(user_transaction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(310, 70, text="MINI STATEMENT", font=("Times New Roman", 24),fill=get_data.get_text_color())
        fram = Frame(canvas)
        fram.place(x=60, y=100, width=550, height=230)
        scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
        scrollbary = Scrollbar(fram, orient=VERTICAL)
        tree = Treeview(fram, columns=("process", "amount", "accnumber", "date", "time"), yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        tree.heading('process', text="process", anchor=W)
        tree.heading('amount', text="amount", anchor=W)
        tree.heading('accnumber', text="accnumber", anchor=W)
        tree.heading('date', text="date", anchor=W)
        tree.heading('time', text="time", anchor=W)
        tree.column('#0', width=0)
        tree.column('#1', width=100)
        tree.column('#2', width=100)
        tree.column('#3', width=100)
        tree.column('#4', width=100)
        tree.pack()
        d1=mm.select_direct_query("select * from mini where  my_account='" + str(account_no) + "'")
        for data in d1:
            tree.insert("", 0, values=data)
        bb = mm.select_direct_query("select balance from user_details where account_no='" + str(account_no) + "'")
        admin_id2 = canvas.create_text(510, 20, text="Balance : "+str(bb[0][0]), font=("Times New Roman", 18),
                                       fill=get_data.get_text_color())
        user_transaction_root.mainloop()