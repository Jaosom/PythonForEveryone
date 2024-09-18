#สร้าง class ก้อใส่ keyword ว่า class
class Theater:
    # Attribute
    theaterName = 'Uncle Engineer Theater'
    #title = 'แฟนฉัน'
    #price = 80

    #Constructor ให้ใส่ __init__ ทำให้กำหนดค่าเองได้
    def __init__(self, title,price):
        self.title = title
        self.price = price

    # Method เป็น function ที่ผูกกับ object
    def hello(self):
        print('สวัสดีคุณลูกค้าทุกท่าน')

#วิธีการสืบทอดคลาส คลาสลูกสามารถให้ Attribute กับ Method คลาสแม่ได้
class Customer(Theater):
    #กำหนดแบบ constructor
    def __init__(self, fullname, age, title, price, seats):
        super().__init__(title, price)
        #self เป็นแยกขอบเขตของ parameter
        self.fullname = fullname
        self.age = age
        self.seats =seats
        self.money = 10000
    #เพิ่ม method คิดราคาตั๋ว
    def buyTicket(self):
        # คำนวนค่าตั๋ว
        self.total = self.price * self.seats
        # หักเงินจากลูกค้า
        self.money -= self.total

        print(f'ชื่อลูกค้า : {self.fullname}')
        print(f'อายุ : {self.age}')
        print(f'เรื่อง : {self.title}')
        print(f'ซื้อ : {self.seats} ที่นั่ง รวมเงิน {self.total}')
        print(f'เหลือเงิน : {self.money} บาท')

#ใส่ parameter 5 ตัว
custom01 = Customer('สมชาย สบายดี', 20 , 'ธี่หยด', 150 , 1)
#เรียกtheaterName เพราะ class customer สืบทอด attribute กับ method จากคลาส theaterName
print(custom01.theaterName)
custom01.hello()
custom01.buyTicket()
print('======================================')
#ลาก mouse คลุม แล้วกด ctrl+d
custom02 = Customer('สมปอง น้องสมชาย', 35 , 'สัปเหร่อ', 120 , 2)
#เรียกtheaterName เพราะ class customer สืบทอด attribute กับ method จากคลาส theaterName
print(custom02.theaterName)
custom02.hello()
custom02.buyTicket()
print('======================================')
custom03 = Customer('สมหญิง จริงใจ', 50 , 'เพื่อน(ไม่)สนิท', 80 , 5)
#เรียกtheaterName เพราะ class customer สืบทอด attribute กับ method จากคลาส theaterName
print(custom03.theaterName)
custom03.hello()
custom03.buyTicket()


#comment รวดเดียว ลากคลุมแล้วกด ctrl + /
'''    
movie01 = Theater('ธี่หยด', 150)
print(movie01.theaterName)
print(movie01.title)
print(movie01.price)
movie01.hello()
print('======================================')
movie02 = Theater('สัปเหร่อ', 120)
print(movie02.theaterName)
print(movie02.title)
print(movie02.price)
movie02.hello()
print('======================================')
movie03 = Theater('เพื่อน(ไม่)สนิท', 80)
print(movie03.theaterName)
print(movie03.title)
print(movie03.price)
movie03.hello()
'''



#สร้าง instant คือ ตัวแปรที่เป็น object ของ class
'''
movie01 = Theater()
print(movie01.theaterName)
print(movie01.title)
print(movie01.price)
movie01.hello()

movie02 = Theater()
print(movie02.theaterName)
print(movie02.title)
print(movie02.price)
movie02.hello()
'''
