# Basics
x=0
for x in range(151):
    print(x)
# multiples of 5
x=0
for x in range(5,1000,5):
    print(x)
# Counting, the Dojo way
x=0
for x in range(100):
    if x % 10==0:
        print("coding Dojo")
    elif x % 5==0:
        print("Coding")
    else:
        print(x)
# woah that suckers huge
x=0
for x in range(500000):
    if x % 2!=0:
        print(x)
# countdown by fours
for x in range(2018,0,-4):
    print(x)
# flexible counter
lowNum=1
highNum=200
mult=3
for x in range(lowNum,highNum):
    if x % mult == 0:
        print(x)