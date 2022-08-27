import keyword
name, age = "Jamila", 20
pi = 3.14
numbers = [1, 2, 3, 4]

print(name)
print(age)
print(pi)
print(numbers)

#### dataTypes

brand = "Amigoscode"
age = 2
numbers = []
PI = 3.14
is_adult = True

print(type(brand))      # str
print(type(age))        # int
print(type(numbers))    # list
print(type(PI))         # float
print(type(is_adult))   # bool

#### dinamically typed -> data type of any variable is checked in during runtime

full_name: str = 'Felipe dos Santos'
is_good: bool = True

#### comments

"""
    I am a comment
"""

#### strings

print(brand.upper())
print(full_name.replace('F', 'f'))
print(len(brand))
print(brand == 'amigoscode')
print('code' in brand) # True

#### multiline and formatting strings

comment = "da ajjjsdolls " \
          "ksdkdkdkddk kdkdk" \
          "kjdjjk kdd dkkdlç ksd" \
          "ksks"
print(comment)

comment = """ 
da ajjjsdolls
ksdkdkdkddk kdkdk
kjdjjk kdd dkkdlç ksd
ksks
"""
print(comment)


email = """
hello {},
how are you?
It was nice talking to you
"""
print(email.format(full_name))

#### or

email = f"""
hello {full_name},
how are you?
It was nice talking to you
age {4+10}
"""
print(email)

#### reserved keywords
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#### arithmetic operators

result = 1 + 2
print(result)
print(8 - 4)
print(4 * 2)
print(4 ** 2)
print(10 / 2)
print(9 % 2)

#### comparison operators

print(10 > 5)
print(7 < 20)
print(15 != 20)
print(10 == 10)

#### logical operators

print(10 > 5 and 1 < 3 and "A" == "A")
print(10 < 5 or 1 > 3 or "A" == "a")
print(not("James" == "Maria"))

#### assignment operator

number = 10

number **= 3
print(number) # 1000

#### if statements

if (number > 0):
    print(f"number {number} is positive")
elif number == 0:
    print(number)
else:
    print(f"number {number} is negative")

#### ternary if statement
message = "positive" if number > 0 else "0 or negative"
print(message)

#### data structures

#### lists []

values = [10, 20, 30, 40, -90, [12, 15]]
print(values)
print(values[0])
print(values[5][0]) # 12

#### useful list methods
values = [10, 20, 30, 40, -90]
values.sort()
print(values)  # [-90, 10, 20, 30, 40]

values.reverse()
print(values)  # [40, 30, 20, 10, -90]

values.append(14)
print(values)  # [40, 30, 20, 10, -90, 14]

print(len(values)) # 6

# values.clear()
# print(values)  # []

print(40 in values) # True

#### deleting items from list

values.remove(40)
print(values) # [30, 20, 10, -90, 14]

values.pop()
print(values) # [30, 20, 10, -90]

del values[0]
print(values) # [20, 10, -90]

del values[0:2]
print(values) # [-90]

#### sets {} unordered

numbersList = [1, 1, 3, 2]      # [1, 1, 3, 2]
numbersSet = {1, 2, 1 , 2, 3}   # {1, 2, 3}

print(numbersList)
print(numbersSet)

### set union intersection and difference

lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "F", "A", "D"}

union = lettersA | lettersB
print(union) # {'A', 'E', 'B', 'F', 'D', 'C'}

intersection = lettersA & lettersB
print(intersection) # {'A', 'D'}

difference = lettersA - lettersB
print(difference) # {'B', 'C'}

# dictionaries

person = {
    "name" : "Jamal",
    "age" : 20,
    "address" : "USA"
}

print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys()) # dict_keys(['name', 'age', 'address'])
print(person.values()) # dict_values(['Jamal', 20, 'USA'])

person["age"] = 100

print(person["age"])

# person.clear()

print(person)


# for loop

names = [
    "James",
    "Mohammed",
    "Chris",
    "Layne",
    "Alanis"
]

for name in names:
    print(name)

### loop through dictionaries

for key in person:
    print(key)

for key in person:
    print(f"key:{key}, value:{person[key]}")

for key, value in person.items():
    print(f"key:{key} value:{value}")

# key:name, value:Jamal
# key:age, value:100
# key:address, value:USA

numbers = [1, 3, 5, 6, 7, 9]

soma = 0
for number in numbers:
    soma += number

print(f"Soma = {soma}")

### while

number = 0

while number < 10:
    print(number)
    number += 1
else:
    print("while loop ended")

### break and continue

# break
number = 0
while number < 10:
    if number == 5:
        break
    number += 1
    print(number)

# continue
number = 0
while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)

### functions

def greet():
    print("Hello, how you doin'?")

greet()

### parameters and arguments

def greet(name):
    print(f"Hello, {name}, how you doin'?")

greet("Felipe")

def greet2(name, age=-1):
    print(f"Hello, {name}, how you doin'?")
    if age >= 0:
        print(f"I know your age = {age}")

greet2("Felipe", 35)

greet2("Monica")

### return values from functions

def is_adult(age):
    return age >= 18

result = is_adult(10)
print(result)

def convert_gender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"

print(convert_gender("P"))




