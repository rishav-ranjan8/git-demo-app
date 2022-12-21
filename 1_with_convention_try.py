
'''
# OBJECTIVE
 - Use logical names for Python functions, variables, methods, classes, modules and packages.
--
Function|Variables|Methods|Modules : Use a lowercase word or words. Separate words by underscores to improve readability.
e.g. employee_name, user_data
Class : Start each word with a capital letter. Do not separate words with underscores. It's called Pascal Case.
e.g. EmployeeInfo, Student
Package : Use a short, lowercase word or words. Do not separate words with underscores.
e.g. reporting, analytics
'''
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_op_1(self):
        return self.a + self.b
    
    def multiply(self):
        return self.a * self.b

    def get_diff(self):
        return self.a - self.b
    
    def calculate_quotient(self):
        return self.a / self.b

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operands = MyClass(num_1, num_2)
choice = 1
while choice != 0:
    print("Enter Choice of Arithmetic Operation")
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    choice = int(input("Enter choice: "))
    print(f"Entered choice is: {choice}")
    if choice == 1:
        print("Result: ", operands.my_op_1())
    elif choice == 2:
        print("Result: ", operands.get_diff())
    elif choice == 3:
        print("Result: ", operands.multiply())
    elif choice == 4:
        print("Result: ", round(operands.calculate_quotient(),2))
    elif choice == 0:
        print("Exiting!")
        print(f"Entered choice 0 to end program execution")
    else:
        print("Not a valid choice")
