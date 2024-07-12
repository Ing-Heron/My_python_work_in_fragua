number = input("Input a number: ")
suma = 0
for numbers in number:
    suma += int(numbers) ** int(number[0])

if suma == int(number):
    print(f"Your number: {number} is a armstrong number")
else:
    print(f"Your number: {number} is not a armstrong number")
