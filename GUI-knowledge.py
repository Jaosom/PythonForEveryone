# import tkinterface มาก่อน
from tkinter import * # * คือ import all function inside main package
from tkinter import ttk
import csv
import os

#os.getcwd cwd = current working directory
path = os.getcwd()


noteicon = os.path.join(path,'noteicon.ico')


def writecsv(data):
    #csvfile ตัวแปรที่เก็บ os.path คือที่อยู่ของ file
    #join เชื่อมต่อ path,แล้วก้อ file 'knowledge.csv'
    #ใช้เครื่องอื่นจะไม่ error 
    csvfile = os.path.join(path,'knowledge.csv')
    # data = data มีลักษณะเป็น list ['john', 14, 500]
    # เปิด หรือสร้าง knowledge.csv 'a'ทำต่อกันไปเรื่อยๆ
    # ถ้าเป็น 'w' จะเป็นการทำครั้งเดียวเหมือนเขียนทับ
    # newline เป็นการขึ้นบรรทัดใหม่ '' ไม่มีช่องว่างระหว่างบรรทัด
    # encoding = 'utf-8' เป็นการเข้ารหัสทำให้ใช้ภาษาไทยได้ 
    with open('knowledge.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #FW = File Writer
        fw.writerow(data) #writerow ทำทีละบรรทัด

GUI = Tk() #Tk เป็น software หลัก เราจะดึงความสามารถของ Tk มาใช้
GUI.title('โปรแกรมบันทึกความรู้')
GUI.geometry('500x500')
GUI.iconbitmap(noteicon) #ใส่ รูป icon ในหัวโปรแกรม

F1 = Frame(GUI) #เอา GUI ไปใส่ในเฟรม ในตัวแปรชื่อ F1
F1.place(x=20,y=50)

#ตอนแรกใส่เป็น GUI ให้เปลี่ยนเป็น F1 ทั้งหมดเพราะเราเอาไปใส่ใน Frame แล้ว
L1 = ttk.Label(F1,text='หัวข้อความรู้',font=('Angsana New',16))
L1.pack()#pady = ระยะห่างของแกน y



#สร้างตัวแปรขึ้นมา เช่น v_title แล้วใส่ใน textvariable
#เป็นการเหมือนกับว่าถ้ามีใครพิมพ์ไรมาให้เก็บไว้ในตัวแปรชื่อ v_title
v_title = StringVar()

#ช่องกรอกข้อมูล width คือ กรอกได้กี่ตัวอักษร height คือ กี่บรรทัด
E1 = ttk.Entry(F1,textvariable=v_title,font=('Angsana New',20),width=50)
#grid = เหมือนตารางไว้ในตารางไหน 
#pack = อยู่ตรงกลาง
#place = กำหนดค่า x,y
E1.pack()

L2 = ttk.Label(F1,text='รายละเอียด',font=('Angsana New',16))
L2.pack()

T1 = Text(F1,font=('Angsana New',18),height=8,width=56)
T1.pack()

def save():
    title = v_title.get()
    textbox = T1.get(1.0,"end-1c")
    print('------------')
    print(title)
    print('------------')
    print(textbox)
    print('------------')
    #data = ตัวแปรด้านบน
    data = [title,textbox]
    writecsv(data)
    v_title.set('') #.set clear data after save
    T1.delete('1.0',END) #clear text box

#command=save ให้กดปุ่มแล้ว save
B1 = ttk.Button(F1,text='บันทึก',command=save)
B1.pack(pady=10,ipadx=20,ipady=10)


######################### Button Flash Card #################

def readcsv():
    with open('knowledge.csv',newline='',encoding='utf8') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data  ##เราจะไม่ print data แต่จะใช้ return แทน

knowledgelist = readcsv()
print(knowledgelist)

global countindex
countindex = 0

#สร้าง function ให้มันโชว์หน้าต่าง โชว์ความรู้ขึ้นมา
def Flashcard():
    knowledgelist = readcsv() 
    #ปิดหน้าต่าง flashcard แล้วเพิ่มข้อมูลจะได้ไม่ต้องปิดโปรแกรมแล้วเปิดใหม่
    GUI2 = Toplevel()
    GUI2.title('ทบทวนความรู้')
    GUI2.geometry('500x400')


    vtext_title = StringVar()
    vtext_detail = StringVar()
    title = ttk.Label(GUI2,textvariable=vtext_title,font=('Angsana New',20,'bold'))
    title.pack()
    vtext_title.set(knowledgelist[0][0])
    detail = ttk.Label(GUI2,textvariable=vtext_detail,font=('Angsana New',14))
    detail.pack()
    vtext_detail.set(knowledgelist[0][1].replace('\r',''))
    

    def Prev():
        global countindex
        if countindex == 0:
            countindex = countindex
        else:
            countindex = countindex - 1

        #set text
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('\r',''))

    def Next():
        global countindex
        if countindex == (len(knowledgelist)-1):
            countindex = len(knowledgelist)-1
        else:
            countindex = countindex + 1

        #set text
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('\r',''))

    BPrev = ttk.Button(GUI2,text='<',command=Prev)
    BPrev.place(x=170,y=350)
    BNext = ttk.Button(GUI2,text='>',command=Next)
    BNext.place(x=250,y=350)
    

    GUI2.mainloop()



notebutton = os.path.join(path,'note.png')
noteicon = PhotoImage(file=notebutton) 

#กด icon แล้วจะมีหน้าต่างใหม่ขึ้นมาที่เราสร้างเป็น GUI2 ที่อยู่ใน function Flashcard
BFlashcard = ttk.Button(GUI,image=noteicon,command=Flashcard)
BFlashcard.place(x=440,y=20)

GUI.mainloop() #mainloop คือทำให้ program run ตลอดโดยไม่ต้องปิดโปรแกรม

