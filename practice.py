import random
# Tax calculator

# amount = 200
# tax = .07
# total = amount + amount*tax

# print(total)

# store_name = "Sarah's store"
# print(store_name)

# hello = "Hello"
# name = input("What's your name?\n")

# greeting = hello + " " + name

# print(greeting)
# my_name = input("What's your name?")

# temp = int(input("What is the temperature?\n"))
# forecast = input("sunny or rain?\n")
# raining = True

# if temp > 80 or temp < 60:
#     print("Stay inside!")
# elif temp < 60:
#     print("It's too cold!\nStay inside!")
# else:
#     print("Enjoy the outdoors!")
# print("Have a good day!")

# if temp < 80 and forecast != "rain":
# if not forecast == "rain":
#     print("Go outside")
# else:
#     print("Stay inside")

# if not raining:
#     print("Go outside!")
# else:
#     print("Stay inside")

# roll = random.randint(1,6)
# guess = int(input('Guess the dice roll(1-6): '))

# if guess == roll:
#     print("Correct! They rolled a " + str(roll))
# else:
#     print("Wrong! they rolled a " + str(roll))

# print("The computer rolled a " + str(roll) + ".")

# acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
# word = 'BFN'

# if word in acronyms:
#     print(word + ' is in list')
# else:
#     print(word + ' is NOT in the list')

# for acronym in acronyms:
#     print(acronym)

# for i in range(7):
#     print(i)

acronyms = {'LOL': 'laugh out loud',
'IDK': "I don't know",
'TBH': 'to be honest'}

# print(acronyms)

# acronyms['TBH'] = 'honestly'

# print(acronyms)

# del acronyms['TBH']

# print(acronyms)

# Get a value that might not be there
# definition = acronyms.get('BTW')
# print(definition)

# if definition:
#     print(definition)
# else:
#     print("Key doesn't exist")

# sentence = 'IDK'+' what happened '+'TBH'
# translation = acronyms.get('IDK') +' what happend '+ acronyms.get('TBH')

# print(sentence)
# print(translation)

menus = {'Breakfast': ['Egg Sandwich', 'Bagel','Coffee'],
'Lunch': ['BLT', 'PB&J','Turkey Sandwich'],
'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']}

# for name, menu in menus.items():
#     print(name, ':', menu)

person = {'name': ' Sarah Smith',
'City': 'Orlando',
'age': '100'}

# print(person.get('name'), 'is', person.get('age'), 'years old.')

# people in space
# import requests
# response = requests.get('http://api.open-notify.org/astros.json')
# json = response.json()

# print('The people currently in space are:')
# for person in json['people']:
#     print(person['name'])
# # print(json)

# input_name = input('Enter your name:\n')

# def greeting(name):
#     print("Hello", name)

# greeting(input_name)

def addition(a, b):
    return a + b

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))

result = addition(num1,num2)

print("The result is", result)