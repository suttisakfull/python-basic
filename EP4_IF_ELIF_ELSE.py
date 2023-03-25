print("=========โปรแกรมตรวจสอบเงื่อนไข:============")
num = int(input("กรุณากรอกข้อมูลตัวเลขจำนวนเต็ม:"))

print("--------------------------------------------------")
# if (num > 20):
#     print("Process 1 Run")

if (num > 200):
    print(" num > 200: True precess: A")
elif (num == 200):
    print("num == 200: True process: B")
else:
    print("num < 200: True process: C")
    
print("-----------End Program -------------")