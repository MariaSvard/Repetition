# args, kwargs #

# def print_skill(*skills): # args
#         for skill in skills:
#             print(f"Skill {skill}")

# print_skill("Hacking", "Networking", "C programming")

# def display_profile(**info): # kwargs
#     for key, value in info.items():
#         print(f"{key.capitalize()}: {value}")
# display_profile(name= "Moa", age= 27, profession= "Cybersecurity Specialist")

# lambda #

# square = lambda x: x ** 2
# print(square(5))

# def multiplier(n):
#     return lambda x:x * n

# double = multiplier(2)

# print(double(5))

# map #

# numbers = [1, 2, 3, 4]
# squared_number = list(map(lambda x:x ** 2, numbers))
# print(squared_number)

# filter #

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x:x % 2 == 0, numbers))
# print(even_numbers)

# while True:
#     user_input = input("Name a integer number: ")
#     if user_input.isdigit():
#         user_number = int(user_input)
#         print("Thank you")
#         break
#     else:
#         print("This isn't a number!")

# try, except #

# try:
#     user_input = input("Type a number: ")
#     user_number = int(user_input) # användaren behöver skriva in ett nummer
#     print(f"You typed in number: {user_number}")

# except ValueError:
#     print("Unapproved input, type a number")

# input validering #

# valid_choices = ["red", "blue", "green"]
# while True:
#     user_input = input("Type a color: (red, blue, green)").lower()
#     if user_input in valid_choices:
#         print(f"You typed a valid color: {user_input}")
#         break
#     else:
#         print("Unvalid color, try again")

class Avatar:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and im {self.age} years old")
              
person1 = Avatar("Alice", 32)
person1.greet()