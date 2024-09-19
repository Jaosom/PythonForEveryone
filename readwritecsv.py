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


def readcsv():
    with open('knowledge.csv',newline='',encoding='utf8') as file:
        fr = csv.reader(file)
        data = list(fr)
        print(data)

readcsv()
#d = ['lisa',16,500]
#writecsv(d)