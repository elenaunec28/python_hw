# # Форматирование строки и целого числа
# name = "Alice"
# age = 30
# text = "My name is %s and I am %d years old." % (name, age)
# print(text)
#
# # Форматирование числа с плавающей точкой
# pi = 3.14159
# text = "The value of pi is approximately %.2f." % pi
# print(text)
# print(pi)

# name = "Alice"
# age = 30
# text = "My name is {} and I am {} years old."
# print(text.format(name, age))
# print(text.format(age, name))

# text = "My name is {name} and I am {age} years old. Are you also {age} years old?"
# # print(text.format(name="Bob", age=25))
# name = "Alice"
# print(text.format(name=name, age=25))
# print(text.format(name="Bob", age=22))
# print(text.format(name=name, age=33))

# text = "Her name is {1} and she is {0} years old. {1} loves Python."
# print(text.format(28, "Anna"))

# text = "The {0} is {color}."
# print(text.format("sky", color="blue"))
# # print(text.format(color="blue", "sky")) # error

# name = "Alice"
# age = 25
# text = f"My name is {name} and I am {age + 1} years old."
# text2 = f"My name is {name} and I am {age + 10} years old."
# print(text)

# x = 10
# y = 20
# text = f"The sum of {x} and {y} is {x + y}."
# print(text)

# text = "Python"
# text_info = f"The length of '{text}' is {len(text)} and its uppercase version is {text.upper()}."
# print(text_info)

# name = "Charlie"
# age = 30
# text = f"""Info
# Name: {name}
# Age: {age}
# """
# print(text)
numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]

print ("Изначальный список: ", numbers)
for i in range(numbers):
    print(numbers[i])
    if numbers[i] % 2 == 1:
        numbers[i] = numbers[i] ** 2
print ("Измененный список: ", numbers)