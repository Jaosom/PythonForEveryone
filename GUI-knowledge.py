# import tkinterface มาก่อน
from tkinter import * # * คือ import all function inside main package
from tkinter import ttk
import csv

def writecsv(data):
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

L1 = ttk.Label(GUI,text='หัวข้อความรู้',font=('Angsana New',16))
L1.pack()



#สร้างตัวแปรขึ้นมา เช่น v_title แล้วใส่ใน textvariable
#เป็นการเหมือนกับว่าถ้ามีใครพิมพ์ไรมาให้เก็บไว้ในตัวแปรชื่อ v_title
v_title = StringVar()

#ช่องกรอกข้อมูล width คือ กรอกได้กี่ตัวอักษร height คือ กี่บรรทัด
E1 = ttk.Entry(GUI,textvariable=v_title,font=('Angsana New',20),width=50)
#grid = เหมือนตารางไว้ในตารางไหน 
#pack = อยู่ตรงกลาง
#place = กำหนดค่า x,y
E1.pack()

L2 = ttk.Label(GUI,text='รายละเอียด',font=('Angsana New',16))
L2.pack()

T1 = Text(GUI,font=('Angsana New',18),height=8,width=56)
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
B1 = ttk.Button(GUI,text='บันทึก',command=save)
B1.pack(pady=10,ipadx=20,ipady=10)


GUI.mainloop() #mainloop คือทำให้ program run ตลอดโดยไม่ต้องปิดโปรแกรม

