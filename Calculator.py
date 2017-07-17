def add(num1, num2):
	return num1+num2

def subtract(num1, num2):
	return num1-num2

def multiply(num1, num2):
	return num1*num2
	
def division(num1, num2):
	return num1/num2
	

def start():
	try:
		myName = input("What is your name?")
		print("Hello " + myName)
		operation = int(input("Which operation would you like to perform? (1-Add, 2-Subtract, 3-Multiply, 4-Divide) : "))
	except:
		print("Invalid Operation. Program will exit now")
		return

	if(operation == 1):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(add(num1, num2))
		
	elif(operation == 2):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(subtract(num1, num2))
		
	elif(operation == 3):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(multiply(num1, num2))
		
	elif(operation == 4):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(division(num1, num2))
		
start()