num1 = 42
# - variable declaration
num2 = 2.3
# - variable declaration
boolean = True
# - Boolean
string = 'Hello World'
# string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# dict Boolian
fruit = ('blueberry', 'strawberry', 'banana')
# var 
print(type(fruit))
# Log statement
print(pizza_toppings[1])
# log statement number of toppings
pizza_toppings.append('Mushrooms')
# add mushrooms
print(person['name'])
# log statement var adn list
person['name'] = 'George'
# list add George
person['eye_color'] = 'blue'
print(fruit[2])
# - conditional
    # - if
    # - else if
    # - else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# - conditional
    # - if
    # - else if
    # - else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    # boolean

for x in range(5):
    print(x)
    # for loops
for x in range(2,5):
    print(x)
    # for loops
for x in range(2,10,3):
    print(x)
    # for loops
x = 0
# variable
while(x < 5):
    print(x)
    x += 1
    # while loops

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# for loop
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
        # function
                # function and for loop

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
        # function and for loop

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)