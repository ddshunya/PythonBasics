def add(num1, num2):
	return num1+num2

def subtract(num1, num2):
	return num1-num2

def multiply(num1, num2):
	return num1*num2
	
def division(num1, num2):
	return num1/num2
	

def start():
	myName = input("What is your name?")
	print("Hello " + myName)
	operation = input("Which operation would you like to perform? : ")
	
	if(operation == 'Add'):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(add(num1, num2))
		
	elif(operation == 'Subtract'):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(subtract(num1, num2))
		
	elif(operation == 'Multiply'):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(multiply(num1, num2))
		
	elif(operation == 'Division'):
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		print(division(num1, num2))
	
	else:
		print("Operation not supported")
		
start()