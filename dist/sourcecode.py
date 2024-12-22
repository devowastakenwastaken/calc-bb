import math

def shell():
    while True:
        command = input(">> ")
        if command.lower() == "exit":
            break
        
        elif command.lower() == ("sqrt"):
            num = float(input("Enter a number: "))
            print(math.sqrt(num))
            
        elif command.lower() == ("fact"):
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(round(math.factorial(num)))
                
        elif command.lower() == ("log"):
            base = float(input("Enter the base: "))
            num = float(input("Enter the number: "))
            if base == 1:
                print("Logarithm base 1 is not defined.")
            elif num <= 0:
                print("Logarithm is not defined for non-positive numbers.")
            else:
                print(math.log(num, base))
                
        elif command.lower() == ("sin"):
            angle = float(input("Enter the angle in degrees: "))
            print(math.sin(math.radians(angle)))
            
        elif command.lower() == ("cos"):
            angle = float(input("Enter the angle in degrees: "))
            print(math.cos(math.radians(angle)))
            
        elif command.lower() == ("tan"):
            angle = float(input("Enter the angle in degrees: "))
            print(math.tan(math.radians(angle)))
            
        elif command.lower() == ("pi"):
            print(math.pi)
            
        elif command.lower() == ("e"):
            print(math.e)
            
        elif command.lower() == ("abs"):
            num = float(input("Enter a number: "))
            print(abs(num))
            
        elif command.lower() == ("floor"):
            num = float(input("Enter a number: "))
            print(math.floor(num))
            
        elif command.lower() == ("ceil"):
            num = float(input("Enter a number: "))
            print(math.ceil(num))
            
        elif command.lower() == ("pow"):
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print(math.pow(base, exponent))
            
        elif command.lower() == ("gcd"):
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(math.gcd(num1, num2))
            
        elif command.lower() == ("lcm"):
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(math.lcm(num1, num2))
            
        elif command.endswith('/0'):
            print('inf')
            
        try:
            result = eval(command)
            if result:
                print(result)
        except:
            try:
                exec(command)
            except Exception as e:
                print('')
                
if __name__ == "__main__":
    shell()