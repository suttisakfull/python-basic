import math

x = 5
y = 2

#z = x + y
print("--------------------------------------------------")
print("ชนิดข้อมูล:",type(x),"\tข้อมูลคือ: x = ",x)
print("ชนิดข้อมูล:",type(y),"\tข้อมูลคือ: y = ",y)
print("--------------------------------------------------")
print("x + y :",(x + y))
print("x - y :",(x - y))
print("x * y :",(x * y))
print("x / y :",(x / y))
print("x % y :",( x % y))
print("x ** y :",(x ** y))
print("x // y :",(x // y)) # หารไม่เอาเศษ
print("square root x:",round(math.sqrt(x),5))
print("พื้นที่วงกลม: x",round(math.pi*x**2,2))

#round(สูตร,5)
