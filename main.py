def month_number(num):
    return num
month = ['Jan', 'Feb','Mar','Apr', 'May', 'June','July','Aug','Sept', 'Oct', 'Nov', 'Dec']
try:
    num = int(input('Enter month number: '))
except ValueError:
    print ("Not number is entered, please try again...")
    pass
except IndexError:
    if num > 12:
        pass
finally:
    print ("Greetings, see you soon!!!")
print(month[num - 1])

#complete task 1#

from random import randrange
N = 15
list = [randrange(99) for i in range (N)]
print (*list)

Unique = True

for i in range (N - 1):
    for j in range (i+1, N):
        if list[i] == list[j]:
            Unique = False
if Unique:
    print("All elements are unique")
else:
    print("Found not unique element (((")
try:
    print(list[100])
except IndexError:
    print ("Sorry, our list is too short for such")

try:
    x = {"want to be added to list"}
    list[8].append (x)
except AttributeError:
    print ("Oh, cannot add num to such...")
try:
    a = input()
    b = a + list[8]
    print(b)
except TypeError:
    pass

#complete task 2 #

class FindAddress(object):
    def __init__(self, house):
        self.house = int(house)

    def my_house(self, house):
        self.house = house
        if not isinstance(house, int):
            raise TypeError("House number must be num")
        if not house in range(0, 1000):
            raise Exception("City numbers of houses do exceed 1000pcs....")

print(f"My house is {FindAddress(88)}")