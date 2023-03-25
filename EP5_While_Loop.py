import time
num = int(input("กรุณากรอกข้อมูลตัวเลข:"))
print("ข้อมูลตัวเลขที่รับค่า:",num)

if(num <= 100):
     while (num <= 50):
         time.sleep(2)
         print("ข้อมูลน้อยกว่า 50 ทำการเพิ่มค่าภายใน loop: ",num)
         num = num + 1
    
     print("จบโปรแกรม :")
else:
    print("คุณกรอกข้อมูลเกิน 100:")