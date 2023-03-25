#============= FOR ============
#  for x in range(start,stop,step):

'''
for i in range(0,(100+1),5):
   print("Hello World อิอิอิ: ",i)
'''
'''
2X1 = 2
2X2 = 4
2X3 = 6
...
2X12 = 24

'''

#print("โปรแกรม สูตร:")
'''
print("2 X 1",":",(1*2))
print("2 X 2",":",(2*2))
print("2 X 3",":",(3*2))
print("2 X 4",":",(4*2))
print("2 X 5",":",(5*2))
print("2 X 6",":",(6*2))
print("2 X 7",":",(7*2))
print("2 X 8",":",(8*2))
print("2 X 9",":",(9*2))
print("2 X 10",":",(10*2))
print("2 X 11",":",(11*2))
print("2 X 12",":",(12*2))
'''
''' 
num = 5 

for i in range(1,(12+1),1):
    print(":",num,"X",i,":",num*i)
'''
'''
num = int(input("รับค่าตัวเลข แม่สูตรคูณ :"))
for i in range(1,(12+1),1):
    print(":",num,"X",i,":",num*i)

print("จบโปรแกรม อิอิอิอิ:")
'''

'''
num2 = 2
for i in range(1,(12+1),1):
    print(":",num2,"X",i,":",num2*i)
print("================================")
num3 = 3
for i in range(1,(12+1),1):
    print(":",num3,"X",i,":",num3*i)
print("================================")
num4 = 4
for i in range(1,(12+1),1):
    print(":",num4,"X",i,":",num4*i)
print("================================")
num5 = 5
for i in range(1,(12+1),1):
    print(":",num5,"X",i,":",num5*i)
print("จบโปรแกรม อิอิอิอิ:")
'''

'''
import time

print("===========โปรแกรมแม่สูตรคูณ:==============")

num_start = int(input("แม่สูตรคูณเริ่มต้น: "))
num_stop = int(input("แม่สูตรคูณเริ่มสิ้นสุด: "))

print("=========================================")
for i in range(num_start,(num_stop+1),1):
    print("แม่สูตรคูณ:", i)
    time.sleep(1)
    for j in range(1,(12+1),1):
        print("  :",j,"X",i,":",j*i)
        time.sleep(0.5)
    print("=====================================")
'''

colors = ["red",'green','blue','black','white','pink','brow']

for item in colors:
    if (item == 'black'):
        print(item)

print('--------------------')       