# 1 Count Down
def CountDown(num):
    Newlist = []
    for x in range(num,-1,-1):
        Newlist.append(x)
    return Newlist
print(CountDown(15))
# 2 Print Return
def PrintReturn(list):
    print(list[0])
    return list [1]
print(PrintReturn([2,25]))
# 3 First Plus Length
def FirstPlusLength(list):
    print(list[0])
    return len(list)
print(FirstPlusLength([25,15,3,2,0]))
# 4 Values Greater Than Second
def ValuesGreaterThanSecond(list1):
    if len(list1)<2:
        return False
    list2 = []
    for value in list1:
        if value>list1[1]:
            list2.append(value)
    print(len(list2))
    return list2
print(ValuesGreaterThanSecond([35,55,25,15,0,2,3,17,23]))
print(ValuesGreaterThanSecond([1]))
# 5 Length and Value
def LengthAndValue(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(LengthAndValue(5,15))