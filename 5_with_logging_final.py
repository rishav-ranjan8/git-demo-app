# add comment from feature
'''
# OBJECTIVE
 - Use logging to track events during program execution
--
Logging is a means of tracking events that happen when some software runs.
The software developer adds logging calls to their code to indicate that certain events have occurred.
Log Levels : NOTSET | DEBUG | INFO | WARNING | ERROR | CRITICAL
'''
# add a dummy comment
# Initialize logger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set Log Format
log_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(message)s', '%d-%b-%y %H:%M:%S')

# Create File Handler for logs
file_handler = logging.FileHandler("logs/calculator.log")
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

# Create Console Handler for logs
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)

class Calculator:
    '''
    A class to perform arithmetic operations.
    ...
    Attributes
    ----------
    operand_1 : int
        - First operand required for arithmetic operation
    operand_2 : int
        - Second operand required for arithmetic operation
    
    Methods
    -------
    calculate_sum():
        Takes in two numbers, returns their sum.
    calculate_product():
        Takes in two numbers, returns their product.
    calculate_difference():
        Takes in two numbers, returns their difference.
    calculate_quotient():
        Takes in two numbers, returns their quotient.
    '''
    def __init__(self, operand_1, operand_2):
        self.operand_1 = operand_1
        self.operand_2 = operand_2

    def calculate_sum(self):
        logger.debug(f"Inside calculate_sum method for calculating sum of operands. Hurray")
        return self.operand_1 + self.operand_2
    
    def calculate_product(self):
        logger.debug(f"Inside calculate_product method for calculating product of operands")
        return self.operand_1 * self.operand_2

    def calculate_difference(self):
        logger.debug(f"Inside calculate_difference method for calculating difference of operands")
        return self.operand_1 - self.operand_2
    
    def calculate_quotient(self):
        logger.debug(f"Inside calculate_quotient method for calculating quotient of operands")
        return self.operand_1 / self.operand_2

def display_result(operand_1, operand_2, operation, result):
    print("#### Output ####")
    print(f"{operation} of {operand_1} and {operand_2} is {result}")
    print("################")

try:
    # Uncomment below line to print Documentation of Calculator class
    # print(Calculator.__doc__)
    try:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
    except ValueError as e:
        logger.error(f"Atleast one of the entered inputs is not a number.")
        raise
    operands = Calculator(num_1, num_2)
    choice = 1
    while choice != 0:
        print("Enter Choice of Arithmetic Operation")
        print("0. Exit")
        print("1. Add")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        try:
            try:
                choice = int(input("Enter choice: "))
                logger.info(f"Entered choice is: {choice}")
            except ValueError:
                raise TypeError("Only numbers are allowed")
            if choice == 1:
                # print("Result: ", operands.calculate_sum())
                display_result(num_1, num_2, "Summation", operands.calculate_sum())
            elif choice == 2:
                # print("Result: ", operands.calculate_difference())
                display_result(num_1, num_2, "Difference", operands.calculate_difference())
            elif choice == 3:
                # print("Result: ", operands.calculate_product())
                display_result(num_1, num_2, "Multiplication", operands.calculate_product())
            elif choice == 4:
                # print("Result: ", round(operands.calculate_quotient(),2))
                display_result(num_1, num_2, "Division", operands.calculate_quotient())
            elif choice == 0:
                print("Exiting!")
                logger.info(f"Entered choice 0 to end program execution")
            else:
                raise ValueError("Not a valid choice")
        except TypeError as type_err:
            logger.error(f"Not a valid choice type: {type_err}")
        except ValueError as val_err:
            logger.error(f"Value of Choice should be between 0 and 4. Entered Value is: {choice}")
        except Exception as err:
            print(f"Encountered exception: {err}")
            raise
except Exception as err:
    print(f"Encountered exception: {err} while running calculator")

# end of file

