import random

favorite_food = ["pizza", "burritos", "pancakes", "steak", "rice"]

print(favorite_food[1])

print(favorite_food[-1])

favorite_food.append("chicken")

print(favorite_food)

favorite_food.insert(0, "apple")

print(favorite_food)

favorite_food.remove("burritos")

print(favorite_food)

print(len(favorite_food))

def print_upper(list):
    for i in range(len(list)):
        print(list[i].upper())

print_upper(favorite_food)

print(favorite_food[0:6:5])

def contains_potato(list):
    b = False

    for i in range(len(list)):
        if list[i] == "potato":
            b = True
        
    if b == True:
        return print("A potato!")
    else:
        return print("No potato!")

    
foods = ["broccoli"]  

print(foods)
contains_potato(foods)




numbers = list(range(20))


def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(numbers):
    return numbers[::5] 

def reverse_and_stride(numbers):
    list = numbers[::-1]
    return list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])

print(numbers[1][1])

numbers.append([11,12,13])

print(numbers)

def sum_nested(list):
    rows = len(list)
    cols = len(list[0])
    i = 0
    total = 0 

    while i < rows:
        total = total + sum(list[i])
        i = i + 1
    
    return total


my_list = [
    [1,2],
    [3,4]
]

sum = sum_nested(my_list)

print(sum)


def five_by_five():
    list = []
    

    for i in range(5):
        row = []
        for j in range(5):
            num = random.randint(1, 25)
            row.append(num)
        
        list.append(row)

    return list

my_list = five_by_five()

print(my_list)

# notes on problem 3.4: I created a a function that generates a random list of numbers between 1 and 25
# Were they supposed to be random or not?
# Make sure to come back later to finish the rest of problem 3.4


ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

print(ages["Mira"])

ages["Milana"] = 52

print(ages)

del ages["Milana"]

print(ages)

for person in ages:
    print(person, "is", ages[person], "years old")



# Include code at the bottom of your file that calls this function and prints the result

for person in ages:
    print(person, "is", ages[person], "years old")
